# -*- coding: utf-8 -*-
# Portafolio en PDF de The Skin Haus (3-nov-2026): para mandar por WhatsApp cuando preguntan "¿qué tratamientos hacen?".
# Sale de datos.py (mismos textos y tiempos de la web), SIN precios. Uso (desde la raíz del repo):
#   python3 _agencia/portafolio/generar.py   → assets/portafolio-the-skin-haus.pdf (+ copia en Documentos)
# Necesita _agencia/portafolio/qr-portafolio.png (QR a WhatsApp con "vi el portafolio").
import os, sys, shutil, subprocess
from html import escape
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, RAIZ)
from datos import ESTETICA, BUSQUEDAS, VALORACION_PASOS, VALORACION_TRAER, DIRECCION, TELEFONO_VISIBLE, MEDICA_ESTETICA
AQUI = os.path.dirname(os.path.abspath(__file__))
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
ORDEN = ["toxina-botulinica", "acido-hialuronico", "relleno-de-labios", "tratamiento-de-ojeras", "armonizacion-facial",
         "bioestimuladores", "skinboosters", "peelings-medicos", "microagujas", "cicatrices-de-acne", "manchas-y-melasma",
         "limpieza-facial-medica", "hiperhidrosis"]
T = {t["slug"]: t for t in ESTETICA + BUSQUEDAS}
NOMBRE = {"toxina-botulinica": "Bótox (toxina botulínica)"}

def foto(slug):
    p = os.path.join(RAIZ, "assets", "fotos", slug + ".jpg")
    return "file://" + p if os.path.exists(p) else "file://" + os.path.join(RAIZ, "assets", "fotos", "piel.jpg")

def tarjeta(slug):
    t = T[slug]; dur, ses, rec = t["como"]
    return '''<div class="tr"><div class="ft" style="background-image:url('%s')"></div><div><h3>%s</h3><p class="li">%s</p>
<ul><li><b>Duración</b> %s</li><li><b>Sesiones</b> %s</li><li><b>Después</b> %s</li></ul><p class="url">theskinhaus.com.co/%s</p></div></div>''' % (
        foto(slug), escape(NOMBRE.get(slug, t["nombre"])), escape(t["linea"]), escape(dur), escape(ses), escape(rec), slug)

CSS = """
@page{size:210mm 297mm;margin:0}*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Arial,Helvetica,sans-serif;color:#111;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.pag{width:210mm;height:297mm;padding:16mm 15mm;position:relative;overflow:hidden;background:#F7F3EE;page-break-after:always}
.pag.marfil{background:#EEE7DE}
.the{font:400 4mm/1 'Libre Caslon Display',serif;letter-spacing:.42em}.sh{font:400 11mm/1 'Libre Caslon Display',serif;letter-spacing:.06em;margin-top:2mm}
.desc{font-size:2.6mm;letter-spacing:.42em;color:#9B8978;margin-top:2.6mm}
h1{font:400 15mm/1.02 'Libre Caslon Display',serif;margin-top:16mm}h1 em,h2 em{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:500}
.sub{font-size:4.2mm;line-height:1.45;color:#3b3530;margin-top:6mm;max-width:120mm}
.arco{position:absolute;right:15mm;bottom:34mm;width:92mm;height:128mm;border-radius:46mm 46mm 6mm 6mm;background-size:cover;background-position:center}
.firma{position:absolute;left:15mm;bottom:16mm;font-size:3.2mm;color:#6b625a;line-height:1.5}
.firma b{color:#111;font-weight:700}
h2{font:400 9mm/1.05 'Libre Caslon Display',serif;margin-bottom:6mm}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:5mm 6mm}
.tr{display:grid;grid-template-columns:20mm 1fr;gap:4mm;background:#fff;border-radius:6mm;padding:4.2mm}
.ft{width:20mm;height:20mm;border-radius:50%;background-size:cover;background-position:center}
.tr h3{font:400 4.6mm/1.15 'Libre Caslon Display',serif}.li{font-size:3mm;color:#3b3530;margin-top:1mm;line-height:1.35}
.tr ul{list-style:none;margin-top:2mm}.tr li{font-size:2.6mm;color:#6b625a;line-height:1.45}.tr li b{color:#111;margin-right:1mm}
.url{font-size:2.4mm;color:#9B8978;margin-top:1.4mm}
.pasos{display:grid;grid-template-columns:repeat(4,1fr);gap:4mm;margin-top:2mm}
.paso{background:#fff;border-radius:6mm;padding:5mm}.paso .n{font:400 7mm/1 'Libre Caslon Display',serif;color:#C6A88F}
.paso b{display:block;font-size:3.4mm;margin-top:2mm}.paso span{display:block;font-size:2.9mm;color:#6b625a;margin-top:1.4mm;line-height:1.4}
.dos{display:grid;grid-template-columns:1.1fr 1fr;gap:8mm;margin-top:10mm;align-items:start}
.caja{background:#fff;border-radius:6mm;padding:6mm}.caja h3{font:400 6mm/1.1 'Libre Caslon Display',serif;margin-bottom:3mm}
.caja li{font-size:3.2mm;line-height:1.5;margin-left:4mm;color:#3b3530}
.qr{text-align:center}.qr img{width:46mm;height:46mm}.qr p{font-size:3.2mm;margin-top:2mm}
.contacto{margin-top:10mm;font-size:3.6mm;line-height:1.6}.contacto b{font-weight:700}
.legal{position:absolute;left:15mm;right:15mm;bottom:12mm;font-size:2.6mm;color:#9B8978}
.cab{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:8mm}.cab .mini{font:400 4mm 'Libre Caslon Display',serif;letter-spacing:.2em}
.cab span{font-size:2.6mm;letter-spacing:.3em;color:#9B8978}
"""

