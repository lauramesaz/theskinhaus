# -*- coding: utf-8 -*-
# The Skin Haus · GUÍA DE VENTAS POR WHATSAPP (página interna: theskinhaus.com.co/equipo, clave 111, noindex, sin enlaces).
# Para quien responde el WhatsApp de la clínica: cómo convertir cada chat en una valoración y cada valoración en un tratamiento.
# 3-nov-2026: la web casi no trae visitas todavía (20 en un mes), así que cada chat que llega (web, recomendación,
# inauguración) vale mucho. Los textos salen de los MISMOS datos de la web (datos.py) para no prometer nada distinto.
# Reglas: el valor exacto se da en la valoración (como dice el blog de precio del bótox); nada de descuentos, cupos ni
# resultados prometidos; horario sin confirmar (no se usa); el control del bótox es "a las dos semanas" (no decir si va incluido).
# 4-nov-2026 · VERSIÓN 2 (plan del Comercializador, "Hoy 5"): Diciembre (fechas de Nochebuena + calculadora /tu-fecha),
# De visita, Invitadas (versión nueva), Verifícanos (INVIMA + RETHUS), Recordatorios en 2 toques (calendario del celular,
# .ics o Google Calendar, sin guardar nada), Cierre del día (8 preguntas → WhatsApp al grupo "Lo que entra", o el
# formulario de Google si CIERRE_FORM_URL tiene valor), Fuera de horario y Etiquetas. Textos con prueba del Policía
# humanizador; tiempos SOLO de _agencia/hechos.md y datos.py. La bienvenida ahora pregunta "¿Vives en Pereira o estás de visita?".
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

# Enlaces que usan los mensajes nuevos
TU_FECHA = WEB + "/tu-fecha"   # calculadora "¿Llegas a diciembre?" (Hoy 1 del plan; la monta otro constructor el 4-nov)
RETHUS = "https://web.sispro.gov.co/THS/Cliente/ConsultasPublicas/ConsultaPublicaDeTHxIdentificacion.aspx"  # hechos.md C1
INVIMA = "https://www.invima.gov.co/consulta-registros-sanitarios"                                          # hechos.md C2
BLOG_PLAYA = WEB + "/blog/peeling-antes-de-un-viaje-a-la-playa"

# Cierre del día: si existe el formulario de Google (sin nombres ni teléfonos), pega aquí su enlace y el botón lo abre.
# Vacío = plan B: el botón arma el mensaje con las 8 respuestas para mandarlo al grupo de WhatsApp "Lo que entra".
CIERRE_FORM_URL = ""

REGLAS = [
    ("Responde rápido", "Quien escribe a una clínica casi siempre le escribe a varias. La primera que responde bien se gana la cita."),
    ("Primero, su nombre", "Pregunta cómo se llama y qué le gustaría mejorar. Úsalo en cada mensaje."),
    ("El valor, en la valoración", "El valor exacto de un tratamiento se da en la valoración, antes de empezar. Por chat se explica de qué depende."),
    ("Mensajes cortos", "Dos o tres líneas. Un enlace de la web vale más que un párrafo."),
    ("Termina en pregunta", "Cada mensaje cierra con una pregunta fácil de responder: “¿Te queda mejor el martes o el jueves?”."),
    ("Nada de promesas", "Ni resultados garantizados, ni descuentos, ni cupos que no existen. Los resultados varían en cada persona."),
]

# 4-nov: la bienvenida pregunta si vive en Pereira o está de visita (así se cuenta a quien viene de afuera) y si tiene fecha.
BIENVENIDA = ("Hola, gracias por escribirnos. Te saluda [tu nombre], de The Skin Haus, en la Torre Médica Oval. ¿Con quién tengo "
              "el gusto? Cuéntame qué te gustaría mejorar y si vives en Pereira o estás de visita. Y si tienes alguna fecha en "
              "diciembre, dímela y miramos qué alcanza.")
BIENVENIDA_AUTO = ("Hola, gracias por escribir a The Skin Haus, en la Torre Médica Oval de Pereira. Para ayudarte más rápido, "
                   "cuéntanos tu nombre, qué te gustaría mejorar y si vives en Pereira o estás de visita.")
PREGUNTAS_CLAVE = [
    "¿Cómo te llamas?",
    "¿Qué te gustaría mejorar? (zona o molestia)",
    "¿Te has hecho algún tratamiento antes? ¿Cuál y cuándo?",
    "¿Vives en Pereira (o cerca: Dosquebradas, Santa Rosa…) o estás de visita?",
    "¿Tienes alguna fecha en mente? (una fiesta, un viaje, Nochebuena)",
]
PORTAFOLIO = "Te comparto nuestro portafolio con todos los tratamientos, sus tiempos y cómo es la valoración: " + WEB + "/assets/portafolio-the-skin-haus.pdf ¿Cuál te llamó la atención?"
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

# 4-nov: control y "repetir" de líneas de expresión con UN solo texto (lo usan el seguimiento y los recordatorios).
MSJ_CONTROL = ("Hola, [nombre]. Ya casi se cumplen las dos semanas de tu aplicación para las líneas de expresión, y es el "
               "momento del control con la %s. ¿Qué día te queda bien venir?" % DRA)
MSJ_REPETIR = ("Hola, [nombre]. Ya van unos 4 meses desde tu aplicación para las líneas de expresión. Entre los 4 y los 6 "
               "meses es cuando suele tocar repetir, y la Dra. te mira el gesto para decirte si ya conviene. ¿Te busco "
               "espacio esta semana o la próxima?")

SEGUIMIENTO = [  # (grupo, [(cuándo, mensaje)]) · las invitadas de la inauguración pasaron a su propia sección (INVITADAS, 4-nov)
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
        ("Líneas de expresión · día 12", MSJ_CONTROL),
        ("Día 21 · pedir reseña", "Hola, {nombre} 🤍 ¿Nos ayudas con tu opinión? Le sirve mucho a otras personas de Pereira para encontrarnos: " + WEB + "/resena ¡Gracias!"),
        ("Líneas de expresión · mes 4", MSJ_REPETIR),
    ]),
    ("Recomendaciones", [
        ("Día 21 · después de la reseña", "Gracias, {nombre} 🤍 Si alguna amiga quiere conocernos, puede escribirnos aquí y decir que va de tu parte: " + WEB + "/recomendada"),
        ("Llega alguien recomendada", "¡Hola! Qué alegría que vengas de parte de {quien recomendó} 🤍 ¿Cómo te llamas y qué te gustaría mejorar?"),
    ]),
]

