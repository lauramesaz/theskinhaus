# -*- coding: utf-8 -*-
# The Skin Haus · genera todas las páginas a partir de datos.py.   Uso:  python3 build.py
import os, time, json
from urllib.parse import quote
from datos import *

AQUI = os.path.dirname(os.path.abspath(__file__))
V = int(time.time())
FL = "&#8594;"  # flecha


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
    hor = "".join("<li>%s<br>%s</li>" % h for h in HORARIO)
    return '''<footer class="pie-web"><div class="caja">
<div class="pie-grid">
  <div>%s<p class="frase-marca" style="margin-top:36px;max-width:15em">Cuidamos la piel con ciencia, sensibilidad y una mirada profundamente personal.</p></div>
  <div><h4>Medicina estética</h4><ul>%s<li><a href="medicina-estetica">Ver todos</a></li></ul></div>
  <div><h4>Medicina vascular</h4><ul>%s</ul></div>
  <div><h4>Visítanos</h4><ul><li>%s</li>%s<li><a href="%s" target="_blank" rel="noopener">WhatsApp %s</a></li><li><a href="%s" target="_blank" rel="noopener">Instagram</a></li></ul></div>
</div>
<div class="pie-final"><span>The Skin Haus · %s · Colombia</span><span>Los resultados varían en cada persona. Toda indicación requiere valoración médica.</span></div>
</div></footer>''' % (logo("completo", True), est, vas, DIRECCION, hor, wa(), TELEFONO_VISIBLE, INSTAGRAM, CIUDAD)


WA_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5c-.2 0-.4.1-.7.3-.2.3-.9.9-.9 2.2s.9 2.5 1 2.7c.1.2 1.8 2.8 4.4 3.9 1.6.7 2.3.8 3.1.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3z"/></svg>'


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
<link href="https://fonts.googleapis.com/css2?family=Libre+Caslon+Display&family=Libre+Caslon+Text:ital@0;1&display=swap" rel="stylesheet">
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


def filas(lista, numerar=True):
    out = ""
    for i, t in enumerate(lista, 1):
        out += '<li class="rev"><a href="%s"><span class="n">%02d</span><b>%s</b><span class="d">%s</span><span class="fl">%s</span></a></li>' % (
            t["slug"], i, t["nombre"], t["linea"], FL)
    return '<ul class="filas">%s</ul>' % out


def faq(pares):
    return '<div class="faq">%s</div>' % "".join(
        '<details class="rev"><summary>%s<i>+</i></summary><p>%s</p></details>' % p for p in pares)


def cierre(titulo="Hablemos de tu piel.", ceja="Valoración médica", fondo="fondo-nude"):
    return '''<section class="bloque cierre %s"><div class="caja">
<p class="ceja rev">%s</p><h2 class="rev">%s</h2>
<p class="sub rev" style="margin:26px auto 0">Primero te escuchamos. Luego recomendamos.</p>
<div class="acciones rev"><a class="btn lleno" href="valoracion">Agenda tu valoración</a><a class="enlace" href="%s" target="_blank" rel="noopener">Escríbenos por WhatsApp</a></div>
</div></section>''' % (fondo, ceja, titulo, wa())


def camino():
    ideas = "".join('<div class="idea rev"><p class="num">%02d</p><p class="ceja">%s</p><p>%s</p></div>' % (i, t, d)
                    for i, (t, d) in enumerate(CAMINO, 1))
    return '''<section class="bloque"><div class="caja">
<div class="dos" style="margin-bottom:clamp(56px,7vw,96px)"><div class="izq"><p class="ceja rev">Así es tu camino</p><h2 class="rev" style="margin-top:24px">Belleza que se acompaña.</h2></div>
<div><p class="sub rev" style="margin-top:12px">La confianza nace de entender cada decisión. Por eso nada empieza con una aguja: empieza con una conversación.</p></div></div>
<div class="ideas cuatro">%s</div>
</div></section>''' % ideas


