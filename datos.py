# -*- coding: utf-8 -*-
# The Skin Haus · contenido de la web. Editar aquí y correr:  python3 build.py

MARCA = "The Skin Haus"
CIUDAD = "Pereira"
DOMINIO = "https://theskinhaus.com.co"          # comprado en GoDaddy 28-sep-2026 (principal SIN www)
WHATSAPP = "573174412203"
TELEFONO_VISIBLE = "+57 317 441 2203"
DIRECCION = "Torre Médica Oval · Pereira"
HORARIO = [("Lunes a viernes", "8:00 a. m. – 6:00 p. m."), ("Sábados", "9:00 a. m. – 1:00 p. m.")]  # PENDIENTE
INSTAGRAM = "https://www.instagram.com/"         # PENDIENTE: usuario real
CORREO = "hola@theskinhaus.com.co"                 # PENDIENTE

# ------------------------------------------------------------------ tratamientos
# linea: frase corta · intro: 1 párrafo · para: a quién · como: (duración, sesiones, recuperación)
# pasos: cómo es la cita · faq: preguntas
ESTETICA = [
    dict(slug="toxina-botulinica", nombre="Toxina botulínica", foto="facial",
         linea="Relaja las líneas de expresión sin quitarte la expresión.",
         intro="Suaviza las arrugas que aparecen al gesticular —frente, entrecejo y patas de gallo— relajando de forma temporal y localizada el músculo que las marca. Bien dosificada, la cara descansa; no se congela.",
         para=["Líneas de expresión en frente, entrecejo o contorno de ojos", "Quienes quieren prevenir que esas líneas se marquen más", "Sudoración excesiva en axilas o manos (hiperhidrosis)"],
         como=("20–30 minutos", "Una sesión; se repite cada 4–6 meses", "Vuelves a tu día de inmediato"),
         faq=[("¿Voy a quedar con la cara rígida?", "No es la idea. Dosificamos según tu musculatura y tus gestos para que el resultado se vea descansado y natural."),
              ("¿Cuándo se ve el efecto?", "Empieza a notarse entre el día 3 y el 7, y se ve completo alrededor de las dos semanas, cuando hacemos control."),
              ("¿Duele?", "Son punciones muy finas y rápidas. La mayoría lo describe como una molestia leve y breve.")]),
    dict(slug="acido-hialuronico", nombre="Ácido hialurónico", foto="retrato",
         linea="Volumen y soporte donde tu rostro los fue perdiendo.",
         intro="Un gel compatible con tu piel que devuelve soporte, contorno o hidratación profunda en zonas puntuales: labios, ojeras, pómulos, mentón o mandíbula. El objetivo es armonía, no cambiar quién eres.",
         para=["Pérdida de volumen en pómulos, sienes u ojeras", "Labios que quieres definir o hidratar sutilmente", "Perfilar mentón o línea mandibular"],
         como=("30–45 minutos", "Una sesión; dura de 9 a 18 meses según la zona", "Puede haber inflamación leve 24–72 horas"),
         faq=[("¿Se puede revertir?", "Sí. El ácido hialurónico se puede disolver con una enzima si alguna vez fuera necesario."),
              ("¿Se nota que me hice algo?", "Trabajamos por capas y en poca cantidad. Lo que la gente suele notar es que te ves bien, no qué te hiciste."),
              ("¿Cuánto producto voy a necesitar?", "Lo definimos en la valoración, después de analizar tu rostro en reposo y en movimiento.")]),
    dict(slug="bioestimuladores", nombre="Bioestimuladores de colágeno", foto="piel",
         linea="Tu piel vuelve a producir lo que necesita.",
         intro="Sustancias como la hidroxiapatita de calcio o el ácido poliláctico estimulan a tu propia piel a fabricar colágeno nuevo. El cambio es progresivo: más firmeza, mejor calidad de piel y un rostro que se sostiene mejor.",
         para=["Flacidez leve a moderada en rostro, cuello o cuerpo", "Piel que se siente más delgada o sin firmeza", "Quienes prefieren un cambio gradual y natural"],
         como=("40–60 minutos", "1 a 3 sesiones, separadas 4–8 semanas", "Enrojecimiento o sensibilidad por 1–3 días"),
         faq=[("¿Cuándo veo resultados?", "El colágeno tarda en formarse: los cambios se empiezan a notar hacia la semana 6–8 y siguen mejorando por meses."),
              ("¿Es lo mismo que un relleno?", "No. El relleno aporta volumen inmediato; el bioestimulador mejora la calidad y firmeza de la piel desde adentro."),
              ("¿Cuánto dura?", "Entre 12 y 24 meses, según el producto, tu piel y tus hábitos.")]),
    dict(slug="skinboosters", nombre="Skinboosters", foto="piel",
         linea="Hidratación profunda que se ve en la luz de tu piel.",
         intro="Microinyecciones de ácido hialurónico ligero, a veces combinado con vitaminas y aminoácidos, que hidratan desde adentro. La piel se ve más luminosa, suave y uniforme, sin cambiar volúmenes.",
         para=["Piel opaca, deshidratada o con textura irregular", "Líneas finas en mejillas, cuello o escote", "Preparar la piel antes de un evento importante"],
         como=("30–40 minutos", "3 sesiones, cada 3–4 semanas; mantenimiento semestral", "Pequeñas pápulas que desaparecen en 24–48 horas"),
         faq=[("¿Me cambia la forma de la cara?", "No. Mejora la calidad de la piel; no aporta volumen."),
              ("¿Puedo combinarlo con otros tratamientos?", "Sí, suele complementar muy bien la toxina y los bioestimuladores. Lo planeamos juntos."),
              ("¿Hay que cuidarse después?", "Evita maquillaje por 12 horas y sol directo por unos días. Te damos las indicaciones por escrito.")]),
    dict(slug="peelings-medicos", nombre="Peelings médicos", foto="piel",
         linea="Renovar la piel, capa por capa, con criterio médico.",
         intro="Soluciones de ácidos elegidas para tu tipo de piel que aceleran la renovación celular. Ayudan con manchas, textura, poros y marcas de acné. Desde peelings suaves sin descamación visible hasta renovaciones más profundas.",
         para=["Manchas, tono irregular o melasma", "Textura rugosa, poros dilatados o marcas de acné", "Piel apagada que necesita renovarse"],
         como=("30 minutos", "Serie de 3 a 6 sesiones, cada 2–4 semanas", "Según la profundidad: de ninguna a una semana de descamación"),
         faq=[("¿Me voy a pelar mucho?", "Depende del peeling. Te explicamos antes qué esperar y elegimos la intensidad según tu agenda y tu piel."),
              ("¿Sirve para pieles morenas?", "Sí, con la elección correcta del ácido y una buena preparación. Por eso valoramos antes."),
              ("¿Puedo hacerlo en cualquier época?", "Sí, con protector solar estricto. En temporadas de mucho sol preferimos opciones más suaves.")]),
    dict(slug="microagujas", nombre="Microagujas", foto="facial",
         linea="Microestímulos precisos para que la piel se repare mejor.",
         intro="Un dispositivo con agujas finísimas crea microcanales controlados que activan la reparación natural de la piel. Mejora cicatrices de acné, poros, textura y firmeza. Puede potenciarse con activos o plasma.",
         para=["Cicatrices de acné y marcas", "Poros dilatados y textura irregular", "Estrías recientes o piel sin firmeza"],
         como=("45–60 minutos", "3 a 5 sesiones, cada 4 semanas", "Enrojecimiento tipo sol por 24–48 horas"),
         faq=[("¿Duele?", "Aplicamos anestesia tópica antes. Se siente una vibración y un leve raspado."),
              ("¿Cuándo puedo maquillarme?", "Después de 24 horas, con productos limpios."),
              ("¿Es para todo tipo de piel?", "Para la mayoría. En acné activo o algunas condiciones de piel primero tratamos eso.")]),
    dict(slug="manchas-y-melasma", nombre="Manchas y melasma", foto="retrato",
         linea="Un plan para el tono de tu piel, no una solución mágica.",
         intro="Las manchas tienen causas distintas —sol, hormonas, inflamación— y por eso no se tratan igual. Combinamos cuidado en casa, peelings, láser o tecnologías según tu diagnóstico, con metas realistas y seguimiento.",
         para=["Melasma en frente, mejillas o bigote", "Manchas por sol o por la edad", "Marcas oscuras que dejó el acné"],
         como=("Plan por etapas", "Sesiones según el diagnóstico", "Variable; siempre con fotoprotección"),
         faq=[("¿El melasma se cura?", "Es una condición crónica: se controla y mejora mucho, pero necesita mantenimiento. Te lo decimos claro desde el inicio."),
              ("¿Por qué necesito valoración?", "Porque tratar una mancha con el método equivocado puede oscurecerla. El diagnóstico va primero."),
              ("¿Qué hago en casa?", "Te armamos una rutina sencilla con los productos que de verdad necesitas.")]),
    dict(slug="limpieza-facial-medica", nombre="Limpieza facial médica", foto="facial",
         linea="El punto de partida de una piel bien cuidada.",
         intro="Una limpieza profunda hecha con criterio médico: extracción cuidadosa, exfoliación, activos según tu piel e hidratación. Es ideal para empezar, para mantener y para preparar otros tratamientos.",
         para=["Puntos negros, poros obstruidos o brotes leves", "Piel que necesita mantenimiento mensual", "Antes de un evento o de otros procedimientos"],
         como=("60 minutos", "Cada 4–6 semanas", "Vuelves a tu día de inmediato"),
         faq=[("¿En qué se diferencia de una limpieza en spa?", "La hace personal entrenado bajo supervisión médica y se ajusta a tu diagnóstico de piel."),
              ("¿Sirve si tengo acné?", "Sí, adaptada. Si el acné es activo, también te orientamos con el manejo médico."),
              ("¿Queda la piel roja?", "Puede quedar un rubor leve por unas horas.")]),
]

