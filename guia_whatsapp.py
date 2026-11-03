# -*- coding: utf-8 -*-
# The Skin Haus · GUÍA DE VENTAS POR WHATSAPP (página interna: theskinhaus.com.co/equipo, clave 111, noindex, sin enlaces).
# Para quien responde el WhatsApp de la clínica: cómo convertir cada chat en una valoración y cada valoración en un tratamiento.
# 3-nov-2026: la web casi no trae visitas todavía (20 en un mes), así que cada chat que llega (web, recomendación,
# inauguración) vale mucho. Los textos salen de los MISMOS datos de la web (datos.py) para no prometer nada distinto.
# Reglas: el valor exacto se da en la valoración (como dice el blog de precio del bótox); nada de descuentos, cupos ni
# resultados prometidos; horario sin confirmar (no se usa); el control del bótox es "a las dos semanas" (no decir si va incluido).
# build.py llama a generar() al final.
import hashlib, json, os, re
from html import escape
from urllib.parse import quote

from datos import (ESTETICA, BUSQUEDAS, WHATSAPP, TELEFONO_VISIBLE, DIRECCION, DOMINIO, MEDICA_ESTETICA,
                   PREGUNTAS_ESTETICA, VALORACION_TRAER)

AQUI = os.path.dirname(os.path.abspath(__file__))
CODIGO = "111"   # regla de Laura: páginas privadas siempre con 111
DRA = MEDICA_ESTETICA["nombre"]
WEB = DOMINIO.replace("https://", "")

REGLAS = [
    ("Responde rápido", "Quien escribe a una clínica casi siempre le escribe a varias. La primera que responde bien se gana la cita."),
    ("Primero, su nombre", "Pregunta cómo se llama y qué le gustaría mejorar. Úsalo en cada mensaje."),
    ("El valor, en la valoración", "El valor exacto de un tratamiento se da en la valoración, antes de empezar. Por chat se explica de qué depende."),
    ("Mensajes cortos", "Dos o tres líneas. Un enlace de la web vale más que un párrafo."),
    ("Termina en pregunta", "Cada mensaje cierra con una pregunta fácil de responder: “¿Te queda mejor el martes o el jueves?”."),
    ("Nada de promesas", "Ni resultados garantizados, ni descuentos, ni cupos que no existen. Los resultados varían en cada persona."),
]

BIENVENIDA = "¡Hola! Gracias por escribir a The Skin Haus 🤍 ¿Con quién tengo el gusto? Cuéntame qué te gustaría mejorar y te explico cómo lo trabajamos."
PREGUNTAS_CLAVE = [
    "¿Cómo te llamas?",
    "¿Qué te gustaría mejorar? (zona o molestia)",
    "¿Te has hecho algún tratamiento antes? ¿Cuál y cuándo?",
    "¿Desde dónde nos escribes? (Pereira, Dosquebradas, Santa Rosa…)",
]
AGENDAR = "Te propongo tu valoración con la %s, médica estética. Ahí te examina, te explica qué tiene sentido para ti y te da el valor exacto. ¿Te queda mejor [día 1] o [día 2]?" % DRA
CONFIRMACION = ("✨ *Tu valoración en The Skin Haus*\n\n"
                "🤍 *Nombre:* \n🗓️ *Fecha:* \n🕰️ *Hora:* \n👩🏻‍⚕️ *Con:* " + DRA + "\n"
                "📍 *Dónde:* " + DIRECCION + "\n\n"
                "*Trae, por favor:*\n" + "\n".join("▫️ " + x for x in VALORACION_TRAER) + "\n\n"
                "Si necesitas mover la cita, escríbenos por aquí con tiempo. ¡Te esperamos!")

