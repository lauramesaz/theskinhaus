# -*- coding: utf-8 -*-
# The Skin Haus · genera todas las páginas a partir de datos.py.   Uso:  python3 build.py
# v3 "fluida": arcos, círculos, gotas, islas marfil, cinta de frases y camino con curva.
import os, time, json, re
from urllib.parse import quote
from datos import *

AQUI = os.path.dirname(os.path.abspath(__file__))
V = int(time.time())
FL = "&#8594;"  # flecha
CIRC = '<span class="circ">%s</span>' % FL


def wa(msg="Hola, quiero agendar una valoración en The Skin Haus."):
    return "https://wa.me/%s?text=%s" % (WHATSAPP, quote(msg))


def foto(n):
    return "assets/fotos/%s.jpg" % n


def logo(clase="compacto", descriptor=False):
    d = '<span class="barra"></span><span class="desc"><span>MEDICAL</span><span>AESTHETICS</span></span>' if descriptor else ""
    return '<span class="logo %s" aria-label="The Skin Haus"><span class="nombre"><span class="the">THE</span><span class="sh">SKIN</span><span class="sh">HAUS</span></span>%s</span>' % (clase, d)


# ---------------------------------------------------------------- piezas
def cabecera(activo):
    items = [("medicina-estetica", "Estética"), ("medicina-vascular", "Vascular"), ("nosotros", "Nosotros")]
    links = "".join('<a href="%s"%s>%s</a>' % (h, ' class="activo"' if h == activo else "", t) for h, t in items)
    return '''<header class="cab"><div class="cab-in">
<a href="./" aria-label="Inicio">%s</a>
<nav class="menu" aria-label="Principal">%s<a class="btn lleno" href="valoracion">Agenda tu valoración</a></nav>
<button class="hamb" aria-label="Menú" aria-expanded="false"><span></span><span></span></button>
</div></header>''' % (logo(), links)


def pie():
    est = "".join('<li><a href="%s">%s</a></li>' % (t["slug"], t["nombre"]) for t in ESTETICA[:6])
    vas = "".join('<li><a href="%s">%s</a></li>' % (t["slug"], t["nombre"]) for t in VASCULAR)
    return '''<footer class="pie-web"><div class="caja">
<div class="pie-grid">
  <div>%s<p class="frase-marca" style="margin-top:36px;max-width:15em">Cuidamos la piel con ciencia, sensibilidad y una mirada profundamente personal.</p></div>
  <div><h4>Medicina estética</h4><ul>%s<li><a href="medicina-estetica">Ver todos</a></li></ul></div>
  <div><h4>Medicina vascular</h4><ul>%s</ul></div>
  <div><h4>Visítanos</h4><ul><li>%s</li><li><a href="%s" target="_blank" rel="noopener">WhatsApp %s</a></li></ul></div>
</div>
<div class="pie-final"><span>The Skin Haus · %s · Colombia</span><span>Los resultados varían en cada persona. Toda indicación requiere valoración médica.</span></div>
</div></footer>''' % (logo("completo", True), est, vas, DIRECCION, wa(), TELEFONO_VISIBLE, CIUDAD)


WA_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5c-.2 0-.4.1-.7.3-.2.3-.9.9-.9 2.2s.9 2.5 1 2.7c.1.2 1.8 2.8 4.4 3.9 1.6.7 2.3.8 3.1.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3z"/></svg>'

SELLO = '''<svg class="sello" viewBox="0 0 124 124" aria-hidden="true"><defs><path id="rueda" d="M62,62 m-46,0 a46,46 0 1,1 92,0 a46,46 0 1,1 -92,0"/></defs>
<text><textPath href="#rueda" textLength="286" lengthAdjust="spacing">Estética · Vascular · Pereira · The Skin Haus ·</textPath></text><circle cx="62" cy="62" r="3" fill="#C6A88F"/></svg>'''


def pagina(archivo, titulo, descripcion, cuerpo, activo="", jsonld=None, imagen="retrato"):
    url = DOMINIO + "/" + ("" if archivo == "index" else archivo)
    ld = '<script type="application/ld+json">%s</script>' % json.dumps(jsonld, ensure_ascii=False) if jsonld else ""
    html = '''<!doctype html>
<html lang="es-CO">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>%s</title>
<meta name="description" content="%s">
<link rel="canonical" href="%s">
<meta property="og:type" content="website"><meta property="og:title" content="%s"><meta property="og:description" content="%s">
<meta property="og:url" content="%s"><meta property="og:image" content="%s/%s"><meta property="og:locale" content="es_CO">
<meta name="theme-color" content="#FAF8F3">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@1,400;1,500&family=Libre+Caslon+Display&family=Libre+Caslon+Text:ital@0;1&display=swap" rel="stylesheet">
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
</html>''' % (titulo, descripcion, url, titulo, descripcion, url, DOMINIO, foto(imagen), V, ld,
              cabecera(activo), cuerpo, pie(), wa(), WA_SVG, V)
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


