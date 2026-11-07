# -*- coding: utf-8 -*-
"""Lee Search Console con el "usuario robot" (cuenta de servicio, solo lectura) y saca la foto semanal en Markdown.

Lo usan las revisiones SEO de los lunes que corren en la nube, así que no hace falta el Chrome ni el computador de Laura.

Uso (desde la raíz del repositorio):
  python3 _agencia/gsc.py PROPIEDAD [--paises] [--sin-indexacion] [--max-urls N]
                         [--sin-marca] [--marca-terminos "a,b"] [--consultas ARCHIVO] [--pares]
  PROPIEDAD: "sc-domain:noon.clinic" (propiedad de dominio) o "https://www.clinicaseravena.com/" (prefijo de URL)

Opciones nuevas (7-nov-2026, plan de 90 días):
  --sin-marca (o --marca)   separa clics y apariciones de quien buscó el nombre de la marca (lista MARCAS de abajo,
                            o --marca-terminos "a,b,c"). "Sin marca" = total menos marca: las búsquedas que Google
                            esconde por raras cuentan como sin marca.
  --consultas ARCHIVO       (o --objetivos ARCHIVO) puesto medio en Colombia de una lista fija de búsquedas. El archivo
                            puede ser una lista con "- búsqueda" bajo un título que diga "fijas" o una tabla Markdown
                            (se toma la primera columna de la primera tabla). Ej.: _agencia/posiciones.md
  --pares                   búsquedas (sin marca) para las que salen 2 o más páginas propias: posibles gemelas.
  Siempre: "Candidatas a mejora" (≥ 20 apariciones, 0-1 clics, puesto 5 a 20) y las páginas APARTE (lo vascular de
  Skin Haus) en su propia sección, fuera de las candidatas.

Llave del robot: variable de entorno GSC_ROBOT_B64 (el JSON de la cuenta de servicio en base64, puesta en el entorno de la
nube) o, en el Mac, el archivo ~/.gsc-robot/llave.json. Nunca imprime la llave. Solo librería estándar + openssl.
"""
from concurrent.futures import ThreadPoolExecutor
import base64, datetime, json, os, re, subprocess, sys, tempfile, time, unicodedata, urllib.error, urllib.parse, urllib.request

ALCANCE = "https://www.googleapis.com/auth/webmasters.readonly"
API = "https://searchconsole.googleapis.com"

# Búsquedas de marca por web: solo las hace quien ya conoce la clínica, así que se cuentan aparte.
MARCAS = {
    "theskinhaus.com.co": ["skin haus", "skinhaus", "the skin", "skin house", "skinhouse"],
}
# Páginas que se miran aparte (no entran a "Candidatas a mejora"): en Skin Haus, lo vascular.
APARTE = {
    "theskinhaus.com.co": ["medicina-vascular", "aranitas-vasculares", "varices", "eco-doppler-venoso",
                           "cuperosis-y-rojeces"],
}


def llave():
    b64 = os.environ.get("GSC_ROBOT_B64", "").strip()
    if b64:
        return json.loads(base64.b64decode(b64))
    ruta = os.path.expanduser("~/.gsc-robot/llave.json")
    if os.path.exists(ruta):
        return json.load(open(ruta))
    sys.exit("FALTA LA LLAVE DEL ROBOT: no está la variable GSC_ROBOT_B64 en el entorno de la nube.")


def b64url(datos):
    return base64.urlsafe_b64encode(datos).rstrip(b"=")


def token(k):
    ahora = int(time.time())
    cabeza = b64url(json.dumps({"alg": "RS256", "typ": "JWT"}).encode())
    cuerpo = b64url(json.dumps({"iss": k["client_email"], "scope": ALCANCE, "aud": k["token_uri"],
                                "iat": ahora, "exp": ahora + 3600}).encode())
    firmar = cabeza + b"." + cuerpo
    with tempfile.NamedTemporaryFile("w", suffix=".pem", delete=False) as f:
        f.write(k["private_key"])
        pem = f.name
    try:
        os.chmod(pem, 0o600)
        firma = subprocess.run(["openssl", "dgst", "-sha256", "-sign", pem], input=firmar,
                               capture_output=True, check=True).stdout
    finally:
        os.remove(pem)
    jwt = firmar + b"." + b64url(firma)
    datos = urllib.parse.urlencode({"grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
                                    "assertion": jwt.decode()}).encode()
    r = urllib.request.urlopen(urllib.request.Request(k["token_uri"], data=datos), timeout=30)
    return json.loads(r.read())["access_token"]