OBJECIONES = [
    ("“¿Cuánto vale?”", "El valor depende de tu caso: la zona, cuánto producto necesitas y lo que buscas. En tu valoración con la %s te lo damos exacto, antes de empezar. ¿Te agendo esta semana?" % DRA),
    ("“¿Por qué no me dan el precio por aquí?”", "Porque sin verte cualquier número sería un invento, y no queremos darte uno que después cambie. En la valoración te examinamos y te damos el valor exacto antes de empezar. ¿Te queda mejor esta semana o la próxima?"),
    ("“En otro lugar me dieron precio por WhatsApp”", "Está muy bien comparar. Cuando compares, pregunta qué producto es y su registro INVIMA, quién lo aplica y si hay control después. Te dejo una guía: %s/blog/como-comparar-cotizaciones-de-tratamientos-esteticos ¿Te agendo para que compares con toda la información?" % WEB),
    ("“¿Quién me lo aplica?”", PREGUNTAS_ESTETICA[1][1] + " ¿Te cuento cómo es la cita?"),
    ("“Me da miedo que se note”", "Es la duda más común. Nuestro criterio es menos y mejor puesto: preferimos quedarnos cortos y completar en el control que pasarnos. ¿Quieres que te cuente cómo es la cita?"),
    ("“¿Duele?”", "Son punciones muy finas y rápidas; la mayoría lo describe como una molestia leve y breve. Te contamos todo en la valoración. ¿Te agendo?"),
    ("“¿Me lo puedo hacer el mismo día?”", PREGUNTAS_ESTETICA[3][1] + " ¿Te reservo un espacio?"),
    ("“Vivo en Dosquebradas / Santa Rosa”", PREGUNTAS_ESTETICA[2][1] + " ¿Qué día te queda fácil venir?"),
    ("“Lo voy a pensar”", "¡Claro! Es tu decisión y no hay afán. ¿Qué te gustaría tener más claro: el resultado, la recuperación o el valor? Te ayudo con eso."),
]

SEGUIMIENTO = [  # (grupo, [(cuándo, mensaje)])
    ("Escribió y no agendó", [
        ("Al día siguiente", "¡Hola, {nombre}! Ayer hablamos de {tratamiento}. ¿Te quedó alguna duda que te pueda resolver? 🤍"),
        ("Día 3", "Te escribo para ayudarte a dar el primer paso: en tu valoración la %s te examina y sales con tu plan y el valor exacto. ¿Te queda mejor esta semana o la próxima?" % DRA),
        ("Día 7 (último)", "Hola, {nombre}. No quiero llenarte de mensajes 🤍 Si más adelante quieres retomar lo de {tratamiento}, aquí estamos. ¿Te escribo en unas semanas?"),
    ]),
    ("Vino a la valoración y no se hizo nada", [
        ("Día 2", "¡Hola, {nombre}! ¿Cómo te quedaste después de tu valoración? Si te surgió alguna pregunta, aquí estoy 🤍"),
        ("Día 7", "¿Pudiste pensar con calma en el plan que te propuso la %s? Si quieres, te ayudo a buscar un espacio para empezar." % DRA),
        ("Día 30", "Hola, {nombre}. Solo quería saber cómo vas. Si no es el momento, está bien; cuando quieras retomarlo, aquí estamos 🤍"),
    ]),
    ("Ya se hizo un tratamiento", [
        ("Día 1", "¡Hola, {nombre}! ¿Cómo amaneciste? Si tienes cualquier duda sobre los cuidados, escríbenos 🤍"),
        ("Bótox · día 12", "Hola, {nombre}. Ya casi se cumplen las dos semanas de tu bótox, el momento de tu control. ¿Qué día te queda bien venir?"),
        ("Día 21 · pedir reseña", "Hola, {nombre} 🤍 ¿Nos ayudas con tu opinión? Le sirve mucho a otras personas de Pereira para encontrarnos: " + WEB + "/resena ¡Gracias!"),
        ("Bótox · mes 4", "Hola, {nombre}. Ya van unos 4 meses desde tu bótox; entre los 4 y los 6 meses es cuando suele tocar repetir. ¿Quieres que te revisemos un espacio?"),
    ]),
    ("Recomendaciones", [
        ("Día 21 · después de la reseña", "Gracias, {nombre} 🤍 Si alguna amiga quiere conocernos, puede escribirnos aquí y decir que va de tu parte: " + WEB + "/recomendada"),
        ("Llega alguien recomendada", "¡Hola! Qué alegría que vengas de parte de {quien recomendó} 🤍 ¿Cómo te llamas y qué te gustaría mejorar?"),
    ]),
    ("Invitadas de la inauguración (16 de octubre)", [
        ("Una sola vez", "¡Hola, {nombre}! Gracias por acompañarnos en la apertura de The Skin Haus 🤍 Ya estamos atendiendo en la Torre Médica Oval, consultorio 904. Si quieres tu valoración con la %s, te busco un espacio. ¿Te queda mejor esta semana o la próxima?" % DRA),
    ]),
]