def hero(ceja, titulo, sub, foto_arco, foto_circ, acciones="", corto=False, alt=""):
    return '''<section class="hero%s">
  <div class="aura a1"></div>
  <div class="texto"><p class="ceja rev">%s</p><h1 class="titular-vivo">%s</h1><p class="sub rev">%s</p>%s</div>
  <div class="compo">%s<div class="arco"><img src="%s" alt="%s" fetchpriority="high"></div><div class="circulo rev" data-vel="-0.08"><img src="%s" alt=""></div></div>
</section>''' % (" corto" if corto else "", ceja, palabras(titulo), sub, acciones, SELLO, foto(foto_arco), alt, foto(foto_circ))


def cinta(frases):
    s = "".join("<span>%s</span>" % f for f in frases)
    return '<div class="cinta" aria-hidden="true"><div class="pista">%s%s</div></div>' % (s, s)


def nube(lista):
    partes = ['<a href="%s">%s</a>' % (t["slug"], t["nombre"]) for t in lista]
    return '<p class="nube rev">%s</p>' % '<span class="pto"></span>'.join(partes)


def faq(pares):
    return '<div class="faq">%s</div>' % "".join(
        '<details class="rev"><summary>%s<span class="circ">+</span></summary><p>%s</p></details>' % p for p in pares)


def cierre(titulo="Hablemos de tu piel.", ceja="Valoración médica"):
    return '''<section class="bloque"><div class="isla lino cierre" style="position:relative">
<div class="aura a1" style="opacity:.8"></div><div class="aura a2"></div>
<div class="flota f1" data-vel="-0.05"><div class="circulo"><img src="assets/fotos/cabina-espejo.jpg" alt="" loading="lazy"></div></div>
<div class="flota f2" data-vel="0.05"><div class="arco"><img src="assets/fotos/manos.jpg" alt="" loading="lazy"></div></div>
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
    "@context": "https://schema.org", "@type": "MedicalClinic", "name": MARCA,
    "description": "Clínica de medicina estética y medicina vascular en Pereira.",
    "url": DOMINIO, "telephone": TELEFONO_VISIBLE, "image": DOMINIO + "/" + foto("recepcion"),
    "address": {"@type": "PostalAddress", "addressLocality": "Pereira", "addressRegion": "Risaralda", "addressCountry": "CO"},
    "medicalSpecialty": "Dermatology",
}

FRASES = ["Belleza que se acompaña", "Tu piel también tiene planes", "Primero te escuchamos", "Resultados sutiles y armónicos", "El cuidado continúa después de tu cita"]


# ---------------------------------------------------------------- inicio
def inicio():
    acciones = '<div class="acciones rev"><a class="btn lleno" href="valoracion">Agenda tu valoración</a><a class="enlace" href="#especialidades">Conoce los tratamientos %s</a></div>' % CIRC

    cuerpo = hero("Medicina estética y vascular · %s" % CIUDAD, "Tu piel también <em>tiene planes.</em>",
                  "Una clínica que combina criterio médico, acompañamiento cercano y resultados armónicos. Sofisticación sin distancia.",
                  "retrato", "manos", acciones, alt="Mujer con piel natural y luz suave") + cinta(FRASES) + '''

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

<section class="bloque" style="padding-top:0"><div class="isla" style="padding:clamp(80px,10vw,140px) 0"><div class="caja">
  <div class="nube-grupo"><p class="ceja rev">Medicina estética</p>%s</div>
  <div class="nube-grupo"><p class="ceja rev">Medicina vascular</p>%s</div>
</div></div></section>

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

<section class="bloque" style="padding-top:0"><div class="isla" style="padding:clamp(80px,10vw,140px) 0"><div class="caja">
  <div class="centro"><p class="ceja rev">Preguntas frecuentes</p><h2 class="rev" style="margin-top:22px">Antes de elegir, <em>entiende.</em></h2></div>
  %s
</div></div></section>

