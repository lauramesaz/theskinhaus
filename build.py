# -*- coding: utf-8 -*-
# The Skin Haus · genera todas las páginas a partir de datos.py.   Uso:  python3 build.py
# v3 "fluida": arcos, círculos, gotas, islas marfil, cinta de frases y camino con curva.
import os, time, json, re
from urllib.parse import quote
from datos import *
import blog

AQUI = os.path.dirname(os.path.abspath(__file__))
V = int(time.time())
FL = "&#8594;"  # flecha
CIRC = '<span class="circ">%s</span>' % FL


def wa(msg="Hola, quiero agendar una valoración en The Skin Haus."):
    return "https://wa.me/%s?text=%s" % (WHATSAPP, quote(msg))


def foto(n):
    return "assets/fotos/%s.webp" % n          # WebP: ~65 % más liviano (19-oct-2026)


def foto_jpg(n):
    return "assets/fotos/%s.jpg" % n           # para redes sociales y datos estructurados


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
  <div><h4>Medicina estética</h4><ul>%s<li><a href="medicina-estetica">Ver todos</a></li><li><a href="blog/">Blog</a></li></ul></div>
  <div><h4>Medicina vascular</h4><ul>%s</ul></div>
  <div><h4>Visítanos</h4><ul><li>%s</li><li><a href="%s" target="_blank" rel="noopener">WhatsApp %s</a></li></ul></div>
</div>
<div class="pie-final"><span>The Skin Haus · %s · Colombia</span><span>Los resultados varían en cada persona. Toda indicación requiere valoración médica.</span></div>
</div></footer>''' % (logo("completo", True), est, vas, DIRECCION, wa(), TELEFONO_VISIBLE, CIUDAD)


WA_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5c-.2 0-.4.1-.7.3-.2.3-.9.9-.9 2.2s.9 2.5 1 2.7c.1.2 1.8 2.8 4.4 3.9 1.6.7 2.3.8 3.1.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3z"/></svg>'

SELLO = '''<svg class="sello" viewBox="0 0 124 124" aria-hidden="true"><defs><path id="rueda" d="M62,62 m-46,0 a46,46 0 1,1 92,0 a46,46 0 1,1 -92,0"/></defs>
<text><textPath href="#rueda" textLength="286" lengthAdjust="spacing">Estética · Vascular · Pereira · The Skin Haus ·</textPath></text><circle cx="62" cy="62" r="3" fill="#C6A88F"/></svg>'''


def pagina(archivo, titulo, descripcion, cuerpo, activo="", jsonld=None, imagen="retrato", tipo="website", precarga=True):
    url = DOMINIO + "/" + ("" if archivo == "index" else archivo[:-5] if archivo.endswith("/index") else archivo)
    ld = '<script type="application/ld+json">%s</script>' % json.dumps(jsonld, ensure_ascii=False) if jsonld else ""
    html = '''<!doctype html>
<html lang="es-CO">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<base href="/">
<title>%s</title>
<meta name="description" content="%s">
<link rel="canonical" href="%s">
<meta property="og:type" content="%s"><meta property="og:title" content="%s"><meta property="og:description" content="%s">
<meta property="og:url" content="%s"><meta property="og:image" content="%s/%s"><meta property="og:locale" content="es_CO">
<meta name="theme-color" content="#FAF8F3">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
%s<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@1,400;1,500&family=Libre+Caslon+Display&family=Libre+Caslon+Text:ital@0;1&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
<noscript><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@1,400;1,500&family=Libre+Caslon+Display&family=Libre+Caslon+Text:ital@0;1&display=swap" rel="stylesheet"></noscript>
<link rel="stylesheet" href="assets/estilo.css?v=%d">
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
</html>''' % (titulo, descripcion, url, tipo, titulo, descripcion, url, DOMINIO, foto_jpg(imagen),
              '<link rel="preload" as="image" href="%s" fetchpriority="high">\n' % foto(imagen) if precarga else "", V, ld,
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
    return '<p class="busquedas rev"><span>También:</span> %s</p>' % " · ".join(
        '<a href="%s">%s</a>' % (b["slug"], b["nombre"]) for b in BUSQUEDAS)


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
                 ld_extra=[faq_ld(PREGUNTAS_ESTETICA)],
                 extra='''<section class="bloque" style="padding-top:0"><div class="caja">
  <div class="centro"><p class="ceja rev">También tratamos</p><h2 class="rev" style="margin-top:22px">Lo que más se busca <em>en Pereira.</em></h2></div>
  %s
