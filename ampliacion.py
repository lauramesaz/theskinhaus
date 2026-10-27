# -*- coding: utf-8 -*-
# The Skin Haus · ampliación de páginas (27-oct-2026). Se carga desde build.py después de datos.py.
# Modifica en el sitio las listas y diccionarios de datos.py (SEO, BUSQUEDAS) y define los textos
# largos de /nosotros y /valoracion. Reglas de contenido: _agencia/INSTRUCCIONES.md §2 (nada inventado,
# nunca precios, nada de antes/después, valoración presencial).
# Fuentes de cada dato: datos.py (tiempos, sesiones, cuidados) y _agencia/hechos.md (RETHUS, INVIMA,
# FDA, CDC, Ley 23 de 1981, tipos de cicatriz). Si algo no está ahí, no va aquí.
# Revisado por el Policía humanizador y el Verificador médico-legal el 27-oct-2026.
from datos import SEO, BUSQUEDAS

POR_SLUG = {b["slug"]: b for b in BUSQUEDAS}

# Consultas públicas oficiales (URL confirmadas en hechos.md §C1 y §C2, 19-oct-2026).
RETHUS = "https://web.sispro.gov.co/THS/Cliente/ConsultasPublicas/ConsultaPublicaDeTHxIdentificacion.aspx"
INVIMA = "https://www.invima.gov.co/consulta-registros-sanitarios"
FUERA = ' target="_blank" rel="noopener"'


# ================================================================== hiperhidrosis
POR_SLUG["hiperhidrosis"]["secciones"] += [
    ("Cómo es la cita para el sudor en Pereira",
     '<p>Empieza con preguntas: las de la lista de abajo, “Qué anotar antes de venir”. Con eso sabemos si hay que revisar otra causa primero.</p>'
     '<p>Si la toxina tiene sentido para ti, se aplica con agujas muy finas y superficiales en la piel de la zona que suda. Es una cita corta: cabe a la salida del trabajo.</p>'
     '<p>No esperes el cambio esa misma tarde. La toxina necesita unos días para actuar.</p>'),
    ("Axilas o manos: lo que cambia",
     '<p>En las axilas, lo que suele pesar es la ropa: la camisa marcada a media mañana, elegir colores oscuros, llevar una muda en el bolso. En las manos es otra cosa. Es el saludo, la hoja que se humedece, el celular que se resbala.</p>'
     '<p>El tratamiento es el mismo. Lo que cambia es la molestia, que en las manos se siente más, y cuánto te dura el efecto, que puede variar de una zona a otra.</p>'),
    ("Qué anotar antes de venir",
     '<ul><li>Cuándo empezó el sudor y si fue de un momento a otro.</li>'
     '<li>Si es en una zona o en todo el cuerpo, y si aparece de noche.</li>'
     '<li>Si has tenido fiebre, pérdida de peso u otro síntoma nuevo.</li>'
     '<li>Los medicamentos que tomas y los antitranspirantes que ya probaste.</li></ul>'
     '<p>Si lo quieres para una fecha, como un matrimonio o una presentación, no lo dejes para la víspera.</p>'),
]
POR_SLUG["hiperhidrosis"]["faq"] += [
    ("¿Dónde tratan la hiperhidrosis en Pereira?", "En The Skin Haus, en la Torre Médica Oval de Pereira. La valoración es presencial y atendemos a pacientes de toda el área: Dosquebradas, Santa Rosa de Cabal, La Virginia y Cartago."),
    ("¿El bótox sirve para cualquier tipo de sudor?", "No. Está pensado para el sudor excesivo de axilas o manos que no depende del calor ni del ejercicio. Si el sudor es en todo el cuerpo, empezó de repente o viene con otros síntomas, primero hay que revisar la causa."),
    ("¿Puedo ir a trabajar después del bótox en las axilas?", "Sí. Vuelves a tu día de inmediato. Las indicaciones para las primeras horas te las damos por escrito."),
]