CLINICA_LD = {
    "@context": "https://schema.org", "@type": "MedicalClinic", "name": MARCA,
    "description": "Clínica de medicina estética y medicina vascular en Pereira.",
    "url": DOMINIO, "telephone": TELEFONO_VISIBLE, "image": DOMINIO + "/" + foto("recepcion"),
    "address": {"@type": "PostalAddress", "addressLocality": "Pereira", "addressRegion": "Risaralda", "addressCountry": "CO"},
    "medicalSpecialty": "Dermatology",
}


# ---------------------------------------------------------------- inicio
def inicio():
    esp = '''<div class="especialidades">
<a class="esp rev" href="medicina-estetica"><figure><img src="%s" alt="Médica evaluando la piel del rostro de una paciente" loading="lazy"></figure>
<div class="pie"><div><p class="ceja fina">01</p><h3 style="margin-top:14px">Medicina estética</h3><p>Toxina, ácido hialurónico, bioestimuladores, calidad de piel y manchas. Resultados sutiles y armónicos.</p></div><span>%s</span></div></a>
<a class="esp rev" href="medicina-vascular"><figure><img src="%s" alt="Eco-doppler venoso de piernas en consulta" loading="lazy"></figure>
<div class="pie"><div><p class="ceja fina">02</p><h3 style="margin-top:14px">Medicina vascular</h3><p>Arañitas, várices, eco-doppler y rojeces del rostro. Diagnóstico preciso antes de tratar.</p></div><span>%s</span></div></a>
</div>''' % (foto("facial"), FL, foto("vascular"), FL)

    voz = [("Decimos", "Evaluamos tu piel antes de recomendar.", ""), ("Evitamos", "Este tratamiento es perfecto para ti.", " no"),
           ("Decimos", "Resultados sutiles, decisiones informadas.", ""), ("Evitamos", "Transforma tu rostro para siempre.", " no")]
    voz_html = "".join('<div class="par%s rev"><p class="ceja">%s</p><p class="frase-marca">%s</p></div>' % (c, a, b) for a, b, c in voz)

    cuerpo = '''
<section class="hero">
  <div class="texto">
    <p class="ceja rev">Medicina estética y vascular · %s</p>
    <h1 class="rev">Tu piel también tiene planes.</h1>
    <p class="sub rev">Una clínica que combina criterio médico, acompañamiento cercano y resultados armónicos. Sofisticación sin distancia.</p>
    <div class="acciones rev"><a class="btn lleno" href="valoracion">Agenda tu valoración</a><a class="enlace" href="#especialidades">Conoce los tratamientos</a></div>
    <div class="pie-hero rev"><span>Pereira</span><span>/</span><span>Colombia</span></div>
  </div>
  <figure><img src="%s" alt="Mujer con piel natural y luz suave" fetchpriority="high"></figure>
</section>

<section class="bloque fondo-arena frase"><div class="caja">
<p class="ceja rev">Idea rectora</p>
<p class="titular rev">Belleza que se acompaña, no que se impone.</p>
</div></section>

<section class="bloque" id="especialidades"><div class="caja">
<div class="dos"><div class="izq"><p class="ceja rev">Dos especialidades, una mirada</p><h2 class="rev" style="margin-top:24px">Piel y circulación, cuidadas juntas.</h2></div>
<div><p class="sub rev" style="margin-top:12px">Lo que se ve en la piel muchas veces empieza más adentro. Por eso reunimos medicina estética y medicina vascular en un mismo lugar, con el mismo criterio.</p></div></div>
%s
</div></section>

<section class="bloque fondo-arena"><div class="caja">
<div class="dos"><div class="izq"><p class="ceja rev">Medicina estética</p><h2 class="rev" style="margin-top:24px">Resultados sutiles, pensados para ti.</h2>
<p class="frase-marca rev">Tu piel cambia. Tu plan también puede hacerlo.</p></div>
<div>%s<div class="acciones rev" style="margin-top:36px"><a class="enlace" href="medicina-estetica">Ver medicina estética</a></div></div></div>
<div class="dos" style="margin-top:clamp(88px,10vw,140px)"><div class="izq"><p class="ceja rev">Medicina vascular</p><h2 class="rev" style="margin-top:24px">Tus venas también hablan.</h2>
<p class="frase-marca rev">Ver antes de decidir.</p></div>
<div>%s<div class="acciones rev" style="margin-top:36px"><a class="enlace" href="medicina-vascular">Ver medicina vascular</a></div></div></div>
</div></section>

%s

<section class="partido fondo-arena">
  <figure><img src="%s" alt="Conversación entre médica y paciente en consulta" loading="lazy"></figure>
  <div class="texto">
    <p class="ceja rev">Nuestra forma de trabajar</p>
    <h2 class="rev" style="margin-top:24px">Medicina estética con criterio propio.</h2>
    <div class="pares">
      <div class="rev"><p class="ceja">Para</p><p>Personas que buscan verse y sentirse mejor sin perder naturalidad.</p></div>
      <div class="rev"><p class="ceja">Ofrecemos</p><p>Una experiencia médica personalizada, serena y transparente.</p></div>
      <div class="rev"><p class="ceja">Porque</p><p>La confianza nace de entender cada decisión y sentirse acompañada.</p></div>
    </div>
  </div>
</section>

<section class="bloque"><div class="caja voz">
  <div><p class="ceja rev">Cómo hablamos</p><h2 class="rev" style="margin-top:24px">Claro. Cercano. Seguro.</h2>
  <p class="frase-marca rev" style="margin-top:clamp(40px,6vw,90px)">Informar sin asustar. Invitar sin presionar. Acompañar sin juzgar.</p></div>
  <div class="lista">%s</div>
</div></section>

<section class="bloque fondo-arena"><div class="caja dos">
  <div class="izq"><p class="ceja rev">Preguntas frecuentes</p><h2 class="rev" style="margin-top:24px">Antes de elegir, entiende.</h2></div>
  <div>%s</div>
</div></section>

%s''' % (CIUDAD, foto("retrato"), esp, filas(ESTETICA), filas(VASCULAR), camino(), foto("consulta"), voz_html,
         faq(PREGUNTAS_GENERALES), cierre())
    pagina("index", "The Skin Haus · Medicina estética y vascular en Pereira",
           "Clínica de medicina estética y vascular en Pereira. Toxina botulínica, ácido hialurónico, bioestimuladores, manchas, arañitas y várices. Agenda tu valoración médica.",
           cuerpo, jsonld=CLINICA_LD)