%s''' % (foto("facial"), CIRC, foto("vascular"), CIRC, nube(ESTETICA), nube(VASCULAR), foto("consulta"),
         camino(en_isla=False), manifiesto("Cuidamos la piel con ciencia, sensibilidad y una mirada profundamente personal. Belleza que se acompaña, no que se impone."), faq(PREGUNTAS_GENERALES), cierre())
    pagina("index", "The Skin Haus · Medicina estética y vascular en Pereira",
           "Clínica de medicina estética y vascular en Pereira. Toxina botulínica, ácido hialurónico, bioestimuladores, manchas, arañitas y várices. Agenda tu valoración médica.",
           cuerpo, jsonld=CLINICA_LD)


# ---------------------------------------------------------------- páginas de especialidad
def tarjetas(lista, etiqueta):
    return '<div class="tarjetas">%s</div>' % "".join(
        '<a class="rev" href="%s"><span class="chip" style="align-self:flex-start">%s</span><h3>%s</h3><p>%s</p>%s</a>' % (
            t["slug"], etiqueta, t["nombre"], t["linea"], CIRC) for t in lista)


def especialidad(archivo, ceja, titulo, sub, img, img2, lista, etiqueta, intro_h, intro_p, titulo_seo, desc_seo, extra=""):
    cuerpo = hero(ceja, titulo, sub, img, img2, '<div class="acciones rev"><a class="btn lleno" href="valoracion">Agenda tu valoración</a></div>', corto=True) + '''
<section class="bloque" style="padding-top:clamp(40px,5vw,70px)"><div class="isla" style="padding:clamp(80px,10vw,140px) 0"><div class="caja">
  <div class="centro"><p class="ceja rev">Tratamientos</p><h2 class="rev" style="margin-top:22px">%s</h2><p class="sub rev" style="margin-top:24px">%s</p></div>
  %s
</div></div></section>
%s
%s
%s''' % (intro_h, intro_p, tarjetas(lista, etiqueta), extra, camino(), cierre())
    pagina(archivo, titulo_seo, desc_seo, cuerpo, activo=archivo, jsonld=CLINICA_LD, imagen=img)


def paginas_especialidad():
    especialidad("medicina-estetica", "Medicina estética · Pereira", "Resultados que <em>respetan tu identidad.</em>",
                 "Tratamientos médicos para la calidad, la firmeza y la armonía de tu piel. Sutiles, dosificados y pensados para ti.",
                 "facial", "manos", ESTETICA, "Estética",
                 "Lo que podemos <em>cuidar juntos.</em>", "Cada tratamiento empieza con una valoración: miramos tu piel en reposo y en movimiento, tus hábitos y lo que quieres lograr.",
                 "Medicina estética en Pereira · The Skin Haus",
                 "Toxina botulínica, ácido hialurónico, bioestimuladores, skinboosters, peelings, microagujas y manejo de manchas en Pereira, con criterio médico.",
                 extra='''<section class="bloque"><div class="caja organico inv"><div class="gota rev"><img src="%s" alt="Cabina de tratamiento" loading="lazy"></div>
<div class="tarjeta rev"><p class="ceja">Nuestro criterio</p><h2 style="margin-top:22px;font-size:clamp(34px,4vw,56px)">Menos, <em>mejor puesto.</em></h2>
<p class="sub" style="margin-top:24px">No trabajamos con paquetes genéricos ni con la promesa de un antes y un después. Trabajamos con planes por etapas, dosis precisas y controles, para que el cambio se sienta tuyo.</p></div></div></section>''' % foto("cabina"))
    senales = ["Pesadez o cansancio al final del día", "Hinchazón en tobillos", "Calambres nocturnos o ardor",
               "Venas abultadas o arañitas que aumentan", "Cambios de color en la piel", "Antecedentes familiares de várices"]
    especialidad("medicina-vascular", "Medicina vascular · Pereira", "Piernas ligeras, <em>decisiones claras.</em>",
                 "Diagnóstico y tratamiento de arañitas, várices y rojeces con técnicas mínimamente invasivas y ambulatorias.",
                 "vascular", "piel", VASCULAR, "Vascular",
                 "Lo que la piel muestra, <em>la circulación lo explica.</em>", "Muchas arañitas y várices son la señal visible de una insuficiencia venosa. Por eso empezamos con un eco-doppler: para tratar la causa y no solo lo que se ve.",
                 "Medicina vascular en Pereira · Arañitas y várices · The Skin Haus",
                 "Tratamiento de arañitas vasculares, várices, eco-doppler venoso y cuperosis en Pereira. Técnicas mínimamente invasivas y valoración médica.",
                 extra='''<section class="bloque"><div class="caja centro"><p class="ceja rev">Señales para consultar</p><h2 class="rev" style="margin-top:22px">Tus piernas <em>te avisan.</em></h2>
