# -*- coding: utf-8 -*-
# The Skin Haus · /cuando-repetir: la calculadora PERMANENTE e indexable (9-nov-2026, ventas ronda 2).
# No es una copia a mano: se arma en cada construcción a partir de tu-fecha.html (la calculadora de diciembre, que
# sigue igual y noindex). Hereda su componente, sus reglas de duración y su medición (calculadora_usada y
# clic_whatsapp con origen "calculadora"); aquí solo se cambia lo que la hace permanente: abre en "¿Cuándo me toca
# repetir?", el modo de fecha se llama "Tengo un evento" y no trae botones de diciembre, y lleva título, descripción,
# datos estructurados, preguntas y enlaces propios. Si tu-fecha.html cambia y una pieza ya no se encuentra, la
# construcción se detiene con el nombre de la pieza (mejor que publicar una página a medias).
# Lo usa build.py; no se corre solo.
import os, re, json

AQUI = os.path.dirname(os.path.abspath(__file__))
SLUG = "cuando-repetir"
TITULO = "¿Cuándo repetir el bótox o el relleno? Calcula tu fecha"
DESC = ("Pon la fecha de tu última aplicación y mira cuándo te toca: bótox cada 4 a 6 meses, ácido hialurónico de 9 a 18. "
        "También para un evento. En Pereira.")
OG_DESC = "Pon la fecha de tu última aplicación, o la de tu evento, y mira tu momento. Luego te valora la médica en Pereira."

# Mismas cifras que usa la calculadora y que afirman las fichas (datos.py) y _agencia/hechos.md, sección B.
PREGUNTAS = [
    ("¿Cada cuánto se repite el bótox?",
     "Por lo general, cada 4 a 6 meses. Cuánto te dura depende de tu musculatura, de la zona y de tus hábitos, y preferimos no adelantarlo."),
    ("¿Cuándo se repite el ácido hialurónico o el relleno de labios?",
     "El ácido hialurónico dura de 9 a 18 meses según la zona, el producto y cómo lo procesa tu cuerpo. En los labios suele durar menos."),
    ("Tengo un evento: ¿con cuánta anticipación me aplico el bótox?",
     "Empieza a notarse entre el día 3 y el 7 y se ve completo hacia las 2 semanas, cuando te vemos en control. Con una semana más queda margen si en el control hay que completar."),
    ("¿Y los labios o las ojeras antes de un evento?",
     "Puede haber inflamación leve o algún morado de 24 a 72 horas. Para una fecha importante pedimos por lo menos 2 semanas de margen, y más si es tu primera vez."),
]
TRATAMIENTOS = [("toxina-botulinica", "Bótox en Pereira"), ("acido-hialuronico", "Ácido hialurónico"), ("relleno-de-labios", "Relleno de labios")]
ARTICULOS = ["cuanto-dura-el-botox", "cuando-volver-a-ponerse-botox", "cuanto-dura-el-relleno-de-labios", "cuanto-rinde-1-ml-de-acido-hialuronico"]

CSS = (".logo{cursor:pointer}"
       ".pregs{display:grid;gap:10px;margin-top:34px;max-width:860px}"
       ".pregs details{background:var(--marfil) url(assets/textura-marfil.jpg) repeat 0 0/560px;border-radius:26px}"
       ".pregs summary{cursor:pointer;font:400 19px/1.3 var(--serif-t);list-style:none;display:flex;justify-content:space-between;gap:16px;padding:18px 24px}"
       ".pregs summary::-webkit-details-marker{display:none}"
       ".pregs summary::after{content:'+';font:400 22px/1 var(--serif);flex:none}"
       ".pregs details[open] summary::after{content:'\\2212'}"
       ".pregs p{margin:-8px 24px 18px;font-size:16px;line-height:1.6;color:#2a2622;max-width:46em}"
       ".sigue{display:flex;flex-wrap:wrap;gap:8px;margin-top:22px}"
       ".sigue a{display:inline-flex;align-items:center;min-height:44px;padding:8px 18px;border-radius:999px;border:1px solid rgba(17,17,17,.14);"
       "background:rgba(255,255,255,.74);font-size:14.5px;line-height:1.3;text-decoration:none}"
       ".sigue a:hover{border-color:rgba(17,17,17,.4)}"
       ".sigue-t{margin-top:44px;font:700 12px/1.4 var(--sans);letter-spacing:.2em;text-transform:uppercase;color:var(--taupe-t)}"
       ".pie nav{display:flex;flex-wrap:wrap;gap:0 22px;font-size:14.5px;margin:0 0 2px}"
       ".pie nav a{text-underline-offset:3px;display:inline-flex;align-items:center;min-height:44px}")