VASCULAR = [
    dict(slug="aranitas-vasculares", nombre="Arañitas vasculares", foto="vascular",
         linea="Piernas más limpias, con un tratamiento sencillo y ambulatorio.",
         intro="Las arañitas (telangiectasias) son pequeños vasos visibles, rojos o violeta. Con escleroterapia —microinyecciones de una sustancia que cierra el vaso— y, cuando conviene, láser, van desapareciendo de forma progresiva.",
         para=["Arañitas rojas o violeta en muslos y piernas", "Venitas azules pequeñas (reticulares)", "Quienes quieren mejorar la apariencia de sus piernas"],
         como=("30–45 minutos", "2 a 4 sesiones, cada 4–6 semanas", "Caminas de inmediato; medias de compresión unos días"),
         faq=[("¿Por qué necesito una ecografía antes?", "Porque muchas arañitas son la señal visible de un problema venoso más profundo. Si no se trata la causa, vuelven."),
              ("¿Duele la escleroterapia?", "Se usan agujas muy finas. Se siente como pequeños pinchazos."),
              ("¿Pueden volver a salir?", "Los vasos tratados no vuelven, pero pueden aparecer nuevos. Te enseñamos cómo prevenirlos.")]),
    dict(slug="varices", nombre="Várices", foto="vascular",
         linea="Más que estética: tus venas también hablan de tu salud.",
         intro="Las várices son venas dilatadas por insuficiencia venosa: la sangre no regresa bien al corazón. Con un diagnóstico preciso elegimos el tratamiento mínimamente invasivo adecuado, casi siempre ambulatorio y sin cirugía abierta.",
         para=["Venas abultadas o visibles en las piernas", "Pesadez, cansancio, calambres o hinchazón al final del día", "Antecedentes familiares de várices"],
         como=("Según la técnica", "Plan definido tras el eco-doppler", "Retomas actividades en pocos días"),
         faq=[("¿Las várices son solo estéticas?", "No siempre. Pueden avanzar y causar hinchazón, cambios en la piel o úlceras. Por eso vale la pena valorarlas."),
              ("¿Hay que operarse?", "Hoy la mayoría se trata con técnicas mínimamente invasivas en consultorio. Te explicamos las opciones según tu caso."),
              ("¿Qué pasa si no las trato?", "Depende del caso. En la valoración te decimos con claridad si es urgente o si puede esperar.")]),
    dict(slug="eco-doppler-venoso", nombre="Eco-doppler venoso", foto="vascular",
         linea="Ver cómo circula tu sangre antes de decidir nada.",
         intro="Una ecografía que muestra en tiempo real cómo funcionan las venas de tus piernas: si las válvulas cierran bien, dónde hay reflujo y cuál es el origen de las várices o arañitas. Es el mapa para un tratamiento acertado.",
         para=["Antes de tratar arañitas o várices", "Pesadez, hinchazón o dolor en piernas", "Seguimiento después de un tratamiento vascular"],
         como=("30–40 minutos", "Un examen", "Sin preparación ni recuperación"),
         faq=[("¿Duele?", "No. Es una ecografía con gel; solo sentirás la presión suave del transductor."),
              ("¿Tengo que ir en ayunas?", "No. Ven con ropa cómoda que permita descubrir las piernas."),
              ("¿Me entregan resultado?", "Sí, con el mapa venoso y la explicación del médico en la misma cita.")]),
    dict(slug="cuperosis-y-rojeces", nombre="Cuperosis y rojeces", foto="retrato",
         linea="Donde la piel y los vasos se encuentran.",
         intro="Los vasitos visibles en nariz y mejillas, el enrojecimiento persistente y la rosácea tienen un componente vascular. Los tratamos con láser o luz pulsada y una rutina que calme la piel, uniendo nuestras dos especialidades.",
         para=["Vasitos visibles en nariz y mejillas", "Enrojecimiento persistente o rosácea", "Piel reactiva que se enrojece con facilidad"],
         como=("20–30 minutos", "2 a 4 sesiones, cada 4 semanas", "Rubor leve por algunas horas"),
         faq=[("¿La rosácea se cura?", "Se controla. Con tratamiento y cuidados, los brotes se reducen mucho."),
              ("¿Puedo tomar sol después?", "Hay que evitarlo unos días y usar protector siempre. Te damos indicaciones claras."),
              ("¿Sirve para pieles morenas?", "Ajustamos la tecnología y los parámetros a tu fototipo. Lo definimos en la valoración.")]),
]

