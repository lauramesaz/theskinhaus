# Metas de 90 días · The Skin Haus (9-nov-2026 al 7-feb-2027)

Lo pone al día la revisión de los lunes (rutina de la nube, 9:50) con `python3 _agencia/gsc.py
sc-domain:theskinhaus.com.co --sin-marca --consultas _agencia/posiciones.md --pares`. Lo que la nube no puede leer
(reseñas, ficha de Google, WhatsApp desde Google) lo anota Claude en una sesión de trabajo o la tarea del navegador
de los lunes; mientras tanto la rutina copia el último valor y no inventa ninguno.

A Laura le llegan solo 3 cifras: **clics sin marca**, **búsquedas de Pereira en la primera página** y **reseñas**.

## Las metas

| Qué medimos | Hoy (punto de partida) | Meta al 7-feb-2027 | Cómo se mide |
|---|---|---|---|
| Clics de Google de búsquedas que no son la marca (28 días) | 3 clics del 4 al 31-oct, sin separar la marca. Lectura del 7-nov (9-oct a 5-nov): 7 clics, 0 de marca | 15 | Lunes, `gsc.py --sin-marca` ("Sin marca" = total menos marca) |
| Veces que la web aparece en Google (28 días) | 231 (2-nov) · 402 en la lectura del 7-nov | 1.000 | Lunes, totales de `gsc.py` |
| Búsquedas de Pereira en la primera página (las 15 fijas de `posiciones.md`) | 7 de 15 el 27-oct, sin ubicación de Pereira. Por la API el 7-nov: 2 con datos, ninguna con puesto medio de 10 o mejor | 10 de 15; "botox pereira" en el puesto 10 o mejor; "ácido hialurónico pereira" con `/acido-hialuronico`; "medicina estética pereira" dentro de los 20 primeros | Lunes, `gsc.py --consultas` (solo las que tienen datos). Una vez al mes, revisión en Google con ubicación de Pereira (SH-27), que es la base real |
| Ficha en el mapa de Google | Creada el 5-nov, sin verificar (no es pública) | Verificada y pública; al buscar "the skin haus pereira" sale la nuestra; entre los 3 primeros del mapa en al menos 1 de las 15 búsquedas | Revisión mensual SH-27 e informe de la ficha |
| Reseñas en Google | 0 | 12, todas respondidas | Conteo en la ficha cada lunes (sesión de trabajo o tarea del navegador) |
| Perfiles externos con el mismo nombre, dirección y teléfono | 0 | 4: ficha de Google, Doctoralia de la Dra. Enciso, consultorio 904 en el Doctoralia del Dr. Puerta y Bing Places | Lista de abajo, revisada una vez al mes |
| Prueba mensual con IA (10 preguntas) | 0 de 10 (1-nov) | 2 de 10, y en la pregunta de marca la fuente es theskinhaus.com.co y no GitHub | Rutina de IA del día 1 (`registro-ia-mensual.md`) |
| Conversaciones de WhatsApp que llegan desde Google | Casi 0 (octubre: 4 visitas desde Google de 20) | 6 al mes | Evento clic_whatsapp de GA4 por canal, cuando el robot tenga acceso (SH-26). Hasta entonces: "sin dato" |
| Páginas del sitemap que están en Google | 40 de 44 (2-nov) · 50 de 53 el 7-nov | Todas, salvo 2 como máximo | Lunes, indexación de `gsc.py` |
| Salto del diseño al cargar (CLS) en las páginas que venden | 0,157 en /medicina-estetica y 0,105 en /toxina-botulinica (antes del 7-nov) | Menos de 0,1 en las dos y en la portada | Lighthouse en celular simulado, en el Mac (no lo mide la rutina) |

## Mes a mes

| Mes | Clics sin marca | Apariciones | Fijas en 1.ª página (API) | Fijas en 1.ª página (Google desde Pereira) | Reseñas | WhatsApp desde Google | Páginas en Google |
|---|---|---|---|---|---|---|---|
| Noviembre (base 9-nov) | | | | | | | |
| Diciembre | | | | | | | |
| Enero | | | | | | | |
| Febrero (cierre 7-feb) | | | | | | | |

## Semana a semana (la revisión de los lunes agrega una fila arriba)

| Lunes | Clics sin marca | Clics de marca | Apariciones | Fijas en 1.ª página (API) | Reseñas | Páginas en Google | Nota |
|---|---|---|---|---|---|---|---|
| 7-nov (lectura previa, Claude) | 7 | 0 | 402 | 0 de 15 (2 con datos) | 0 | 50 de 53 | Lectura de prueba del lector nuevo; la base oficial es la del 9-nov |

## Perfiles externos (enlace de cada uno cuando exista)

- Ficha de Google: creada el 5-nov, sin verificar.
- Doctoralia de la Dra. Valeria Enciso: no existe todavía.
- Consultorio 904 en el Doctoralia del Dr. Puerta: no está todavía.
- Bing Places: no existe todavía.