# ---------------------------------------------------------------- versión 2 (4-nov-2026)
# Fechas de Nochebuena (jueves 24-dic-2026) calculadas en el plan: líneas de expresión y ácido hialurónico, con calma hasta
# el jue 3-dic (21 días) y justo hasta el jue 10-dic (14 días; el mar 8 es festivo); skinbooster 1 o 2 de 3 sesiones si
# empieza ya; bioestimuladores para enero y febrero (cambios desde la semana 6 a 8); limpieza cabe siempre.
DICIEMBRE = dict(
    general=("Si pregunta qué alcanza para diciembre",
             "Depende de qué te quieras hacer: hay tratamientos que se ven completos hacia las dos semanas y otros que conviene "
             "empezar desde ya. Si pones tu fecha aquí, te sale qué alcanza: " + TU_FECHA + " ¿Para qué fecha lo quieres?"),
    tratamientos=[  # (nombre, resumen de fechas, mensaje)
        ("Líneas de expresión", "Con calma hasta el jue 3 · justo hasta el jue 10",
         "Para el 24, lo ideal es aplicarlo a más tardar el jueves 3 de diciembre: el efecto se ve completo hacia las dos semanas "
         "y en ese momento te hacemos el control, todavía antes de tu fecha. Hasta el jueves 10 alcanza, pero muy justo y sin ese "
         "margen. ¿Te busco espacio esta semana o la próxima?"),
        ("Labios y ojeras", "Con calma hasta el jue 3 · justo hasta el jue 10",
         "Con el ácido hialurónico en labios u ojeras puede haber una inflamación leve de 24 a 72 horas, por eso para una fecha "
         "importante dejamos por lo menos dos semanas, y un poco más si es tu primera vez o son labios. Para el 24: con calma, "
         "hasta el jueves 3 de diciembre; muy justo, hasta el jueves 10. ¿Qué día te queda bien venir a la valoración?"),
        ("Skinbooster", "Si empieza ya, alcanza 1 o 2 de las 3 sesiones",
         "El skinbooster va en serie: son 3 sesiones, una cada 3 a 4 semanas. Si empiezas en estos días, antes del 24 alcanzas "
         "1 o 2, y la serie se completa después. ¿Te agendo la valoración para arrancar esta semana?"),
        ("Bioestimuladores", "Para enero y febrero",
         "Los bioestimuladores van despacio: los primeros cambios aparecen entre la semana 6 y la 8, y la mejoría sigue por "
         "meses. Si empiezas ahora, el 24 apenas se vería el comienzo. Por eso son más para enero y febrero. ¿Te busco espacio "
         "para la valoración y lo dejamos planeado?"),
        ("Peeling médico", "Según la profundidad: lo define la Dra.",
         "Depende de qué tan profundo sea el peeling: con uno suave casi ni se nota que la piel se pela, y con uno más profundo "
         "se puede pelar hasta una semana. Cuál te conviene antes de tu fecha lo define la Dra. en la valoración. ¿Para cuándo "
         "es tu fecha?"),
        ("Limpieza facial médica", "Cabe siempre",
         "La limpieza facial médica te alcanza aunque falte poco. Dura más o menos una hora y de ahí sigues con tus cosas. A "
         "veces la piel queda un poco roja unas horas. ¿Qué día te queda bien?"),
    ],
    no_alcanza=("Si para su fecha ya no alcanza (ponle la etiqueta «Volver en enero»)",
                "Para esa fecha ya no nos da el tiempo, y no queremos hacerlo a las carreras. Lo podemos dejar para enero, con "
                "calma. ¿Te escribo la primera semana del año y lo cuadramos?"),
)

VISITA_CABE = [  # pestaña "Vengo de visita" del plan
    ("Líneas de expresión", "caben con control si la visita dura 16 días o más y la aplicación es en los primeros días. Si dura menos, lo define la Dra. en la valoración."),
    ("Labios y ojeras", "mejor al comienzo de la visita, por la inflamación leve de 24 a 72 horas."),
    ("Skinbooster", "cabe 1 sesión."),
    ("Bioestimuladores", "se aplican aquí y el cambio se empieza a notar ya de vuelta en casa, desde la semana 6 a 8."),
    ("Peeling", "depende de si después hay playa o sol fuerte."),
    ("Limpieza facial médica", "cabe siempre."),
]
VISITA = [
    ("Cuando dice que viene de visita",
     "Qué bueno que nos escribas antes de venir. ¿Qué día llegas a Pereira y qué día te vas? Con esas dos fechas te digo qué cabe "
     "en tu visita. Lo ideal es la valoración en tus primeros días, para que si te haces algo que lleva control, alcancemos a "
     "hacerlo antes de que te vayas."),
    ("Visita de 16 días o más (líneas de expresión)",
     "Para las líneas de expresión, con esos días sí alcanza. Si vienes a la valoración apenas llegues, se puede aplicar ese "
     "mismo día si la Dra. lo ve adecuado y tú te animas, y el control de las dos semanas queda antes de tu regreso. ¿Te "
     "aparto la cita para tu primer o segundo día aquí?"),
    ("Visita más corta (menos de 16 días)",
     "Para las líneas de expresión el control es a las dos semanas, y con [número] días puede que no alcance. Como no queremos "
     "saltárnoslo, lo miramos con la Dra. en la valoración, y si no cabe, te dice qué sí tiene sentido. ¿Te busco espacio "
     "para tu primer día aquí?"),
    ("Si pregunta por peeling y después va a playa o a sol fuerte",
     "Con el peeling importa mucho si después vas a playa o a sol fuerte. Aquí lo explicamos contando desde el vuelo: "
     + BLOG_PLAYA + " ¿Para cuándo es tu viaje?"),
    ("Para que una paciente se lo reenvíe a quien viene en diciembre",
     "Si vienes a Pereira en diciembre, escríbenos al " + TELEFONO_VISIBLE + " antes de volar. Con tu fecha de llegada y la de "
     "regreso te decimos qué cabe en tu visita y te buscamos la valoración en tus primeros días. Estamos en la Torre Médica "
     "Oval, consultorio 904."),
]

INVITADAS = [
    ("El mensaje (una sola vez)",
     "Hola, [nombre], te escribe [tu nombre] de The Skin Haus. Gracias otra vez por venir a la apertura: ya estamos atendiendo "
     "en el 904. Si tienes una fecha en diciembre, aquí miras qué te alcanza: " + TU_FECHA + ". Y si alguien que conozcas se "
     "anima, que nos escriba de tu parte. ¿Te busco un espacio para tu valoración con la " + DRA + "?"),
    ("Si dice que una amiga quiere venir",
     "Qué bien, gracias. Dile que nos escriba a este mismo número y nos cuente que va de tu parte. ¿Cómo se llama, para estar "
     "pendientes de su mensaje?"),
]

VERIFICANOS = [
    ("Al dar el valor (con la foto de la caja)",
     "Te mando la foto de la caja del producto que te propuso la Dra., con su registro INVIMA, para que lo revises tú en la "
     "página del INVIMA: " + INVIMA + " A la " + DRA + " también la puedes buscar en el RETHUS, el registro del Ministerio de "
     "Salud: " + RETHUS + " Preferimos que lo revises todo antes de decidir."),
    ("Si pregunta qué marca o qué producto usan",
     "El producto depende de tu caso, y eso lo define la Dra. en la valoración. Ahí mismo te mostramos la caja con su registro "
     "INVIMA, para que lo verifiques. ¿Te agendo?"),
    ("“En otro lado me sale más barato”",
     "Está bien comparar; pregunta quién lo aplica y si es médico, qué producto es y cuál es su registro INVIMA. Con esas tres "
     "respuestas ya comparas lo mismo con lo mismo. Si quieres, te mando cómo verificarnos a nosotros."),
    ("Si pide cómo verificar a la Dra. (pruébalo tú una vez antes; si no sale, pregúntale a la Dra. con qué nombre aparece)",
     "Claro. Entra al RETHUS, el registro del Ministerio de Salud: " + RETHUS + " En primer nombre escribe Valeria y en primer "
     "apellido, Enciso. Copia los números de la imagen y te sale su profesión y si está autorizada para ejercer. ¿Me cuentas "
     "si te sale?"),
]