TODOS = ESTETICA + VASCULAR

# pasos de la experiencia (home)
CAMINO = [
    ("Te escuchamos", "Conversamos sobre lo que quieres cuidar y lo que no quieres cambiar."),
    ("Evaluamos", "Analizamos tu piel, tu rostro o tus venas con criterio médico antes de recomendar."),
    ("Tu plan", "Te explicamos opciones, tiempos y costos. Decides con calma, sin presión."),
    ("Te acompañamos", "El cuidado continúa después de tu cita, con controles y seguimiento."),
]

PREGUNTAS_GENERALES = [
    ("¿La valoración tiene costo?", "Te lo confirmamos al agendar. En la valoración médica revisamos tu caso y definimos un plan, sin compromiso de hacerte ningún tratamiento."),
    ("¿Quién me atiende?", "Siempre un médico. Los procedimientos los realiza o supervisa directamente el equipo médico de la clínica."),
    ("¿Puedo hacerme un tratamiento el mismo día de la valoración?", "En muchos casos sí, si el médico lo considera adecuado y tú te sientes lista o listo para decidir."),
]

# ------------------------------------------------------------------ para escanear rápido
# 2 datos clave por tratamiento (tarjetas) + frase corta de para qué sirve
CLAVE = {
    "toxina-botulinica": ("Líneas de expresión", "20–30 min", "Sin incapacidad"),
    "acido-hialuronico": ("Volumen y contorno", "30–45 min", "Dura 9–18 meses"),
    "bioestimuladores": ("Firmeza y colágeno", "1–3 sesiones", "Cambio progresivo"),
    "skinboosters": ("Hidratación y luz", "3 sesiones", "Sin incapacidad"),
    "peelings-medicos": ("Manchas y textura", "30 min", "Serie de 3–6"),
    "microagujas": ("Cicatrices y poros", "45–60 min", "Rubor 24–48 h"),
    "manchas-y-melasma": ("Tono uniforme", "Plan por etapas", "Con seguimiento"),
    "limpieza-facial-medica": ("Piel limpia y sana", "60 min", "Sin incapacidad"),
    "aranitas-vasculares": ("Piernas más limpias", "30–45 min", "Caminas de inmediato"),
    "varices": ("Venas y pesadez", "Ambulatorio", "Sin cirugía abierta"),
    "eco-doppler-venoso": ("Diagnóstico preciso", "30–40 min", "Sin preparación"),
    "cuperosis-y-rojeces": ("Rojeces del rostro", "20–30 min", "2–4 sesiones"),
}


# ================================================================== SEO medicina estética (19-oct-2026)
# Estrategia: _agencia/estrategia.md. Solo medicina estética en Pereira.
ACTUALIZADO = "2026-10-27"          # fecha de la última revisión de las páginas fijas (va al sitemap)
AREA = ["Pereira", "Dosquebradas", "Santa Rosa de Cabal", "La Virginia", "Cartago"]