<div class="chips grandes rev" style="justify-content:center;margin-top:50px">%s</div></div></section>''' % "".join('<span class="chip">%s</span>' % s for s in senales))


# ---------------------------------------------------------------- tratamiento
def tratamiento(t, hermanos, esp_slug, esp_nombre, etiqueta):
    rel = [h for h in hermanos if h["slug"] != t["slug"]][:3]
    dur, ses, rec = t["como"]
    circ_foto = {"facial": "piel", "retrato": "manos", "piel": "facial-detalle", "vascular": "vascular-detalle"}.get(t["foto"], "manos")
    acciones = '<div class="acciones rev"><a class="btn lleno" href="valoracion">Agenda tu valoración</a><a class="enlace" href="%s" target="_blank" rel="noopener">Pregúntanos %s</a></div>' % (
        wa("Hola, quiero información sobre %s en The Skin Haus." % t["nombre"].lower()), CIRC)
    cuerpo = hero('<a href="%s">%s</a> · Pereira' % (esp_slug, esp_nombre), t["nombre"], t["linea"], t["foto"], circ_foto, acciones, corto=True, alt=t["nombre"]) + '''
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
<section class="bloque"><div class="caja">
  <div class="centro"><p class="ceja rev">Preguntas frecuentes</p><h2 class="rev" style="margin-top:22px">Lo que suelen <em>preguntarnos.</em></h2></div>
  %s
</div></section>
<section class="bloque" style="padding-top:0"><div class="isla" style="padding:clamp(70px,9vw,120px) 0"><div class="caja">
  <div class="centro"><p class="ceja rev">También te puede interesar</p></div>%s
</div></div></section>
%s''' % (t["intro"], dur, ses, rec, "".join('<span class="chip">%s</span>' % p for p in t["para"]),
         camino(), faq(t["faq"]), tarjetas(rel, etiqueta), cierre("Conversemos sobre lo que <em>quieres cuidar.</em>"))
    ld = [CLINICA_LD, {"@context": "https://schema.org", "@type": "MedicalProcedure", "name": t["nombre"], "description": t["intro"]},
          {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
              {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]}]
    pagina(t["slug"], "%s en Pereira · The Skin Haus" % t["nombre"], "%s %s" % (t["linea"], t["intro"][:110].rsplit(" ", 1)[0] + "…"),
           cuerpo, activo=esp_slug, jsonld=ld, imagen=t["foto"])


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
                  "recepcion", "manos", corto=True, alt="Recepción de The Skin Haus") + cinta(FRASES) + '''
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
    opciones = "".join("<option>%s</option>" % t["nombre"] for t in TODOS)
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
    pagina("valoracion", "Agenda tu valoración · The Skin Haus Pereira", "Agenda tu valoración médica en The Skin Haus, clínica de medicina estética y vascular en Pereira.",
           cuerpo, activo="valoracion", jsonld=CLINICA_LD, imagen="cabina")


def extras():
    urls = ["", "medicina-estetica", "medicina-vascular", "nosotros", "valoracion"] + [t["slug"] for t in TODOS]
    with open(os.path.join(AQUI, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s</urlset>\n' % "".join(
            "  <url><loc>%s/%s</loc></url>\n" % (DOMINIO, u) for u in urls))
    with open(os.path.join(AQUI, "robots.txt"), "w") as f:
        f.write("User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n" % DOMINIO)
    with open(os.path.join(AQUI, "assets", "favicon.svg"), "w") as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><circle cx="32" cy="32" r="32" fill="#F3EEE5"/><text x="32" y="42" text-anchor="middle" font-family="Georgia,serif" font-size="26" fill="#111">SH</text></svg>')


if __name__ == "__main__":
    inicio()
    paginas_especialidad()
    for t in ESTETICA:
        tratamiento(t, ESTETICA, "medicina-estetica", "Medicina estética", "Estética")
    for t in VASCULAR:
        tratamiento(t, VASCULAR, "medicina-vascular", "Medicina vascular", "Vascular")
    nosotros()
    valoracion()
    extras()
    print("listo:", 5 + len(TODOS), "páginas")
