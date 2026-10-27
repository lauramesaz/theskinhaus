# -*- coding: utf-8 -*-
# The Skin Haus · genera todas las páginas a partir de datos.py.   Uso:  python3 build.py
# v3 "fluida": arcos, círculos, gotas, islas marfil, cinta de frases y camino con curva.
import os, time, json, re
from urllib.parse import quote
from datos import *
from ampliacion import NOSOTROS_TEXTO, VALORACION_TEXTO   # 27-oct-2026: páginas más completas
import blog

AQUI = os.path.dirname(os.path.abspath(__file__))
V = int(time.time())
FL = "&#8594;"  # flecha
CIRC = '<span class="circ">%s</span>' % FL


def wa(msg="Hola, quiero agendar una valoración en The Skin Haus."):
    return "https://wa.me/%s?text=%s" % (WHATSAPP, quote(msg))


def foto(n):
    if n.startswith("assets/"):               # ruta completa sin extensión (p. ej. assets/equipo/valeria-enciso)
        return n + ".webp"
    return "assets/fotos/%s.webp" % n          # WebP: ~65 % más liviano (19-oct-2026)


def foto_jpg(n):
    if n.startswith("assets/"):
        return n + ".jpg"
    return "assets/fotos/%s.jpg" % n           # para redes sociales y datos estructurados


def foto_trat(t):
    """27-oct-2026: foto propia por tratamiento (Higgsfield, assets/fotos/<slug>.webp) si existe; si no, la genérica."""
    return t["slug"] if os.path.exists(os.path.join(AQUI, "assets", "fotos", t["slug"] + ".webp")) else t["foto"]


def logo(clase="compacto", descriptor=False):
    d = '<span class="barra"></span><span class="desc"><span>MEDICAL</span><span>AESTHETICS</span></span>' if descriptor else ""
    return '<span class="logo %s" aria-label="The Skin Haus"><span class="nombre"><span class="the">THE</span><span class="sh">SKIN</span><span class="sh">HAUS</span></span>%s</span>' % (clase, d)


# ---------------------------------------------------------------- piezas
def cabecera(activo):
    items = [("medicina-estetica", "Estética"), ("medicina-vascular", "Vascular"), ("blog/", "Blog"), ("nosotros", "Nosotros")]
    links = "".join('<a href="%s"%s>%s</a>' % (h, ' class="activo"' if h == activo else "", t) for h, t in items)
    return '''<header class="cab"><div class="cab-in">
<a href="./" aria-label="Inicio">%s</a>
<nav class="menu" aria-label="Principal">%s<a class="btn lleno" href="valoracion">Agenda tu valoración</a></nav>
<button class="hamb" aria-label="Menú" aria-expanded="false"><span></span><span></span></button>
</div></header>''' % (logo(), links)


def pie():
    est = "".join('<li><a href="%s">%s</a></li>' % (t["slug"], t["nombre"]) for t in ESTETICA[:4] + BUSQUEDAS[:2])
    vas = "".join('<li><a href="%s">%s</a></li>' % (t["slug"], t["nombre"]) for t in VASCULAR)
    return '''<footer class="pie-web"><div class="caja">
<div class="pie-grid">
  <div>%s<p class="frase-marca" style="margin-top:36px;max-width:15em">Cuidamos la piel con ciencia, sensibilidad y una mirada profundamente personal.</p></div>
  <div><h4>Medicina estética</h4><ul>%s<li><a href="medicina-estetica">Ver todos</a></li><li><a href="preguntas-frecuentes">Preguntas frecuentes</a></li><li><a href="blog/">Blog</a></li></ul></div>
  <div><h4>Medicina vascular</h4><ul>%s</ul></div>
  <div><h4>Visítanos</h4><ul><li>%s</li><li><a href="%s" target="_blank" rel="noopener">WhatsApp %s</a></li></ul></div>
</div>
<div class="pie-final"><span>The Skin Haus · %s · Colombia</span><span>Los resultados varían en cada persona. Toda indicación requiere valoración médica.</span><span>Web y SEO: <a href="https://posicion-seo.com/">Visibla</a></span></div>
</div></footer>''' % (logo("completo", True), est, vas, DIRECCION, wa(), TELEFONO_VISIBLE, CIUDAD)


WA_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5c-.2 0-.4.1-.7.3-.2.3-.9.9-.9 2.2s.9 2.5 1 2.7c.1.2 1.8 2.8 4.4 3.9 1.6.7 2.3.8 3.1.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3z"/></svg>'

SELLO = '''<svg class="sello" viewBox="0 0 124 124" aria-hidden="true"><defs><path id="rueda" d="M62,62 m-46,0 a46,46 0 1,1 92,0 a46,46 0 1,1 -92,0"/></defs>
<text><textPath href="#rueda" textLength="286" lengthAdjust="spacing">Estética · Vascular · Pereira · The Skin Haus ·</textPath></text><circle cx="62" cy="62" r="3" fill="#C6A88F"/></svg>'''


# Medición (aprobada por Laura 20-oct-2026): Google Analytics 4 (cuenta aparte "The Skin Haus") + Clarity (proyecto
# "The Skin Haus", sector Salud). El clic a WhatsApp se cuenta en app.js (evento clic_whatsapp).
GA4 = "G-79WV8JCLPD"
CLARITY = "z0v793pqdy"
HEAD_MEDICION = (
    '<script async src="https://www.googletagmanager.com/gtag/js?id=' + GA4 + '"></script>\n'
    "<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}"
    "gtag('js',new Date());gtag('config','" + GA4 + "');</script>\n"
    '<script>(function(c,l,a,r,i,t,y){c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};'
    't=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;y=l.getElementsByTagName(r)[0];'
    'y.parentNode.insertBefore(t,y);})(window,document,"clarity","script","' + CLARITY + '");</script>\n'
)


_CSS = None


def estilo_en_linea():
    """27-oct-2026 (velocidad): el CSS va dentro de cada página en vez de un archivo aparte que bloquea el
    primer pintado. PageSpeed móvil mostraba ~2 s de 'retraso en la renderización' de la foto principal."""
    global _CSS
    if _CSS is None:
        css = open(os.path.join(AQUI, "assets", "estilo.css"), encoding="utf-8").read()
        css = re.sub(r"url\((textura-[a-z]+\.jpg)\)", r"url(assets/\1)", css)     # rutas relativas a assets/
        css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)                            # sin comentarios
        _CSS = re.sub(r"\n\s*", "\n", css).strip()
    return _CSS


def pagina(archivo, titulo, descripcion, cuerpo, activo="", jsonld=None, imagen="retrato", tipo="website", precarga=True, robots=None, extra_head=""):
    url = DOMINIO + "/" + ("" if archivo == "index" else archivo[:-5] if archivo.endswith("/index") else archivo)
    ld = '<script type="application/ld+json">%s</script>' % json.dumps(jsonld, ensure_ascii=False) if jsonld else ""
    ld = HEAD_MEDICION + ld
    html = '''<!doctype html>
<html lang="es-CO">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<base href="/">
<title>%s</title>
<meta name="description" content="%s">
<link rel="canonical" href="%s">%s
<meta property="og:type" content="%s"><meta property="og:title" content="%s"><meta property="og:description" content="%s">
<meta property="og:url" content="%s"><meta property="og:image" content="%s/%s"><meta property="og:locale" content="es_CO">
<meta name="theme-color" content="#FAF8F3">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
%s<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@1,400;1,500&family=Libre+Caslon+Display&family=Libre+Caslon+Text:ital@0;1&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
<noscript><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@1,400;1,500&family=Libre+Caslon+Display&family=Libre+Caslon+Text:ital@0;1&display=swap" rel="stylesheet"></noscript>
<style>%s</style>
%s
</head>
<body>
%s
<main>
%s
</main>
%s
<a class="wa" href="%s" target="_blank" rel="noopener" aria-label="Escríbenos por WhatsApp">%s</a>
<script src="assets/app.js?v=%d" defer></script>
</body>
</html>''' % (titulo, descripcion, url, ('\n<meta name="robots" content="%s">' % robots if robots else "") + extra_head, tipo, titulo, descripcion, url, DOMINIO, foto_jpg(imagen),
              '<link rel="preload" as="image" href="%s" fetchpriority="high">\n' % foto(imagen) if precarga else "", estilo_en_linea(), ld,
              cabecera(activo), cuerpo, pie(), wa(), WA_SVG, V)
    os.makedirs(os.path.dirname(os.path.join(AQUI, archivo)), exist_ok=True)
    with open(os.path.join(AQUI, archivo + ".html"), "w", encoding="utf-8") as f:
        f.write(html)