# Por tratamiento de estética: título y descripción para Google, h1 visible (opcional),
# secciones largas (h2, html) y preguntas reales de Google que se suman a las de la página.
SEO = {
    "toxina-botulinica": dict(
        titulo="Bótox en Pereira (toxina botulínica) · The Skin Haus",
        desc="Bótox en Pereira con criterio médico: frente, entrecejo y patas de gallo en 20–30 minutos y sin incapacidad. Valoración en la Torre Médica Oval.",
        h1="Toxina botulínica <em>(bótox)</em>",
        secciones=[
            ("¿Bótox y toxina botulínica son lo mismo?",
             "<p>Sí, en lo esencial. Botox es el nombre comercial más conocido de la toxina botulínica tipo A, y por eso en Pereira casi todo el mundo dice “bótox”. Existen otras marcas con registro sanitario.</p>"
             "<p>Lo que de verdad importa no es el nombre de la caja: es que el producto tenga registro INVIMA, que lo aplique un médico y que la dosis se decida después de ver cómo se mueve tu cara. En la valoración te decimos qué producto usamos y por qué.</p>"),
            ("Cómo es tu cita de bótox en Pereira",
             "<p>Primero conversamos y miramos tus gestos: cómo levantas las cejas, cómo frunces, cómo sonríes. Con eso decidimos dónde y cuánto. Luego limpiamos la piel y aplicamos con agujas muy finas, en pocos minutos.</p>"
             "<p>La cita completa toma de 20 a 30 minutos y vuelves a tu día de inmediato, así que cabe a la hora del almuerzo o al salir del trabajo. El efecto empieza a notarse entre el día 3 y el 7 y a las dos semanas te vemos en control.</p>"),
            ("Cuidados después de la aplicación",
             "<p>Las primeras horas evita acostarte, hacer ejercicio intenso y masajear la zona tratada. Si al día siguiente no ves nada, es normal: la toxina necesita unos días para actuar. Te damos las indicaciones por escrito.</p>"
             "<p>Si quieres el detalle, lee <a href=\"blog/que-no-hacer-despues-del-botox\">qué no hacer después del bótox</a> y <a href=\"blog/cuanto-dura-el-botox\">cuánto dura el bótox</a>, mes a mes.</p>"),
            ("Lo que el bótox no hace",
             "<p>No rellena ni levanta: relaja. Las arrugas que se ven con la cara quieta, los surcos o la pérdida de volumen se trabajan mejor con <a href=\"acido-hialuronico\">ácido hialurónico</a> o <a href=\"bioestimuladores\">bioestimuladores</a>. Si es tu caso, te lo decimos en la valoración en vez de poner más toxina.</p>"),
        ],
        faq=[("¿Cuánto vale una sesión de bótox en Pereira?", "Depende de las zonas que tratemos y de la cantidad de producto que necesita tu musculatura. Te damos el valor exacto en la valoración, antes de empezar, para que decidas con toda la información. Si estás comparando, lee <a href=\"blog/precio-del-botox-en-pereira\">cómo comparar el precio del bótox en Pereira</a>."),
             ("¿Cuánto dura el efecto del bótox en la cara?", "Por lo general se repite cada 4 a 6 meses. Cuánto te dura a ti depende de tu musculatura, la zona tratada y tus hábitos."),
             ("¿Qué diferencia hay entre bótox y toxina botulínica?", "Botox es una marca de toxina botulínica tipo A. Hay otras marcas con registro sanitario; lo importante es que el producto sea legal y lo aplique un médico.")]),

    "acido-hialuronico": dict(
        titulo="Ácido hialurónico en Pereira: labios, ojeras y pómulos",
        desc="Ácido hialurónico en Pereira para labios, ojeras, pómulos, mentón y mandíbula. Resultados que duran de 9 a 18 meses según la zona y que se pueden revertir.",
        secciones=[
            ("¿Para qué zonas sirve el ácido hialurónico?",
             "<ul><li><strong><a href=\"relleno-de-labios\">Labios</a>.</strong> Definir el contorno, hidratar o dar un volumen sutil.</li>"
             "<li><strong><a href=\"tratamiento-de-ojeras\">Ojeras</a>.</strong> Suavizar la sombra cuando la ojera es un hundimiento.</li>"
             "<li><strong>Pómulos y sienes.</strong> Devolver soporte donde el rostro lo fue perdiendo.</li>"
             "<li><strong>Mentón y mandíbula.</strong> Perfilar y dar proporción al tercio inferior.</li></ul>"
             "<p>Cuando el objetivo es el rostro completo y no una zona suelta, lo planeamos como una <a href=\"armonizacion-facial\">armonización facial</a>.</p>"),
            ("¿Cuánto ácido hialurónico voy a necesitar?",
             "<p>Se habla mucho de “1 ml”, que es una jeringa pequeña. Cuánto hace falta depende de la zona, de cuánto soporte perdiste y del resultado que buscas. Por eso no cotizamos por mililitro a ciegas: primero miramos tu rostro en reposo y en movimiento, y luego te proponemos un plan.</p>"
             "<p>Nuestro criterio es sencillo: menos, mejor puesto. Preferimos quedarnos cortos y completar después que pasarnos.</p>"),
            ("Antes de un evento",
             "<p>Puede haber inflamación leve o algún morado durante 24 a 72 horas. Si tienes un grado, un matrimonio o una foto importante, agenda con un margen de por lo menos dos semanas.</p>"
             "<p>Y si alguna vez hiciera falta, el ácido hialurónico se puede disolver con una enzima llamada hialuronidasa. Es una de las razones por las que lo preferimos para empezar.</p>"),
        ],
        faq=[("¿Cuánto dura el ácido hialurónico?", "Entre 9 y 18 meses, según la zona, el producto y cómo lo procesa tu cuerpo. En las zonas con mucho movimiento, como los labios, suele durar menos."),
             ("¿Cuánto cobran por inyectar ácido hialurónico en Pereira?", "Depende de las zonas y de la cantidad de producto que necesites. Te damos el valor exacto en la valoración, después de ver tu rostro y antes de empezar.")]),

    "bioestimuladores": dict(
        titulo="Bioestimuladores de colágeno en Pereira · The Skin Haus",
        desc="Bioestimuladores de colágeno en Pereira (ácido poliláctico e hidroxiapatita de calcio) para flacidez y firmeza. Un cambio progresivo que dura de 12 a 24 meses.",
        secciones=[
            ("Sculptra, Radiesse y otros nombres que has oído",
             "<p>Quizás los conoces por sus marcas. Sculptra es ácido poliláctico y Radiesse es hidroxiapatita de calcio: dos sustancias distintas que tienen algo en común, hacen que tu propia piel fabrique colágeno nuevo.</p>"
             "<p>No hay uno mejor que otro en general. Cuál conviene depende de tu piel, de la zona y de si buscas sobre todo firmeza o también un poco de soporte. En la valoración te decimos cuál usaríamos en tu caso y por qué.</p>"),
            ("¿Para quién es y para quién no?",
             "<p>Es una buena opción si notas flacidez leve o moderada, la piel más delgada o un rostro que se sostiene menos que antes. También en cuello o en zonas del cuerpo.</p>"
             "<p>Si la flacidez es marcada, ningún inyectable reemplaza una cirugía, y te lo vamos a decir con claridad.</p>"),
            ("¿Cuándo se ven los resultados?",
             "<p>El colágeno tarda en formarse. Los cambios se empiezan a notar hacia la semana 6 a 8 y siguen mejorando durante meses. Por eso se planean de 1 a 3 sesiones, separadas de 4 a 8 semanas.</p>"
             "<p>Es un tratamiento para quien prefiere verse mejor poco a poco, sin un “cambio” de un día para otro.</p>"),
        ],
        faq=[("¿Qué es mejor, Sculptra o Radiesse?", "Ninguno es mejor en general. Son sustancias distintas que estimulan colágeno; cuál conviene depende de tu piel, la zona y el objetivo. Lo definimos en la valoración."),
             ("¿Cuánto duran los bioestimuladores en la cara?", "Entre 12 y 24 meses, según el producto, tu piel y tus hábitos.")]),

    "skinboosters": dict(
        titulo="Skinbooster en Pereira: piel hidratada y luminosa",
        desc="Skinboosters en Pereira: microinyecciones de ácido hialurónico ligero para piel opaca o deshidratada. 3 sesiones cada 3 a 4 semanas, sin cambiar volúmenes.",
        secciones=[
            ("¿Skinbooster o Profhilo?",
             "<p>Profhilo es una de las marcas más conocidas de este tipo de tratamiento. Otros skinboosters combinan ácido hialurónico con vitaminas y aminoácidos. Todos buscan lo mismo: mejorar la calidad de la piel, no cambiar la forma de tu cara.</p>"
             "<p>En la valoración miramos tu piel y te decimos qué producto conviene y cuántas sesiones necesitas.</p>"),
            ("Si es para un evento, empieza con tiempo",
             "<p>La serie inicial son 3 sesiones con 3 a 4 semanas entre una y otra: unos dos meses en total. Si es para un grado, un matrimonio o diciembre, lo ideal es empezar con ese margen.</p>"
             "<p>Después, un mantenimiento cada seis meses ayuda a sostener el resultado.</p>"),
        ],
        faq=[("¿Cuánto tiempo dura el efecto del skinbooster?", "Con la serie inicial de 3 sesiones y un mantenimiento cada seis meses, la mejoría se sostiene. Sin mantenimiento, la piel vuelve poco a poco a su estado anterior."),
             ("¿Cuántas sesiones de skinbooster necesito?", "Normalmente 3, cada 3 a 4 semanas, y luego mantenimiento semestral. Lo ajustamos según tu piel.")]),

    "peelings-medicos": dict(
        titulo="Peeling químico en Pereira: manchas, poros y acné",
        desc="Peelings médicos en Pereira elegidos para tu tipo de piel: manchas, textura, poros y marcas de acné. Desde peelings suaves sin descamación hasta más profundos.",
        secciones=[
            ("Los tipos de peeling",
             "<p>Los peelings se suelen dividir en superficiales, medios y profundos, según hasta qué capa de la piel actúan. A más profundidad, más descamación y más días de cuidado.</p>"
             "<p>Elegimos el ácido y la intensidad según tu piel, tu tono y tu agenda. Si tienes una semana ocupada, hay opciones que casi no se notan.</p>"),
            ("Peeling y sol: la regla que no se negocia",
             "<p>Durante la serie la piel queda más sensible al sol. El protector solar todos los días, también cuando está nublado, es parte del tratamiento. En temporadas de mucho sol preferimos opciones más suaves.</p>"),
        ],
        faq=[("¿Cuántas sesiones de peeling necesito?", "Lo habitual es una serie de 3 a 6 sesiones, cada 2 a 4 semanas. Depende de lo que queremos mejorar."),
             ("¿Cuáles son los tipos de peeling?", "Superficiales, medios y profundos, según hasta qué capa de la piel actúan. En la valoración elegimos el que conviene a tu piel.")]),

    "microagujas": dict(
        titulo="Microagujas (dermapen) en Pereira · The Skin Haus",
        desc="Microagujas o dermapen en Pereira para cicatrices de acné, poros y textura. De 3 a 5 sesiones cada 4 semanas, con anestesia tópica y rubor de 24 a 48 horas.",
        h1="Microagujas <em>(dermapen)</em>",
        secciones=[
            ("Microagujas, dermapen o microneedling",
             "<p>Son nombres para lo mismo. Dermapen es una marca de dispositivo muy conocida, y “microneedling” es el término en inglés. La idea es crear microcanales controlados para que la piel active su propia reparación.</p>"),
            ("Qué esperar, sesión a sesión",
             "<p>La mejoría es gradual: la piel se ve más uniforme después de cada sesión y el cambio se acumula. Para <a href=\"cicatrices-de-acne\">cicatrices de acné</a> profundas lo combinamos con otros tratamientos, y te decimos desde el inicio hasta dónde se puede llegar.</p>"
             "<p>Si tienes acné activo, primero tratamos eso. Hacer microagujas sobre un brote no es buena idea.</p>"),
        ],
        faq=[("¿Qué tan efectivo es el dermapen en la cara?", "Mejora textura, poros y cicatrices de forma progresiva, a lo largo de varias sesiones. No borra las cicatrices: las suaviza."),
             ("¿Qué riesgos tiene el dermapen?", "Enrojecimiento y sensibilidad por 24 a 48 horas. Con mala técnica o poca higiene puede haber infección o manchas; por eso se hace en consultorio, con material estéril y sin acné activo.")]),

    "manchas-y-melasma": dict(
        titulo="Tratamiento de manchas y melasma en Pereira · The Skin Haus",
        desc="Tratamiento de manchas en la cara y melasma en Pereira con un plan por etapas: diagnóstico, cuidado en casa, peelings y tecnologías según tu tipo de mancha.",
        secciones=[
            ("No todas las manchas son iguales",
             "<ul><li><strong>Melasma.</strong> Manchas en frente, mejillas o bigote, muy ligadas a las hormonas y al sol.</li>"
             "<li><strong>Manchas por sol o por la edad.</strong> Aparecen en las zonas más expuestas con los años.</li>"
             "<li><strong>Marcas que deja el acné.</strong> Manchas oscuras o rojizas donde hubo un brote.</li></ul>"
             "<p>Cada una se trata distinto. Usar el método equivocado puede oscurecer una mancha, por eso el diagnóstico va primero.</p>"),
            ("¿Qué es lo más efectivo para el melasma?",
             "<p>La constancia. Protector solar todos los días, una rutina en casa bien elegida y tratamientos en consultorio por etapas, como <a href=\"peelings-medicos\">peelings médicos</a>. El melasma se controla y mejora mucho, pero no se cura: necesita mantenimiento. Desconfía de las promesas de quitarlo para siempre.</p>"),
            ("¿Qué médico trata las manchas de la cara?",
             "<p>Las manchas se tratan en medicina estética y en dermatología. Si en la valoración vemos una lesión que debe revisar un dermatólogo, por ejemplo un lunar que cambió de forma o de color, te lo decimos y te orientamos.</p>"),
        ],
        faq=[("¿Qué especialista quita las manchas de la cara?", "Un médico con formación en piel: medicina estética o dermatología. Lo importante es que primero diagnostique qué tipo de mancha tienes."),
             ("¿Por qué me salen manchas en la cara?", "Por el sol, por cambios hormonales, por inflamación (como el acné) o por la edad. Muchas veces se suman varias causas.")]),

    "limpieza-facial-medica": dict(
        titulo="Limpieza facial profunda en Pereira · The Skin Haus",
        desc="Limpieza facial médica en Pereira: extracción cuidadosa, exfoliación, activos según tu piel e hidratación, en 60 minutos. Ideal cada 4 a 6 semanas.",
        secciones=[
            ("¿Qué incluye la limpieza facial?",
             "<ol><li>Revisión de tu piel para elegir los productos.</li><li>Limpieza y exfoliación.</li>"
             "<li>Extracción cuidadosa de puntos negros y poros obstruidos.</li><li>Activos según lo que tu piel necesita.</li>"
             "<li>Hidratación para cerrar.</li></ol><p>Son unos 60 minutos y vuelves a tu día de inmediato.</p>"),
            ("Limpieza médica o limpieza de spa",
             "<p>Las dos pueden sentirse bien. La diferencia es el criterio: la nuestra la hace personal entrenado bajo supervisión médica, se ajusta a tu diagnóstico y, si hay acné activo, te orientamos también con el manejo médico.</p>"
             "<p>Además es un buen punto de partida para preparar la piel antes de otros tratamientos.</p>"),
        ],
        faq=[("¿Cada cuánto debo hacerme una limpieza facial?", "Cada 4 a 6 semanas como mantenimiento. Si tu piel es grasa o tiene tendencia al acné, puede ser con más frecuencia; te lo decimos según tu piel."),
             ("¿Cuánto vale una limpieza facial en Pereira?", "Te damos el valor al agendar. Incluye la revisión de tu piel y los activos que elegimos para ti.")]),
}

