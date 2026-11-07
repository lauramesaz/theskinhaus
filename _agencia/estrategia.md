# Estrategia SEO · The Skin Haus · medicina estética en Pereira

Hecha el 19-oct-2026 a partir de lo que Google mostraba ese día en Pereira (búsquedas desde el
Chrome de Laura, Colombia, español).

## 1. Qué encontramos

- **La web es nueva (en vivo desde el 28-sep-2026) y Google casi no la conoce**: no aparece para
  ninguna búsqueda de tratamiento en Pereira y no está dada de alta en Search Console.
- **Arriba están los directorios**: Doctoralia, TopDoctors, AgendaPro y clinicasesteticas.com.co
  salen en casi todas las búsquedas. Luego, webs de médicos con **una página por tratamiento +
  ciudad** ("botox-pereira", "bioestimuladores-de-colageno-en-pereira") y dos webs con blog activo
  y artículos localizados ("relleno de labios natural en Pereira", "precio de peelings en Pereira").
- **En el mapa (los 3 primeros de Google Maps)** salen médicas y centros con ficha de Google y
  reseñas. Sin ficha de Google, The Skin Haus no entra a ese bloque.
- **La gente escribe "bótox", no "toxina botulínica"**. La web no usaba la palabra "bótox" en
  ninguna parte. Lo mismo con "dermapen" (microagujas), "Sculptra/Radiesse" (bioestimuladores) y
  "Profhilo" (skinboosters).
- **Casi todas las preguntas son de precio y duración**: "¿cuánto vale una sesión de bótox?",
  "¿cuánto dura el bótox?", "¿cuánto vale 1 ml de ácido hialurónico?", "¿cuántas sesiones de
  Profhilo?", "¿qué es mejor, Sculptra o Radiesse?", "¿el melasma se cura?".
- **Las páginas de tratamiento eran cortas** (unas 250 palabras). Las que ganan tienen 700+.

## 2. Búsquedas objetivo y su página dueña

| Búsqueda (como la escriben) | Página dueña |
|---|---|
| medicina estética Pereira · clínica estética Pereira | `/` (inicio) y `/medicina-estetica` |
| bótox Pereira · toxina botulínica Pereira | `/toxina-botulinica` |
| bótox Pereira precios | artículo `blog/precio-del-botox-en-pereira` |
| ácido hialurónico Pereira | `/acido-hialuronico` |
| relleno de labios Pereira | `/relleno-de-labios` |
| ojeras Pereira · tratamiento de ojeras | `/tratamiento-de-ojeras` |
| armonización facial Pereira | `/armonizacion-facial` |
| bioestimuladores Pereira · Sculptra Pereira · Radiesse | `/bioestimuladores` |
| skinbooster Pereira · Profhilo Pereira | `/skinboosters` |
| peeling Pereira · peeling químico | `/peelings-medicos` |
| dermapen Pereira · microagujas | `/microagujas` |
| cicatrices de acné Pereira | `/cicatrices-de-acne` |
| manchas en la cara Pereira · melasma Pereira | `/manchas-y-melasma` |
| limpieza facial Pereira | `/limpieza-facial-medica` |
| hiperhidrosis Pereira · bótox para el sudor | `/hiperhidrosis` |

## 3. Preguntas reales de Google (para FAQ y temas del blog)

Bótox: ¿Cuánto vale una sesión de bótox? · ¿Cuánto dura el efecto del bótox en la cara? · ¿Qué
diferencia hay entre bótox y toxina botulínica? · ¿Cuánto cuesta un tratamiento de toxina?
Ácido hialurónico: ¿Cuánto vale 1 ml de ácido hialurónico en Colombia? · ¿Cuánto cobran por
inyectar ácido hialurónico? · ¿Cuánto cobran por relleno de labios?
Bioestimuladores: ¿Cuánto duran los bioestimuladores en la cara? · ¿Qué tan efectivos son? ·
¿Qué es mejor, el Sculptra o el Radiesse? · ¿Qué tan recomendable es el Sculptra facial?
Skinbooster / Profhilo: ¿Cuánto tiempo dura el efecto? · ¿Qué es el Profhilo en la cara? ·
¿Cuántas sesiones de Profhilo son necesarias?
Peeling: ¿Cuánto cuesta una sesión de peeling? · ¿Cuáles son los 3 tipos de peeling?
Dermapen: ¿Cuánto vale una sesión? · ¿Qué tan efectivo es el Dermapen en la cara? · ¿Qué riesgos tiene?
Manchas / melasma: ¿Qué es lo más efectivo para quitar el melasma? · ¿Qué médico trata el
melasma? · ¿Qué especialista quita las manchas de la cara? · ¿Qué enfermedad puede provocar manchas?
Limpieza facial: ¿Cuánto cobran por una limpieza facial? · ¿Qué incluye una limpieza facial?

