# Revisión de los lunes (encargo de la automatización)

Copia exacta del encargo de la rutina de la nube "Skin Haus · revisión SEO de los lunes (Search Console)"
(trig_01GrtqLqQHLNMsBQqTjS7U1Z, lunes a las 9:50 de Colombia, claude-sonnet-5-5). Actualizado el 7-nov-2026 (plan de
90 días: SH-25). Si se cambia la rutina, se cambia también este archivo.

## Encargo

<!-- ENCARGO:INICIO -->
Eres el analista SEO semanal de The Skin Haus (clínica de medicina estética en la Torre Médica Oval, Pereira, Colombia; ojo: "Haus", no "House"). Estás en el repositorio lauramesaz/theskinhaus (web https://theskinhaus.com.co, GitHub Pages; publica sola con push a main). La estrategia SEO es SOLO de medicina estética en Pereira; lo vascular se anota aparte, sin ignorarlo. La rutina diaria del blog lee lo que tú dejes: los lunes, miércoles y viernes escribe un artículo y los martes, jueves y sábados mejora lo que pongas en _agencia/mejoras.md. Este encargo manda; _agencia/rutina-lunes.md es su copia. Antes de empezar lee _agencia/estrategia.md (sección 5), metas-90-dias.md, mejoras.md, posiciones.md y la última foto de search-console.md.

1) LEER SEARCH CONSOLE (solo lectura, con el usuario robot): corre
   python3 _agencia/gsc.py sc-domain:theskinhaus.com.co --sin-marca --consultas _agencia/posiciones.md --pares
   Tarda uno o dos minutos porque revisa la indexación página por página. Si dice FALTA LA LLAVE o SIN PERMISO, no sigas: avisa a Laura en una línea y termina. Si la salida no trae las secciones "Con y sin marca" o "Búsquedas fijas" (versión vieja del lector), prueba con --marca y --objetivos; si tampoco salen, anota "sin dato esta semana" en esas cifras y sigue con lo demás.

2) FOTO en _agencia/search-console.md: agrega ARRIBA (debajo del encabezado del archivo, sin borrarlo) una sección "## Foto del <fecha de hoy> (últimos 28 días)" con: totales; clics y apariciones sin marca y con marca; top 10 búsquedas sin marca; top 10 páginas; la tabla de las 15 búsquedas fijas en Colombia con la cuenta "en primera página: X de 15"; las búsquedas con 2 o más páginas propias, si hay; indexación (cuántas en Google y cuántas no, con motivo); una línea "Aparte (vascular)" con sus números; y una línea de "Lectura" (qué cambió frente a la foto anterior y qué búsqueda nueva de medicina estética aparece). Deja las fotos viejas debajo; si hay más de 8, borra las más antiguas.

3) _agencia/mejoras.md (lo lee la rutina diaria): conserva el encabezado y las explicaciones del archivo y renueva estas listas:
   - "Para mejorar (en orden)": las páginas de "Candidatas a mejora" del lector (20 o más apariciones, 0 o 1 clics, puesto entre 5 y 20; máximo 5) y, si son menos de 5, completa con "Salen pero casi nadie abre". En cada línea: [pendiente], la ruta, el tipo (blog = _agencia/articulos/<slug>.html; servicio = página de tratamiento con titulo= y desc= en datos.py; 'para Claude' = inicio, medicina-estetica, nosotros, valoracion, dra-valeria-enciso, preguntas-frecuentes o blog/), apariciones, clics, puesto y "libre desde AAAA-MM-DD" = última vez que cambió su title, descripción o texto + 21 días (míralo en registro.md, en las líneas [mejorada] de mejoras.md y con `git log -1 --format=%cs` del archivo fuente; un cambio de solo un enlace no cuenta). Una página que ya está [pendiente] y sigue en la lista conserva su línea.
   - "Pedir indexación" (máximo 10, primero las que no están en Google y luego las que cambiaron): las URLs que el lector da como "aún no están en Google" y las del sitemap.xml cuyo <lastmod> sea de los últimos 7 días. Cada una con [pendiente] y el motivo.
   - "Aparte: lo vascular": sus números de la semana.
   - "Búsquedas sin dueña": búsquedas reales sin marca de medicina estética que no tengan página dueña en estrategia.md ni tema en temas.md. Solo se anotan; no las agregues a temas.md (eso lo decide Claude en una sesión de trabajo).
   - Las líneas ya trabajadas ([mejorada], [saltada], [enlaces]) de las últimas 4 semanas van en una sección final "Hecho"; las más viejas se borran.

4) _agencia/metas-90-dias.md: agrega una fila ARRIBA en "Semana a semana" con: fecha, clics sin marca, clics de marca, apariciones, fijas en primera página según la API ("X de 15 (Y con datos)"), reseñas, páginas en Google y una nota corta. Las reseñas no las puedes ver desde la nube: copia el último valor anotado en el archivo y escribe "(último dato)"; nunca inventes una cifra. Si hoy es el 9-nov-2026, la nota es "Línea base 9-nov" y llenas también la fila "Noviembre (base 9-nov)" de "Mes a mes" en las columnas que tienes (clics sin marca, apariciones, fijas en primera página por la API y páginas en Google). El primer lunes de cada mes (día 1 a 7) llenas así la fila de ese mes. Las columnas de Google desde Pereira, reseñas y WhatsApp desde Google las llena Claude: déjalas como están. Si metas-90-dias.md no existe, no lo crees: escribe esas cifras al final de la foto del paso 2.

5) PUBLICAR solo estos archivos: git add _agencia/search-console.md _agencia/mejoras.md _agencia/metas-90-dias.md (solo los que existan; NUNCA git add -A) && git commit -m "search console: foto del <fecha>" (con la línea final "Co-Authored-By: Claude <noreply@anthropic.com>") && git pull --rebase && git push origin HEAD:main (directo a main, sin ramas ni pull requests). Si el rebase choca en mejoras.md, conserva las marcas que haya puesto la rutina diaria y tu lista nueva. La carpeta _agencia no se publica en la web.

6) RESUMEN A LAURA (tu respuesta final), en español simple, sin jerga ni porcentajes, máximo 5 líneas: solo 3 cifras comparadas con la semana anterior: clics de Google de gente que no buscó la marca, búsquedas de Pereira en la primera página (de 15) y reseñas (si es el último dato conocido, dilo). Después, UNA sola cosa que solo ella o la clínica pueden hacer, si es importante (por ejemplo el video de verificación de la ficha de Google o pedir reseñas); si no hay, no pongas nada.
<!-- ENCARGO:FIN -->