# Recordatorios en 2 toques (plan: control día 12 a 14 de líneas de expresión, skinbooster a las 3 semanas, peeling a las
# 2 a 4, microagujas a las 4, limpieza a las 4 a 6 y "repetir" líneas de expresión a los 4 meses). El evento va a las
# 9:00 a. m. de Colombia; si cae domingo, pasa al lunes. Nada se guarda: el archivo se arma en el celular.
RECORDATORIOS = [  # (clave, tratamiento, [evento])
    ("lineas", "Líneas de expresión", [
        dict(dias=12, titulo="control de líneas de expresión", rango="día 12 a 14", msj=MSJ_CONTROL),
        dict(meses=4, titulo="repetir líneas de expresión", rango="4 meses", msj=MSJ_REPETIR),
    ]),
    ("skinbooster", "Skinbooster", [
        dict(dias=21, titulo="siguiente skinbooster", rango="3 a 4 semanas",
             msj="Hola, [nombre]. Ya van 3 semanas desde tu sesión de skinbooster, así que se acerca la siguiente: van cada 3 a "
                 "4 semanas. ¿Te busco espacio esta semana o la próxima?"),
    ]),
    ("peeling", "Peeling médico", [
        dict(dias=14, titulo="siguiente peeling", rango="2 a 4 semanas",
             msj="Hola, [nombre]. Ya van 2 semanas desde tu peeling. La siguiente sesión va entre la semana 2 y la 4, según lo "
                 "que te indicó la Dra. ¿Qué día te queda bien?"),
    ]),
    ("microagujas", "Microagujas", [
        dict(dias=28, titulo="siguiente sesión de microagujas", rango="4 semanas",
             msj="Hola, [nombre]. Ya se cumplen 4 semanas desde tu sesión de microagujas, que es el tiempo para la siguiente. "
                 "¿Qué día te queda bien venir?"),
    ]),
    ("limpieza", "Limpieza facial médica", [
        dict(dias=28, titulo="siguiente limpieza facial", rango="4 a 6 semanas",
             msj="Hola, [nombre]. Ya va un mes desde tu limpieza facial; la siguiente suele ir entre la semana 4 y la 6. ¿Te "
                 "busco espacio en estos días?"),
    ]),
]

CIERRE_FUENTES = ["Google", "Instagram", "Recomendada", "Aliado", "Inauguración", "Calculadora", "De visita", "Otro"]
CIERRE_PREGUNTAS = [  # (id, pregunta, ayuda) · la 2 son las fuentes y la 8 es sí/no
    ("c-chats", "Chats nuevos", "Personas que escribieron por primera vez"),
    ("c-fuentes", "¿De dónde vinieron?", "Cuántos de cada lado, si lo sabes"),
    ("c-agendadas", "Citas agendadas", "Valoraciones que quedaron con fecha hoy"),
    ("c-vinieron", "Citas que vinieron", "Valoraciones de hoy a las que sí llegaron"),
    ("c-tratamientos", "Tratamientos hechos", "Lo que se aplicó o se hizo hoy"),
    ("c-volvieron", "Pacientes que volvieron", "Controles, siguientes sesiones o repetir"),
    ("c-pesos", "Pesos que entraron", "Lo que se cobró hoy"),
    ("c-cuotas", "¿Alguien preguntó por cuotas?", ""),
]

FUERA_HORARIO = [
    ("Hasta el 10 de diciembre",
     "Gracias por escribir a The Skin Haus. En este momento no estamos atendiendo, pero te respondemos apenas abramos. Mientras "
     "tanto, si tienes una fecha en diciembre, aquí miras qué te alcanza: " + TU_FECHA),
    ("Desde el 11 de diciembre",
     "Gracias por escribir a The Skin Haus. En este momento no estamos atendiendo, pero te respondemos apenas abramos. Si nos "
     "dejas tu nombre y qué te gustaría mejorar, te contestamos con eso en la mano."),
]

ETIQUETAS = [  # (nombre, color sugerido, muestra, cuándo se usa)
    ("Nueva", "azul", "#4f9be0", "Escribió por primera vez y todavía no agenda. Se la quitas cuando agende."),
    ("Agendó", "amarillo", "#f0c43c", "Ya tiene fecha para la valoración."),
    ("Vino", "verde", "#4caf72", "Vino a la valoración."),
    ("Se hizo algo", "morado", "#9478cf", "Se hizo un tratamiento: le toca su recordatorio y pedirle la reseña."),
    ("De visita", "naranja", "#ee8f45", "Vive afuera y viene a Pereira: se agenda en sus primeros días."),
    ("Volver en enero", "gris", "#a4a6a9", "Para su fecha ya no alcanzaba o lo dejó para después: se le escribe una vez en enero."),
]

ATAJOS = [("hola", BIENVENIDA), ("portafolio", PORTAFOLIO), ("agendar", AGENDAR), ("precio", OBJECIONES[0][1]), ("porque", OBJECIONES[1][1]),
          ("comparar", OBJECIONES[2][1]), ("miedo", OBJECIONES[4][1]), ("duele", OBJECIONES[5][1]),
          ("pensar", OBJECIONES[8][1]), ("dosquebradas", OBJECIONES[7][1])]
for _g, _ms in SEGUIMIENTO:
    for _c, _m in _ms:
        _k = {"Al día siguiente": "sincita1", "Día 3": "sincita3", "Día 7 (último)": "sincita7", "Día 2": "valor2", "Día 7": "valor7",
              "Día 30": "valor30", "Día 1": "cuidados", "Líneas de expresión · día 12": "control", "Día 21 · pedir reseña": "resena", "Líneas de expresión · mes 4": "retoque",
              "Día 21 · después de la reseña": "recomienda", "Llega alguien recomendada": "recomendada"}[_c]
        ATAJOS.append((_k, _m))
ATAJOS += [("diciembre", DICIEMBRE["general"][1]), ("diclineas", DICIEMBRE["tratamientos"][0][2]),
           ("diclabios", DICIEMBRE["tratamientos"][1][2]), ("dicskin", DICIEMBRE["tratamientos"][2][2]),
           ("noalcanza", DICIEMBRE["no_alcanza"][1]), ("visita", VISITA[0][1]),
           ("inauguracion", INVITADAS[0][1]), ("amiga", INVITADAS[1][1]),
           ("verificar", VERIFICANOS[0][1]), ("barato", VERIFICANOS[2][1])]