# Páginas nuevas por búsqueda (19-oct-2026): mismos campos que ESTETICA + "padre" (página de la que dependen).
# Solo tratamientos que la web ya ofrecía dentro de ESTETICA.
BUSQUEDAS = [
    dict(slug="relleno-de-labios", nombre="Relleno de labios", foto="retrato", padre="acido-hialuronico",
         linea="Labios definidos e hidratados, que siguen pareciendo tuyos.",
         intro="Con ácido hialurónico podemos definir el contorno, dar un poco de volumen o simplemente hidratar en profundidad. Trabajamos en poca cantidad y respetando la proporción de tu boca con el resto de tu cara.",
         para=["Labios finos o que perdieron volumen con los años", "Contorno poco definido o asimetrías leves", "Labios resecos que quieres hidratar sin agrandar"],
         como=("30–45 minutos", "Una sesión", "Inflamación leve 24–72 horas"),
         faq=[("¿Cuánto cobran por un relleno de labios en Pereira?", "Depende de la cantidad de producto y de lo que buscamos: hidratar, definir o dar volumen. Te damos el valor exacto en la valoración, antes de empezar."),
              ("¿Cuánto dura el relleno de labios?", "Varios meses. En los labios suele durar menos que en otras zonas porque es una zona con mucho movimiento. Te damos una referencia según el producto y tu caso."),
              ("¿Se puede revertir?", "Sí. El ácido hialurónico se puede disolver con una enzima (hialuronidasa) si alguna vez fuera necesario."),
              ("¿Se va a notar que me hice algo?", "La idea es que se note que te ves bien, no qué te hiciste. Empezamos con poca cantidad y, si hace falta, completamos después.")],
         titulo="Relleno de labios en Pereira con ácido hialurónico",
         desc="Relleno de labios en Pereira con ácido hialurónico: definición, hidratación o volumen sutil en 30–45 minutos, en proporción con tu rostro. Y es reversible.",
         secciones=[
             ("Relleno de labios natural en Pereira",
              "<p>Si lo que te frena es el miedo a que se note, empecemos por ahí. Un relleno de labios no tiene que ser “más boca”. Puede ser solo perfilar el borde, corregir una asimetría leve o devolver hidratación a unos labios que se ven secos.</p>"
              "<p>Antes de poner producto miramos tu cara completa: la nariz, el mentón, cómo sonríes. La boca tiene que verse en armonía con todo lo demás.</p>"),
             ("Definir, hidratar o dar volumen",
              "<ul><li><strong>Definir.</strong> Marcar el contorno para que el labio se vea más nítido.</li>"
              "<li><strong>Hidratar.</strong> Mejorar la textura y las líneas finas sin cambiar el tamaño.</li>"
              "<li><strong>Volumen sutil.</strong> Un poco más de cuerpo, en poca cantidad.</li></ul>"
              "<p>Muchas veces es una mezcla de las tres. Lo definimos juntos en la valoración.</p>"),
             ("Antes de un evento",
              "<p>Los labios se pueden inflamar durante 24 a 72 horas y a veces aparece un pequeño morado. Si tienes una fecha importante, agenda con por lo menos dos semanas de margen. Y si es tu primera vez, mejor todavía con más tiempo.</p>"),
         ]),

    dict(slug="tratamiento-de-ojeras", nombre="Tratamiento de ojeras", foto="facial", padre="acido-hialuronico",
         linea="Una mirada descansada, sin cambiar tu expresión.",
         intro="No todas las ojeras son iguales. Cuando la ojera es un hundimiento debajo del ojo, el ácido hialurónico puede suavizar esa sombra. Cuando es pigmento o una bolsa, la solución es otra, y te lo decimos.",
         para=["Ojera hundida que da aspecto de cansancio", "Sombra marcada entre el párpado y la mejilla", "Quienes quieren verse descansados sin cirugía"],
         como=("30–45 minutos", "Una sesión", "Inflamación leve 24–72 horas"),
         faq=[("¿El ácido hialurónico quita las ojeras oscuras?", "Si lo oscuro es pigmento, no. El ácido hialurónico mejora la sombra que produce un hundimiento. Para el pigmento hay otros tratamientos, como peelings o manejo de manchas."),
              ("¿Cuánto dura el tratamiento de ojeras?", "El ácido hialurónico dura de 9 a 18 meses según la zona y la persona. Te damos una referencia para tu caso en la valoración."),
              ("¿Es seguro rellenar las ojeras?", "Es una zona delicada que pide experiencia, poca cantidad y buena técnica. Todo procedimiento tiene riesgos; por eso lo hace un médico después de valorarte.")],
         titulo="Tratamiento de ojeras en Pereira · The Skin Haus",
         desc="Tratamiento de ojeras en Pereira: si tu ojera es hundida, el ácido hialurónico suaviza la sombra en 30–45 minutos. Si es pigmento o bolsa, te decimos qué sirve.",
         secciones=[
             ("¿Qué tipo de ojera tienes?",
              "<ul><li><strong>Hundida.</strong> Un surco entre el párpado y la mejilla que hace sombra. Es la que mejor responde al ácido hialurónico.</li>"
              "<li><strong>Pigmentada.</strong> La piel es más oscura en esa zona. Se trabaja como una mancha, con <a href=\"manchas-y-melasma\">manejo de manchas</a>.</li>"
              "<li><strong>Bolsa.</strong> Un abultamiento debajo del ojo. Rellenar puede empeorarla; a veces la respuesta es una cirugía de párpados y te orientamos.</li></ul>"
              "<p>Muchas personas tienen una mezcla. Por eso la valoración pesa tanto aquí.</p>"),
             ("Por qué preferimos poca cantidad",
              "<p>La piel debajo del ojo es fina y cualquier exceso se nota. Trabajamos con poco producto, en el plano correcto, y preferimos completar después que pasarnos. El objetivo es que te veas descansada o descansado, no distinta o distinto.</p>"),
         ]),

    dict(slug="armonizacion-facial", nombre="Armonización facial", foto="retrato", padre="acido-hialuronico",
         linea="Proporción, no volumen. Que tu rostro se vea en equilibrio.",
         intro="Armonizar es mirar el rostro completo antes de tocar una sola zona. A veces es un poco de soporte en el pómulo, otras definir el mentón o relajar una línea de expresión. El plan se arma por etapas y con poca cantidad.",
         para=["Quienes sienten su rostro cansado o desproporcionado", "Perfil con mentón o mandíbula poco definidos", "Quienes quieren un plan completo, no un tratamiento suelto"],
         como=("Plan por etapas", "Sesiones según el plan", "Según los tratamientos elegidos"),
         faq=[("¿Cuánto cuesta una armonización facial en Pereira?", "Depende del plan: qué zonas, qué tratamientos y cuánto producto. Te damos el valor en la valoración, por etapas, para que decidas con calma."),
              ("¿Se hace todo en una sola cita?", "No necesariamente. Muchas veces conviene hacerlo por etapas: así el cambio es gradual y podemos ajustar en el control."),
              ("¿Se ve natural?", "Ese es el objetivo. No buscamos cambiar quién eres, sino que tu rostro se vea en proporción y descansado.")],
         titulo="Armonización facial en Pereira · The Skin Haus",
         desc="Armonización facial en Pereira: un plan por etapas con ácido hialurónico, bótox o bioestimuladores, pensado para tu proporción y no para cambiar quién eres.",
         secciones=[
             ("Qué puede incluir una armonización facial",
              "<ul><li><strong><a href=\"acido-hialuronico\">Ácido hialurónico</a></strong> para pómulos, mentón, mandíbula o <a href=\"relleno-de-labios\">labios</a>.</li>"
              "<li><strong><a href=\"toxina-botulinica\">Bótox</a></strong> para relajar líneas de expresión.</li>"
              "<li><strong><a href=\"bioestimuladores\">Bioestimuladores</a></strong> para firmeza y calidad de piel.</li>"
              "<li><strong><a href=\"skinboosters\">Skinboosters</a></strong> para hidratación y luz.</li></ul>"
              "<p>No siempre hacen falta todos. Muchas veces dos cosas bien elegidas hacen más que cinco.</p>"),
             ("Lo que no hacemos",
              "<p>No copiamos rostros de redes sociales ni ponemos producto para “llenar”. Evitamos los excesos y los resultados genéricos. Si algo no te va a favorecer, te lo decimos aunque lo traigas en la lista.</p>"),
             ("Cómo empieza una armonización facial en Pereira",
              "<p>Con una valoración presencial: miramos tu rostro de frente, de perfil y en movimiento, conversamos sobre lo que quieres cuidar y lo que no quieres cambiar, y te proponemos un plan por etapas con tiempos y costos claros.</p>"),
         ]),

    dict(slug="hiperhidrosis", nombre="Hiperhidrosis", foto="manos", padre="toxina-botulinica",
         linea="Bótox para el sudor excesivo de axilas y manos.",
         intro="Cuando el sudor de axilas o manos no depende del calor ni del ejercicio y te cambia la forma de vestirte o de saludar, la toxina botulínica puede reducirlo de forma temporal, actuando sobre la señal que activa las glándulas del sudor.",
         para=["Sudor excesivo en axilas que mancha la ropa", "Manos que sudan aunque no haga calor", "Quienes ya probaron antitranspirantes sin resultado"],
         como=("Una cita corta", "Una sesión; el efecto dura meses", "Vuelves a tu día de inmediato"),
         faq=[("¿El bótox para el sudor duele?", "Son punciones muy finas y superficiales. En las manos la zona es más sensible; te explicamos antes cómo manejamos la molestia."),
              ("¿Cuánto dura el efecto del bótox en las axilas?", "Varios meses. Cuando el sudor vuelve a aumentar, se repite. Te damos una referencia según la zona en la valoración."),
              ("¿Dejo de sudar en todo el cuerpo?", "No. Solo disminuye el sudor en la zona tratada; el resto del cuerpo sigue regulando la temperatura normalmente.")],
         titulo="Bótox para hiperhidrosis en Pereira · The Skin Haus",
         desc="Bótox para la hiperhidrosis en Pereira: la toxina botulínica reduce el sudor excesivo de axilas y manos de forma temporal, en una cita corta y sin incapacidad.",
         secciones=[
             ("Cómo funciona",
              "<p>La <a href=\"toxina-botulinica\">toxina botulínica</a> se aplica con agujas muy finas en la piel de la zona que suda. Actúa sobre la señal nerviosa que activa las glándulas del sudor, y la sudoración en esa zona baja durante meses.</p>"
              "<p>No es permanente: cuando el efecto pasa, se repite.</p>"),
             ("Cuándo conviene revisar otra causa primero",
              "<p>Si el sudor empezó de repente, es en todo el cuerpo, aparece de noche o viene con otros síntomas como fiebre o pérdida de peso, puede tener otra causa y hay que revisarla antes. En la valoración te lo preguntamos y, si hace falta, te orientamos con el especialista adecuado.</p>"),
         ]),

    dict(slug="cicatrices-de-acne", nombre="Cicatrices de acné", foto="piel", padre="microagujas",
         linea="Mejorar la textura que dejó el acné, paso a paso.",
         intro="Las marcas del acné no son todas iguales: hay hundimientos, textura irregular y manchas oscuras o rojizas. Por eso las tratamos combinando microagujas, peelings y manejo de manchas, en un plan por etapas y con metas realistas.",
         para=["Cicatrices hundidas o textura irregular", "Marcas oscuras o rojizas que dejó el acné", "Poros dilatados después de años de acné"],
         como=("45–60 minutos por sesión", "3 a 5 sesiones, cada 4 semanas", "Rubor tipo sol 24–48 horas"),
         faq=[("¿Se pueden quitar del todo las cicatrices de acné?", "Casi nunca del todo. Lo que sí se logra es suavizarlas de forma visible y mejorar la textura. Te decimos desde el inicio qué esperar en tu caso."),
              ("¿Cuántas sesiones necesito?", "Con microagujas, normalmente de 3 a 5 sesiones cada 4 semanas, a veces combinadas con peelings. Depende del tipo y la profundidad de las cicatrices."),
              ("¿Sirve si tengo la piel morena?", "Sí, eligiendo bien la técnica y preparando la piel. Por eso valoramos antes de empezar.")],
         titulo="Tratamiento de cicatrices de acné en Pereira · The Skin Haus",
         desc="Tratamiento de cicatrices de acné en Pereira con microagujas, peelings y manejo de manchas: un plan por etapas de 3 a 5 sesiones, con metas realistas.",
         secciones=[
             ("¿Cicatriz o mancha?",
              "<p>Una cicatriz cambia la textura: se siente o se ve como un hundimiento. Una mancha cambia el color: la piel está lisa, pero más oscura o rojiza. Las cicatrices se trabajan con <a href=\"microagujas\">microagujas</a>; las manchas, con <a href=\"peelings-medicos\">peelings</a> y <a href=\"manchas-y-melasma\">manejo de manchas</a>. Casi siempre hay de las dos.</p>"),
             ("Primero, el acné activo",
              "<p>Si todavía tienes brotes, empezamos por controlarlos. Tratar cicatrices sobre un acné activo no funciona bien y puede irritar la piel.</p>"),
             ("Qué se puede esperar",
              "<p>La mejoría es progresiva y se acumula sesión a sesión. No borramos cicatrices: las suavizamos para que la piel se vea más uniforme. Con esa meta clara, el tratamiento se disfruta más y se abandona menos.</p>"),
         ]),
]