def palabras(html):
    """Envuelve cada palabra del titular para animarla; mantiene la cursiva <em> por palabra."""
    out, i = [], 0
    for trozo in re.split(r"(<em>.*?</em>)", html):
        if not trozo:
            continue
        cursiva = trozo.startswith("<em>")
        texto = trozo[4:-5] if cursiva else trozo
        for w in texto.split():
            i += 1
            w = "<em>%s</em>" % w if cursiva else w
            out.append('<span class="w"><span style="--i:%d">%s</span></span>' % (i, w))
    return " ".join(out)


# íconos de línea por tratamiento (trazo fino, se ven en la tarjeta)
ICONOS = {
    "toxina-botulinica": '<path d="M12 21a8 8 0 1 0 0-16 8 8 0 0 0 0 16z"/><path d="M8.5 10.5c1-.8 2-.8 3 0M12.5 10.5c1-.8 2-.8 3 0M9 15c1.8 1.3 4.2 1.3 6 0"/><path d="M9 3.5h6"/>',
    "acido-hialuronico": '<path d="M12 3s6 6.8 6 11a6 6 0 0 1-12 0c0-4.2 6-11 6-11z"/><path d="M9.5 14.5a2.5 2.5 0 0 0 2.5 2.5"/>',
    "bioestimuladores": '<path d="M12 12m-2 0a2 2 0 1 0 4 0a2 2 0 1 0-4 0"/><path d="M12 12m-5 0a5 5 0 1 0 10 0a5 5 0 1 0-10 0"/><path d="M12 12m-8.5 0a8.5 8.5 0 1 0 17 0a8.5 8.5 0 1 0-17 0" stroke-dasharray="2 3"/>',
    "skinboosters": '<path d="M12 3v4M12 17v4M3 12h4M17 12h4"/><path d="M12 8.5l1.2 2.3 2.3 1.2-2.3 1.2L12 15.5l-1.2-2.3L8.5 12l2.3-1.2z"/>',
    "peelings-medicos": '<path d="M4 8l8-4 8 4-8 4-8-4z"/><path d="M4 12l8 4 8-4"/><path d="M4 16l8 4 8-4"/>',
    "microagujas": '<path d="M6 6h.01M10 6h.01M14 6h.01M18 6h.01M6 10h.01M10 10h.01M14 10h.01M18 10h.01M6 14h.01M10 14h.01M14 14h.01M18 14h.01M6 18h.01M10 18h.01M14 18h.01M18 18h.01" stroke-width="2.4"/>',
    "manchas-y-melasma": '<path d="M12 12m-4 0a4 4 0 1 0 8 0a4 4 0 1 0-8 0"/><path d="M12 2.5v2.5M12 19v2.5M2.5 12H5M19 12h2.5M5.3 5.3l1.8 1.8M16.9 16.9l1.8 1.8M5.3 18.7l1.8-1.8M16.9 7.1l1.8-1.8"/>',
    "limpieza-facial-medica": '<path d="M8 15m-4 0a4 4 0 1 0 8 0a4 4 0 1 0-8 0"/><path d="M16.5 8.5m-3 0a3 3 0 1 0 6 0a3 3 0 1 0-6 0"/><path d="M17 17m-1.8 0a1.8 1.8 0 1 0 3.6 0a1.8 1.8 0 1 0-3.6 0"/>',
    "aranitas-vasculares": '<path d="M12 21V12M12 12l-5-5M12 12l5-5M7 7l-3 1M7 7l-1-3M17 7l3 1M17 7l1-3M12 16l-3 2M12 16l3 2"/>',
    "varices": '<path d="M10 3c0 4-3 5-3 9s3 5 3 9"/><path d="M15 3c0 3 2 4 2 7s-3 3-3 6 1 3 1 5"/>',
    "eco-doppler-venoso": '<path d="M3 12h3l2-5 3 10 3-8 2 3h5"/>',
    "cuperosis-y-rojeces": '<path d="M12 21a8 8 0 1 0 0-16 8 8 0 0 0 0 16z"/><path d="M8 13.5h.01M9.5 15h.01M14.5 15h.01M16 13.5h.01" stroke-width="2.4"/><path d="M10 10h.01M14 10h.01" stroke-width="2"/>',
    "relleno-de-labios": '<path d="M3 12c2.5-3 5-4.5 6.5-4.5 1 0 1.8.6 2.5 1.3.7-.7 1.5-1.3 2.5-1.3C16 7.5 18.5 9 21 12c-2.5 3-5.5 4.5-9 4.5S5.5 15 3 12z"/><path d="M3 12h18"/>',
    "tratamiento-de-ojeras": '<path d="M2.5 11S6 5.5 12 5.5s9.5 5.5 9.5 5.5-3.5 5.5-9.5 5.5S2.5 11 2.5 11z"/><path d="M12 11m-2.4 0a2.4 2.4 0 1 0 4.8 0a2.4 2.4 0 1 0-4.8 0"/><path d="M7 19.5c1.5.8 3.2 1.2 5 1.2s3.5-.4 5-1.2"/>',
    "armonizacion-facial": '<path d="M12 3c-4 0-6.5 3.2-6.5 7.5 0 5 3.2 10.5 6.5 10.5s6.5-5.5 6.5-10.5C18.5 6.2 16 3 12 3z"/><path d="M12 3v18" stroke-dasharray="1.5 2.5"/><path d="M8.5 10.5h2M13.5 10.5h2"/>',
    "hiperhidrosis": '<path d="M9 4s4 4.6 4 7.4a4 4 0 0 1-8 0C5 8.6 9 4 9 4z"/><path d="M17 10s2.6 3 2.6 4.8a2.6 2.6 0 0 1-5.2 0c0-1.8 2.6-4.8 2.6-4.8z"/>',
    "cicatrices-de-acne": '<path d="M3 15c2 0 2-3 4.5-3S9.5 15 12 15s2-3 4.5-3 2.5 3 4.5 3"/><path d="M3 19c2 0 2-2 4.5-2S9.5 19 12 19s2-2 4.5-2 2.5 2 4.5 2"/><path d="M8 7h.01M12 5h.01M16 7h.01" stroke-width="2.4"/>',
}


def icono(slug):
    return '<span class="ico"><svg viewBox="0 0 24 24" aria-hidden="true">%s</svg></span>' % ICONOS.get(slug, ICONOS["skinboosters"])


def tarjeta_trat(t):
    que, d1, d2 = CLAVE[t["slug"]]
    return ('<a class="ttrat rev" href="%s">%s<span class="que">%s</span><h3>%s</h3><p>%s</p>'
            '<span class="datos-mini"><span>%s</span><span>%s</span></span><span class="ver">Ver tratamiento %s</span></a>') % (
        t["slug"], icono(t["slug"]), que, t["nombre"], t["linea"], d1, d2, FL)


def hero(ceja, titulo, sub, foto_arco, foto_circ, acciones="", corto=False, alt="", h1_ceja=False):
    """h1_ceja=True: el <h1> es la ceja (con la búsqueda, p. ej. 'Medicina estética en Pereira') y el
    titular de marca se ve igual pero como párrafo. Así el diseño no cambia y Google lee la búsqueda."""
    if h1_ceja:
        cab = '<h1 class="ceja rev">%s</h1><p class="titular-vivo h1v">%s</p>' % (ceja, palabras(titulo))
    else:
        cab = '<p class="ceja rev">%s</p><h1 class="titular-vivo">%s</h1>' % (ceja, palabras(titulo))
    return '''<section class="hero%s">
  <div class="aura a1"></div>
  <div class="texto">%s<p class="sub rev">%s</p>%s</div>
  <div class="compo">%s<div class="arco"><img src="%s" alt="%s" fetchpriority="high"></div><div class="circulo rev" data-vel="-0.08"><img src="%s" alt=""></div></div>
</section>''' % (" corto" if corto else "", cab, sub, acciones, SELLO, foto(foto_arco), alt, foto(foto_circ))


def cinta(frases):
    s = "".join("<span>%s</span>" % f for f in frases)
    return '<div class="cinta" aria-hidden="true"><div class="pista">%s%s</div></div>' % (s, s)


def faq(pares):
    return '<div class="faq">%s</div>' % "".join(
        '<details class="rev"><summary>%s<span class="circ">+</span></summary><p>%s</p></details>' % p for p in pares)