def generar():
    mitad = 7
    pag2 = "".join(tarjeta(s) for s in ORDEN[:mitad]); pag3 = "".join(tarjeta(s) for s in ORDEN[mitad:])
    pasos = "".join('<div class="paso"><div class="n">%d</div><b>%s</b><span>%s</span></div>' % (i, escape(a), escape(b.replace(", o tus piernas si es vascular", "")))
                    for i, (a, b) in enumerate(VALORACION_PASOS, 1))
    traer = "".join("<li>%s</li>" % escape(x) for x in VALORACION_TRAER)
    cab = '<div class="cab"><div class="mini">THE SKIN HAUS</div><span>PORTAFOLIO · %s</span></div>'
    html = """<!doctype html><html lang="es"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Libre+Caslon+Display&family=Cormorant+Garamond:ital,wght@1,500&display=swap" rel="stylesheet">
<style>%s</style></head><body>
<section class="pag marfil"><div class="the">THE</div><div class="sh">SKIN HAUS</div><div class="desc">MEDICAL AESTHETICS</div>
<h1>Medicina estética<br><em>en Pereira.</em></h1>
<p class="sub">Tratamientos con criterio médico, en poca cantidad y bien puestos, para que el resultado se vea descansado y se sienta tuyo.</p>
<div class="arco" style="background-image:url('%s')"></div>
<div class="firma"><b>%s</b>, médica estética<br>%s<br>WhatsApp %s · theskinhaus.com.co</div></section>
<section class="pag">%s<h2>Nuestros <em>tratamientos</em></h2><div class="grid">%s</div></section>
<section class="pag">%s<div class="grid">%s</div>
<p class="legal" style="bottom:16mm">El tratamiento correcto se define en tu valoración: no todos los tratamientos son para todas las personas.</p></section>
<section class="pag marfil">%s<h2>Así es tu <em>valoración</em></h2><div class="pasos">%s</div>
<div class="dos"><div class="caja"><h3>Qué traer</h3><ul>%s</ul></div>
<div class="caja qr"><img src="file://%s"><p>Escanea y escríbenos<br>por WhatsApp</p></div></div>
<div class="contacto"><b>Dónde:</b> %s<br><b>WhatsApp:</b> %s<br><b>Web:</b> theskinhaus.com.co</div>
<p class="legal">Los resultados varían en cada persona. Toda indicación requiere valoración médica. El valor exacto de cada tratamiento se da en la valoración, antes de empezar.</p></section>
</body></html>""" % (CSS, "file://" + os.path.join(RAIZ, "assets", "fotos", "consulta.jpg"), escape(MEDICA_ESTETICA["nombre"]), escape(DIRECCION),
                     escape(TELEFONO_VISIBLE), cab % "1/2", pag2, cab % "2/2", pag3, cab % "VALORACIÓN", pasos, traer,
                     os.path.join(AQUI, "qr-portafolio.png"), escape(DIRECCION), escape(TELEFONO_VISIBLE))
    ruta_html = os.path.join(AQUI, "portafolio.html")
    with open(ruta_html, "w", encoding="utf-8") as f:
        f.write(html)
    salida = os.path.join(RAIZ, "assets", "portafolio-the-skin-haus.pdf")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--allow-file-access-from-files",
                    "--virtual-time-budget=8000", "--print-to-pdf=" + salida, "file://" + ruta_html], capture_output=True)
    docs = os.path.expanduser("~/Documents/Skin Haus - Ventas")
    os.makedirs(docs, exist_ok=True); shutil.copy(salida, os.path.join(docs, "Portafolio The Skin Haus.pdf"))
    return salida

if __name__ == "__main__":
    print(generar())