CLAVE.update({
    "relleno-de-labios": ("Definición e hidratación", "30–45 min", "Reversible"),
    "tratamiento-de-ojeras": ("Mirada descansada", "30–45 min", "Según tu ojera"),
    "armonizacion-facial": ("Proporción y equilibrio", "Plan por etapas", "Resultado natural"),
    "hiperhidrosis": ("Sudor excesivo", "Cita corta", "Sin incapacidad"),
    "cicatrices-de-acne": ("Textura y marcas", "3–5 sesiones", "Plan por etapas"),
})

# preguntas de la página /medicina-estetica
PREGUNTAS_ESTETICA = [
    ("¿Qué es la medicina estética?", "Es la rama de la medicina que trata la calidad de la piel, las arrugas, la pérdida de volumen y las manchas con procedimientos mínimamente invasivos, como la toxina botulínica, el ácido hialurónico o los peelings, siempre después de una valoración médica."),
    ("¿Quién me atiende en The Skin Haus?", "Siempre un médico. Los procedimientos los realiza o supervisa directamente el equipo médico de la clínica, en la Torre Médica Oval de Pereira."),
    ("¿Atienden pacientes de Dosquebradas y Santa Rosa de Cabal?", "Sí. Estamos en la Torre Médica Oval, en Pereira, y atendemos a pacientes de toda el área: Dosquebradas, Santa Rosa de Cabal, La Virginia y Cartago."),
    ("¿Puedo hacerme el tratamiento el mismo día de la valoración?", "En muchos casos sí, si el médico lo considera adecuado y tú te sientes lista o listo para decidir."),
]