def cierre(titulo="Hablemos de tu piel.", ceja="Valoración médica"):
    return '''<section class="bloque"><div class="isla lino cierre" style="position:relative">
<div class="aura a1" style="opacity:.8"></div><div class="aura a2"></div>
<div class="flota f1" data-vel="-0.05"><div class="circulo"><img src="assets/fotos/cabina-espejo.webp" alt="" loading="lazy"></div></div>
<div class="flota f2" data-vel="0.05"><div class="arco"><img src="assets/fotos/manos.webp" alt="" loading="lazy"></div></div>
<div class="sobre"><p class="ceja rev">%s</p><h2 class="rev">%s</h2>
<p class="sub rev" style="margin:26px auto 0">Primero te escuchamos. Luego recomendamos.</p>
<div class="acciones rev"><a class="btn lleno" href="valoracion">Agenda tu valoración</a><a class="enlace" href="%s" target="_blank" rel="noopener">Escríbenos por WhatsApp %s</a></div></div>
</div></section>''' % (ceja, titulo, wa(), CIRC)


def manifiesto(texto, ceja="Lo que nos mueve"):
    ws = " ".join('<span>%s</span>' % w for w in texto.split())
    return '''<section class="bloque" style="padding-top:0"><div class="isla lino manifiesto" style="padding:clamp(90px,12vw,170px) 0"><div class="caja">
<p class="ceja centro">%s</p><p class="manif">%s</p>
</div></div></section>''' % (ceja, ws)


def camino(en_isla=True):
    pasos = "".join('<div class="paso rev"><p class="num">%d</p><p class="ceja">%s</p><p>%s</p></div>' % (i, t, d)
                    for i, (t, d) in enumerate(CAMINO, 1))
    inner = '''<div class="caja"><div class="centro"><p class="ceja rev">Así es tu camino</p><h2 class="rev" style="margin-top:22px">Belleza que <em>se acompaña.</em></h2>
<p class="sub rev" style="margin-top:24px">La confianza nace de entender cada decisión. Por eso nada empieza con una aguja: empieza con una conversación.</p></div>
<div class="camino"><svg class="curva" aria-hidden="true"><path d=""/></svg><div class="pasos">%s</div></div></div>''' % pasos
    if en_isla:
        return '<section class="bloque" style="padding-top:0"><div class="isla" style="padding:clamp(80px,10vw,140px) 0">%s</div></section>' % inner
    return '<section class="bloque">%s</section>' % inner


CLINICA_LD = {
    "@context": "https://schema.org", "@type": "MedicalClinic", "@id": DOMINIO + "/#clinica", "name": MARCA,
    "alternateName": "The Skin Haus Pereira",
    "description": "Clínica de medicina estética en Pereira: toxina botulínica (bótox), ácido hialurónico, bioestimuladores, skinboosters, peelings, microagujas y manejo de manchas. También medicina vascular.",
    "url": DOMINIO, "telephone": TELEFONO_VISIBLE, "image": DOMINIO + "/" + foto_jpg("recepcion"),
    "address": {"@type": "PostalAddress", "streetAddress": "Torre Médica Oval", "addressLocality": "Pereira", "addressRegion": "Risaralda", "addressCountry": "CO"},
    "areaServed": [{"@type": "City", "name": c} for c in AREA],
    "medicalSpecialty": "Dermatology",
    "availableService": [{"@type": "MedicalProcedure", "name": t["nombre"], "url": DOMINIO + "/" + t["slug"]} for t in ESTETICA + BUSQUEDAS],
}


def medica_ld():
    return {"@context": "https://schema.org", "@type": "Physician", "@id": DOMINIO + "/" + MEDICA_ESTETICA["slug"] + "#medica",
            "name": MEDICA_ESTETICA["nombre"], "description": MEDICA_ESTETICA["titulo"], "jobTitle": MEDICA_ESTETICA["titulo"],
            "image": DOMINIO + "/" + MEDICA_ESTETICA["foto"] + ".jpg", "url": DOMINIO + "/" + MEDICA_ESTETICA["slug"],
            "medicalSpecialty": "Dermatology", "knowsAbout": [t["nombre"] for t in ESTETICA + BUSQUEDAS],
            "worksFor": {"@id": DOMINIO + "/#clinica"}}


def vascular_ld():
    return {"@context": "https://schema.org", "@type": "Physician", "name": MEDICO_VASCULAR["nombre"],
            "description": MEDICO_VASCULAR["titulo"], "medicalSpecialty": "Cardiovascular",
            "url": MEDICO_VASCULAR["perfil"], "sameAs": [MEDICO_VASCULAR["perfil"], MEDICO_VASCULAR["doctoralia"]],
            "worksFor": {"@id": DOMINIO + "/#clinica"}}


def tu_medica():
    """Bloque 'Tu médica' (Dra. Valeria Enciso) para medicina estética."""
    return '''<section class="bloque"><div class="caja organico">
  <div class="gota rev"><img src="%s.webp" alt="%s, médica estética de The Skin Haus en Pereira" loading="lazy"></div>
  <div class="tarjeta rev"><p class="ceja">Tu médica</p><h2 style="margin-top:22px;font-size:clamp(34px,4vw,56px)">Dra. Valeria <em>Enciso.</em></h2>
  <p class="cargo">%s · The Skin Haus</p>
  <p class="sub" style="margin-top:22px">Te escucha, te valora y te acompaña en tus tratamientos de medicina estética, con el criterio de la casa: menos, mejor puesto, y resultados que respetan quién eres.</p>
  <div class="acciones" style="margin-top:30px"><a class="btn lleno" href="valoracion">Agenda tu valoración</a><a class="enlace" href="%s">Conoce a la Dra. Enciso %s</a></div></div>
</div></section>''' % (MEDICA_ESTETICA["foto"], MEDICA_ESTETICA["nombre"], MEDICA_ESTETICA["titulo"], MEDICA_ESTETICA["slug"], CIRC)


def migas_ld(pasos):
    """pasos = [(nombre, ruta), ...] desde el inicio."""
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i, "name": n, "item": DOMINIO + "/" + r} for i, (n, r) in enumerate(pasos, 1)]}


def faq_ld(pares):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}} for q, a in pares]}


def secciones(lista, ceja="En detalle"):
    """Bloque de lectura larga (h2 + párrafos) para las páginas de tratamiento."""
    if not lista:
        return ""
    cuerpo = "".join('<h2 class="rev">%s</h2><div class="rev">%s</div>' % (h, html) for h, html in lista)
    return '''<section class="bloque" style="padding-top:0"><div class="caja"><div class="lectura">
  <p class="ceja rev">%s</p>%s
</div></div></section>''' % (ceja, cuerpo)

FRASES = ["Belleza que se acompaña", "Tu piel también tiene planes", "Primero te escuchamos", "Resultados sutiles y armónicos", "El cuidado continúa después de tu cita"]


# ---------------------------------------------------------------- inicio
def inicio():
    acciones = '<div class="acciones rev"><a class="btn lleno" href="valoracion">Agenda tu valoración</a><a class="enlace" href="#especialidades">Conoce los tratamientos %s</a></div>' % CIRC

    cuerpo = hero("Medicina estética y vascular en %s" % CIUDAD, "Tu piel también <em>tiene planes.</em>",
                  "Una clínica que combina criterio médico, acompañamiento cercano y resultados armónicos. Sofisticación sin distancia.",
                  "retrato", "manos", acciones, alt="Mujer con piel natural y luz suave", h1_ceja=True) + '''

<section class="bloque" id="especialidades"><div class="caja">
  <div class="centro"><p class="ceja rev">Dos especialidades, una mirada</p><h2 class="rev" style="margin-top:22px">Piel y circulación, <em>cuidadas juntas.</em></h2>
  <p class="sub rev" style="margin-top:24px">Lo que se ve en la piel muchas veces empieza más adentro. Por eso reunimos medicina estética y medicina vascular en un mismo lugar, con el mismo criterio.</p></div>
  <div class="dupla">
    <a class="rev" href="medicina-estetica"><div class="arco"><img src="%s" alt="Médica evaluando la piel del rostro de una paciente" loading="lazy"></div>
      <div class="pie-arco"><div><h3>Medicina estética</h3><p>Toxina, ácido hialurónico, bioestimuladores, calidad de piel y manchas.</p></div>%s</div></a>
    <a class="rev" href="medicina-vascular" data-vel="-0.06"><div class="arco"><img src="%s" alt="Eco-doppler venoso en consulta" loading="lazy"></div>
      <div class="pie-arco"><div><h3>Medicina vascular</h3><p>Arañitas, várices, eco-doppler y rojeces del rostro.</p></div>%s</div></a>
  </div>
</div></section>

<section class="bloque" style="padding-top:0"><div class="caja">
  <div class="centro"><p class="ceja rev">Tratamientos</p><h2 class="rev" style="margin-top:22px">Lo que podemos <em>cuidar juntos.</em></h2></div>
  <div class="pestanas rev" role="tablist">
    <button role="tab" aria-selected="true" data-pan="p-est">Medicina estética</button><button role="tab" aria-selected="false" data-pan="p-vas">Medicina vascular</button>
  </div>
  <div class="panel" id="p-est">%s%s</div>
  <div class="panel" id="p-vas" hidden>%s</div>
  <p class="nota-lista centro">Todo empieza con una valoración médica.</p>
</div></section>

<section class="bloque"><div class="caja organico">
  <div class="gota rev"><img src="%s" alt="Conversación entre médica y paciente" loading="lazy"></div>
  <div class="tarjeta rev">
    <p class="ceja">Nuestra forma de trabajar</p>
    <h2 style="margin-top:22px;font-size:clamp(34px,4vw,56px)">Medicina estética con <em>criterio propio.</em></h2>
    <div class="pares">
      <div><p class="ceja">Para</p><p>Personas que buscan verse y sentirse mejor sin perder naturalidad.</p></div>
      <div><p class="ceja">Ofrecemos</p><p>Una experiencia médica personalizada, serena y transparente.</p></div>
      <div><p class="ceja">Porque</p><p>La confianza nace de entender cada decisión y sentirse acompañada.</p></div>
    </div>
  </div>
</div></section>

%s

%s

%s

%s''' % (foto("facial"), CIRC, foto("vascular"), CIRC, tarjetas(ESTETICA), busquedas_enlaces(), tarjetas(VASCULAR), foto("consulta"),
         camino(en_isla=False), blog.del_blog(), manifiesto("Cuidamos la piel con ciencia, sensibilidad y una mirada profundamente personal. Belleza que se acompaña, no que se impone."), cierre())
    pagina("index", "Medicina estética en Pereira · The Skin Haus",
           "Clínica de medicina estética en Pereira: bótox, ácido hialurónico, bioestimuladores, manchas y calidad de piel, con criterio médico. También medicina vascular.",
           cuerpo, jsonld=[CLINICA_LD, {"@context": "https://schema.org", "@type": "WebSite", "name": MARCA, "url": DOMINIO + "/"}])