# ================================================================== armonización facial
POR_SLUG["armonizacion-facial"]["secciones"] += [
    ("Cada tratamiento tiene su propio tiempo",
     '<p>Una armonización no se ve completa al salir de la cita. Cada parte del plan avanza a su ritmo, y conviene saberlo antes de empezar.</p>'
     '<ul><li><strong>Bótox.</strong> Empieza a notarse entre el día 3 y el 7 y se ve completo hacia las dos semanas, cuando hacemos control.</li>'
     '<li><strong>Ácido hialurónico.</strong> El soporte se ve desde el principio, pero puede haber inflamación leve de 24 a 72 horas.</li>'
     '<li><strong>Bioestimuladores.</strong> El colágeno tarda: los cambios se notan hacia la semana 6 a 8 y siguen mejorando por meses.</li>'
     '<li><strong>Skinboosters.</strong> La serie inicial suele ser de 3 sesiones, con 3 a 4 semanas entre una y otra.</li></ul>'
     '<p>Por eso vamos por etapas. Vemos cómo responde tu cara a un paso antes de dar el siguiente.</p>'),
    ("Tu primera armonización facial en Pereira: por dónde empezar",
     '<p>No hace falta llegar con la lista hecha. Basta con saber qué te molesta cuando te ves en una foto y qué te gusta tal como está.</p>'
     '<p>Con eso, y viéndote en persona, elegimos la primera etapa. Preferimos empezar por lo que más aporta a la proporción con menos producto.</p>'
     '<p>Lo demás, después del control.</p>'
     '<p>Si vienes desde Dosquebradas, Santa Rosa de Cabal, La Virginia o Cartago, pregunta en la valoración cuántas citas tiene tu plan. Así organizas los viajes desde el principio.</p>'),
    ("Cuándo no es lo que necesitas",
     '<p>Si lo que te molesta es una flacidez marcada, ningún inyectable reemplaza una cirugía. Con algunas bolsas debajo de los ojos pasa algo parecido: rellenarlas puede empeorarlas.</p>'
     '<p>Tampoco conviene empezar un plan completo con el evento encima. El bótox necesita unas dos semanas para verse completo, y después del ácido hialurónico se recomienda un margen de por lo menos dos semanas por la inflamación o algún morado. Para el grado o el matrimonio de diciembre, cuenta hacia atrás.</p>'
     '<p>En cualquiera de esos casos te lo decimos en la valoración y te orientamos.</p>'),
]
POR_SLUG["armonizacion-facial"]["faq"] += [
    ("¿Qué pasa si no me gusta el resultado?", "Lo hablamos en el control. El ácido hialurónico se puede disolver con una enzima, la hialuronidasa, si fuera necesario. Y el efecto del bótox es temporal. Los bioestimuladores, en cambio, actúan poco a poco y su efecto dura de 12 a 24 meses, según el producto y tu piel, así que se deciden con más calma. Por eso empezamos con poca cantidad: es más fácil completar que quitar."),
    ("¿Cuánto tiempo toma una armonización facial completa?", "Depende de cuántas etapas tenga tu plan y de qué tratamientos incluya. El bótox se ve completo hacia las dos semanas y los bioestimuladores empiezan a notarse hacia la semana 6 a 8. En la valoración te decimos los tiempos de tu plan."),
    ("¿Puedo empezar con un solo tratamiento?", "Sí, y muchas veces conviene: una etapa, un control y luego decidimos juntos si seguimos."),
]


# ================================================================== cicatrices de acné
POR_SLUG["cicatrices-de-acne"]["secciones"] += [
    ("Cómo es una sesión de microagujas en Pereira",
     '<p>Antes de empezar aplicamos anestesia tópica. Durante la sesión se siente una vibración y un leve raspado.</p>'
     '<p>Cada sesión dura de 45 a 60 minutos y se hace en consultorio, con material estéril. Al salir vas a tener la cara roja, como si hubieras pasado la mañana al sol. Eso dura de 24 a 48 horas.</p>'
     '<p>El maquillaje espera 24 horas, y después va con productos limpios. Los primeros días, nada de sol directo, ejercicio intenso ni piscina. Protector solar, todos los días.</p>'
     '<p>Si tienes una reunión o un evento, no pongas la sesión el día anterior.</p>'),
    ("No todas las cicatrices hundidas responden igual",
     '<p>Hay hundimientos estrechos y profundos, tipo “picahielo”, otros de borde marcado y otros más suaves, como ondulaciones. Una misma piel puede tener varios tipos.</p>'
     '<p>En estudios pequeños con microagujas, las cicatrices ondulantes y las de borde marcado mejoraron más que las estrechas y profundas, que suelen pedir más trabajo y combinarse con otros procedimientos. Y si tus marcas sobresalen de la piel en vez de hundirse, el plan cambia: las microagujas funcionan mejor en las hundidas.</p>'
     '<p>Por eso el número de sesiones se confirma después de examinarte.</p>'),
    ("Cuándo seguir y cuándo parar",
     '<p>Antes de la primera sesión, tómate una foto con luz de ventana y sin maquillaje. Te va a servir para comparar.</p>'
     '<p>El número de sesiones no es fijo. Si la mejoría llegó a un punto que te gusta, puedes parar. Si las cicatrices más profundas casi no cambian, toca hablar de otras opciones, no sumar sesiones iguales.</p>'),
]
POR_SLUG["cicatrices-de-acne"]["faq"] += [
    ("¿Cuándo me puedo maquillar después de las microagujas?", "Después de 24 horas, con productos limpios. La piel puede seguir un poco roja hasta las 48 horas."),
    ("¿Las microagujas sirven para cicatrices elevadas?", "Funcionan mejor en las cicatrices hundidas. Si tus marcas sobresalen de la piel, lo vemos en la valoración y te orientamos."),
    ("¿Qué pasa si me sale un brote durante el tratamiento?", "Avísanos antes de la sesión. Sobre acné activo no hacemos microagujas: primero lo controlamos y después seguimos con el plan."),
]