# Médico vascular (confirmado por Laura 19-oct-2026: es el mismo de Seravena, Medellín). Perfil completo en Seravena.
MEDICO_VASCULAR = dict(
    nombre="Dr. José David Puerta Rojas",
    titulo="Médico internista · Subespecialista en medicina vascular",
    perfil="https://www.clinicaseravena.com/dr-jose-david-puerta-rojas",
    doctoralia="https://www.doctoralia.co/perfil/jose-david-puerta-rojas",
)

# ---------------------------------------------------------------- ampliación de páginas cortas (19-oct-2026)
SEO["skinboosters"]["secciones"] += [
    ("Qué se siente y qué cuidar después",
     "<p>Son microinyecciones superficiales repartidas en la zona. Se sienten como pinchazos pequeños y rápidos. Después pueden quedar unas pápulas, como granitos de agua, que desaparecen en 24 a 48 horas.</p>"
     "<p>Ese día evita el maquillaje por 12 horas y el sol directo por unos días. Te damos las indicaciones por escrito para que no tengas que acordarte de memoria.</p>"),
    ("Para quién no es",
     "<p>Si lo que buscas es levantar o rellenar, el skinbooster se queda corto: no aporta volumen. Para eso existen el <a href=\"acido-hialuronico\">ácido hialurónico</a> o los <a href=\"bioestimuladores\">bioestimuladores</a>, y muchas veces se combinan. En la valoración te decimos qué tiene sentido para tu piel.</p>"),
]
SEO["skinboosters"]["faq"] += [
    ("¿Duele el skinbooster?", "Son pinchazos pequeños y rápidos. La mayoría lo tolera bien; si tu piel es sensible, te explicamos antes cómo manejamos la molestia."),
]