ATAJOS = [("hola", BIENVENIDA), ("agendar", AGENDAR), ("precio", OBJECIONES[0][1]), ("porque", OBJECIONES[1][1]),
          ("comparar", OBJECIONES[2][1]), ("miedo", OBJECIONES[4][1]), ("duele", OBJECIONES[5][1]),
          ("pensar", OBJECIONES[8][1]), ("dosquebradas", OBJECIONES[7][1])]
for _g, _ms in SEGUIMIENTO:
    for _c, _m in _ms:
        _k = {"Al día siguiente": "sincita1", "Día 3": "sincita3", "Día 7 (último)": "sincita7", "Día 2": "valor2", "Día 7": "valor7",
              "Día 30": "valor30", "Día 1": "cuidados", "Bótox · día 12": "control", "Día 21 · pedir reseña": "resena", "Bótox · mes 4": "retoque",
              "Día 21 · después de la reseña": "recomienda", "Llega alguien recomendada": "recomendada", "Una sola vez": "inauguracion"}[_c]
        ATAJOS.append((_k, _m))

PERFIL = [
    ("Descripción (perfil de WhatsApp Business)", "Medicina estética en Pereira con criterio médico. Valoración con la %s, médica estética. Torre Médica Oval, consultorio 904." % DRA),
    ("Dirección", DIRECCION),
    ("Sitio web", DOMINIO),
    ("Mensaje de bienvenida (automático)", BIENVENIDA),
    ("Mensaje de ausencia (automático)", "¡Gracias por escribir a The Skin Haus! 🤍 En este momento no podemos responder, pero te contestamos apenas abramos. Cuéntanos tu nombre y qué te gustaría mejorar."),
]


def _corto(texto, n=2):
    partes = re.split(r"(?<=[.!?])\s+", texto.strip())
    return " ".join(partes[:n])


def _trat():
    out = []
    for t in ESTETICA + BUSQUEDAS:
        dur, ses, rec = t.get("como", ("", "", ""))
        nombre = "Bótox (toxina botulínica)" if t["slug"] == "toxina-botulinica" else t["nombre"]
        en_frase = "el bótox" if t["slug"] == "toxina-botulinica" else nombre.lower()
        out.append({
            "slug": t["slug"], "nombre": nombre,
            "que": _corto(t.get("linea", "") + " " + t.get("intro", ""), 2),
            "datos": [x for x in (("Duración", dur), ("Sesiones", ses), ("Recuperación", rec)) if x[1]],
            "para": list(t.get("para", []))[:3],
            "faq": [list(f) for f in list(t.get("faq", []))[:3]],
            "info": "Te dejo la información de %s: %s/%s ¿Quieres que te agende la valoración para ver tu caso?" % (en_frase, WEB, t["slug"]),
            "precio": "El valor de %s depende de tu caso. Te lo damos exacto en tu valoración con la %s, antes de empezar. ¿Te agendo esta semana?" % (en_frase, DRA),
        })
    return out


def _wa(m):
    return "https://wa.me/%s?text=%s" % (WHATSAPP, quote(m))