# ================================================================== tratamiento de ojeras
POR_SLUG["tratamiento-de-ojeras"]["secciones"] += [
    ("Qué pasa en la cita de ojeras en Pereira",
     '<p>Lo primero es saber qué ojera tienes, y eso solo se ve en persona. Miramos tu cara en reposo y en movimiento, y te preguntamos desde cuándo la notas y qué te has hecho antes.</p>'
     '<p>Si es un hundimiento y el ácido hialurónico tiene sentido, la aplicación toma de 30 a 45 minutos, en una sesión. Puede haber inflamación leve de 24 a 72 horas y, a veces, un pequeño morado.</p>'
     '<p>En muchos casos se hace el mismo día de la valoración, si el médico lo considera adecuado y tú te sientes lista o listo.</p>'),
    ("Qué se puede combinar",
     '<p>Si tu ojera es una mezcla, el plan también puede serlo.</p>'
     '<ul><li><strong>Hundimiento.</strong> <a href="acido-hialuronico">Ácido hialurónico</a>, en poca cantidad.</li>'
     '<li><strong>Pigmento.</strong> Va por otro camino: un plan por etapas que puede incluir <a href="peelings-medicos">peelings médicos</a>.</li>'
     '<li><strong>Patas de gallo.</strong> Las líneas del contorno del ojo que aparecen al gesticular se suavizan con <a href="toxina-botulinica">bótox</a>, no con relleno.</li></ul>'
     '<p>Si además sientes la cara cansada en general, quizá no es solo la ojera. Ahí tiene más sentido mirar el rostro completo, como en una <a href="armonizacion-facial">armonización facial</a>.</p>'),
]
POR_SLUG["tratamiento-de-ojeras"]["faq"] += [
    ("¿Puedo hacerme las ojeras una semana antes de un evento?", "Mejor con más margen. Puede haber inflamación leve o algún morado de 24 a 72 horas, y si hace falta completar, necesitas tiempo. Agenda por lo menos dos semanas antes."),
    ("¿Se puede revertir el relleno de ojeras?", "Sí. El ácido hialurónico se puede disolver con una enzima, la hialuronidasa, si fuera necesario. En una piel tan fina, ese margen da tranquilidad."),
    ("¿Sirve si mis ojeras son bolsas?", "Rellenar una bolsa puede empeorarla, así que ahí el ácido hialurónico no suele ser la respuesta. A veces lo que corresponde es una cirugía de párpados."),
]