def busquedas_enlaces():
    # 27-oct-2026: "Lo más buscado en Pereira" con las palabras que escribe la gente (bótox, ácido hialurónico)
    locales = [("toxina-botulinica", "Bótox en Pereira"), ("acido-hialuronico", "Ácido hialurónico")]
    return '<p class="busquedas rev"><span>Lo más buscado en Pereira:</span> %s</p>' % " · ".join(
        '<a href="%s">%s</a>' % par for par in locales + [(b["slug"], b["nombre"]) for b in BUSQUEDAS])


# ---------------------------------------------------------------- páginas de especialidad
def tarjetas(lista, etiqueta=""):
    return '<div class="rejilla-trat">%s</div>' % "".join(tarjeta_trat(t) for t in lista)


def especialidad(archivo, ceja, titulo, sub, img, img2, lista, etiqueta, intro_h, intro_p, titulo_seo, desc_seo, extra="", ld_extra=()):
    cuerpo = hero(ceja, titulo, sub, img, img2, '<div class="acciones rev"><a class="btn lleno" href="valoracion">Agenda tu valoración</a></div>', corto=True, h1_ceja=True) + '''
<section class="bloque" style="padding-top:clamp(40px,5vw,70px)"><div class="isla" style="padding:clamp(80px,10vw,140px) 0"><div class="caja">
  <div class="centro"><p class="ceja rev">Tratamientos</p><h2 class="rev" style="margin-top:22px">%s</h2><p class="sub rev" style="margin-top:24px">%s</p></div>
  %s
</div></div></section>
%s
%s
%s''' % (intro_h, intro_p, tarjetas(lista, etiqueta), extra, camino(), cierre())
    pagina(archivo, titulo_seo, desc_seo, cuerpo, activo=archivo, jsonld=[CLINICA_LD, migas_ld([("Inicio", ""), (etiqueta == "Estética" and "Medicina estética" or "Medicina vascular", archivo)])] + list(ld_extra), imagen=img)


def paginas_especialidad():
    especialidad("medicina-estetica", "Medicina estética en Pereira", "Resultados que <em>respetan tu identidad.</em>",
                 "Tratamientos médicos para la calidad, la firmeza y la armonía de tu piel. Sutiles, dosificados y pensados para ti.",
                 "facial", "manos", ESTETICA, "Estética",
                 "Lo que podemos <em>cuidar juntos.</em>", "Cada tratamiento empieza con una valoración: miramos tu piel en reposo y en movimiento, tus hábitos y lo que quieres lograr.",
                 "Tratamientos de medicina estética en Pereira · The Skin Haus",
                 "Medicina estética en Pereira: bótox, ácido hialurónico, relleno de labios, bioestimuladores, skinboosters, peelings, microagujas y manchas, con criterio médico.",
                 ld_extra=[faq_ld(PREGUNTAS_ESTETICA), medica_ld()],
                 extra='''<section class="bloque" style="padding-top:0"><div class="caja">
  <div class="centro"><p class="ceja rev">También tratamos</p><h2 class="rev" style="margin-top:22px">Lo que más se busca <em>en Pereira.</em></h2></div>
  %s
</div></section>
%s
<section class="bloque"><div class="caja organico inv"><div class="gota rev"><img src="%s" alt="Cabina de tratamiento" loading="lazy"></div>
<div class="tarjeta rev"><p class="ceja">Nuestro criterio</p><h2 style="margin-top:22px;font-size:clamp(34px,4vw,56px)">Menos, <em>mejor puesto.</em></h2>
<p class="sub" style="margin-top:24px">No trabajamos con paquetes genéricos ni con la promesa de un antes y un después. Trabajamos con planes por etapas, dosis precisas y controles, para que el cambio se sienta tuyo.</p></div></div></section>
<section class="bloque" style="padding-top:0"><div class="caja">
  <div class="centro"><p class="ceja rev">Preguntas frecuentes</p><h2 class="rev" style="margin-top:22px">Antes de <em>tu primera cita.</em></h2></div>
  %s
  <p class="centro rev" style="margin-top:28px"><a class="enlace" href="preguntas-frecuentes">Más preguntas frecuentes %s</a></p>
</div></section>
%s''' % (tarjetas(BUSQUEDAS), tu_medica(), foto("cabina"), faq(PREGUNTAS_ESTETICA), CIRC, blog.del_blog("Del blog", "Para leer <em>antes de decidir.</em>")))
    senales = ["Pesadez o cansancio al final del día", "Hinchazón en tobillos", "Calambres nocturnos o ardor",
               "Venas abultadas o arañitas que aumentan", "Cambios de color en la piel", "Antecedentes familiares de várices"]
    especialidad("medicina-vascular", "Medicina vascular · Pereira", "Piernas ligeras, <em>decisiones claras.</em>",
                 "Diagnóstico y tratamiento de arañitas, várices y rojeces con técnicas mínimamente invasivas y ambulatorias.",
                 "vascular", "piel", VASCULAR, "Vascular",
                 "Lo que la piel muestra, <em>la circulación lo explica.</em>", "Muchas arañitas y várices son la señal visible de una insuficiencia venosa. Por eso empezamos con un eco-doppler: para tratar la causa y no solo lo que se ve.",
                 "Medicina vascular en Pereira · Arañitas y várices · The Skin Haus",
                 "Tratamiento de arañitas vasculares, várices, eco-doppler venoso y cuperosis en Pereira. Técnicas mínimamente invasivas y valoración médica.",
                 extra='''<section class="bloque"><div class="caja centro"><p class="ceja rev">Señales para consultar</p><h2 class="rev" style="margin-top:22px">Tus piernas <em>te avisan.</em></h2>
<div class="chips grandes rev" style="justify-content:center;margin-top:50px">%s</div></div></section>
<section class="bloque" style="padding-top:0"><div class="isla" style="padding:clamp(70px,9vw,120px) 0"><div class="caja centro">
  <p class="ceja rev">Tu especialista</p><h2 class="rev" style="margin-top:22px">%s</h2>
  <p class="sub rev" style="margin-top:20px">%s. Atiende medicina vascular en The Skin Haus, en Pereira, y también en <a class="subrayado" href="%s" target="_blank" rel="noopener">Seravena, en Medellín</a>.</p>
  <p class="rev" style="margin-top:30px"><a class="enlace" href="%s" target="_blank" rel="noopener">Ver su perfil completo %s</a></p>
</div></div></section>''' % ("".join('<span class="chip">%s</span>' % s for s in senales), MEDICO_VASCULAR["nombre"], MEDICO_VASCULAR["titulo"], MEDICO_VASCULAR["perfil"], MEDICO_VASCULAR["perfil"], CIRC),
                 ld_extra=[vascular_ld()])