## 4. Plan (lo que hace Claude)

1. **Base técnica y de contenido** (hecho 19-oct, en local): títulos con las palabras que la gente
   usa, "bótox"/"dermapen"/marcas explicadas, páginas de tratamiento de ~250 a 700+ palabras con
   secciones y preguntas reales, datos estructurados completos, migas, sitemap con fechas, llms.txt.
2. **5 páginas nuevas por búsqueda** (hecho 19-oct, en local): relleno de labios, ojeras,
   armonización facial, hiperhidrosis, cicatrices de acné. Todas con tratamientos que la web ya ofrecía.
3. **Blog + agencia diaria** con Policía humanizador (montado 19-oct; 3 primeros artículos).
   Hasta el 8-nov, 1 artículo al día desde `temas.md`; desde el 9-nov, 3 nuevos por semana y 3 días de mejora (§5).
4. **Google**: alta en Search Console + envío del sitemap + IndexNow (Bing/ChatGPT) al publicar.
5. **Cada lunes**: la revisión de la nube (9:50) lee Search Console con `gsc.py --sin-marca --consultas`, escribe
   `mejoras.md` y pone al día `metas-90-dias.md`; martes, jueves y sábados la rutina diaria mejora lo de esa lista.

Lo que solo puede hacer la clínica: crear y verificar la ficha de Google (Google Business
Profile) en la Torre Médica Oval, pedir reseñas a las pacientes, y confirmar nombre y registro del
médico para mostrarlo en la web.

## 5. Reglas del blog desde el 7-nov-2026 (plan de 90 días)

- **Máximo 1 artículo de bótox cada 2 semanas.** Cuenta como "de bótox" todo artículo cuya página dueña en
  `temas.md` sea `toxina-botulinica`. Antes de escribir uno, mira en `registro.md` la fecha del último: si fue hace
  menos de 14 días, salta ese tema (queda `pendiente`) y toma el siguiente. Hasta el 19-dic-2026 aprox. bótox está
  en pausa: van 9 de 28 y el último salió el 7-nov.
- **Ritmo:** lunes, miércoles y viernes, 1 artículo nuevo; martes, jueves y sábado, día de mejora sobre
  `mejoras.md` (la escribe la revisión de los lunes); domingo, solo la limpieza del Policía humanizador.
- **Nada se mejora dos veces seguidas:** una página cuyo title, descripción o texto cambió hace menos de 3 semanas no
  se vuelve a tocar (Google necesita tiempo para medir el cambio). Un cambio de solo un enlace no cuenta.
- **Servicios con pocos enlaces desde el blog** (conteo del 7-nov): `hiperhidrosis` 0; `microagujas`,
  `manchas-y-melasma`, `limpieza-facial-medica`, `tratamiento-de-ojeras` y `cicatrices-de-acne` 2 cada uno;
  `skinboosters` 3. Los días de mejora suman enlaces hacia ellos cuando el texto lo pide de verdad.
- **Búsqueda nueva con dueña:** "cuánto dura el bótox en las axilas" → artículo del tema 47 cuando se publique;
  `/hiperhidrosis` se queda con "bótox para el sudor en Pereira" e "hiperhidrosis Pereira", y su pregunta de duración
  sigue en una línea ("varios meses"). Cuando el artículo salga, Claude le agrega a esa respuesta el enlace al
  artículo en una sesión de trabajo (la rutina no toca esa parte de `datos.py`).
- **La clínica y la médica:** The Skin Haus hace medicina estética (y vascular con el Dr. Puerta, que esta agencia
  no toca). Nunca se escribe "dermatología", "dermatológica" ni "dermatóloga" para la clínica ni para la Dra. Valeria
  Enciso. Su nombre enlaza siempre a `dra-valeria-enciso`. Los H1 de las páginas de servicio llevan "en Pereira"
  (en `datos.py`) y ninguna rutina los quita.