# ---------------------------------------------------------------- páginas de especialidad
def especialidad(archivo, ceja, titulo, sub, img, lista, frase, intro_h, intro_p, titulo_seo, desc_seo, extra=""):
    cuerpo = '''
<section class="hero corto">
  <div class="texto"><p class="ceja rev">%s</p><h1 class="rev">%s</h1><p class="sub rev">%s</p>
  <div class="acciones rev"><a class="btn lleno" href="valoracion">Agenda tu valoración</a></div></div>
  <figure><img src="%s" alt="" fetchpriority="high"></figure>
</section>
<section class="bloque"><div class="caja dos">
  <div class="izq"><p class="ceja rev">Tratamientos</p><h2 class="rev" style="margin-top:24px">%s</h2><p class="sub rev">%s</p><p class="frase-marca rev">%s</p></div>
  <div>%s</div>
</div></section>
%s
%s
%s''' % (ceja, titulo, sub, foto(img), intro_h, intro_p, frase, filas(lista), extra, camino(), cierre())
    pagina(archivo, titulo_seo, desc_seo, cuerpo, activo=archivo, jsonld=CLINICA_LD, imagen=img)


def paginas_especialidad():
    especialidad("medicina-estetica", "Medicina estética · Pereira", "Resultados que respetan tu identidad.",
                 "Tratamientos médicos para la calidad, la firmeza y la armonía de tu piel. Sutiles, dosificados y pensados para ti.",
                 "facial", ESTETICA, "Primero te escuchamos. Luego recomendamos.",
                 "Lo que podemos cuidar juntos.", "Cada tratamiento empieza con una valoración: miramos tu piel en reposo y en movimiento, tus hábitos y lo que quieres lograr.",
                 "Medicina estética en Pereira · The Skin Haus",
                 "Toxina botulínica, ácido hialurónico, bioestimuladores, skinboosters, peelings, microagujas y manejo de manchas en Pereira, con criterio médico.",
                 extra='''<section class="partido fondo-arena inv"><figure><img src="%s" alt="Cabina de tratamiento" loading="lazy"></figure>
<div class="texto"><p class="ceja rev">Nuestro criterio</p><h2 class="rev" style="margin-top:24px">Menos, mejor puesto.</h2>
<p class="sub rev" style="margin-top:28px">No trabajamos con paquetes genéricos ni con la promesa de un antes y un después. Trabajamos con planes por etapas, dosis precisas y controles, para que el cambio se sienta tuyo.</p></div></section>''' % foto("cabina"))
    especialidad("medicina-vascular", "Medicina vascular · Pereira", "Piernas ligeras, decisiones claras.",
                 "Diagnóstico y tratamiento de arañitas, várices y rojeces con técnicas mínimamente invasivas y ambulatorias.",
                 "vascular", VASCULAR, "Ver antes de decidir.",
                 "Lo que la piel muestra, la circulación lo explica.", "Muchas arañitas y várices son la señal visible de una insuficiencia venosa. Por eso empezamos con un eco-doppler: para tratar la causa y no solo lo que se ve.",
                 "Medicina vascular en Pereira · Arañitas y várices · The Skin Haus",
                 "Tratamiento de arañitas vasculares, várices, eco-doppler venoso y cuperosis en Pereira. Técnicas mínimamente invasivas y valoración médica.",
                 extra='''<section class="bloque fondo-arena"><div class="caja dos">
<div class="izq"><p class="ceja rev">Señales para consultar</p><h2 class="rev" style="margin-top:24px">Tus piernas te avisan.</h2></div>
<div><ul class="puntos">%s</ul></div></div></section>''' % "".join('<li class="rev">%s</li>' % s for s in [
                     "Pesadez o cansancio en las piernas al final del día", "Hinchazón en tobillos que mejora al descansar",
                     "Calambres nocturnos o sensación de ardor", "Venas visibles, abultadas o arañitas que aumentan",
                     "Cambios de color en la piel de las piernas", "Antecedentes familiares de várices"]))