# ---------------------------------------------------------------- tratamiento
NOMBRE_DE = {t["slug"]: t["nombre"] for t in TODOS + BUSQUEDAS}


def tratamiento(t, hermanos, esp_slug, esp_nombre, etiqueta, padre=None):
    """Página de un tratamiento. padre = slug del tratamiento del que depende (páginas de BUSQUEDAS)."""
    seo = SEO.get(t["slug"], t)          # BUSQUEDAS traen su SEO en el mismo dict
    if padre:
        p = next(x for x in ESTETICA if x["slug"] == padre)
        rel = [p] + [h for h in BUSQUEDAS if h["slug"] != t["slug"] and h.get("padre") == padre][:1]
        rel += [h for h in ESTETICA if h["slug"] not in (padre, t["slug"])][:3 - len(rel)]
        ceja = '<a href="%s">%s</a> · Pereira' % (padre, p["nombre"])
        migas = [("Inicio", ""), (esp_nombre, esp_slug), (p["nombre"], padre), (t["nombre"], t["slug"])]
    else:
        # 27-oct-2026: primero las páginas que dependen de esta (bótox → hiperhidrosis; ácido hialurónico → labios, ojeras…)
        hijos = [b for b in BUSQUEDAS if b.get("padre") == t["slug"]]
        rel = (hijos + [h for h in hermanos if h["slug"] != t["slug"]])[:3]
        ceja = '<a href="%s">%s</a> · Pereira' % (esp_slug, esp_nombre)
        migas = [("Inicio", ""), (esp_nombre, esp_slug), (t["nombre"], t["slug"])]
    dur, ses, rec = t["como"]
    principal = foto_trat(t)
    if principal != t["foto"]:
        circ_foto = t["foto"]           # con foto propia, el círculo muestra la foto genérica de antes
    else:
        circ_foto = {"facial": "piel", "retrato": "manos", "piel": "facial-detalle", "vascular": "vascular-detalle", "manos": "piel"}.get(t["foto"], "manos")
    acciones = '<div class="acciones rev"><a class="btn lleno" href="valoracion">Agenda tu valoración</a><a class="enlace" href="%s" target="_blank" rel="noopener">Pregúntanos %s</a></div>' % (
        wa("Hola, quiero información sobre %s en The Skin Haus." % t["nombre"].lower()), CIRC)
    preguntas = list(t["faq"]) + list(seo.get("faq", []) if seo is not t else [])
    alt = "%s en Pereira: %s" % (t["nombre"], t["linea"][0].lower() + t["linea"][1:].rstrip("."))
    cuerpo = hero(ceja, seo.get("h1", t["nombre"]), t["linea"], principal, circ_foto, acciones, corto=True, alt=alt) + '''
<section class="bloque" style="padding-top:clamp(40px,5vw,70px)"><div class="caja" style="max-width:1040px">
  <p class="ceja rev centro">Qué es</p>
  <p class="rev centro" style="font-family:var(--serif-texto);font-size:clamp(22px,2.4vw,32px);line-height:1.45;margin-top:26px">%s</p>
  <div class="burbujas rev"><div class="burbuja"><p class="ceja">Duración</p><p>%s</p></div><div class="burbuja"><p class="ceja">Sesiones</p><p>%s</p></div><div class="burbuja"><p class="ceja">Recuperación</p><p>%s</p></div></div>
  <p class="aviso rev centro">Los tiempos son orientativos. En tu valoración te decimos qué aplica a tu caso.</p>
</div></section>
<section class="bloque" style="padding-top:0"><div class="caja centro">
  <p class="ceja rev">Para quién</p><h2 class="rev" style="margin-top:22px">¿Es <em>para ti?</em></h2>
  <div class="chips grandes rev" style="justify-content:center;margin-top:44px">%s</div>
  <p class="frase-marca rev" style="margin-top:44px">Evaluamos antes de recomendar.</p>%s
</div></section>
%s
<section class="bloque" style="padding-top:0"><div class="caja">
  <div class="centro"><p class="ceja rev">Preguntas frecuentes</p><h2 class="rev" style="margin-top:22px">Lo que suelen <em>preguntarnos.</em></h2></div>
  %s
  <p class="centro rev" style="margin-top:28px"><a class="enlace" href="preguntas-frecuentes">Más preguntas frecuentes %s</a></p>
</div></section>
%s
<section class="bloque" style="padding-top:0"><div class="isla" style="padding:clamp(70px,9vw,120px) 0"><div class="caja">
  <div class="centro"><p class="ceja rev">También te puede interesar</p></div>%s
</div></div></section>
%s''' % (t["intro"], dur, ses, rec, "".join('<span class="chip">%s</span>' % x for x in t["para"]),
         ('\n  <p class="rev" style="margin-top:18px">Te valora la <a class="subrayado" href="%s">%s</a>, médica estética de The Skin Haus.</p>' % (
             MEDICA_ESTETICA["slug"], MEDICA_ESTETICA["nombre"]) if esp_slug == "medicina-estetica" else ""),
         secciones(seo.get("secciones", [])), faq(preguntas), CIRC, blog.lecturas(t["slug"]), tarjetas(rel, etiqueta),
         cierre("Conversemos sobre lo que <em>quieres cuidar.</em>"))
    url = DOMINIO + "/" + t["slug"]
    ld = [CLINICA_LD,
          {"@context": "https://schema.org", "@type": "MedicalProcedure", "name": t["nombre"], "url": url,
           "description": t["intro"], "howPerformed": t["intro"], "provider": {"@id": DOMINIO + "/#clinica"},
           "image": DOMINIO + "/" + foto_jpg(principal)},
          faq_ld(preguntas), migas_ld(migas)]
    titulo = seo.get("titulo", "%s en Pereira · The Skin Haus" % t["nombre"])
    desc = seo.get("desc", "%s %s" % (t["linea"], t["intro"][:110].rsplit(" ", 1)[0] + "…"))
    pagina(t["slug"], titulo, desc, cuerpo, activo=esp_slug, jsonld=ld, imagen=principal)


# ---------------------------------------------------------------- nosotros
def nosotros():
    ideas = [("Propósito", "Ayudar a cada persona a sentirse bien en su propia piel, con decisiones informadas."),
             ("Promesa", "Acompañamiento médico claro y resultados que respetan la identidad."),
             ("Diferencial", "Sofisticación sin distancia: precisión clínica con una experiencia cálida."),
             ("Idea rectora", "Belleza que se acompaña, no que se impone.")]
    ideas_html = "".join('<div class="paso rev"><p class="num">%d</p><p class="ceja">%s</p><p>%s</p></div>' % (i, a, b) for i, (a, b) in enumerate(ideas, 1))
    valoras = ["Naturalidad", "Criterio profesional", "Privacidad", "Calidez visible", "Información clara", "Escucha real", "Seguridad", "Seguimiento"]
    evitamos = ["Excesos", "Promesas mágicas", "Presión comercial", "Resultados genéricos"]
    cuerpo = hero("Qué es The Skin Haus", "Piel real. <em>Cuidado real.</em>",
                  "Una clínica de medicina estética y vascular en Pereira que combina criterio médico, acompañamiento cercano y resultados armónicos.",
                  "recepcion", "manos", corto=True, alt="Recepción de The Skin Haus") + '''
<section class="bloque" style="padding-top:clamp(40px,5vw,70px)"><div class="isla" style="padding:clamp(80px,10vw,140px) 0"><div class="caja">
  <div class="centro"><p class="ceja rev">La marca en cuatro ideas</p><h2 class="rev" style="margin-top:22px">Lo que <em>nos mueve.</em></h2>
  <p class="frase-marca rev" style="margin-top:24px">Cuidamos la piel con ciencia, sensibilidad y una mirada profundamente personal.</p></div>
  <div class="camino"><svg class="curva" aria-hidden="true"><path d=""/></svg><div class="pasos">%s</div></div>
</div></div></section>
<section class="bloque"><div class="caja centro">
  <p class="ceja rev">A quién le hablamos</p><h2 class="rev" style="margin-top:22px">No a una edad: <em>a una actitud.</em></h2>
  <p class="frase-marca rev" style="margin-top:24px">Hablar con la persona, nunca con su inseguridad.</p>
  <div class="chips grandes rev" style="justify-content:center;margin-top:50px">%s</div>
  <p class="ceja rev" style="margin-top:60px">Lo que evitamos</p>
  <div class="chips rev" style="justify-content:center;margin-top:20px">%s</div>
</div></section>
<section class="bloque" style="padding-top:0"><div class="caja">
  <div class="centro"><p class="ceja rev">Quién te atiende</p><h2 class="rev" style="margin-top:22px">Médicos que <em>te explican.</em></h2></div>
  <div class="equipo">
    <article class="medico rev" id="valeria-enciso"><div class="arco"><img src="%s.webp" alt="%s, médica estética de The Skin Haus" loading="lazy"></div>
      <p class="ceja">Medicina estética</p><h3>%s</h3><p>%s. Valora y acompaña tus tratamientos de medicina estética: bótox, ácido hialurónico, bioestimuladores y calidad de piel.</p>
      <a class="enlace" href="dra-valeria-enciso">Conoce a la Dra. Enciso %s</a></article>
    <article class="medico rev"><div class="arco ini"><span>JP</span></div>
      <p class="ceja">Medicina vascular</p><h3>%s</h3><p>%s. Atiende arañitas, várices e insuficiencia venosa en Pereira y también en <a class="subrayado" href="%s" target="_blank" rel="noopener">Seravena, Medellín</a>.</p>
      <a class="enlace" href="medicina-vascular">Ver tratamientos %s</a></article>
  </div>
</div></section>
<section class="bloque" style="padding-top:0"><div class="caja">
  <div class="centro"><p class="ceja rev">El espacio</p><h2 class="rev" style="margin-top:22px">Un lugar para <em>bajar el ritmo.</em></h2></div>
  <div class="galeria"><div class="arco rev"><img src="%s" alt="Recepción" loading="lazy"></div>
  <div class="der"><div class="circulo rev"><img src="%s" alt="Detalle de cuidado de la piel" loading="lazy"></div><div class="gota rev"><img src="%s" alt="Cabina de tratamiento" loading="lazy"></div></div></div>
</div></section>
%s
%s''' % (ideas_html, "".join('<span class="chip">%s</span>' % v for v in valoras),
         "".join('<span class="chip" style="text-decoration:line-through">%s</span>' % v for v in evitamos),
         MEDICA_ESTETICA["foto"], MEDICA_ESTETICA["nombre"], MEDICA_ESTETICA["nombre"], MEDICA_ESTETICA["titulo"], CIRC,
         MEDICO_VASCULAR["nombre"], MEDICO_VASCULAR["titulo"], MEDICO_VASCULAR["perfil"], CIRC,
         foto("recepcion"), foto("manos"), foto("cabina"), secciones(NOSOTROS_TEXTO, "Más sobre nosotros"), cierre())
    pagina("nosotros", "Nosotros · The Skin Haus Pereira", "The Skin Haus: medicina estética y vascular en Pereira con criterio médico, acompañamiento cercano y resultados armónicos.",
           cuerpo, activo="nosotros", jsonld=[CLINICA_LD, medica_ld(), vascular_ld()], imagen="recepcion")


