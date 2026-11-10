# -*- coding: utf-8 -*-
# The Skin Haus · blog. Lee los artículos de _agencia/articulos/<slug>.html (cabecera JSON + cuerpo)
# y genera blog/<slug>.html (dirección /blog/<slug>) y blog/index.html (dirección /blog/).
# Lo usa build.py; no se corre solo.
import os, re, json, glob

AQUI = os.path.dirname(os.path.abspath(__file__))
CARPETA = os.path.join(AQUI, "_agencia", "articulos")
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
B = {}          # funciones y datos de build.py (pagina, tarjetas, cierre, faq, ...) → configurar()
_cache = None


def configurar(ctx):
    B.update(ctx)


def fecha(iso):
    a, m, d = iso.split("-")
    return "%d de %s de %s" % (int(d), MESES[int(m) - 1], a)


def cargar():
    """Artículos publicados, del más nuevo al más viejo."""
    global _cache
    if _cache is not None:
        return _cache
    arts = []
    for ruta in sorted(glob.glob(os.path.join(CARPETA, "*.html"))):
        txt = open(ruta, encoding="utf-8").read()
        m = re.match(r"\s*<!--(.*?)-->", txt, re.S)
        if not m:
            print("  ! sin cabecera:", os.path.basename(ruta)); continue
        try:
            a = json.loads(m.group(1))
        except ValueError as e:
            print("  ! cabecera inválida:", os.path.basename(ruta), e); continue
        if a.get("estado") != "publicado":
            continue
        cuerpo = re.sub(r"<!--.*?-->", "", txt[m.end():], flags=re.S).strip()
        cuerpo = re.sub(r'href="(?!https?:|#|mailto:|tel:)/?([^"]*?)\.html', r'href="\1', cuerpo)   # enlaces internos limpios
        a["cuerpo"] = cuerpo
        a.setdefault("slug", os.path.basename(ruta)[:-5])
        a.setdefault("actualizado", a.get("publicado"))
        a.setdefault("tratamientos", [])
        a["faq"] = [tuple(x) for x in a.get("faq", [])]
        a["palabras"] = len(re.sub("<[^>]+>", " ", cuerpo).split())
        arts.append(a)
    arts.sort(key=lambda a: (a.get("publicado", ""), a["slug"]), reverse=True)
    _cache = arts
    return arts


def foto_de(a):
    if a.get("foto"):
        return a["foto"]
    trat = {t["slug"]: t for t in B["ESTETICA"] + B["BUSQUEDAS"]}
    for s in a["tratamientos"]:
        if s in trat:
            return B["foto_trat"](trat[s])       # 27-oct-2026: foto propia del tratamiento si existe
    return "piel"


def tarjeta(a):
    return ('<a class="tblog rev" href="blog/%s"><div class="tblog-foto"><img src="%s" alt="" loading="lazy"></div>'
            '<div class="tblog-txt"><span class="que">%s</span><h3>%s</h3><p>%s</p><span class="ver">Leer %s</span></div></a>') % (
        a["slug"], B["foto"](foto_de(a)), a.get("ceja", "Blog"), a["title"], a.get("intro", ""), B["FL"])


def rejilla(lista):
    return '<div class="rejilla-blog">%s</div>' % "".join(tarjeta(a) for a in lista)


def del_blog(ceja="Del blog", titulo="Para leer <em>antes de tu cita.</em>"):
    arts = cargar()[:3]
    if not arts:
        return ""
    return '''<section class="bloque"><div class="caja">
  <div class="centro"><p class="ceja rev">%s</p><h2 class="rev" style="margin-top:22px">%s</h2></div>
  %s
  <p class="centro rev" style="margin-top:44px"><a class="enlace" href="blog/">Ver todo el blog %s</a></p>
</div></section>''' % (ceja, titulo, rejilla(arts), B["CIRC"])


def lecturas(slug):
    arts = [a for a in cargar() if slug in a["tratamientos"]][:3]
    if not arts:
        return ""
    return '''<section class="bloque" style="padding-top:0"><div class="caja">
  <div class="centro"><p class="ceja rev">Del blog</p><h2 class="rev" style="margin-top:22px">Para leer <em>antes de tu cita.</em></h2></div>
  %s
</div></section>''' % rejilla(arts)


def para_sitemap():
    arts = cargar()
    filas = [("blog/%s" % a["slug"], a["actualizado"]) for a in arts]
    if arts:
        filas.insert(0, ("blog/", max(a["actualizado"] for a in arts)))
    return filas