def generar(ctx):
    """ctx = globals() de build.py (DOMINIO, CLINICA_LD, migas_ld, faq_ld, blog)."""
    dominio = ctx["DOMINIO"]
    html = open(os.path.join(AQUI, "tu-fecha.html"), encoding="utf-8").read()

    def cambia(viejo, nuevo, veces=1, que=""):
        nonlocal html
        if html.count(viejo) != veces:
            raise SystemExit("calculadora.py: en tu-fecha.html esperaba %d vez/veces «%s» y hay %d. Revisa %s." % (
                veces, (que or viejo)[:70], html.count(viejo), "calculadora.py"))
        html = html.replace(viejo, nuevo)

    def cambia_re(patron, nuevo, que):
        nonlocal html
        html, n = re.subn(patron, lambda m: nuevo, html, count=1, flags=re.S)
        if n != 1:
            raise SystemExit("calculadora.py: no encontré en tu-fecha.html la pieza «%s»." % que)

    url = dominio + "/" + SLUG
    arts = {a["slug"]: a for a in ctx["blog"].cargar()}
    ld = [ctx["CLINICA_LD"],
          {"@context": "https://schema.org", "@type": "WebPage", "name": TITULO, "description": DESC, "url": url, "inLanguage": "es-CO",
           "about": [{"@type": "MedicalProcedure", "name": n, "url": dominio + "/" + s} for s, n in TRATAMIENTOS],
           "publisher": {"@id": dominio + "/#clinica"}},
          ctx["faq_ld"](PREGUNTAS),
          ctx["migas_ld"]([("Inicio", ""), ("Medicina estética", "medicina-estetica"), ("¿Cuándo me toca repetir?", SLUG)])]

    # ---- cabeza: indexable, con título, descripción, dirección y datos estructurados propios
    cambia('<meta name="robots" content="noindex">\n', '<base href="/">\n', que="noindex")
    cambia_re(r"<title>.*?</title>", "<title>%s</title>" % TITULO, "title")
    cambia_re(r'<meta name="description" content="[^"]*">', '<meta name="description" content="%s">' % DESC, "description")
    cambia_re(r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="%s">' % TITULO, "og:title")
    cambia_re(r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="%s">' % OG_DESC, "og:description")
    cambia(dominio + "/tu-fecha", url, 2, "canonical y og:url")
    cambia("</style>", CSS + "</style>", que="</style>")
    cambia("</head>", '<script type="application/ld+json">%s</script>\n</head>' % json.dumps(ld, ensure_ascii=False), que="</head>")

    # ---- el logo lleva al inicio (en la landing de diciembre no es enlace)
    logo = '<span class="logo" aria-label="The Skin Haus"><span class="the">THE</span><span class="sh">SKIN</span><span class="sh">HAUS</span></span>'
    cambia(logo, '<a class="logo" href="./" aria-label="The Skin Haus, inicio"><span class="the">THE</span><span class="sh">SKIN</span><span class="sh">HAUS</span></a>', 2, "logo")

    # ---- primera pantalla: abre en "repetir"; la fecha es "Tengo un evento" y sin botones de diciembre
    cambia_re(r"<h1>.*?</h1>", '<h1>¿Cuándo me toca repetir <span class="it">mi bótox o mi relleno?</span></h1>', "h1")
    cambia_re(r'<p class="lead">Cada tratamiento tiene su propio reloj\..*?</p>',
              '<p class="lead">Pon la fecha de tu última aplicación y te mostramos tu momento. Y si tienes un evento, con cuánta anticipación conviene aplicártelo.</p>', "lead")
    cambia_re(r'<div class="pestanas" role="tablist".*?</div>',
              '<div class="pestanas" role="tablist" aria-label="Qué quieres calcular">\n'
              '        <button type="button" role="tab" id="t-repetir" aria-controls="p-repetir" aria-selected="true" data-p="repetir">¿Cuándo me toca repetir?</button>\n'
              '        <button type="button" role="tab" id="t-fecha" aria-controls="p-fecha" aria-selected="false" tabindex="-1" data-p="fecha">Tengo un evento</button>\n'
              '        <button type="button" role="tab" id="t-visita" aria-controls="p-visita" aria-selected="false" tabindex="-1" data-p="visita">Vengo de visita</button>\n'
              '      </div>', "pestañas")
    cambia('<div class="panel" id="p-fecha" role="tabpanel" aria-labelledby="t-fecha">', '<div class="panel" id="p-fecha" role="tabpanel" aria-labelledby="t-fecha" hidden>', que="panel fecha")
    cambia('<div class="panel" id="p-repetir" role="tabpanel" aria-labelledby="t-repetir" hidden>', '<div class="panel" id="p-repetir" role="tabpanel" aria-labelledby="t-repetir">', que="panel repetir")
    cambia_re(r'\s*<button type="button" class="rapida" data-fecha=.*?</button>(?=\s*<button type="button" class="rapida" data-otra)', "", "botones de diciembre")
    html = re.sub(r'\s*<button type="button" class="rapida" data-fecha=.*?</button>', "", html, flags=re.S)
    cambia('<div class="rapidas">', '<div class="rapidas" hidden>', que="rapidas")
    cambia('<label class="campo" id="campo-fecha" hidden><span>Tu fecha</span>', '<label class="campo" id="campo-fecha" style="margin-top:0"><span>La fecha de tu evento</span>', que="campo fecha")
    cambia('data-r="lineas">Líneas de expresión</button>', 'data-r="lineas">Bótox</button>', que="chip bótox")
    cambia('<div class="resumen" id="resumen" aria-live="polite">Elige tu fecha y te mostramos el momento ideal para cada tratamiento.</div>',
           '<div class="resumen" id="resumen" aria-live="polite">Elige qué te hiciste y cuándo fue la última vez.</div>', que="resumen inicial")

    # ---- reglas: las mismas; solo cambia el nombre visible (aquí sí decimos "bótox", como en /toxina-botulinica)
    cambia("{ id: 'lineas', n: 'Líneas de expresión', msj: 'líneas de expresión',", "{ id: 'lineas', n: 'Bótox · líneas de expresión', msj: 'bótox',", que="TRAT líneas")
    cambia("lineas: { n: 'Líneas de expresión', msj: 'líneas de expresión',", "lineas: { n: 'Bótox · líneas de expresión', msj: 'bótox',", que="REPETIR líneas")
    cambia("var E = { pestana: 'fecha',", "var E = { pestana: 'repetir',", que="estado inicial")
    cambia("if (qp === 'visita' || qp === 'repetir') activar(qp); else calcular(false);",
           "if (qp === 'evento' || (qf && !qp)) qp = 'fecha';\n    if (qp === 'visita' || qp === 'fecha') activar(qp); else calcular(false);", que="pestaña por enlace")
    cambia("'¿Tienes una fecha en diciembre? <button type=\"button\" data-ir=\"fecha\">Planea tu calendario</button>'",
           "'¿Tienes un evento? <button type=\"button\" data-ir=\"fecha\">Mira con cuánta anticipación aplicártelo</button>'", que="enlace a la otra pestaña")
    cambia('<b>Líneas de expresión</b><span>Empiezan a notarse', '<b>Bótox · líneas de expresión</b><span>Empiezan a notarse', que="así contamos")

    # ---- preguntas (visibles, las mismas del JSON-LD) y enlaces a las fichas y a los artículos de duración
    pregs = "".join("<details><summary>%s</summary><p>%s</p></details>" % p for p in PREGUNTAS)
    fichas = "".join('<a href="%s">%s</a>' % par for par in TRATAMIENTOS)
    lecturas = "".join('<a href="blog/%s">%s</a>' % (s, arts[s]["title"]) for s in ARTICULOS if s in arts)
    bloque = '''<section class="sec" id="preguntas">
  <div class="caja">
    <p class="ceja">Preguntas frecuentes</p>
    <h2>Repetir, <span class="gris">sin adelantarse.</span></h2>
    <div class="pregs">%s</div>
    <p class="sigue-t">Los tratamientos</p>
    <div class="sigue">%s</div>%s
  </div>
</section>

''' % (pregs, fichas, '\n    <p class="sigue-t">Para leer con calma</p>\n    <div class="sigue">%s</div>' % lecturas if lecturas else "")
    cambia('<section class="sec cierre-sec">', bloque + '<section class="sec cierre-sec">', que="cierre")
    cambia('    <p class="legal">', '    <nav aria-label="Más de The Skin Haus"><a href="./">Inicio</a><a href="medicina-estetica">Medicina estética</a>'
           '<a href="blog/">Blog</a><a href="valoracion?desde=%s">Agenda por formulario</a></nav>\n    <p class="legal">' % SLUG, que="pie")

    for resto in ("diciembre", "Nochebuena", "noindex"):
        visible = re.sub(r"<!--.*?-->|<script>.*?</script>", "", html, flags=re.S)
        if resto in visible:
            raise SystemExit("calculadora.py: quedó «%s» visible en /%s." % (resto, SLUG))
    with open(os.path.join(AQUI, SLUG + ".html"), "w", encoding="utf-8") as f:
        f.write(html)