# ---------------------------------------------------------------- valoración
def valoracion():
    opciones = "".join("<option>%s</option>" % t["nombre"] for t in ESTETICA + BUSQUEDAS + VASCULAR)
    cuerpo = '''
<section class="bloque" style="padding-top:clamp(150px,16vw,210px);overflow:hidden"><div class="aura a1"></div><div class="caja contacto sobre">
  <div>
    <p class="ceja rev">Agenda tu valoración</p><h1 class="rev" style="margin:24px 0 28px;font-size:clamp(46px,6vw,88px)">Conversemos sobre lo que <em>quieres cuidar.</em></h1>
    <p class="sub rev">Cuéntanos qué te interesa y te respondemos por WhatsApp para encontrar tu espacio. Sin compromiso y sin presión.</p>
    <div class="info-contacto rev">
      <div><p class="ceja">WhatsApp</p><p><a class="enlace" style="letter-spacing:.08em" href="%s" target="_blank" rel="noopener">%s %s</a></p></div>
      <div><p class="ceja">Dónde estamos</p><p>%s</p></div>
    </div>
  </div>
  <form class="form isla rev" id="form-valoracion" data-wa="%s" data-clarity-mask="true" style="margin:0">
    <label><span class="ceja">Tu nombre</span><input name="nombre" required autocomplete="name"></label>
    <label><span class="ceja">¿Qué te interesa?</span><select name="interes"><option value="">Aún no sé, quiero orientación</option>%s</select></label>
    <label><span class="ceja">Cuéntanos un poco (opcional)</span><textarea name="mensaje" placeholder="Lo que quieres cuidar, dudas, horarios que te sirven…"></textarea></label>
    <button class="btn lleno" type="submit">Enviar por WhatsApp %s</button>
    <p class="aviso" style="margin-top:0">Tus datos solo se usan para responderte. Se abrirá WhatsApp con tu mensaje listo.</p>
  </form>
</div></section>
<section class="bloque" style="padding-top:0"><div class="caja">
  <div class="centro"><p class="ceja rev">Tu primera cita</p><h2 class="rev" style="margin-top:22px">Qué pasa en <em>tu valoración.</em></h2></div>
  <div class="camino"><svg class="curva" aria-hidden="true"><path d=""/></svg><div class="pasos">%s</div></div>
</div></section>
<section class="bloque" style="padding-top:0"><div class="isla" style="padding:clamp(70px,9vw,120px) 0"><div class="caja centro">
  <p class="ceja rev">Para que aprovechemos el tiempo</p><h2 class="rev" style="margin-top:22px">Qué <em>traer.</em></h2>
  <div class="chips grandes rev" style="justify-content:center;margin-top:44px">%s</div>
</div></div></section>
%s
<section class="bloque" style="padding-top:0"><div class="caja">
  <div class="centro"><p class="ceja rev">Preguntas frecuentes</p><h2 class="rev" style="margin-top:22px">Antes de <em>agendar.</em></h2></div>
  %s
  <p class="centro rev" style="margin-top:28px"><a class="enlace" href="preguntas-frecuentes">Más preguntas frecuentes %s</a></p>
</div></section>''' % (wa(), TELEFONO_VISIBLE, CIRC, DIRECCION, WHATSAPP, opciones, FL,
         "".join('<div class="paso rev"><p class="num">%d</p><p class="ceja">%s</p><p>%s</p></div>' % (i, a, b) for i, (a, b) in enumerate(VALORACION_PASOS, 1)),
         "".join('<span class="chip">%s</span>' % x for x in VALORACION_TRAER), secciones(VALORACION_TEXTO, "Antes de tu cita"), faq(VALORACION_FAQ), CIRC)
    pagina("valoracion", "Agenda tu valoración · The Skin Haus Pereira", "Agenda tu valoración médica en The Skin Haus, en la Torre Médica Oval de Pereira. Te respondemos por WhatsApp para encontrar tu espacio, sin compromiso.",
           cuerpo, activo="valoracion", jsonld=[CLINICA_LD, faq_ld(VALORACION_FAQ), migas_ld([("Inicio", ""), ("Agenda tu valoración", "valoracion")])], imagen="cabina", precarga=False)