# ================================================================== toxina botulínica (bótox)
SEO["toxina-botulinica"]["secciones"] += [
    ("Dónde hacerte el bótox en Pereira: lo que conviene revisar",
     '<p>Más que el sitio, mira quién te inyecta y con qué. Cuatro cosas lo dicen casi todo:</p>'
     '<ul><li><strong>Que lo aplique un médico.</strong> Pide su nombre completo y búscalo en el <a href="' + RETHUS + '"' + FUERA + '>RETHUS</a>, la consulta pública del Ministerio de Salud.</li>'
     '<li><strong>Que el producto tenga registro INVIMA.</strong> En 2025 el INVIMA alertó sobre un producto vendido como toxina botulínica sin registro sanitario y con etiquetas en otro idioma.</li>'
     '<li><strong>Que sea en un lugar de salud.</strong> Los CDC de Estados Unidos investigaron casos de efectos adversos ligados a toxina falsificada o a inyecciones aplicadas por personas sin licencia o en lugares que no son de salud, como casas o spas. Su recomendación: inyectarse solo con profesionales con licencia y entrenamiento, en lugares de salud habilitados.</li>'
     '<li><strong>Que haya control.</strong> Hacia las dos semanas el efecto se ve completo, y ese es el momento de revisar.</li></ul>'
     '<p>Puedes hacernos estas mismas preguntas en la Torre Médica Oval. El paso a paso para verificar está en <a href="blog/como-elegir-medico-estetico-en-pereira">cómo elegir médico estético en Pereira</a>.</p>'),
    ("Si es tu primera vez con bótox",
     '<p>Quizá te preocupa quedar con la cara “congelada”. Por eso en la primera aplicación preferimos quedarnos cortos y completar en el control, cuando ya vimos cómo responde tu musculatura.</p>'
     '<p>Tampoco hace falta tratar todo a la vez. Frente, entrecejo y patas de gallo son zonas distintas, y en la valoración decidimos contigo por cuál empezar.</p>'
     '<p>Y elige bien la fecha: para la foto del grado, agenda por lo menos dos semanas antes.</p>'),
]
SEO["toxina-botulinica"]["faq"] += [
    ("¿Dónde hacerme el bótox en Pereira?", "Donde lo aplique un médico, con un producto con registro INVIMA que puedas verificar, después de una valoración presencial y con control a las dos semanas. En The Skin Haus te atendemos en la Torre Médica Oval de Pereira, también si vienes de Dosquebradas, Santa Rosa de Cabal, La Virginia o Cartago."),
    ("¿A qué edad se puede empezar con bótox?", "No hay una edad fija. El bótox sirve para suavizar líneas de expresión que ya se marcan y también para prevenir que se marquen más. Cuándo tiene sentido empezar en tu caso lo definimos en la valoración, viendo cómo se mueve tu cara."),
    ("¿Hay retoque después del bótox?", "Si hace falta, sí. Hacia las dos semanas te vemos en control, cuando el efecto ya se ve completo, y ahí completamos lo que se haya quedado corto. Ese control es el que nos deja ser prudentes la primera vez."),
    ("¿Qué pasa si dejo de aplicarme bótox?", "El efecto es temporal. Si no lo repites, se va pasando con los meses y el músculo vuelve a moverse como antes, así que las líneas se marcan otra vez al gesticular. Por lo general se repite cada 4 a 6 meses, y en cada ciclo decides si sigues."),
]


# ================================================================== relleno de labios
POR_SLUG["relleno-de-labios"]["secciones"] += [
    ("Tu primer relleno de labios, paso a paso",
     '<p>Primero miramos tu boca en reposo, al hablar y al sonreír, porque el labio cambia mucho con el movimiento. Luego decidimos contigo si buscamos definir, hidratar o dar un poco de volumen.</p>'
     '<p>La aplicación toma de 30 a 45 minutos. Al salir, los labios pueden verse más grandes de lo que van a quedar: la inflamación leve dura de 24 a 72 horas.</p>'
     '<p>No los juzgues el primer día.</p>'
     '<p>Empezamos con poca cantidad. Si cuando baja la inflamación sientes que faltó un poco, se completa después. Quitar también se puede, con hialuronidasa, pero preferimos no necesitarlo.</p>'),
]
POR_SLUG["relleno-de-labios"]["faq"] += [
    ("¿Dónde hacerme un relleno de labios en Pereira?", "Con un médico, después de una valoración presencial y con un producto de ácido hialurónico con registro INVIMA que puedas verificar. La FDA de Estados Unidos recomienda no comprar rellenos por internet ni inyectárselos uno mismo. En The Skin Haus te atendemos en la Torre Médica Oval de Pereira."),
    ("¿Cuántos ml de ácido hialurónico se ponen en los labios?", "Depende de tu boca y de lo que buscas. En una revisión de estudios sobre aumento de labios, la mayoría de protocolos usó de 1 a 2 ml por sesión, pero no es una receta. Si lo que quieres es hidratar o definir, la conversación cambia. Lo decidimos al verte."),
]