def articulo(a, todos):
    url = "%s/blog/%s" % (B["DOMINIO"], a["slug"])
    minutos = max(3, round(a["palabras"] / 200))
    trat = {t["slug"]: t for t in B["ESTETICA"] + B["BUSQUEDAS"]}
    rel = [trat[s] for s in a["tratamientos"] if s in trat][:3]
    otros = [x for x in todos if x["slug"] != a["slug"]][:3]
    faq_html = ""
    if a["faq"]:
        faq_html = '''<section class="bloque" style="padding-top:0"><div class="caja">
  <div class="centro"><p class="ceja rev">Preguntas frecuentes</p><h2 class="rev" style="margin-top:22px">Lo que también <em>se pregunta.</em></h2></div>
  %s
</div></section>''' % B["faq"](a["faq"])
    rel_html = ""
    if rel:
        rel_html = '''<section class="bloque" style="padding-top:0"><div class="isla" style="padding:clamp(70px,9vw,120px) 0"><div class="caja">
  <div class="centro"><p class="ceja rev">Tratamientos relacionados</p></div>%s
</div></div></section>''' % B["tarjetas"](rel)
    otros_html = ""
    if otros:
        otros_html = '''<section class="bloque" style="padding-top:0"><div class="caja">
  <div class="centro"><p class="ceja rev">Sigue leyendo</p></div>%s
</div></section>''' % rejilla(otros)
    msg_blog = "Hola, leí «%s» en el blog de la web y quiero agendar una valoración en The Skin Haus." % a["title"]
    # 9-nov-2026 (ventas, tanda 1): bloque de valoración después del segundo H2 (antes del tercero), con WhatsApp
    # que nombra el artículo. Así todos los artículos tienen una invitación dentro del texto.
    nota = '''<aside class="nota-cita"><p class="ceja">Valoración médica</p>
<p>¿Quieres saber si esto aplica para ti? Escríbenos y lo revisamos en tu valoración.</p>
<div class="acciones">%s%s</div></aside>''' % (
        B["boton_wa"]("Hola, leí «%s» y quiero saber si aplica para mí." % a["title"], "blog-medio", "Pregúntanos por WhatsApp"),
        B["por_formulario"]("blog-medio"))
    # 9-nov-2026 (ronda 2): los artículos de duración (cuánto dura, cuánto rinde, cuándo volver) enlazan la calculadora
    # permanente /cuando-repetir. Va en la plantilla, al final del texto: el cuerpo del artículo no se toca.
    calc = ""
    if re.search(r"cuanto-dura|cuanto-rinde|cuando-volver", a["slug"]) and set(a["tratamientos"]) & set(B["CON_CALCULADORA"]):
        calc = '''\n<aside class="nota-cita"><p class="ceja">Calculadora</p>
<p>¿Ya te lo aplicaste? Pon la fecha de tu última aplicación y mira cuándo te toca repetir. Sirve también si tienes un evento.</p>
<div class="acciones"><a class="enlace" href="%s" data-ev="clic_calculadora" data-destino="%s">Calcular mi fecha %s</a></div></aside>''' % (
            B["calculadora"].SLUG, B["calculadora"].SLUG, B["CIRC"])
    h2s = [m.start() for m in re.finditer(r"<h2[\s>]", a["cuerpo"])]
    texto = a["cuerpo"][:h2s[2]] + nota + "\n" + a["cuerpo"][h2s[2]:] if len(h2s) >= 3 else a["cuerpo"] + "\n" + nota
    interes = next((s for s in a["tratamientos"] if s in B["NOMBRE_DE"]), None)
    cuerpo = '''<section class="bloque art-cab"><div class="aura a1"></div><div class="caja sobre">
  <nav class="migas rev" aria-label="Migas"><a href="">Inicio</a><span>/</span><a href="blog/">Blog</a><span>/</span><span>%s</span></nav>
  <p class="ceja rev">%s</p>
  <h1 class="rev">%s</h1>
  <p class="sub rev">%s</p>
  <p class="art-meta rev">Equipo médico The Skin Haus · Actualizado el %s · %d min de lectura</p>
</div></section>
<section class="bloque" style="padding-top:0"><div class="caja"><div class="art-foto rev"><img src="%s" alt="%s" fetchpriority="high"></div></div></section>
<section class="bloque" style="padding-top:0"><div class="caja"><article class="lectura">
%s%s
<p class="aviso">Este contenido es informativo y no reemplaza una valoración médica. Los resultados varían en cada persona.</p>
</article></div></section>
%s
%s
%s
%s''' % (a.get("ceja", "Blog"), a.get("ceja", "Blog"), a.get("h1", a["title"]), a.get("intro", ""), fecha(a["actualizado"]), minutos,
         B["foto"](foto_de(a)), a["title"], texto, calc, faq_html,
         B["cierre"]("Conversemos sobre lo que <em>quieres cuidar.</em>", msg=msg_blog, wa_primero=True), rel_html, otros_html)
    imagen = "%s/%s" % (B["DOMINIO"], B["foto_jpg"](foto_de(a)))
    ld = [{"@context": "https://schema.org", "@type": "BlogPosting", "headline": a["title"], "description": a["descripcion"],
           "datePublished": a["publicado"], "dateModified": a["actualizado"], "inLanguage": "es-CO",
           "image": imagen, "mainEntityOfPage": url, "url": url,
           "author": {"@type": "Organization", "name": "Equipo médico The Skin Haus", "url": B["DOMINIO"] + "/nosotros"},
           "publisher": {"@id": B["DOMINIO"] + "/#clinica"}, "about": [{"@type": "MedicalProcedure", "name": t["nombre"]} for t in rel]},
          B["CLINICA_LD"],
          B["migas_ld"]([("Inicio", ""), ("Blog", "blog/"), (a["title"], "blog/" + a["slug"])])]
    if a["faq"]:
        ld.append(B["faq_ld"](a["faq"]))
    t = a["title"]
    titulo = t + " · The Skin Haus" if len(t) + 16 <= 62 else t
    B["pagina"]("blog/" + a["slug"], titulo, a["descripcion"], cuerpo, activo="blog/", jsonld=ld, imagen=foto_de(a), tipo="article", wa_msg=msg_blog, interes=interes)