SEO["peelings-medicos"]["secciones"] += [
    ("Antes y después de tu peeling",
     "<p>Antes, a veces preparamos la piel unas semanas con productos en casa, sobre todo si hay manchas o si tu piel es morena. Después, la regla es simple: hidratar, no arrancar la piel que se descama y usar protector solar todos los días.</p>"
     "<p>Según la profundidad, puedes no notar descamación o tener alrededor de una semana de piel pelándose. Te decimos qué esperar antes de empezar, para que lo planees con tu agenda.</p>"),
    ("¿Peeling o microagujas?",
     "<p>El peeling trabaja mejor el color y la superficie: manchas, tono apagado, poros. Las <a href=\"microagujas\">microagujas</a> trabajan mejor la textura: cicatrices y firmeza. Para <a href=\"cicatrices-de-acne\">cicatrices de acné</a> muchas veces se combinan en un mismo plan.</p>"),
]
SEO["peelings-medicos"]["faq"] += [
    ("¿Puedo hacerme un peeling si tengo melasma?", "Sí, con el ácido y la intensidad correctos y con protección solar estricta. El melasma se trata con cuidado porque un método equivocado puede oscurecerlo; por eso valoramos primero."),
]

SEO["limpieza-facial-medica"]["secciones"] += [
    ("Si tienes acné",
     "<p>Una limpieza ayuda a destapar los poros, pero no reemplaza el manejo médico del acné. Si hay brotes activos, adaptamos la extracción para no irritar la piel y te orientamos con el tratamiento que necesitas.</p>"),
    ("Una buena forma de empezar",
     "<p>Si nunca te has hecho un tratamiento en la cara, la limpieza médica es un primer paso tranquilo: conoces la clínica, revisamos tu piel y sales con una idea clara de lo que le conviene, sin compromiso de hacerte nada más.</p>"),
]

SEO["microagujas"]["secciones"] += [
    ("Cuidados después de la sesión",
     "<p>La piel queda roja, como después de un día de sol, por 24 a 48 horas. Puedes maquillarte después de 24 horas con productos limpios. Evita el sol, el ejercicio intenso y las piscinas los primeros días, y usa protector solar todos los días.</p>"),
]
SEO["microagujas"]["faq"] += [
    ("¿Cuántas sesiones de dermapen necesito?", "Normalmente de 3 a 5 sesiones, separadas 4 semanas. Depende de lo que queremos mejorar: no es lo mismo afinar poros que suavizar cicatrices profundas."),
]

# página de valoración
VALORACION_PASOS = [
    ("Conversamos", "Qué te gustaría mejorar, qué no quieres cambiar y qué te has hecho antes."),
    ("Te examinamos", "Miramos tu piel y tu rostro en reposo y en movimiento, o tus piernas si es vascular."),
    ("Te explicamos", "Las opciones que tienen sentido para ti, con tiempos, cuidados y costos claros."),
    ("Decides con calma", "Sin presión. En muchos casos puedes hacerte el tratamiento ese mismo día, si el médico lo considera adecuado."),
]
VALORACION_TRAER = [
    "Los medicamentos que tomas y si tienes alguna enfermedad o alergia",
    "Qué tratamientos te has hecho antes y cuándo",
    "Si estás embarazada o lactando, cuéntanoslo",
    "Tus preguntas anotadas en el celular",
]
VALORACION_FAQ = PREGUNTAS_GENERALES + [
    ("¿La valoración es presencial?", "Sí. Por WhatsApp te ayudamos a agendar y resolvemos dudas generales, pero el diagnóstico y el plan se hacen en persona, en la Torre Médica Oval de Pereira."),
    ("¿Cuánto dura la valoración?", "Lo suficiente para escucharte y examinarte sin afán. Si decides hacerte el tratamiento el mismo día, la cita se alarga lo que dure ese tratamiento."),
]

# Médica estética (confirmado por Laura 19-oct-2026). Mismo nombre y cargo que en noon.clinic/especialistas; no inventar títulos.
MEDICA_ESTETICA = dict(
    nombre="Dra. Valeria Enciso",
    titulo="Médica estética",
    foto="assets/equipo/valeria-enciso",   # + .webp / .jpg
    slug="dra-valeria-enciso",             # su página propia (27-oct-2026)
)

# Enlace "Escribir una reseña" de la ficha de Google Maps de The Skin Haus. PENDIENTE: la ficha aún no existe.
# Cuando exista, pegar aquí el enlace que da Google (g.page/r/…/review) y /resena redirige solo; el QR impreso no cambia.
RESENA_URL = ""