# ================================================================== ácido hialurónico
SEO["acido-hialuronico"]["secciones"] += [
    ("Relleno, bioestimulador o skinbooster: no son lo mismo",
     '<p>Los tres se inyectan y por eso se confunden. Buscan cosas distintas:</p>'
     '<ul><li><strong>Ácido hialurónico de relleno.</strong> Aporta soporte o volumen desde el primer día, en una zona puntual.</li>'
     '<li><strong><a href="bioestimuladores">Bioestimuladores</a>.</strong> Hacen que tu piel fabrique colágeno. Mejoran la firmeza y la calidad de la piel, y el cambio se nota hacia la semana 6 a 8.</li>'
     '<li><strong><a href="skinboosters">Skinboosters</a>.</strong> Usan un ácido hialurónico ligero que hidrata y da luz. No aportan volumen.</li></ul>'
     '<p>Si lo que te molesta es una flacidez leve o moderada y no una zona hundida, puede que te sirva más un bioestimulador. Lo vemos en la valoración.</p>'),
    ("Ácido hialurónico en Pereira: qué revisar del producto",
     '<p>Pregunta qué producto te van a aplicar y pide su número de registro sanitario. Lo puedes buscar en la <a href="' + INVIMA + '"' + FUERA + '>consulta de registros del INVIMA</a>, que muestra si es válido y en qué estado está.</p>'
     '<p>No es exceso de cuidado. En 2025 el INVIMA alertó sobre un lote falsificado de un relleno de ácido hialurónico que se vendía por plataformas digitales. La FDA de Estados Unidos recomienda no comprar rellenos por internet y considera la inyección un procedimiento médico, no un tratamiento cosmético.</p>'
     '<p>En la valoración te decimos qué producto conviene para tu caso, y puedes verificarlo antes de empezar.</p>'),
]
SEO["acido-hialuronico"]["faq"] += [
    ("¿Dónde ponerse ácido hialurónico en Pereira?", "En un lugar de salud, con un médico que te valore en persona antes de inyectar y con un producto con registro INVIMA. En The Skin Haus estamos en la Torre Médica Oval de Pereira."),
    ("¿Qué riesgos tiene el ácido hialurónico?", "Puede haber inflamación leve o algún morado de 24 a 72 horas. El riesgo que más preocupa a la FDA es que el producto entre por accidente en un vaso sanguíneo, y por eso importa tanto quién inyecta. Todo procedimiento tiene riesgos y los resultados varían en cada persona."),
]


# ================================================================== /nosotros
# Secciones largas (h2, html) que se agregan al final de /nosotros (antes del cierre).
NOSOTROS_TEXTO = [
    ("Quiénes somos y dónde estamos",
     '<p>The Skin Haus es una clínica de medicina estética y medicina vascular en la Torre Médica Oval de Pereira. Se escribe Haus, no House, por si alguna vez nos buscas en Google.</p>'
     '<p>Atendemos a pacientes de Pereira y de toda el área: Dosquebradas, Santa Rosa de Cabal, La Virginia y Cartago. Le hablamos a quien quiere cuidarse sin dejar de verse como es.</p>'
     '<p>Por WhatsApp agendas y resuelves dudas generales. El diagnóstico y el plan se hacen en persona, porque una cara o una piel no se valoran por foto.</p>'),
    ("Cómo trabajamos",
     '<p>Antes de cualquier aguja, conversamos: qué te gustaría mejorar, qué no quieres cambiar y qué te has hecho antes. Después te examinamos en reposo y en movimiento, y solo entonces recomendamos.</p>'
     '<p>La valoración es médica y presencial, y no te compromete a hacerte nada. Te explicamos las opciones con tiempos, cuidados y costos claros, y decides con calma. Si con una cosa alcanza, no te proponemos tres. En muchos casos el tratamiento se puede hacer ese mismo día, si el médico lo considera adecuado y tú te sientes lista o listo.</p>'
     '<p>Vamos por etapas y con poca cantidad. Preferimos quedarnos cortos y completar en el control antes que pasarnos. No trabajamos con paquetes genéricos ni con la promesa de un antes y un después.</p>'
     '<p>Menos, mejor puesto.</p>'
     '<p>Y el cuidado sigue después de la cita. Te damos las indicaciones por escrito y te vemos en control: en el <a href="toxina-botulinica">bótox</a>, por ejemplo, hacia las dos semanas, cuando el efecto ya se ve completo.</p>'),
    ("Siempre un médico",
     '<p>Los procedimientos los realiza o supervisa directamente el equipo médico de la clínica.</p>'
     '<p>En medicina estética está la Dra. Valeria Enciso, nuestra médica estética. Si vienes por bótox, <a href="acido-hialuronico">ácido hialurónico</a>, <a href="bioestimuladores">bioestimuladores</a> o un tratamiento de calidad de piel, es ella quien te valora y te acompaña.</p>'
     '<p>En medicina vascular atiende el Dr. José David Puerta Rojas, médico internista con subespecialidad en medicina vascular. Trata arañitas, várices e insuficiencia venosa, y también tiene consulta en Seravena, en Medellín.</p>'
     '<p>La <a href="limpieza-facial-medica">limpieza facial médica</a> la hace personal entrenado bajo supervisión médica. Si quieres verificar a cualquier profesional de la salud, también a nosotros, búscalo en el <a href="' + RETHUS + '"' + FUERA + '>RETHUS</a> con su primer nombre y su primer apellido.</p>'),
    ("Por qué estética y vascular en un mismo lugar",
     '<p>Lo que se ve en la piel muchas veces empieza más adentro. Las arañitas de las piernas, por ejemplo, pueden ser la señal visible de un problema venoso más profundo. Por eso, para las arañitas y las várices, en <a href="medicina-vascular">medicina vascular</a> empezamos con un eco-doppler: para tratar la causa y no quedarnos en lo que se ve.</p>'
     '<p>En la cara pasa algo parecido. La <a href="cuperosis-y-rojeces">cuperosis y las rojeces</a> tienen un componente vascular, y ahí se juntan las dos especialidades.</p>'
     '<p>Para ti, la ventaja es práctica: un solo lugar y el mismo criterio, consultes por tu cara o por tus piernas.</p>'),
]