PLANTILLA = r"""<!doctype html>
<html lang="es-CO"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow"><title>Guía de WhatsApp · The Skin Haus (uso interno)</title>
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@1,500&family=Libre+Caslon+Display&display=swap" rel="stylesheet">
<style>
:root{--blanco:#FAF8F3;--marfil:#F3EEE5;--lino:#ECE5DA;--nude:#C6A88F;--taupe:#9B8978;--negro:#111;--tenue:#6b625a;--linea:#e4dbcf;
--serif:"Libre Caslon Display","Big Caslon",Georgia,serif;--cursiva:"Cormorant Garamond",Georgia,serif;--sans:-apple-system,"Helvetica Neue",Arial,sans-serif}
*{box-sizing:border-box}html{scroll-padding-top:120px;scroll-behavior:smooth}
body{margin:0;background:var(--blanco) url(assets/textura-blanca.jpg);color:var(--negro);font:16px/1.55 var(--sans)}
#candado{position:fixed;inset:0;display:grid;place-items:center;background:var(--marfil);z-index:9}
#candado form{background:#fff;border-radius:28px;padding:36px 32px;width:min(340px,90vw);text-align:center;box-shadow:0 20px 60px rgba(17,17,17,.08)}
#candado input{width:100%;font:600 24px var(--sans);letter-spacing:.4em;text-align:center;padding:14px;border:1px solid var(--linea);border-radius:999px;margin:18px 0 8px;background:var(--blanco)}
.logo{font:400 13px/1 var(--serif);letter-spacing:.32em}.logo b{display:block;font:400 26px/1 var(--serif);letter-spacing:.2em;margin-top:6px}
.mal{color:#9a3b2a;font-size:14px;min-height:20px}
.cab .logo{font-size:10px;white-space:nowrap}.cab .logo b{font-size:18px;white-space:nowrap}.cab .eti{text-align:right}
header{position:sticky;top:0;z-index:5;background:rgba(250,248,243,.94);backdrop-filter:blur(10px);border-bottom:1px solid var(--linea)}
.cab{max-width:980px;margin:0 auto;padding:14px 20px 0;display:flex;justify-content:space-between;align-items:center;gap:12px}
.cab .eti{font:600 11px var(--sans);letter-spacing:.16em;text-transform:uppercase;color:var(--taupe)}
nav{max-width:980px;margin:0 auto;display:flex;gap:8px;overflow-x:auto;padding:12px 20px 14px;scrollbar-width:none}
nav a{flex:none;text-decoration:none;color:var(--negro);font:500 14px var(--sans);padding:8px 14px;border-radius:999px;background:#fff;border:1px solid var(--linea)}
main{max-width:980px;margin:0 auto;padding:28px 20px 80px}
h1{font:400 clamp(32px,6vw,48px)/1.05 var(--serif);margin:10px 0 10px}h1 em,h2 em{font-family:var(--cursiva);font-style:italic}
h2{font:400 clamp(26px,4.4vw,34px)/1.1 var(--serif);margin:56px 0 16px}
.sub{color:var(--tenue);max-width:40em}
.reglas{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:12px}
.regla{background:#fff;border-radius:22px;padding:18px 20px}.regla b{display:block;margin-bottom:4px}.regla span{color:var(--tenue);font-size:15px}
.msj{background:#fff;border-radius:22px;padding:18px 20px;margin-bottom:12px}
.msj .cuando{font:600 11px var(--sans);letter-spacing:.14em;text-transform:uppercase;color:var(--taupe);margin-bottom:6px}
.msj p{margin:0 0 12px;white-space:pre-line}
.copiar{font:600 13px var(--sans);border:1px solid var(--negro);background:var(--negro);color:#fff;border-radius:999px;padding:8px 14px;cursor:pointer}
.copiar.ok{background:#fff;color:var(--negro)}
.lista{margin:0 0 12px;padding-left:18px}.lista li{margin-bottom:4px}
details{background:#fff;border-radius:22px;margin-bottom:10px;overflow:hidden}
summary{cursor:pointer;list-style:none;padding:18px 20px;font:400 21px var(--serif);display:flex;justify-content:space-between;gap:12px}
summary::-webkit-details-marker{display:none}summary::after{content:"+";font-family:var(--sans);color:var(--taupe)}details[open] summary::after{content:"–"}
.dentro{padding:0 20px 20px}.dentro .msj{background:var(--marfil)}
.datos{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 14px}.datos span{background:var(--marfil);border-radius:999px;padding:6px 12px;font-size:14px}
.datos b{font-weight:600;margin-right:4px}
.pregunta{margin:0 0 10px}.pregunta b{display:block}
table{width:100%;border-collapse:collapse;background:#fff;border-radius:22px;overflow:hidden;font-size:15px}
td{padding:12px 16px;border-bottom:1px solid var(--linea);vertical-align:top}td:first-child{font-weight:600;white-space:nowrap;width:1%}
.nota{color:var(--tenue);font-size:14px}
@media(max-width:600px){td:first-child{white-space:normal}}
</style></head><body>
<div id="candado"><form id="f"><div class="logo">THE<b>SKIN HAUS</b></div><p class="nota" style="margin:14px 0 0">Guía interna del equipo. Escribe la clave.</p>
<input id="c" type="password" inputmode="numeric" maxlength="6" autofocus autocomplete="off"><div class="mal" id="mal"></div></form></div>
<header><div class="cab"><div class="logo">THE<b>SKIN HAUS</b></div><span class="eti">Guía de WhatsApp · uso interno</span></div>
<nav>%%NAV%%</nav></header>
<main>%%CUERPO%%</main>
<script>
const H="%%HASH%%";
async function sha(t){const b=await crypto.subtle.digest("SHA-256",new TextEncoder().encode(t));return [...new Uint8Array(b)].map(x=>x.toString(16).padStart(2,"0")).join("")}
function abrir(){document.getElementById("candado").remove()}
try{if(sessionStorage.getItem("sh-guia")===H)abrir()}catch(e){}
document.getElementById("c").addEventListener("input",async e=>{const v=e.target.value;if(v.length<3)return;if(await sha(v)===H){try{sessionStorage.setItem("sh-guia",H)}catch(_){}abrir()}else if(v.length>=3){document.getElementById("mal").textContent="Clave incorrecta"}});
document.getElementById("f").addEventListener("submit",e=>e.preventDefault());
document.addEventListener("click",e=>{const b=e.target.closest(".copiar");if(!b)return;navigator.clipboard.writeText(b.dataset.t).then(()=>{b.textContent="Copiado ✓";b.classList.add("ok");setTimeout(()=>{b.textContent="Copiar mensaje";b.classList.remove("ok")},1500)})});
</script></body></html>"""