# ---------------------------------------------------------------- tratamiento
def tratamiento(t, grupo, hermanos, esp_slug, esp_nombre):
    rel = [h for h in hermanos if h["slug"] != t["slug"]][:3]
    rel_html = "".join('<a class="rev" href="%s"><p class="ceja fina">%s</p><h3>%s</h3><p>%s</p></a>' % (h["slug"], esp_nombre, h["nombre"], h["linea"]) for h in rel)
    dur, ses, rec = t["como"]
    cuerpo = '''
<section class="hero corto">
  <div class="texto"><p class="ceja rev"><a href="%s">%s</a> · Pereira</p><h1 class="rev">%s</h1><p class="sub rev">%s</p>
  <div class="acciones rev"><a class="btn lleno" href="valoracion">Agenda tu valoración</a><a class="enlace" href="%s" target="_blank" rel="noopener">Pregúntanos por WhatsApp</a></div></div>
  <figure><img src="%s" alt="%s" fetchpriority="high"></figure>
</section>
<section class="bloque"><div class="caja dos">
  <div class="izq"><p class="ceja rev">Qué es</p><h2 class="rev" style="margin-top:24px">Con precisión, sin exceso.</h2></div>
  <div><p class="sub rev" style="margin-top:10px;max-width:none">%s</p>
  <div class="datos rev" style="margin-top:56px"><div><p class="ceja">Duración</p><p>%s</p></div><div><p class="ceja">Sesiones</p><p>%s</p></div><div><p class="ceja">Recuperación</p><p>%s</p></div></div>
  <p class="aviso rev">Los tiempos son orientativos. En tu valoración te decimos qué aplica a tu caso.</p></div>
</div></section>
<section class="bloque fondo-arena"><div class="caja dos">
  <div class="izq"><p class="ceja rev">Para quién</p><h2 class="rev" style="margin-top:24px">¿Es para ti?</h2><p class="frase-marca rev">Evaluamos antes de recomendar.</p></div>
  <div><ul class="puntos">%s</ul></div>
</div></section>
%s
<section class="bloque fondo-arena"><div class="caja dos">
  <div class="izq"><p class="ceja rev">Preguntas frecuentes</p><h2 class="rev" style="margin-top:24px">Lo que suelen preguntarnos.</h2></div>
  <div>%s</div>
</div></section>
<section class="bloque"><div class="caja">
  <p class="ceja rev">También te puede interesar</p><div class="rel">%s</div>
</div></section>
%s''' % (esp_slug, esp_nombre, t["nombre"], t["linea"], wa("Hola, quiero información sobre %s en The Skin Haus." % t["nombre"].lower()),
         foto(t["foto"]), t["nombre"], t["intro"], dur, ses, rec, "".join('<li class="rev">%s</li>' % p for p in t["para"]),
         camino(), faq(t["faq"]), rel_html, cierre("Conversemos sobre lo que quieres cuidar."))
    ld = [CLINICA_LD, {"@context": "https://schema.org", "@type": "MedicalProcedure", "name": t["nombre"], "description": t["intro"],
                       "howPerformed": t["intro"], "procedureType": "https://schema.org/NoninvasiveProcedure"},
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
    ideas_html = "".join('<div class="idea rev"><p class="num">%02d</p><p class="ceja">%s</p><p>%s</p></div>' % (i, a, b) for i, (a, b) in enumerate(ideas, 1))
    valores = [("Valoras", ["Naturalidad", "Criterio profesional", "Privacidad", "Calidez visible"]),
               ("Necesitas", ["Información clara", "Escucha real", "Seguridad", "Seguimiento"]),
               ("Evitamos", ["Excesos", "Promesas mágicas", "Presión comercial", "Resultados genéricos"])]
    val_html = "".join('<div class="rev"><p class="ceja" style="padding-top:22px;border-top:1px solid var(--linea)">%s</p><ul class="puntos" style="margin-top:20px">%s</ul></div>' % (
        a, "".join("<li>%s</li>" % x for x in b)) for a, b in valores)
    cuerpo = '''
<section class="hero corto">
  <div class="texto"><p class="ceja rev">Qué es The Skin Haus</p><h1 class="rev">Cuidado real para piel real.</h1>
  <p class="sub rev">Una clínica de medicina estética y vascular en Pereira que combina criterio médico, acompañamiento cercano y resultados armónicos.</p></div>
  <figure><img src="%s" alt="Recepción de The Skin Haus" fetchpriority="high"></figure>
</section>
<section class="bloque fondo-arena"><div class="caja">
  <div class="dos" style="margin-bottom:clamp(56px,7vw,96px)"><div class="izq"><p class="ceja rev">La marca en cuatro ideas</p><h2 class="rev" style="margin-top:24px">Lo que nos mueve.</h2></div>
  <div><p class="frase-marca rev" style="margin-top:12px">Cuidamos la piel con ciencia, sensibilidad y una mirada profundamente personal.</p></div></div>
  <div class="ideas cuatro">%s</div>
</div></section>
<section class="bloque"><div class="caja">
  <div class="dos"><div class="izq"><p class="ceja rev">A quién le hablamos</p><h2 class="rev" style="margin-top:24px">No a una edad: a una actitud.</h2>
  <p class="frase-marca rev">Hablar con la persona, nunca con su inseguridad.</p></div>
  <div class="ideas" style="grid-template-columns:repeat(3,1fr);gap:28px">%s</div></div>
</div></section>
<section class="bloque fondo-arena"><div class="caja">
  <p class="ceja rev">El espacio</p><h2 class="rev" style="margin-top:24px;max-width:12em">Un lugar pensado para bajar el ritmo.</h2>
  <div class="galeria"><figure class="alta rev"><img src="%s" alt="Recepción" loading="lazy"></figure><figure class="rev"><img src="%s" alt="Cabina de tratamiento" loading="lazy"></figure><figure class="rev"><img src="%s" alt="Detalle de cuidado de la piel" loading="lazy" style="aspect-ratio:16/9"></figure></div>
</div></section>
%s''' % (foto("recepcion"), ideas_html, val_html, foto("recepcion"), foto("cabina"), foto("manos"), cierre())
    pagina("nosotros", "Nosotros · The Skin Haus Pereira", "The Skin Haus: medicina estética y vascular en Pereira con criterio médico, acompañamiento cercano y resultados armónicos.",
           cuerpo, activo="nosotros", jsonld=CLINICA_LD, imagen="recepcion")


# ---------------------------------------------------------------- valoración
def valoracion():
    opciones = "".join("<option>%s</option>" % t["nombre"] for t in TODOS)
    hor = "".join("<p>%s · %s</p>" % h for h in HORARIO)
    cuerpo = '''
<section class="bloque" style="padding-top:clamp(150px,16vw,210px)"><div class="caja contacto">
  <div>
    <p class="ceja rev">Agenda tu valoración</p><h1 class="rev" style="margin:24px 0 28px">Conversemos sobre lo que quieres cuidar.</h1>
    <p class="sub rev">Cuéntanos qué te interesa y te respondemos por WhatsApp para encontrar tu espacio. Sin compromiso y sin presión.</p>
    <div class="info-contacto rev" style="margin-top:56px">
      <div><p class="ceja">WhatsApp</p><p><a class="enlace" style="letter-spacing:.08em" href="%s" target="_blank" rel="noopener">%s</a></p></div>
      <div><p class="ceja">Dónde estamos</p><p>%s</p></div>
      <div><p class="ceja">Horario</p>%s</div>
    </div>
  </div>
  <form class="form rev" id="form-valoracion" data-wa="%s">
    <label><span class="ceja">Tu nombre</span><input name="nombre" required autocomplete="name"></label>
    <label><span class="ceja">¿Qué te interesa?</span><select name="interes"><option value="">Aún no sé, quiero orientación</option>%s</select></label>
    <label><span class="ceja">Cuéntanos un poco (opcional)</span><textarea name="mensaje" placeholder="Lo que quieres cuidar, dudas, horarios que te sirven…"></textarea></label>
    <button class="btn lleno" type="submit">Enviar por WhatsApp %s</button>
    <p class="aviso" style="margin-top:0">Tus datos solo se usan para responderte. Se abrirá WhatsApp con tu mensaje listo.</p>
  </form>
</div></section>
<section class="partido fondo-arena"><figure><img src="%s" alt="Cabina de tratamiento" loading="lazy"></figure>
<div class="texto"><p class="ceja rev">Qué pasa en tu valoración</p><h2 class="rev" style="margin-top:24px">Primero te escuchamos.</h2>
<ul class="puntos" style="margin-top:40px">%s</ul></div></section>''' % (
        wa(), TELEFONO_VISIBLE, DIRECCION, hor, WHATSAPP, opciones, FL, foto("cabina"),
        "".join('<li class="rev"><b>%s.</b> %s</li>' % c for c in CAMINO))
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
        f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" fill="#FAF8F3"/><text x="32" y="44" text-anchor="middle" font-family="Georgia,serif" font-size="30" fill="#111">SH</text></svg>')


if __name__ == "__main__":
    inicio()
    paginas_especialidad()
    for t in ESTETICA:
        tratamiento(t, "estetica", ESTETICA, "medicina-estetica", "Medicina estética")
    for t in VASCULAR:
        tratamiento(t, "vascular", VASCULAR, "medicina-vascular", "Medicina vascular")
    nosotros()
    valoracion()
    extras()
    print("listo:", 5 + len(TODOS), "páginas")