def pedir(tok, ruta, cuerpo):
    req = urllib.request.Request(API + ruta, data=json.dumps(cuerpo).encode(),
                                 headers={"Authorization": "Bearer " + tok, "Content-Type": "application/json"})
    try:
        return json.loads(urllib.request.urlopen(req, timeout=60).read())
    except urllib.error.HTTPError as e:
        detalle = e.read().decode()[:300]
        if e.code == 403:
            sys.exit("SIN PERMISO (403): agrega al robot como usuario 'Restringido' en esta propiedad de Search Console. " + detalle)
        raise SystemExit("ERROR %d de Search Console: %s" % (e.code, detalle))


def analitica(tok, prop, inicio, fin, dims, filas=25, pais=None):
    ruta = "/webmasters/v3/sites/%s/searchAnalytics/query" % urllib.parse.quote(prop, safe="")
    cuerpo = {"startDate": inicio, "endDate": fin, "rowLimit": filas, "dataState": "all"}
    if dims:
        cuerpo["dimensions"] = dims
    if pais:
        cuerpo["dimensionFilterGroups"] = [{"filters": [{"dimension": "country", "operator": "equals",
                                                         "expression": pais}]}]
    filas_api = pedir(tok, ruta, cuerpo).get("rows", [])
    # Google ordena solo por clics; con pocos clics el top queda alfabético. Mejor: clics y luego impresiones.
    return sorted(filas_api, key=lambda r: (-r["clicks"], -r["impressions"]))


def fila(r):
    return "%d | %d | %.1f%% | %.1f" % (r["clicks"], r["impressions"], 100 * r["ctr"], r["position"])


def normal(texto):
    """minúsculas, sin tildes y con un solo espacio: 'Bótox  Pereira' y 'botox pereira' cuentan igual."""
    sin_tildes = "".join(c for c in unicodedata.normalize("NFKD", texto) if not unicodedata.combining(c))
    return " ".join(sin_tildes.lower().split())


def dominio(prop):
    d = prop.split(":", 1)[1] if prop.startswith("sc-domain:") else urllib.parse.urlparse(prop).netloc
    d = d.lower().strip("/")
    return d[4:] if d.startswith("www.") else d


def terminos_marca(prop, a):
    if "--marca-terminos" in a:
        return [t.strip() for t in a[a.index("--marca-terminos") + 1].split(",") if t.strip()]
    return MARCAS.get(dominio(prop)) or [dominio(prop).split(".")[0]]


def es_marca(consulta, terminos):
    q = normal(consulta)
    return any(re.search(r"\b" + re.escape(normal(t)) + r"\b", q) for t in terminos)


def es_aparte(url, prop):
    ruta = urllib.parse.urlparse(url).path.strip("/")
    return ruta in APARTE.get(dominio(prop), [])


def leer_consultas(ruta):
    """Lista fija de búsquedas: viñetas bajo un título con 'fijas' o, si no hay, la 1.ª columna de la 1.ª tabla."""
    lineas = open(ruta, encoding="utf-8").read().splitlines()
    lista, dentro = [], False
    for l in lineas:
        if l.startswith("#"):
            dentro = "fijas" in normal(l)
            continue
        if dentro and re.match(r"\s*[-*]\s+\S", l):
            lista.append(re.sub(r"^\s*[-*]\s+", "", l).strip())
    if lista:
        return list(dict.fromkeys(lista))
    tabla = False
    for l in lineas:
        if l.strip().startswith("|"):
            celdas = [c.strip() for c in l.strip().strip("|").split("|")]
            primera = celdas[0] if celdas else ""
            if not primera or set(primera) <= set("-: ") or normal(primera) in ("busqueda", "consulta"):
                tabla = True
                continue
            tabla = True
            lista.append(re.sub(r"[*_`]", "", primera))
        elif tabla and lista:
            break
    return list(dict.fromkeys(lista))