# ---------------------------------------------------------------- página de la médica estética (27-oct-2026)
def medica():
    m = MEDICA_ESTETICA
    acciones = '<div class="acciones rev"><a class="btn lleno" href="valoracion">Agenda tu valoración</a><a class="enlace" href="%s" target="_blank" rel="noopener">Escríbenos por WhatsApp %s</a></div>' % (
        wa("Hola, quiero agendar una valoración con la Dra. Valeria Enciso en The Skin Haus."), CIRC)
    lista = "".join('<li><a href="%s">%s</a></li>' % (t["slug"], t["nombre"]) for t in ESTETICA + BUSQUEDAS)
    traer = "".join("<li>%s.</li>" % x for x in VALORACION_TRAER)
    texto = [
        ("Tu médica estética en Pereira",
         "<p>La Dra. Valeria Enciso es la médica estética de The Skin Haus, en la Torre Médica Oval de Pereira. Te escucha, te valora y te acompaña en tus tratamientos de medicina estética: <a href=\"toxina-botulinica\">bótox</a>, <a href=\"acido-hialuronico\">ácido hialurónico</a>, <a href=\"bioestimuladores\">bioestimuladores</a> y calidad de piel.</p>"
         "<p>Atiende a pacientes de Pereira, Dosquebradas, Santa Rosa de Cabal, La Virginia y Cartago. La primera cita siempre es una <a href=\"valoracion\">valoración presencial</a>: por WhatsApp agendamos y resolvemos dudas generales, pero el plan se decide en persona.</p>"),
        ("Cómo trabaja",
         "<p>Con el criterio de la casa: menos, mejor puesto. Antes de recomendar nada, mira tu rostro en reposo y en movimiento, conversa contigo sobre lo que quieres cuidar y lo que no quieres cambiar, y te explica las opciones con tiempos, cuidados y costos claros.</p>"
         "<p>Los planes se arman por etapas y con controles. Si hace falta, es preferible quedarse corto y completar en el control que pasarse. Y si algo no te va a favorecer, te lo dice aunque lo traigas en la lista.</p>"),
        ("Tratamientos que valora y acompaña", "<ul>%s</ul>" % lista),
        ("Antes de tu cita con ella",
         "<p>Para aprovechar el tiempo de la valoración, ten a mano:</p><ul>%s</ul>"
         "<p>En muchos casos puedes hacerte el tratamiento ese mismo día, si la médica lo considera adecuado y tú te sientes lista o listo para decidir.</p>" % traer),
        ("Cómo verificar a cualquier médico",
         "<p>En Colombia puedes consultar si un profesional de la salud está autorizado para ejercer en el <a href=\"https://web.sispro.gov.co/THS/Cliente/ConsultasPublicas/ConsultaPublicaDeTHxIdentificacion.aspx\" target=\"_blank\" rel=\"noopener\">RETHUS</a>, el registro del Ministerio de Salud. Se busca con el número de documento o con el nombre y el primer apellido, y muestra la profesión y el estado de autorización.</p>"
         "<p>Y el producto también se verifica: pregunta su nombre y búscalo en la <a href=\"https://www.invima.gov.co/consulta-registros-sanitarios\" target=\"_blank\" rel=\"noopener\">consulta de registros sanitarios del INVIMA</a>. Si quieres más criterios, lee <a href=\"blog/como-elegir-medico-estetico-en-pereira\">cómo elegir médico estético en Pereira</a>.</p>"),
    ]
    preguntas = [
        ("¿Dónde atiende la Dra. Valeria Enciso?", "En The Skin Haus, en la Torre Médica Oval de Pereira. Atiende pacientes de Pereira, Dosquebradas, Santa Rosa de Cabal, La Virginia y Cartago."),
        ("¿Cómo agendo una valoración con ella?", "Escríbenos por WhatsApp al %s o deja tus datos en la página de valoración y te respondemos para encontrar tu espacio." % TELEFONO_VISIBLE),
        ("¿La valoración es presencial?", "Sí. Por WhatsApp agendamos y resolvemos dudas generales, pero el diagnóstico y el plan se hacen en persona."),
        ("¿Puedo hacerme el tratamiento el mismo día de la valoración?", "En muchos casos sí, si la médica lo considera adecuado y tú te sientes lista o listo para decidir."),
        ("¿Cómo verifico que un médico está autorizado para ejercer?", "En el RETHUS, el registro del Ministerio de Salud. Se consulta con el número de documento o con el nombre y el primer apellido del profesional, y muestra su profesión y su estado de autorización."),
    ]
    rel = [x for x in ESTETICA if x["slug"] in ("toxina-botulinica", "acido-hialuronico")] + [x for x in BUSQUEDAS if x["slug"] == "relleno-de-labios"]
    cuerpo = (hero("Médica estética · Pereira", "Dra. Valeria <em>Enciso.</em>",
                   "Médica estética de The Skin Haus, en la Torre Médica Oval de Pereira. Primero te escucha; luego recomienda.",
                   m["foto"], "piel", acciones, corto=True, alt="%s, médica estética de The Skin Haus en Pereira" % m["nombre"])
              + secciones(texto, "Quién te atiende")
              + '<section class="bloque" style="padding-top:0"><div class="caja">'
              + '<div class="centro"><p class="ceja rev">Preguntas frecuentes</p><h2 class="rev" style="margin-top:22px">Antes de <em>agendar con ella.</em></h2></div>'
              + faq(preguntas) + '</div></section>'
              + '<section class="bloque" style="padding-top:0"><div class="isla" style="padding:clamp(70px,9vw,120px) 0"><div class="caja">'
              + '<div class="centro"><p class="ceja rev">Lo que más le consultan</p></div>' + tarjetas(rel) + '</div></div></section>'
              + cierre("Agenda con la <em>Dra. Enciso.</em>"))
    pagina(m["slug"], "Dra. Valeria Enciso · Médica estética en Pereira",
           "Dra. Valeria Enciso, médica estética de The Skin Haus en la Torre Médica Oval de Pereira: valoración presencial, bótox, ácido hialurónico, bioestimuladores y calidad de piel.",
           cuerpo, activo="nosotros", imagen=m["foto"], tipo="profile",
           jsonld=[CLINICA_LD, medica_ld(), {"@context": "https://schema.org", "@type": "ProfilePage", "url": DOMINIO + "/" + m["slug"],
                                              "mainEntity": {"@id": DOMINIO + "/" + m["slug"] + "#medica"}},
                   faq_ld(preguntas), migas_ld([("Inicio", ""), ("Nosotros", "nosotros"), (m["nombre"], m["slug"])])])


# ---------------------------------------------------------------- preguntas frecuentes (27-oct-2026)
PREGUNTAS_LOCALES = [
    ("¿Dónde queda The Skin Haus?", "En la Torre Médica Oval de Pereira. Atendemos pacientes de toda el área: Pereira, Dosquebradas, Santa Rosa de Cabal, La Virginia y Cartago."),
    ("¿Cómo agendo una cita?", "Por WhatsApp al %s o dejando tus datos en la página de valoración. Te respondemos para encontrar tu espacio." % TELEFONO_VISIBLE),
    ("¿Cuánto cuestan los tratamientos?", "Depende de la zona, del producto y de la cantidad que necesites. Te damos el valor exacto en la valoración, antes de empezar, para que decidas con toda la información."),
]
PREGUNTAS_SEGURIDAD = [
    ("¿Cómo sé que mi médico está autorizado para ejercer?", "Puedes consultarlo en el RETHUS, el registro del Ministerio de Salud, con el número de documento o con el nombre y el primer apellido del profesional. Muestra su profesión y su estado de autorización."),
    ("¿Cómo sé si el producto es legal?", "Pregunta el nombre del producto y búscalo en la consulta de registros sanitarios del INVIMA, la entidad que los emite en Colombia."),
    ("¿Los resultados son iguales para todas las personas?", "No. Los resultados varían en cada persona y todo procedimiento tiene riesgos. Por eso la indicación siempre sale de una valoración médica."),
]


def preguntas_frecuentes():
    generales = PREGUNTAS_LOCALES + PREGUNTAS_GENERALES + VALORACION_FAQ[len(PREGUNTAS_GENERALES):] + PREGUNTAS_ESTETICA[2:3]
    vistos, grupos = set(q for q, _ in generales), []
    for t in ESTETICA + BUSQUEDAS:
        seo = SEO.get(t["slug"], t)
        extra = list(seo.get("faq", [])) if seo is not t else []
        todas = [q for q in extra if "Pereira" in q[0]] + list(t["faq"]) + [q for q in extra if "Pereira" not in q[0]]
        elegidas = []
        for q in todas:
            if q[0] not in vistos and len(elegidas) < 4:
                vistos.add(q[0])
                elegidas.append(q)
        grupos.append((t, elegidas))
    indice = " · ".join('<a href="preguntas-frecuentes#%s">%s</a>' % (t["slug"], t["nombre"]) for t, _ in grupos)
    bloques = "".join(
        '<section class="bloque" style="padding-top:0" id="%s"><div class="caja">'
        '<div class="centro"><p class="ceja rev">%s</p><h2 class="rev" style="margin-top:22px">Preguntas sobre <em>%s.</em></h2></div>'
        '%s<p class="centro rev" style="margin-top:28px"><a class="enlace" href="%s">Todo sobre %s en Pereira %s</a></p>'
        '</div></section>\n' % (t["slug"], t["nombre"], t["nombre"].lower(), faq(qs), t["slug"], t["nombre"].lower(), CIRC)
        for t, qs in grupos)
    cuerpo = (hero("Preguntas frecuentes sobre medicina estética en Pereira", "Lo que suelen <em>preguntarnos.</em>",
                   "Respuestas claras sobre la valoración, los tratamientos, los tiempos y la seguridad. Lo que aplica a tu caso lo definimos en persona.",
                   "consulta", "manos", '<div class="acciones rev"><a class="btn lleno" href="valoracion">Agenda tu valoración</a></div>',
                   corto=True, h1_ceja=True, alt="Conversación entre médica y paciente")
              + '<section class="bloque" style="padding-top:clamp(40px,5vw,70px)"><div class="caja">'
              + '<div class="centro"><p class="ceja rev">Antes de tu primera cita</p><h2 class="rev" style="margin-top:22px">La valoración y <em>cómo agendar.</em></h2></div>'
              + faq(generales) + '<p class="busquedas rev"><span>Por tratamiento:</span> %s</p></div></section>\n' % indice
              + '<section class="bloque" style="padding-top:0"><div class="isla" style="padding:clamp(70px,9vw,120px) 0"><div class="caja">'
              + '<div class="centro"><p class="ceja rev">Seguridad</p><h2 class="rev" style="margin-top:22px">Cómo decidir <em>con tranquilidad.</em></h2></div>'
              + faq(PREGUNTAS_SEGURIDAD) + '</div></div></section>\n'
              + bloques + cierre())
    pagina("preguntas-frecuentes", "Preguntas frecuentes de medicina estética en Pereira",
           "Respuestas sobre bótox, ácido hialurónico, relleno de labios, bioestimuladores, manchas y la valoración en The Skin Haus, Torre Médica Oval de Pereira.",
           cuerpo, activo="medicina-estetica", imagen="consulta",
           jsonld=[CLINICA_LD, faq_ld(generales + PREGUNTAS_SEGURIDAD), migas_ld([("Inicio", ""), ("Preguntas frecuentes", "preguntas-frecuentes")])])