PERFIL = [
    ("Descripción (perfil de WhatsApp Business)", "Medicina estética en Pereira con criterio médico. Valoración con la %s, médica estética. Torre Médica Oval, consultorio 904." % DRA),
    ("Dirección", DIRECCION),
    ("Sitio web", DOMINIO),
    ("Mensaje de bienvenida (automático)", BIENVENIDA_AUTO),
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
header{position:sticky;top:0;z-index:5;background:rgba(250,248,243,.94);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border-bottom:1px solid var(--linea)}
.cab{max-width:980px;margin:0 auto;padding:14px 20px 0;display:flex;justify-content:space-between;align-items:center;gap:12px}
.cab .eti{font:600 12px var(--sans);letter-spacing:.14em;text-transform:uppercase;color:var(--taupe)}
nav{max-width:980px;margin:0 auto;display:flex;gap:8px;overflow-x:auto;padding:12px 20px 14px;scrollbar-width:none}
nav::-webkit-scrollbar{display:none}
nav a{flex:none;text-decoration:none;color:var(--negro);font:500 14px var(--sans);padding:8px 14px;border-radius:999px;background:#fff;border:1px solid var(--linea);transition:background .2s,color .2s}
nav a.activo{background:var(--negro);border-color:var(--negro);color:#fff}
main{max-width:980px;margin:0 auto;padding:28px 20px 80px}
h1{font:400 clamp(32px,6vw,48px)/1.05 var(--serif);margin:10px 0 10px}h1 em,h2 em{font-family:var(--cursiva);font-style:italic}
h2{font:400 clamp(26px,4.4vw,34px)/1.1 var(--serif);margin:56px 0 16px}
.sub{color:var(--tenue);max-width:40em}.sub a,.nota a{color:var(--negro)}
.reglas{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:12px}
.regla{background:#fff;border-radius:22px;padding:18px 20px}.regla b{display:block;margin-bottom:4px}.regla span{color:var(--tenue);font-size:15px}
.msj{background:#fff;border-radius:22px;padding:18px 20px;margin-bottom:12px}
.msj .cuando,.tarjeta .cuando,.rec .cuando,.etq{font:600 12px var(--sans);letter-spacing:.12em;text-transform:uppercase;color:var(--taupe);margin-bottom:6px}
.msj p{margin:0 0 12px;white-space:pre-line}
.msj p,td{overflow-wrap:anywhere}
.copiar{font:600 13px var(--sans);border:1px solid var(--negro);background:var(--negro);color:#fff;border-radius:999px;padding:12px 16px;cursor:pointer}
.copiar.ok{background:#fff;color:var(--negro)}
.copiar.mini{font-size:12px;padding:12px 14px;margin-top:8px}
.lista{margin:0 0 12px;padding-left:18px}.lista li{margin-bottom:4px}
details{background:#fff;border-radius:22px;margin-bottom:10px;overflow:hidden}
summary{cursor:pointer;list-style:none;padding:18px 20px;font:400 21px var(--serif);display:flex;justify-content:space-between;gap:12px}
summary::-webkit-details-marker{display:none}summary::after{content:"+";font-family:var(--sans);color:var(--taupe)}details[open] summary::after{content:"–"}
summary small{display:block;font:500 13px/1.4 var(--sans);color:var(--tenue);margin-top:5px}
.dentro{padding:0 20px 20px}.dentro .msj{background:var(--marfil)}
.datos{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 14px}.datos span{background:var(--marfil);border-radius:999px;padding:6px 12px;font-size:14px}
.datos b{font-weight:600;margin-right:4px}
.pregunta{margin:0 0 10px}.pregunta b{display:block}
table{width:100%;border-collapse:collapse;background:#fff;border-radius:22px;overflow:hidden;font-size:15px}
td{padding:12px 16px;border-bottom:1px solid var(--linea);vertical-align:top}td:first-child{font-weight:600;white-space:nowrap;width:1%}
.nota{color:var(--tenue);font-size:14px}
.tarjeta{background:#fff;border-radius:22px;padding:18px 20px;margin-bottom:12px}
.tarjeta .lista{margin:0}.tarjeta .lista li{margin-bottom:6px}
.campo{margin:0 0 18px}.campo:last-child{margin-bottom:0}
.campo label.etq,.campo .etq{display:block}
.campo input[type=text],.campo input[type=date]{display:block;width:100%;font:500 17px var(--sans);color:var(--negro);padding:12px 16px;border:1px solid var(--linea);border-radius:14px;background:var(--blanco);-webkit-appearance:none;appearance:none;min-height:50px}
.campo input:focus,.paso input:focus,.pesos input:focus{outline:2px solid var(--nude);outline-offset:1px}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chip{font:500 15px var(--sans);color:var(--negro);background:var(--blanco);border:1px solid var(--linea);border-radius:999px;padding:11px 15px;cursor:pointer}
.chip[aria-pressed=true]{background:var(--negro);border-color:var(--negro);color:#fff}
.accion{display:flex;align-items:center;justify-content:center;gap:8px;width:100%;font:600 15px var(--sans);padding:14px 18px;border-radius:999px;border:1px solid var(--negro);background:var(--negro);color:#fff;text-decoration:none;cursor:pointer;margin-top:12px;text-align:center}
.accion.sec{background:#fff;color:var(--negro)}
.accion.off{opacity:.3;pointer-events:none}
.accion svg{width:18px;height:18px;flex:none}
.aviso{display:flex;gap:10px;align-items:flex-start;background:var(--marfil);border-radius:16px;padding:12px 14px;font-size:14px;line-height:1.45;margin:0 0 12px}
.aviso svg{flex:none;width:18px;height:18px;margin-top:1px}
.rec{background:#fff;border-radius:22px;padding:16px 20px;margin-bottom:10px}
.rec .que{font:400 21px/1.2 var(--serif);margin:0 0 2px}
.rec .pista{color:var(--tenue);font-size:14px;margin:0}
.cal{display:inline-flex;align-items:center;gap:7px;font:600 13px var(--sans);padding:12px 16px;border-radius:999px;border:1px solid var(--negro);background:#fff;color:var(--negro);text-decoration:none;margin-top:12px}
.botones{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}.botones .cal,.botones .copiar{margin-top:0}
.cal svg{width:16px;height:16px}.cal.prim{background:var(--negro);color:#fff}.cal.off{opacity:.3;pointer-events:none}
#rec .accion{margin-top:4px}#rec-pista:empty{display:none}
.rec.pasado .cuando{color:#8a5a2b}
.rec .vista{font-size:14px;margin-top:8px}
.fila{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:10px 0;border-bottom:1px solid var(--linea)}
.fila:last-child{border-bottom:0}
.fila>span{font-weight:600;line-height:1.3}.fila>span small{display:block;font-weight:400;color:var(--tenue);font-size:13px;margin-top:2px}
.paso{display:flex;align-items:center;border:1px solid var(--linea);border-radius:999px;background:var(--blanco);flex:none}
.paso button{width:42px;height:42px;border:0;background:none;font:400 22px/1 var(--sans);color:var(--negro);cursor:pointer;border-radius:999px}
.paso input{width:42px;text-align:center;border:0;background:none;font:600 17px var(--sans);color:var(--negro);padding:0}
.fuentes{display:grid;grid-template-columns:1fr 1fr;gap:8px;background:var(--marfil);border-radius:16px;padding:10px;margin:2px 0 6px}
.fuente{background:#fff;border-radius:14px;padding:9px 8px 8px 12px;display:flex;flex-direction:column;gap:6px;min-width:0}
.fuente>span{font-size:14px;font-weight:500;line-height:1.2}
.fuente .paso{align-self:flex-start}
.paso.chico button{width:40px;height:40px;font-size:19px}.paso.chico input{width:28px;font-size:16px}
#c-cuotas{flex-wrap:nowrap;flex:none}
.alerta:empty{display:none}
.pesos{position:relative;flex:none;width:52%}
.pesos::before{content:"$";position:absolute;left:14px;top:50%;transform:translateY(-50%);color:var(--tenue);font:500 17px var(--sans)}
.pesos input{width:100%;font:600 17px var(--sans);color:var(--negro);padding:11px 14px 11px 28px;border:1px solid var(--linea);border-radius:999px;background:var(--blanco);text-align:right;-webkit-appearance:none;appearance:none}
.vista{background:var(--marfil);border-radius:16px;padding:14px 16px;white-space:pre-line;font-size:15px;line-height:1.5;margin:8px 0 0}
.alerta{color:#8a5a2b;font-size:13px;margin:4px 0 0}
.etiq{display:flex;gap:14px;align-items:flex-start;padding:12px 0;border-bottom:1px solid var(--linea)}
.etiq:first-child{padding-top:2px}.etiq:last-child{border-bottom:0;padding-bottom:2px}
.punto{flex:none;width:14px;height:14px;border-radius:50%;margin-top:4px}
.etiq b{font-weight:600}.etiq .color{color:var(--taupe);font:600 12px var(--sans);letter-spacing:.1em;text-transform:uppercase;margin-left:6px}
.etiq p{margin:2px 0 0;color:var(--tenue);font-size:15px}
.pasos-wa{margin:0;padding-left:20px}.pasos-wa li{margin-bottom:6px}
@media(min-width:760px){#rec,#rec-lista,#cierre-f,#c-caja,.aviso{max-width:640px}}
@media(max-width:600px){td:first-child{white-space:normal}
table,tbody,tr,td{display:block;width:auto}tr{border-bottom:1px solid var(--linea)}tr:last-child{border-bottom:0}
td{border-bottom:0}td:first-child{width:auto;padding-bottom:0;color:var(--taupe);font:600 12px var(--sans);letter-spacing:.08em}td+td{padding-top:4px}}
</style></head><body>
<div id="candado"><form id="f"><div class="logo">THE<b>SKIN HAUS</b></div><p class="nota" style="margin:14px 0 0">Guía interna del equipo. Escribe la clave.</p>
<input id="c" type="password" inputmode="numeric" maxlength="6" autofocus autocomplete="off"><div class="mal" id="mal"></div></form></div>
<header><div class="cab"><div class="logo">THE<b>SKIN HAUS</b></div><span class="eti">Guía de WhatsApp · uso interno</span></div>
<nav>%%NAV%%</nav></header>
<main>%%CUERPO%%</main>
<script>
const H="%%HASH%%";
async function sha(t){const b=await crypto.subtle.digest("SHA-256",new TextEncoder().encode(t));return [...new Uint8Array(b)].map(x=>x.toString(16).padStart(2,"0")).join("")}
function abrir(){const k=document.getElementById("candado");if(k)k.remove()}
let dentro=false;try{dentro=sessionStorage.getItem("sh-guia")===H}catch(e){}
if(dentro){abrir()}else{
document.getElementById("c").addEventListener("input",async e=>{const v=e.target.value;if(v.length<3)return;if(await sha(v)===H){try{sessionStorage.setItem("sh-guia",H)}catch(_){}abrir()}else{document.getElementById("mal").textContent="Clave incorrecta"}});
document.getElementById("f").addEventListener("submit",e=>e.preventDefault());}

/* Copiar: portapapeles moderno y, si el navegador no lo deja, el método viejo */
function viejo(t){return new Promise((ok,ko)=>{const a=document.createElement("textarea");a.value=t;a.setAttribute("readonly","");a.style.cssText="position:fixed;top:0;left:0;opacity:0";document.body.appendChild(a);a.select();a.setSelectionRange(0,t.length);let r=false;try{r=document.execCommand("copy")}catch(e){}a.remove();r?ok():ko()})}
function copiarTexto(t){return navigator.clipboard&&window.isSecureContext?navigator.clipboard.writeText(t).catch(()=>viejo(t)):viejo(t)}
document.addEventListener("click",e=>{const b=e.target.closest("button.copiar");if(!b)return;if(!b.dataset.l)b.dataset.l=b.textContent;
copiarTexto(b.dataset.t||"").then(()=>{b.textContent="Copiado ✓";b.classList.add("ok")},()=>{b.textContent="No se pudo copiar"}).finally(()=>setTimeout(()=>{b.textContent=b.dataset.l;b.classList.remove("ok")},1600))});

/* El menú de arriba marca la sección en la que vas */
(()=>{const nav=document.querySelector("nav");if(!nav)return;const por={};nav.querySelectorAll("a").forEach(a=>por[a.hash.slice(1)]=a);
const hs=[...document.querySelectorAll("main h2[id]")];let act=null,pend=false;
function marcar(){pend=false;let id=hs.length?hs[0].id:"";for(const h of hs){if(h.getBoundingClientRect().top<170)id=h.id;else break}
const a=por[id];if(!a||a===act)return;if(act)act.classList.remove("activo");a.classList.add("activo");act=a;nav.scrollTo({left:a.offsetLeft-nav.offsetLeft-(nav.clientWidth-a.offsetWidth)/2,behavior:"smooth"})}
addEventListener("scroll",()=>{if(!pend){pend=true;requestAnimationFrame(marcar)}},{passive:true});marcar()})();

const dos=n=>String(n).padStart(2,"0");
const DC=["dom","lun","mar","mié","jue","vie","sáb"];
const DL=["domingo","lunes","martes","miércoles","jueves","viernes","sábado"],ML=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"];
const hoy=()=>{const d=new Date();return new Date(d.getFullYear(),d.getMonth(),d.getDate())};

/* Recordatorios en 2 toques: todo se arma en este celular; la web no guarda ni envía nada */
(()=>{const R=%%RECS%%;const caja=document.getElementById("rec");if(!caja)return;
const nom=document.getElementById("rec-nombre"),fec=document.getElementById("rec-fecha"),lista=document.getElementById("rec-lista"),btn=document.getElementById("rec-ics"),pista=document.getElementById("rec-pista");
const android=/Android/i.test(navigator.userAgent);let trat=null,listos=[];const CAL=%%CALSVG%%;
const iso=d=>d.getFullYear()+"-"+dos(d.getMonth()+1)+"-"+dos(d.getDate());
fec.value=iso(hoy());
const leer=v=>{const p=(v||"").split("-").map(Number);return p.length===3&&p[0]?new Date(p[0],p[1]-1,p[2]):null};
const corta=d=>DC[d.getDay()]+" "+d.getDate()+" de "+ML[d.getMonth()]+(d.getFullYear()!==hoy().getFullYear()?" de "+d.getFullYear():"");
/* Festivos de Colombia: fijos, los que pasan al lunes (Ley Emiliani) y los de Semana Santa */
function pascua(y){const a=y%19,b=Math.floor(y/100),c=y%100,d=Math.floor(b/4),e=b%4,f=Math.floor((b+8)/25),g=Math.floor((b-f+1)/3),h=(19*a+b-d-g+15)%30,i=Math.floor(c/4),k=c%4,l=(32+2*e+2*i-h-k)%7,m=Math.floor((a+11*h+22*l)/451),x=h+l-7*m+114;return new Date(y,Math.floor(x/31)-1,x%31+1)}
const FEST={};const clave=d=>d.getFullYear()+"-"+d.getMonth()+"-"+d.getDate();
function festivos(y){if(FEST[y])return FEST[y];const s=new Set(),p=pascua(y);const fijo=(m,d)=>s.add(clave(new Date(y,m,d)));
const lunes=(m,d)=>{const x=new Date(y,m,d);x.setDate(x.getDate()+(8-x.getDay())%7);s.add(clave(x))};const pas=n=>s.add(clave(new Date(y,p.getMonth(),p.getDate()+n)));
[[0,1],[4,1],[6,20],[7,7],[11,8],[11,25]].forEach(a=>fijo(...a));[[0,6],[2,19],[5,29],[7,15],[9,12],[10,1],[10,11]].forEach(a=>lunes(...a));[-3,-2,43,64,71].forEach(pas);return FEST[y]=s}
function fechaDe(b,ev){let d;if(ev.meses){const ult=new Date(b.getFullYear(),b.getMonth()+ev.meses+1,0).getDate();d=new Date(b.getFullYear(),b.getMonth()+ev.meses,Math.min(b.getDate(),ult))}else{d=new Date(b.getFullYear(),b.getMonth(),b.getDate()+ev.dias)}
let motivo="";for(let i=0;i<7&&(d.getDay()===0||festivos(d.getFullYear()).has(clave(d)));i++){if(!motivo)motivo=d.getDay()===0?"cae domingo":"cae festivo";d.setDate(d.getDate()+1)}
return{d,corrido:motivo?motivo+", pasa al "+DL[d.getDay()]:""}}
const ymd=d=>d.getFullYear()+dos(d.getMonth()+1)+dos(d.getDate());
const utc=(d,h,m)=>ymd(d)+"T"+dos(h)+dos(m)+"00Z"; /* 9:00 a. m. en Colombia (UTC-5, sin horario de verano) = 14:00 UTC */
const esc=t=>t.replace(/\\/g,"\\\\").replace(/;/g,"\\;").replace(/,/g,"\\,").replace(/\r?\n/g,"\\n");
const enc=new TextEncoder();
function doblar(l){const out=[];let act="",n=0;for(const ch of l){const b=enc.encode(ch).length;if(n+b>(out.length?74:75)){out.push(act);act=ch;n=b}else{act+=ch;n+=b}}out.push(act);return out.join("\r\n ")}
function ics(evs){const st=new Date().toISOString().replace(/[-:]/g,"").replace(/\.\d+/,"");
const L=["BEGIN:VCALENDAR","VERSION:2.0","PRODID:-//The Skin Haus//Recordatorios del equipo//ES","CALSCALE:GREGORIAN","METHOD:PUBLISH"];
evs.forEach((e,i)=>L.push("BEGIN:VEVENT","UID:"+st+"-"+i+"-"+Math.random().toString(36).slice(2,10)+"@theskinhaus.com.co","DTSTAMP:"+st,"DTSTART:"+utc(e.d,14,0),"DTEND:"+utc(e.d,14,15),"SUMMARY:"+esc(e.titulo),"DESCRIPTION:"+esc(e.detalle),"BEGIN:VALARM","ACTION:DISPLAY","DESCRIPTION:"+esc(e.titulo),"TRIGGER:PT0M","END:VALARM","END:VEVENT"));
L.push("END:VCALENDAR");return L.map(doblar).join("\r\n")+"\r\n"}
const google=e=>"https://calendar.google.com/calendar/render?"+new URLSearchParams({action:"TEMPLATE",text:e.titulo,dates:utc(e.d,14,0)+"/"+utc(e.d,14,15),details:e.detalle,ctz:"America/Bogota"}).toString();
const limpio=t=>t.normalize("NFD").replace(/[\u0300-\u036f]/g,"").toLowerCase().replace(/[^a-z0-9]+/g,"-").replace(/^-+|-+$/g,"")||"paciente";
function el(tag,cls,txt){const x=document.createElement(tag);if(cls)x.className=cls;if(txt!=null)x.textContent=txt;return x}
function pintar(){const n=nom.value.trim().replace(/\s+/g," ");const base=leer(fec.value);lista.textContent="";listos=[];
if(!trat||!base){lista.appendChild(el("p","nota",!trat?"Toca un tratamiento y aquí salen sus recordatorios.":"Falta la fecha de la aplicación."));btn.classList.add("off");pista.textContent="";return}
const t=R[trat],quien=n||"[nombre]",h=hoy();
t.eventos.forEach(ev=>{const {d,corrido}=fechaDe(base,ev);const msj=ev.msj.split("[nombre]").join(quien);
const e={d,titulo:"Escribir a "+quien+" · "+ev.titulo+" ("+ev.rango+")",detalle:"Fecha de la aplicación: "+corta(base)+" ("+t.nombre+").\n\nMensaje para mandarle por WhatsApp:\n"+msj};
const c=el("div","rec");const pasado=d<h;if(pasado)c.classList.add("pasado");
c.appendChild(el("div","cuando",pasado?"Ya pasó: era el "+corta(d):corta(d)+" · 9:00 a. m."+(corrido?" · "+corrido:"")));
c.appendChild(el("p","que",ev.titulo.charAt(0).toUpperCase()+ev.titulo.slice(1)));
c.appendChild(el("p","pista",pasado?"Escríbele hoy. El mensaje:":"Escribirle a "+quien+" ("+ev.rango+"). Lleva este mensaje:"));
const m=el("div","vista",msj);c.appendChild(m);
const bs=el("div","botones");const cp=el("button","copiar mini","Copiar mensaje");cp.type="button";cp.dataset.t=msj;
if(!pasado){listos.push(e);const g=el("a","cal"+(android?" prim":""));g.href=google(e);g.target="_blank";g.rel="noopener";g.innerHTML=CAL;g.appendChild(document.createTextNode("Google Calendar"));if(!n)g.classList.add("off");bs.appendChild(g)}
bs.appendChild(cp);c.appendChild(bs);
lista.appendChild(c)});
btn.classList.toggle("off",!n||!listos.length);btn.classList.toggle("sec",android);
btn.textContent=listos.length>1?"Agregar los "+listos.length+" al calendario":"Agregar al calendario";
pista.textContent=!n?"Escribe el nombre para activar los botones.":(android?"En Android, usa «Google Calendar» en cada recordatorio.":"")}
caja.addEventListener("click",e=>{const ch=e.target.closest(".chip");if(!ch)return;caja.querySelectorAll(".chip").forEach(x=>x.setAttribute("aria-pressed",x===ch?"true":"false"));trat=ch.dataset.k;pintar()});
nom.addEventListener("input",pintar);fec.addEventListener("input",pintar);fec.addEventListener("change",pintar);
btn.addEventListener("click",()=>{if(!listos.length)return;const a=document.createElement("a");a.href="data:text/calendar;charset=utf-8,"+encodeURIComponent(ics(listos));a.download="recordatorio-"+limpio(nom.value)+"-"+trat+".ics";a.target="_blank";a.rel="noopener";document.body.appendChild(a);a.click();a.remove()});
pintar()})();

/* Cierre del día: 8 respuestas → un solo mensaje, sin nombres ni teléfonos */
(()=>{const caja=document.getElementById("cierre-f");if(!caja)return;const F=%%FUENTES%%;
const vista=document.getElementById("c-vista"),wa=document.getElementById("c-wa"),cp=document.getElementById("c-copiar"),al=document.getElementById("c-alerta");
const val=id=>parseInt((document.getElementById(id).value||"").replace(/\D/g,""),10)||0;
const miles=v=>String(v).replace(/\B(?=(\d{3})+(?!\d))/g,".");
let cuotas="No";
function armar(){const d=new Date();const fu=F.map((f,i)=>[f,val("c-f"+i)]).filter(x=>x[1]>0);const suma=fu.reduce((s,x)=>s+x[1],0);const chats=val("c-chats");
const txt=["*Cierre del día · The Skin Haus*",DL[d.getDay()].charAt(0).toUpperCase()+DL[d.getDay()].slice(1)+" "+d.getDate()+" de "+ML[d.getMonth()],
"Chats nuevos: "+chats+(fu.length?" ("+fu.map(x=>x[0]+" "+x[1]).join(", ")+")":""),"Citas agendadas: "+val("c-agendadas"),"Citas que vinieron: "+val("c-vinieron"),
"Tratamientos hechos: "+val("c-tratamientos"),"Pacientes que volvieron: "+val("c-volvieron"),"Pesos que entraron: $"+miles(val("c-pesos")),"¿Preguntaron por cuotas?: "+cuotas].join("\n");
const ls=txt.split("\n");vista.textContent="";const b=document.createElement("b");b.textContent=ls[0].replace(/\*/g,"");vista.appendChild(b);vista.appendChild(document.createTextNode("\n"+ls.slice(1).join("\n")));cp.dataset.t=txt;wa.href="https://wa.me/?text="+encodeURIComponent(txt);
al.textContent=suma&&suma!==chats?"Ojo: «de dónde» suma "+suma+" y pusiste "+chats+" chats nuevos.":""}
caja.addEventListener("click",e=>{const b=e.target.closest(".paso button");if(b){const i=b.parentElement.querySelector("input");i.value=Math.max(0,(parseInt(i.value,10)||0)+Number(b.dataset.d));armar();return}
const ch=e.target.closest(".chip");if(ch){caja.querySelectorAll("#c-cuotas .chip").forEach(x=>x.setAttribute("aria-pressed",x===ch?"true":"false"));cuotas=ch.textContent;armar()}});
caja.addEventListener("input",e=>{const t=e.target;if(t.closest(".paso"))t.value=t.value.replace(/\D/g,"").slice(0,3);if(t.id==="c-pesos"){const v=t.value.replace(/\D/g,"").replace(/^0+(?=\d)/,"").slice(0,11);t.value=v?miles(v):""}armar()});
armar()})();
</script></body></html>"""

CANDADO_SVG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="5" y="11" width="14" '
               'height="10" rx="2.5"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>')
CAL_SVG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3.5" y="5" width="17" '
           'height="15.5" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/></svg>')
WA_SVG = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 '
          '18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 '
          '1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5c-.2 0-.4.1-.7.3-.2.3-.9.9-.9 '
          '2.2s.9 2.5 1 2.7c.1.2 1.8 2.8 4.4 3.9 1.6.7 2.3.8 3.1.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3z"/></svg>')


def _msj(texto, cuando=""):
    c = '<div class="cuando">%s</div>' % escape(cuando) if cuando else ""
    return '<div class="msj">%s<p>%s</p><button class="copiar" type="button" data-t="%s">Copiar mensaje</button></div>' % (c, escape(texto), escape(texto, quote=True))


def _enlace(url, texto=None):
    return '<a href="https://%s" target="_blank" rel="noopener">%s</a>' % (escape(url, quote=True), escape(texto or url))


def _paso(id_, etiqueta="", ayuda=""):
    """Fila con contador − n + (sirve para teclear también)."""
    t = '<span>%s%s</span>' % (escape(etiqueta), ('<small>%s</small>' % escape(ayuda)) if ayuda else "")
    return ('<div class="fila">%s<div class="paso"><button type="button" data-d="-1" aria-label="Uno menos">−</button>'
            '<input id="%s" type="text" inputmode="numeric" pattern="[0-9]*" value="0" aria-label="%s"><button type="button" data-d="1" '
            'aria-label="Uno más">+</button></div></div>') % (t, id_, escape(etiqueta, quote=True))


def _fuente(id_, etiqueta):
    """Celda compacta para el "¿de dónde vinieron?" del cierre (2 columnas en el celular)."""
    return ('<div class="fuente"><span>%s</span><div class="paso chico"><button type="button" data-d="-1" aria-label="Uno menos">−</button>'
            '<input id="%s" type="text" inputmode="numeric" pattern="[0-9]*" value="0" aria-label="%s"><button type="button" data-d="1" '
            'aria-label="Uno más">+</button></div></div>') % (escape(etiqueta), id_, escape(etiqueta, quote=True))


def _diciembre():
    acc = "".join('<details><summary><span>%s<small>%s</small></span></summary><div class="dentro">%s</div></details>'
                  % (escape(n), escape(r), _msj(m)) for n, r, m in DICIEMBRE["tratamientos"])
    return ('<h2 id="diciembre">Diciembre: <em>qué alcanza</em></h2>'
            '<p class="sub">Las fechas son para Nochebuena (jueves 24 de diciembre). Para cualquier otra fecha (el grado, la fiesta de '
            'la empresa, fin de año), la calculadora hace la cuenta: %s. El martes 8 es festivo: esa semana hay un día menos para '
            'agendar.</p>' % _enlace(TU_FECHA)
            + _msj(DICIEMBRE["general"][1], DICIEMBRE["general"][0])
            + '<p class="nota" style="margin:18px 0 10px">Por tratamiento, para Nochebuena:</p>' + acc
            + _msj(DICIEMBRE["no_alcanza"][1], DICIEMBRE["no_alcanza"][0]))


def _visita():
    cabe = "".join("<li><b>%s:</b> %s</li>" % (escape(a), escape(b)) for a, b in VISITA_CABE)
    return ('<h2 id="visita">Vienen <em>de visita</em></h2>'
            '<p class="sub">A quien viene de afuera se le agenda la valoración en sus primeros días en Pereira, para que el control '
            'alcance antes de que se vaya. Pregúntale siempre qué día llega y qué día se va. Ponle la etiqueta «De visita» y súmala '
            'en el cierre del día. En la calculadora está la pestaña «Vengo de visita»: %s.</p>' % _enlace(TU_FECHA)
            + '<div class="tarjeta"><div class="cuando">Qué cabe en una visita</div><ul class="lista">%s</ul></div>' % cabe
            + "".join(_msj(m, c) for c, m in VISITA))


def _invitadas():
    return ('<h2 id="invitadas">Invitadas de la <em>inauguración</em></h2>'
            '<p class="sub">Para quienes fueron a la apertura del 16 de octubre. Se manda una sola vez, de 10 en 10 y chat por chat, '
            'nunca como lista de difusión. Si ya le mandaste el mensaje anterior, no se lo mandes otra vez. Sin descuentos. Si '
            'responde, sigue con el seguimiento de siempre.</p>'
            + "".join(_msj(m, c) for c, m in INVITADAS))


def _verificanos():
    return ('<h2 id="verificanos"><em>Verifícanos</em></h2>'
            '<p class="sub">Después de la valoración, cuando ya se habló del valor, mándale la foto de la caja del producto que '
            'propuso la Dra., con el registro INVIMA a la vista, y el enlace del RETHUS. Si compara antes de la valoración, manda solo '
            'el RETHUS (el último mensaje de abajo). En la foto no puede salir nada de otra persona. Enlaces oficiales: <a href="%s" target="_blank" rel="noopener">INVIMA</a> · '
            '<a href="%s" target="_blank" rel="noopener">RETHUS</a>.</p>' % (escape(INVIMA, quote=True), escape(RETHUS, quote=True))
            + "".join(_msj(m, c) for c, m in VERIFICANOS))


def _recordatorios():
    chips = "".join('<button type="button" class="chip" data-k="%s" aria-pressed="false">%s</button>' % (k, escape(n)) for k, n, _ in RECORDATORIOS)
    return ('<h2 id="recordatorios">Recordatorios <em>en 2 toques</em></h2>'
            '<p class="sub">Al terminar la cita: escribe el nombre, toca el tratamiento y revisa la fecha. Salen los recordatorios '
            'para tu calendario, cada uno con el mensaje listo para mandar ese día.</p>'
            '<div class="aviso">%s<span><b>No se guarda ningún dato.</b> El nombre se queda en tu celular y en tu calendario. '
            'Escribe solo el nombre, sin apellido ni teléfono.</span></div>' % CANDADO_SVG
            + '<div class="tarjeta" id="rec">'
            '<div class="campo"><label class="etq" for="rec-nombre">Nombre</label><input id="rec-nombre" type="text" '
            'autocomplete="off" autocapitalize="words" spellcheck="false" placeholder="Solo el nombre" maxlength="30"></div>'
            '<div class="campo"><span class="etq">Tratamiento</span><div class="chips">%s</div></div>' % chips
            + '<div class="campo"><label class="etq" for="rec-fecha">Fecha de la aplicación</label><input id="rec-fecha" type="date"></div>'
            '<button type="button" class="accion off" id="rec-ics">Agregar al calendario</button>'
            '<p class="nota" id="rec-pista" style="margin:10px 0 0;text-align:center"></p>'
            '</div><div id="rec-lista" aria-live="polite"></div>')


def _cierre():
    if CIERRE_FORM_URL:
        preguntas = "".join("<li>%s</li>" % escape(p) for _, p, _ in CIERRE_PREGUNTAS)
        cuerpo = ('<div class="tarjeta"><div class="cuando">Lo que te va a preguntar</div><ol class="lista">%s</ol>'
                  '<a class="accion" href="%s" target="_blank" rel="noopener">Abrir el cierre del día</a></div>'
                  % (preguntas, escape(CIERRE_FORM_URL, quote=True)))
    else:
        filas = []
        for id_, preg, ayuda in CIERRE_PREGUNTAS:
            if id_ == "c-fuentes":
                filas.append('<div class="fila" style="border-bottom:0;padding-bottom:4px"><span>%s<small>%s</small></span></div>'
                             '<div class="fuentes">%s</div><p class="alerta" id="c-alerta" aria-live="polite"></p>'
                             % (escape(preg), escape(ayuda), "".join(_fuente("c-f%d" % i, f) for i, f in enumerate(CIERRE_FUENTES))))
            elif id_ == "c-pesos":
                filas.append('<div class="fila"><span>%s<small>%s</small></span><div class="pesos"><input id="c-pesos" type="text" '
                             'inputmode="numeric" autocomplete="off" placeholder="0" aria-label="%s"></div></div>'
                             % (escape(preg), escape(ayuda), escape(preg, quote=True)))
            elif id_ == "c-cuotas":
                filas.append('<div class="fila"><span>%s</span><div class="chips" id="c-cuotas"><button type="button" class="chip" '
                             'aria-pressed="true">No</button><button type="button" class="chip" aria-pressed="false">Sí</button></div></div>'
                             % escape(preg))
            else:
                filas.append(_paso(id_, preg, ayuda))
        cuerpo = ('<div class="tarjeta" id="cierre-f">%s</div>'
                  '<div class="tarjeta" id="c-caja"><div class="cuando">Así se va al grupo</div><div class="vista" id="c-vista" style="margin:0"></div>'
                  '<a class="accion" id="c-wa" href="#" target="_blank" rel="noopener">%sEnviar al grupo «Lo que entra»</a>'
                  '<button class="copiar accion sec" type="button" id="c-copiar" data-t="">Copiar el resumen</button></div>'
                  % ("".join(filas), WA_SVG))
    return ('<h2 id="cierre">Cierre <em>del día</em></h2>'
            '<p class="sub">Al cerrar, 30 segundos: llena los números del día y mándalos al grupo «Lo que entra». Solo números, sin '
            'nombres ni teléfonos. Las etiquetas de WhatsApp te ayudan a contarlos.</p>' + cuerpo)


def _fuera_horario():
    return ('<h2 id="ausencia">Fuera <em>de horario</em></h2>'
            '<p class="sub">En WhatsApp Business: Herramientas para la empresa → Mensaje de ausencia → actívalo y, en Programar, '
            'elige «Fuera del horario comercial» (sirve solo si el horario está puesto en el perfil; si no, usa «Horario '
            'personalizado»). Hasta el 10 de diciembre va el primero; desde el 11, cámbialo por el segundo.</p>'
            + "".join(_msj(m, c) for c, m in FUERA_HORARIO))


def _etiquetas():
    filas = "".join('<div class="etiq"><span class="punto" style="background:%s"></span><div><b>%s</b><span class="color">%s</span>'
                    '<p>%s</p></div></div>' % (hexa, escape(n), escape(col), escape(cu)) for n, col, hexa, cu in ETIQUETAS)
    return ('<h2 id="etiquetas">Las <em>etiquetas</em></h2>'
            '<p class="sub">En WhatsApp Business: Herramientas para la empresa → Etiquetas → crea estas 6 con su color. Para marcar un '
            'chat, mantenlo presionado y toca la etiqueta (en iPhone: desliza el chat a la izquierda → Más → Etiquetar chat). Con '
            'ellas sale fácil el cierre del día.</p><div class="tarjeta">%s</div>' % filas)


def generar():
    secciones = [("reglas", "Reglas"), ("primer", "Primer mensaje"), ("diciembre", "Diciembre"), ("visita", "De visita"),
                 ("tratamientos", "Tratamientos"), ("objeciones", "Dudas y objeciones"), ("verificanos", "Verifícanos"),
                 ("seguimiento", "Seguimiento"), ("invitadas", "Invitadas"), ("recordatorios", "Recordatorios"),
                 ("cierre", "Cierre del día"), ("atajos", "Respuestas rápidas"), ("perfil", "Perfil de WhatsApp"),
                 ("ausencia", "Fuera de horario"), ("etiquetas", "Etiquetas")]
    nav = "".join('<a href="#%s">%s</a>' % s for s in secciones)
    c = []
    c.append('<h1>Cada chat, <em>una cita.</em></h1><p class="sub">Guía para responder el WhatsApp de The Skin Haus (%s). Los mensajes se copian con un toque. Cambia lo que está entre corchetes o llaves, como <b>[nombre]</b> o <b>{nombre}</b>, antes de enviar.</p>' % escape(TELEFONO_VISIBLE))
    c.append('<h2 id="reglas">Las 6 <em>reglas</em></h2><div class="reglas">%s</div>' % "".join('<div class="regla"><b>%s</b><span>%s</span></div>' % (escape(a), escape(b)) for a, b in REGLAS))
    c.append('<h2 id="primer">El primer <em>mensaje</em></h2>' + _msj(BIENVENIDA, "Cuando alguien escribe")
             + '<p class="nota" style="margin:-4px 4px 14px">Si el mensaje automático de bienvenida ya le preguntó esto, no lo repitas: responde a lo que te contó.</p>'
             + '<div class="msj"><div class="cuando">Las %d preguntas que siempre haces</div><ol class="lista">%s</ol></div>' % (len(PREGUNTAS_CLAVE), "".join("<li>%s</li>" % escape(p) for p in PREGUNTAS_CLAVE))
             + _msj(PORTAFOLIO, "Si pregunta qué tratamientos hacen (manda el portafolio en PDF)")
             + _msj(AGENDAR, "Para agendar (ofrece siempre dos opciones)") + _msj(CONFIRMACION, "Cuando confirma: mensaje de confirmación"))
    c.append(_diciembre())
    c.append(_visita())
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
    c.append(_verificanos())
    seg = []
    for grupo, msjs in SEGUIMIENTO:
        seg.append('<details %s><summary>%s</summary><div class="dentro">%s</div></details>' % ("open" if not seg else "", escape(grupo), "".join(_msj(m, cu) for cu, m in msjs)))
    c.append('<h2 id="seguimiento">El <em>seguimiento</em></h2><p class="sub">Aquí se gana la mayoría de las citas. Si alguien no contesta tres mensajes seguidos, se pausa y se vuelve a intentar en dos meses. Anota la fecha de cada mensaje.</p>' + "".join(seg))
    c.append(_invitadas())
    c.append(_recordatorios())
    c.append(_cierre())
    filas = "".join('<tr><td>/%s</td><td>%s<br><button class="copiar mini" type="button" data-t="%s">Copiar</button></td></tr>'
                    % (escape(k), escape(m), escape(m, quote=True)) for k, m in ATAJOS)
    c.append('<h2 id="atajos">Respuestas <em>rápidas</em></h2><p class="sub">En WhatsApp Business: Herramientas para la empresa → Respuestas rápidas → +. Escribe el atajo (sin la barra) y pega el mensaje. Después, en un chat, escribes / y eliges.</p><table>%s</table>' % filas)
    perfil = "".join(_msj(v, k) for k, v in PERFIL)
    c.append('<h2 id="perfil">Perfil de <em>WhatsApp Business</em></h2><p class="sub">Textos listos para Herramientas para la empresa → Perfil y Mensaje de bienvenida. El mensaje de ausencia está en «Fuera de horario».</p>' + perfil)
    c.append(_fuera_horario())
    c.append(_etiquetas())
    recs = {k: {"nombre": n, "eventos": evs} for k, n, evs in RECORDATORIOS}
    js = lambda o: json.dumps(o, ensure_ascii=False).replace("</", "<\\/")
    html = (PLANTILLA.replace("%%NAV%%", nav).replace("%%CUERPO%%", "\n".join(c))
            .replace("%%RECS%%", js(recs)).replace("%%FUENTES%%", js(CIERRE_FUENTES)).replace("%%CALSVG%%", js(CAL_SVG))
            .replace("%%HASH%%", hashlib.sha256(CODIGO.encode()).hexdigest()))
    with open(os.path.join(AQUI, "equipo.html"), "w", encoding="utf-8") as f:
        f.write(html)
    return len(ESTETICA + BUSQUEDAS)


if __name__ == "__main__":
    print("Guía de WhatsApp: %d tratamientos." % generar())