</div></section>
<section class="bloque"><div class="caja organico inv"><div class="gota rev"><img src="%s" alt="Cabina de tratamiento" loading="lazy"></div>
<div class="tarjeta rev"><p class="ceja">Nuestro criterio</p><h2 style="margin-top:22px;font-size:clamp(34px,4vw,56px)">Menos, <em>mejor puesto.</em></h2>
<p class="sub" style="margin-top:24px">No trabajamos con paquetes genéricos ni con la promesa de un antes y un después. Trabajamos con planes por etapas, dosis precisas y controles, para que el cambio se sienta tuyo.</p></div></div></section>
<section class="bloque" style="padding-top:0"><div class="caja">
  <div class="centro"><p class="ceja rev">Preguntas frecuentes</p><h2 class="rev" style="margin-top:22px">Antes de <em>tu primera cita.</em></h2></div>
  %s
</div></section>
%s''' % (tarjetas(BUSQUEDAS), foto("cabina"), faq(PREGUNTAS_ESTETICA), blog.del_blog("Del blog", "Para leer <em>antes de decidir.</em>")))
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
                 ld_extra=[{"@context": "https://schema.org", "@type": "Physician", "name": MEDICO_VASCULAR["nombre"],
                            "description": MEDICO_VASCULAR["titulo"], "medicalSpecialty": "Cardiovascular",
                            "url": MEDICO_VASCULAR["perfil"], "sameAs": [MEDICO_VASCULAR["perfil"], MEDICO_VASCULAR["doctoralia"]],
                            "worksFor": {"@id": DOMINIO + "/#clinica"}}])


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
        rel = [h for h in hermanos if h["slug"] != t["slug"]][:3]
        ceja = '<a href="%s">%s</a> · Pereira' % (esp_slug, esp_nombre)
        migas = [("Inicio", ""), (esp_nombre, esp_slug), (t["nombre"], t["slug"])]
    dur, ses, rec = t["como"]
    circ_foto = {"facial": "piel", "retrato": "manos", "piel": "facial-detalle", "vascular": "vascular-detalle", "manos": "piel"}.get(t["foto"], "manos")
    acciones = '<div class="acciones rev"><a class="btn lleno" href="valoracion">Agenda tu valoración</a><a class="enlace" href="%s" target="_blank" rel="noopener">Pregúntanos %s</a></div>' % (
        wa("Hola, quiero información sobre %s en The Skin Haus." % t["nombre"].lower()), CIRC)
    preguntas = list(t["faq"]) + list(seo.get("faq", []) if seo is not t else [])
    cuerpo = hero(ceja, seo.get("h1", t["nombre"]), t["linea"], t["foto"], circ_foto, acciones, corto=True, alt=t["nombre"]) + '''
<section class="bloque" style="padding-top:clamp(40px,5vw,70px)"><div class="caja" style="max-width:1040px">
  <p class="ceja rev centro">Qué es</p>
  <p class="rev centro" style="font-family:var(--serif-texto);font-size:clamp(22px,2.4vw,32px);line-height:1.45;margin-top:26px">%s</p>
  <div class="burbujas rev"><div class="burbuja"><p class="ceja">Duración</p><p>%s</p></div><div class="burbuja"><p class="ceja">Sesiones</p><p>%s</p></div><div class="burbuja"><p class="ceja">Recuperación</p><p>%s</p></div></div>
  <p class="aviso rev centro">Los tiempos son orientativos. En tu valoración te decimos qué aplica a tu caso.</p>
</div></section>
<section class="bloque" style="padding-top:0"><div class="caja centro">
  <p class="ceja rev">Para quién</p><h2 class="rev" style="margin-top:22px">¿Es <em>para ti?</em></h2>
  <div class="chips grandes rev" style="justify-content:center;margin-top:44px">%s</div>
  <p class="frase-marca rev" style="margin-top:44px">Evaluamos antes de recomendar.</p>
</div></section>
%s
<section class="bloque" style="padding-top:0"><div class="caja">
  <div class="centro"><p class="ceja rev">Preguntas frecuentes</p><h2 class="rev" style="margin-top:22px">Lo que suelen <em>preguntarnos.</em></h2></div>
  %s
</div></section>
%s
<section class="bloque" style="padding-top:0"><div class="isla" style="padding:clamp(70px,9vw,120px) 0"><div class="caja">
  <div class="centro"><p class="ceja rev">También te puede interesar</p></div>%s