def urls_sitemap(prop):
    base = "https://" + prop.split(":", 1)[1] + "/" if prop.startswith("sc-domain:") else prop
    try:
        xml = urllib.request.urlopen(urllib.parse.urljoin(base, "sitemap.xml"), timeout=30).read().decode("utf-8", "ignore")
    except Exception as e:
        return [], "no se pudo leer el sitemap (%s)" % e
    return re.findall(r"<loc>\s*([^<]+?)\s*</loc>", xml), ""


def main():
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    prop = a[0]
    max_urls = int(a[a.index("--max-urls") + 1]) if "--max-urls" in a else 400
    tok = token(llave())
    fin = datetime.date.today() - datetime.timedelta(days=2)
    inicio = fin - datetime.timedelta(days=27)
    i, f = inicio.isoformat(), fin.isoformat()
    print("# Search Console · %s · %s a %s (28 días)\n" % (prop, i, f))

    tot = analitica(tok, prop, i, f, None, 1)
    t = tot[0] if tot else {"clicks": 0, "impressions": 0, "ctr": 0, "position": 0}
    print("**Totales:** %d clics · %d impresiones · CTR %.1f%% · posición media %.1f\n"
          % (t["clicks"], t["impressions"], 100 * t["ctr"], t["position"]))

    if "--paises" in a:
        print("## Países (top 10)\npaís | clics | impresiones | CTR | posición\n---|---|---|---|---")
        for r in analitica(tok, prop, i, f, ["country"], 250)[:10]:
            print(r["keys"][0].upper() + " | " + fila(r))
        print()

    consultas = analitica(tok, prop, i, f, ["query"], 5000)
    print("## Búsquedas (top 15)\nbúsqueda | clics | impresiones | CTR | posición\n---|---|---|---|---")
    for r in consultas[:15]:
        print(r["keys"][0] + " | " + fila(r))
    print()

    terminos = terminos_marca(prop, a)
    if "--sin-marca" in a or "--marca" in a:
        de_marca = [r for r in consultas if es_marca(r["keys"][0], terminos)]
        mc, mi = sum(r["clicks"] for r in de_marca), sum(r["impressions"] for r in de_marca)
        print("## Con y sin marca")
        print("- Con marca (%s): %d clics · %d apariciones" % (", ".join(terminos), mc, mi))
        print("- **Sin marca: %d clics · %d apariciones** (total menos marca; las búsquedas que Google esconde por raras"
              " cuentan aquí)" % (t["clicks"] - mc, t["impressions"] - mi))
        print("\nbúsqueda sin marca (top 10) | clics | impresiones | CTR | posición\n---|---|---|---|---")
        for r in [r for r in consultas if not es_marca(r["keys"][0], terminos)][:10]:
            print(r["keys"][0] + " | " + fila(r))
        print()

    paginas = analitica(tok, prop, i, f, ["page"], 500)
    print("## Páginas (top 15)\npágina | clics | impresiones | CTR | posición\n---|---|---|---|---")
    for r in paginas[:15]:
        print(r["keys"][0] + (" (aparte)" if es_aparte(r["keys"][0], prop) else "") + " | " + fila(r))
    print()

    cand = [r for r in paginas if r["position"] <= 20 and r["clicks"] <= 1 and r["impressions"] >= 10]
    print("## Salen pero casi nadie abre (posición ≤ 20, 0-1 clics, ≥ 10 impresiones)")
    print("\n".join("- " + r["keys"][0] + (" (aparte)" if es_aparte(r["keys"][0], prop) else "") + " · " + fila(r)
                    for r in cand) or "- ninguna")
    print()

    mejora = [r for r in paginas if not es_aparte(r["keys"][0], prop) and r["impressions"] >= 20
              and r["clicks"] <= 1 and 5 <= r["position"] <= 20][:5]
    print("## Candidatas a mejora (≥ 20 apariciones, 0-1 clics, puesto 5 a 20; máximo 5, sin las de aparte)")
    print("\n".join("- " + r["keys"][0] + " · " + fila(r) for r in mejora) or "- ninguna esta semana")
    print()

    aparte = [r for r in paginas if es_aparte(r["keys"][0], prop)]
    if APARTE.get(dominio(prop)):
        print("## Páginas aparte (no son de la estrategia del blog; en Skin Haus, lo vascular)")
        print("\n".join("- " + r["keys"][0] + " · " + fila(r) for r in aparte) or "- sin apariciones")
        print()

    pares_filas = None
    if "--consultas" in a or "--objetivos" in a:
        bandera = "--consultas" if "--consultas" in a else "--objetivos"
        archivo = a[a.index(bandera) + 1]
        try:
            fijas = leer_consultas(archivo)
        except OSError as e:
            fijas = []
            print("## Búsquedas fijas\n- no se pudo leer %s (%s)\n" % (archivo, e))
        if fijas:
            en_col = analitica(tok, prop, i, f, ["query"], 5000, pais="col")
            pares_filas = analitica(tok, prop, i, f, ["query", "page"], 5000)
            print("## Búsquedas fijas en Colombia (%d, de %s)" % (len(fijas), archivo))
            print("búsqueda | apariciones | clics | puesto medio | página que más sale\n---|---|---|---|---")
            primera, con_datos = 0, 0
            for b in fijas:
                n = normal(b)
                filas_b = [r for r in en_col if normal(r["keys"][0]) == n]
                imp = sum(r["impressions"] for r in filas_b)
                if not imp:
                    print("%s | 0 | 0 | sin datos | —" % b)
                    continue
                con_datos += 1
                clics = sum(r["clicks"] for r in filas_b)
                puesto = sum(r["position"] * r["impressions"] for r in filas_b) / imp
                primera += puesto <= 10
                pags = {}
                for r in pares_filas:
                    if normal(r["keys"][0]) == n:
                        pags[r["keys"][1]] = pags.get(r["keys"][1], 0) + r["impressions"]
                top = max(pags, key=pags.get) if pags else "—"
                top = urllib.parse.urlparse(top).path or top
                print("%s | %d | %d | %.1f | %s" % (b, imp, clics, puesto, top))
            print("\n**En primera página (puesto medio ≤ 10): %d de %d.** Con datos: %d; sin datos: %d (Google no la"
                  " mostró o la esconde por pocas búsquedas)." % (primera, len(fijas), con_datos, len(fijas) - con_datos))
            print()

    if "--pares" in a:
        pares_filas = pares_filas or analitica(tok, prop, i, f, ["query", "page"], 5000)
        grupos = {}
        for r in pares_filas:
            q = r["keys"][0]
            if es_marca(q, terminos):
                continue
            grupos.setdefault(normal(q), []).append(r)
        dobles = [(q, rs) for q, rs in grupos.items() if len({x["keys"][1] for x in rs}) >= 2]
        dobles.sort(key=lambda x: -sum(r["impressions"] for r in x[1]))
        print("## Búsquedas con 2 o más páginas propias (posibles gemelas, sin marca)")
        if not dobles:
            print("- ninguna")
        for q, rs in dobles[:15]:
            detalle = "; ".join("%s (%d apar., puesto %.1f)" % (urllib.parse.urlparse(r["keys"][1]).path,
                                                                 r["impressions"], r["position"])
                                for r in sorted(rs, key=lambda r: -r["impressions"]))
            print("- %s → %s" % (q, detalle))
        print()

    if "--sin-indexacion" in a:
        return
    urls, error = urls_sitemap(prop)
    print("## Indexación (inspección de las páginas del sitemap)")
    if error:
        print("- " + error)
        return
    def inspeccionar(u):
        res = pedir(tok, "/v1/urlInspection/index:inspect", {"inspectionUrl": u, "siteUrl": prop, "languageCode": "es"})
        return u, res.get("inspectionResult", {}).get("indexStatusResult", {})

    estados, fuera = {}, []
    with ThreadPoolExecutor(max_workers=6) as grupo:  # varias a la vez: una por una tarda ~5 s por página
        for u, st in grupo.map(inspeccionar, urls[:max_urls]):
            estado = st.get("coverageState", "sin dato")
            estados[estado] = estados.get(estado, 0) + 1
            if st.get("verdict") != "PASS":
                fuera.append((u, estado))
    en_google = len(urls[:max_urls]) - len(fuera)
    print("- %d páginas en el sitemap, revisadas %d: **%d en Google**, %d todavía no."
          % (len(urls), len(urls[:max_urls]), en_google, len(fuera)))
    for estado, n in sorted(estados.items(), key=lambda x: -x[1]):
        print("  - %s: %d" % (estado, n))
    if fuera:
        print("- Páginas que aún no están en Google:")
        for u, estado in fuera[:40]:
            print("  - %s (%s)" % (u, estado))


if __name__ == "__main__":
    main()