def _msj(texto, cuando=""):
    c = '<div class="cuando">%s</div>' % escape(cuando) if cuando else ""
    return '<div class="msj">%s<p>%s</p><button class="copiar" type="button" data-t="%s">Copiar mensaje</button></div>' % (c, escape(texto), escape(texto, quote=True))


def generar():
    secciones = [("reglas", "Reglas"), ("primer", "Primer mensaje"), ("tratamientos", "Tratamientos"), ("objeciones", "Dudas y objeciones"),
                 ("seguimiento", "Seguimiento"), ("atajos", "Respuestas rápidas"), ("perfil", "Perfil de WhatsApp")]
    nav = "".join('<a href="#%s">%s</a>' % s for s in secciones)
    c = []
    c.append('<h1>Cada chat, <em>una cita.</em></h1><p class="sub">Guía para responder el WhatsApp de The Skin Haus (%s). Los mensajes se copian con un toque. Cambia lo que está entre corchetes o llaves, como <b>{nombre}</b>, antes de enviar.</p>' % escape(TELEFONO_VISIBLE))
    c.append('<h2 id="reglas">Las 6 <em>reglas</em></h2><div class="reglas">%s</div>' % "".join('<div class="regla"><b>%s</b><span>%s</span></div>' % (escape(a), escape(b)) for a, b in REGLAS))
    c.append('<h2 id="primer">El primer <em>mensaje</em></h2>' + _msj(BIENVENIDA, "Cuando alguien escribe")
             + '<div class="msj"><div class="cuando">Las 4 preguntas que siempre haces</div><ol class="lista">%s</ol></div>' % "".join("<li>%s</li>" % escape(p) for p in PREGUNTAS_CLAVE)
             + _msj(AGENDAR, "Para agendar (ofrece siempre dos opciones)") + _msj(CONFIRMACION, "Cuando confirma: mensaje de confirmación"))
    tr = []
    for t in _trat():
        datos = "".join('<span><b>%s</b>%s</span>' % (escape(a), escape(b)) for a, b in t["datos"])
        para = "".join("<li>%s</li>" % escape(x) for x in t["para"])
        faq = "".join('<div class="pregunta"><b>%s</b>%s</div>' % (escape(q), escape(r)) for q, r in t["faq"])
        tr.append('<details><summary>%s</summary><div class="dentro"><p>%s</p><div class="datos">%s</div>%s%s%s%s</div></details>' % (
            escape(t["nombre"]), escape(t["que"]), datos,
            ('<p class="nota" style="margin:0 0 4px">Es para:</p><ul class="lista">%s</ul>' % para) if para else "",
            ('<p class="nota" style="margin:8px 0">Lo que más preguntan (respuestas de la web):</p>' + faq) if faq else "",
            _msj(t["info"], "Enviar la información"), _msj(t["precio"], "Si pregunta el valor")))
    c.append('<h2 id="tratamientos">Por <em>tratamiento</em></h2><p class="sub">Toca un tratamiento para ver qué es, sus tiempos y los mensajes listos.</p>' + "".join(tr))
    c.append('<h2 id="objeciones">Dudas y <em>objeciones</em></h2>' + "".join('<details><summary>%s</summary><div class="dentro">%s</div></details>' % (escape(q), _msj(r)) for q, r in OBJECIONES))
    seg = []
    for grupo, msjs in SEGUIMIENTO:
        seg.append('<details %s><summary>%s</summary><div class="dentro">%s</div></details>' % ("open" if not seg else "", escape(grupo), "".join(_msj(m, cu) for cu, m in msjs)))
    c.append('<h2 id="seguimiento">El <em>seguimiento</em></h2><p class="sub">Aquí se gana la mayoría de las citas. Si alguien no contesta tres mensajes seguidos, se pausa y se vuelve a intentar en dos meses. Anota la fecha de cada mensaje.</p>' + "".join(seg))
    filas = "".join("<tr><td>/%s</td><td>%s</td></tr>" % (escape(k), escape(m)) for k, m in ATAJOS)
    c.append('<h2 id="atajos">Respuestas <em>rápidas</em></h2><p class="sub">En WhatsApp Business: Herramientas para la empresa → Respuestas rápidas → +. Escribe el atajo (sin la barra) y pega el mensaje. Después, en un chat, escribes / y eliges.</p><table>%s</table>' % filas)
    perfil = "".join(_msj(v, k) for k, v in PERFIL)
    c.append('<h2 id="perfil">Perfil de <em>WhatsApp Business</em></h2><p class="sub">Textos listos para Herramientas para la empresa → Perfil, Mensaje de bienvenida y Mensaje de ausencia.</p>' + perfil)
    html = (PLANTILLA.replace("%%NAV%%", nav).replace("%%CUERPO%%", "\n".join(c))
            .replace("%%HASH%%", hashlib.sha256(CODIGO.encode()).hexdigest()))
    with open(os.path.join(AQUI, "equipo.html"), "w", encoding="utf-8") as f:
        f.write(html)
    return len(ESTETICA + BUSQUEDAS)


if __name__ == "__main__":
    print("Guía de WhatsApp: %d tratamientos." % generar())
