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