# ================================================================== /valoracion
# Secciones largas (h2, html) que se agregan en /valoracion (antes de las preguntas frecuentes).
VALORACION_TEXTO = [
    ("Qué decidir antes de llegar",
     '<p>Abriste el formulario y no sabes qué marcar en “¿Qué te interesa?”. No pasa nada: para eso es la valoración, y puedes elegir “Aún no sé, quiero orientación”.</p>'
     '<p>Lo que sí ayuda es traer dos frases claras. Una cosa que te gustaría mejorar y una que no quieres cambiar por nada.</p>'
     '<p>Piensa también en tu calendario. Si tienes una fecha importante encima, dilo desde el principio: el bótox tarda unas dos semanas en verse completo y el ácido hialurónico puede dejar inflamación leve de 24 a 72 horas, así que la fecha cambia el plan.</p>'
     '<p>Y piensa si te gustaría hacerte el tratamiento ese mismo día, si el médico lo considera adecuado, o prefieres llevarte la propuesta a casa. Las dos opciones están bien.</p>'),
    ("Qué preguntarle al médico en la valoración",
     '<p>Son preguntas normales y nadie debería molestarse por ellas:</p>'
     '<ul><li><strong>¿Quién me lo va a aplicar?</strong> Pide el nombre completo. En el <a href="' + RETHUS + '"' + FUERA + '>RETHUS</a>, la consulta pública del Ministerio de Salud, ves su profesión y si está autorizado para ejercer.</li>'
     '<li><strong>¿Qué producto es y cuál es su registro INVIMA?</strong> Con ese número lo buscas en la <a href="' + INVIMA + '"' + FUERA + '>consulta de registros sanitarios del INVIMA</a>.</li>'
     '<li><strong>¿Qué riesgos tiene y qué hacemos si algo no sale como esperamos?</strong> En Colombia, la Ley 23 de 1981 pide al médico tu consentimiento y que te advierta del riesgo previsto antes del tratamiento.</li>'
     '<li><strong>¿Hay control?</strong> Que te digan desde el principio cuándo es y qué se revisa.</li>'
     '<li><strong>¿Cuánto dura y cada cuánto se repite?</strong> Así haces cuentas del año completo y no solo de la primera sesión.</li>'
     '<li><strong>¿Cuál es el valor?</strong> Te lo damos en la valoración, antes de empezar.</li></ul>'
     '<p>Házselas también a nosotros. Si quieres hacer la verificación con calma, en <a href="blog/como-elegir-medico-estetico-en-pereira">cómo elegir médico estético en Pereira</a> va paso a paso.</p>'),
    ("Si decides no hacerte nada",
     '<p>Está bien. La valoración no te compromete a ningún tratamiento.</p>'
     '<p>A veces la conclusión es esperar, empezar por una rutina en casa o cambiar el orden de lo que traías pensado. Otras veces lo que te molesta no se resuelve con un inyectable, y te lo decimos. Si vemos algo que debe revisar otro especialista, como un lunar que cambió de forma o de color, te orientamos.</p>'
     '<p>Sales con información clara para decidir cuando quieras. Si necesitas un día para pensarlo, tómatelo.</p>'),
]