# ---------------------------------------------------------------- 404 y reseñas (27-oct-2026)
def pagina_404():
    cuerpo = (hero("Error 404", "Esta página <em>no existe.</em>",
                   "Puede que la dirección haya cambiado o tenga un error. Aquí tienes lo que más buscan nuestras pacientes en Pereira.",
                   "piel", "manos", '<div class="acciones rev"><a class="btn lleno" href="./">Ir al inicio</a><a class="enlace" href="preguntas-frecuentes">Preguntas frecuentes %s</a></div>' % CIRC,
                   corto=True, alt="Piel cuidada")
              + '<section class="bloque" style="padding-top:clamp(40px,5vw,70px)"><div class="caja">'
              + '<div class="centro"><p class="ceja rev">Tratamientos</p><h2 class="rev" style="margin-top:22px">Lo más <em>buscado.</em></h2></div>'
              + tarjetas(ESTETICA[:3] + BUSQUEDAS[:3]) + busquedas_enlaces() + '</div></section>\n'
              + cierre())
    pagina("404", "Página no encontrada · The Skin Haus", "La página que buscas no existe. Mira los tratamientos de medicina estética de The Skin Haus en Pereira.",
           cuerpo, robots="noindex", imagen="piel", precarga=False)


def resena():
    """/resena: a donde lleva el QR del consultorio. Con RESENA_URL (datos.py) redirige a la ficha de Google."""
    if RESENA_URL:
        boton = '<a class="btn lleno" href="%s" rel="noopener">Escribir mi reseña en Google</a>' % RESENA_URL
        refresco = '\n<meta http-equiv="refresh" content="0;url=%s">' % RESENA_URL
    else:
        boton = '<a class="btn lleno" href="%s" target="_blank" rel="noopener">Cuéntanos por WhatsApp</a>' % wa("Hola, quiero contarles cómo me fue en The Skin Haus.")
        refresco = ""
    cuerpo = hero("Gracias por venir", "¿Cómo te <em>fue?</em>",
                  "Tu opinión ayuda a otras personas de Pereira a decidir con tranquilidad. Te toma un minuto.",
                  "manos", "piel", '<div class="acciones rev">%s</div>' % boton, corto=True, alt="Manos cuidadas")
    pagina("resena", "Cuéntanos cómo te fue · The Skin Haus", "Deja tu reseña de The Skin Haus, medicina estética en Pereira.",
           cuerpo, robots="noindex", imagen="manos", precarga=False, extra_head=refresco)



def extras():
    fijas = ["", "medicina-estetica", "medicina-vascular", "nosotros", "valoracion", MEDICA_ESTETICA["slug"], "preguntas-frecuentes"] + [t["slug"] for t in ESTETICA + BUSQUEDAS + VASCULAR]
    filas = [(u, ACTUALIZADO) for u in fijas] + blog.para_sitemap()
    with open(os.path.join(AQUI, "sitemap.xml"), "w") as f:
        # 27-oct-2026: cada tratamiento declara su foto propia (para salir en Google Imágenes)
        imgs = {t["slug"]: foto_jpg(foto_trat(t)) for t in ESTETICA + BUSQUEDAS + VASCULAR if foto_trat(t) == t["slug"]}
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
                'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n%s</urlset>\n' % "".join(
            "  <url><loc>%s/%s</loc><lastmod>%s</lastmod>%s</url>\n" % (
                DOMINIO, u, d, "<image:image><image:loc>%s/%s</image:loc></image:image>" % (DOMINIO, imgs[u]) if u in imgs else "")
            for u, d in filas))
    with open(os.path.join(AQUI, "robots.txt"), "w") as f:
        f.write("User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n" % DOMINIO)
    # llms.txt: resumen para buscadores con IA (ChatGPT, Perplexity, Gemini). 27-oct-2026: equipo, cómo agendar,
    # zona que atendemos y preguntas frecuentes en texto plano, para que la IA pueda recomendar con datos correctos.
    def plano(s):
        return re.sub("<[^>]+>", "", s)
    lin = ["# %s" % MARCA, "",
           "> Clínica de medicina estética en la Torre Médica Oval de Pereira (Risaralda, Colombia). Atiende pacientes de "
           "%s. Valoración médica presencial; se agenda por WhatsApp %s. También atiende medicina vascular." % (", ".join(AREA[:-1]) + " y " + AREA[-1], TELEFONO_VISIBLE), "",
           "## Datos clave",
           "- Nombre: The Skin Haus (no confundir con negocios de nombre parecido). Web oficial: %s" % DOMINIO,
           "- Dónde: Torre Médica Oval, Pereira, Risaralda, Colombia.",
           "- Cómo agendar: WhatsApp %s o %s/valoracion" % (TELEFONO_VISIBLE, DOMINIO),
           "- Primera cita: valoración médica presencial, sin compromiso de hacerse ningún tratamiento. El valor de cada tratamiento se da en la valoración.",
           "- Criterio: menos, mejor puesto; planes por etapas, dosis precisas y controles; resultados naturales.", "",
           "## Equipo médico",
           "- [%s](%s/%s): %s de The Skin Haus. Valora y acompaña los tratamientos de medicina estética." % (MEDICA_ESTETICA["nombre"], DOMINIO, MEDICA_ESTETICA["slug"], MEDICA_ESTETICA["titulo"].lower().capitalize()),
           "- %s: %s. Atiende medicina vascular en The Skin Haus." % (MEDICO_VASCULAR["nombre"], MEDICO_VASCULAR["titulo"]), "",
           "## Medicina estética"]
    lin += ["- [%s](%s/%s): %s" % (t["nombre"], DOMINIO, t["slug"], t["linea"]) for t in ESTETICA + BUSQUEDAS]
    lin += ["", "## Medicina vascular"] + ["- [%s](%s/%s): %s" % (t["nombre"], DOMINIO, t["slug"], t["linea"]) for t in VASCULAR]
    lin += ["", "## Preguntas frecuentes", "Todas en %s/preguntas-frecuentes" % DOMINIO, ""]
    for q, a in PREGUNTAS_LOCALES + PREGUNTAS_GENERALES[1:] + PREGUNTAS_SEGURIDAD[:2]:
        lin += ["### %s" % q, plano(a), ""]
    lin += ["## Blog"] + ["- [%s](%s/blog/%s): %s" % (a["title"], DOMINIO, a["slug"], a["descripcion"]) for a in blog.cargar()]
    lin += ["", "## La clínica", "- [Nosotros](%s/nosotros)" % DOMINIO, "- [Agenda tu valoración](%s/valoracion)" % DOMINIO,
            "- [Preguntas frecuentes](%s/preguntas-frecuentes)" % DOMINIO]
    with open(os.path.join(AQUI, "llms.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(lin) + "\n")
    with open(os.path.join(AQUI, "assets", "favicon.svg"), "w") as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><circle cx="32" cy="32" r="32" fill="#F3EEE5"/><text x="32" y="42" text-anchor="middle" font-family="Georgia,serif" font-size="26" fill="#111">SH</text></svg>')


blog.configurar(globals())

if __name__ == "__main__":
    inicio()
    paginas_especialidad()
    for t in ESTETICA:
        tratamiento(t, ESTETICA, "medicina-estetica", "Medicina estética", "Estética")
    for t in BUSQUEDAS:
        tratamiento(t, ESTETICA, "medicina-estetica", "Medicina estética", "Estética", padre=t["padre"])
    for t in VASCULAR:
        tratamiento(t, VASCULAR, "medicina-vascular", "Medicina vascular", "Vascular")
    nosotros()
    valoracion()
    medica()
    preguntas_frecuentes()
    pagina_404()
    resena()
    n_blog = blog.generar()
    extras()
    print("listo:", 7 + len(TODOS) + len(BUSQUEDAS), "páginas (+ 404 y reseña) +", n_blog, "artículos del blog")