</div></div></section>
%s''' % (t["intro"], dur, ses, rec, "".join('<span class="chip">%s</span>' % x for x in t["para"]),
         secciones(seo.get("secciones", [])), faq(preguntas), blog.lecturas(t["slug"]), tarjetas(rel, etiqueta),
         cierre("Conversemos sobre lo que <em>quieres cuidar.</em>"))
    url = DOMINIO + "/" + t["slug"]
    ld = [CLINICA_LD,
          {"@context": "https://schema.org", "@type": "MedicalProcedure", "name": t["nombre"], "url": url,
           "description": t["intro"], "howPerformed": t["intro"], "provider": {"@id": DOMINIO + "/#clinica"}},
          faq_ld(preguntas), migas_ld(migas)]
    titulo = seo.get("titulo", "%s en Pereira · The Skin Haus" % t["nombre"])
    desc = seo.get("desc", "%s %s" % (t["linea"], t["intro"][:110].rsplit(" ", 1)[0] + "…"))
    pagina(t["slug"], titulo, desc, cuerpo, activo=esp_slug, jsonld=ld, imagen=t["foto"])


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
  <div class="centro"><p class="ceja rev">El espacio</p><h2 class="rev" style="margin-top:22px">Un lugar para <em>bajar el ritmo.</em></h2></div>
  <div class="galeria"><div class="arco rev"><img src="%s" alt="Recepción" loading="lazy"></div>
  <div class="der"><div class="circulo rev"><img src="%s" alt="Detalle de cuidado de la piel" loading="lazy"></div><div class="gota rev"><img src="%s" alt="Cabina de tratamiento" loading="lazy"></div></div></div>
</div></section>
%s''' % (ideas_html, "".join('<span class="chip">%s</span>' % v for v in valoras),
         "".join('<span class="chip" style="text-decoration:line-through">%s</span>' % v for v in evitamos),
         foto("recepcion"), foto("manos"), foto("cabina"), cierre())
    pagina("nosotros", "Nosotros · The Skin Haus Pereira", "The Skin Haus: medicina estética y vascular en Pereira con criterio médico, acompañamiento cercano y resultados armónicos.",
           cuerpo, activo="nosotros", jsonld=CLINICA_LD, imagen="recepcion")


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
  <form class="form isla rev" id="form-valoracion" data-wa="%s" style="margin:0">
    <label><span class="ceja">Tu nombre</span><input name="nombre" required autocomplete="name"></label>
    <label><span class="ceja">¿Qué te interesa?</span><select name="interes"><option value="">Aún no sé, quiero orientación</option>%s</select></label>
    <label><span class="ceja">Cuéntanos un poco (opcional)</span><textarea name="mensaje" placeholder="Lo que quieres cuidar, dudas, horarios que te sirven…"></textarea></label>
    <button class="btn lleno" type="submit">Enviar por WhatsApp %s</button>
    <p class="aviso" style="margin-top:0">Tus datos solo se usan para responderte. Se abrirá WhatsApp con tu mensaje listo.</p>
  </form>
</div></section>
%s''' % (wa(), TELEFONO_VISIBLE, CIRC, DIRECCION, WHATSAPP, opciones, FL, camino())
    pagina("valoracion", "Agenda tu valoración · The Skin Haus Pereira", "Agenda tu valoración médica en The Skin Haus, en la Torre Médica Oval de Pereira. Te respondemos por WhatsApp para encontrar tu espacio, sin compromiso.",
           cuerpo, activo="valoracion", jsonld=CLINICA_LD, imagen="cabina", precarga=False)


def extras():
    fijas = ["", "medicina-estetica", "medicina-vascular", "nosotros", "valoracion"] + [t["slug"] for t in ESTETICA + BUSQUEDAS + VASCULAR]
    filas = [(u, ACTUALIZADO) for u in fijas] + blog.para_sitemap()
    with open(os.path.join(AQUI, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s</urlset>\n' % "".join(
            "  <url><loc>%s/%s</loc><lastmod>%s</lastmod></url>\n" % (DOMINIO, u, d) for u, d in filas))
    with open(os.path.join(AQUI, "robots.txt"), "w") as f:
        f.write("User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n" % DOMINIO)
    # llms.txt: resumen para buscadores con IA (ChatGPT, Perplexity, Gemini)
    lin = ["# %s" % MARCA, "",
           "> Clínica de medicina estética en la Torre Médica Oval, Pereira (Risaralda, Colombia). Valoración médica presencial. "
           "WhatsApp %s. También atiende medicina vascular." % TELEFONO_VISIBLE, "",
           "## Medicina estética"]
    lin += ["- [%s](%s/%s): %s" % (t["nombre"], DOMINIO, t["slug"], t["linea"]) for t in ESTETICA + BUSQUEDAS]
    lin += ["", "## Blog"] + ["- [%s](%s/blog/%s): %s" % (a["title"], DOMINIO, a["slug"], a["descripcion"]) for a in blog.cargar()]
    lin += ["", "## La clínica", "- [Nosotros](%s/nosotros)" % DOMINIO, "- [Agenda tu valoración](%s/valoracion)" % DOMINIO]
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
    n_blog = blog.generar()
    extras()
    print("listo:", 5 + len(TODOS) + len(BUSQUEDAS), "páginas +", n_blog, "artículos del blog")