def indice(arts):
    msg = "Hola, vengo del blog de la web y quiero agendar mi valoración."
    cuerpo = '''<section class="bloque art-cab"><div class="aura a1"></div><div class="caja sobre centro">
  <h1 class="ceja rev">Blog de medicina estética en Pereira</h1>
  <p class="titular-vivo h1v" style="margin:26px 0 24px">%s</p>
  <p class="sub rev">Respuestas claras a lo que más se pregunta antes de un tratamiento: cuánto dura, cuánto vale, si se nota y en quién confiar. Escritas por el equipo médico de The Skin Haus.</p>
</div></section>
<section class="bloque" style="padding-top:0"><div class="caja">%s</div></section>
%s''' % (B["palabras"]("Lo que conviene saber <em>antes de tu cita.</em>"),
         rejilla(arts) if arts else '<p class="centro sub">Muy pronto, los primeros artículos.</p>', B["cierre"](msg=msg))
    ld = [B["CLINICA_LD"], {"@context": "https://schema.org", "@type": "Blog", "name": "Blog de The Skin Haus",
                            "url": B["DOMINIO"] + "/blog/", "inLanguage": "es-CO",
                            "blogPost": [{"@type": "BlogPosting", "headline": a["title"], "url": "%s/blog/%s" % (B["DOMINIO"], a["slug"]),
                                          "datePublished": a["publicado"]} for a in arts]},
          B["migas_ld"]([("Inicio", ""), ("Blog", "blog/")])]
    B["pagina"]("blog/index", "Blog de medicina estética en Pereira · The Skin Haus",
                "Respuestas claras sobre bótox, ácido hialurónico, manchas y cuidado de la piel, escritas por el equipo médico de The Skin Haus en Pereira.",
                cuerpo, activo="blog/", jsonld=ld, imagen="piel", wa_msg=msg)


def generar():
    arts = cargar()
    os.makedirs(os.path.join(AQUI, "blog"), exist_ok=True)
    vivos = {a["slug"] + ".html" for a in arts} | {"index.html"}
    for viejo in os.listdir(os.path.join(AQUI, "blog")):       # si un artículo vuelve a borrador, su página se quita
        if viejo.endswith(".html") and viejo not in vivos:
            os.remove(os.path.join(AQUI, "blog", viejo))
    for a in arts:
        articulo(a, arts)
    indice(arts)
    return len(arts)
