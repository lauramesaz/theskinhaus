# Agencia SEO · The Skin Haus (solo medicina estética · Pereira)

> Manual compartido por todos los agentes. La carpeta empieza por `_` y NO se publica (GitHub Pages
> con Jekyll ignora las carpetas que empiezan por `_`; no crear `.nojekyll`).
> Repositorio: `lauramesaz/theskinhaus` (GitHub Pages, publica al hacer push a `main`).
> Web: https://theskinhaus.com.co · Ojo: la marca es "The Skin Haus" (Haus, no House).

## 0. Misión

Traer pacientes de **medicina estética** a The Skin Haus (Torre Médica Oval, Pereira) desde Google.
**Solo medicina estética**: bótox (toxina botulínica), ácido hialurónico (labios, ojeras, pómulos,
mentón, mandíbula), bioestimuladores de colágeno, skinboosters, peelings médicos, microagujas,
manchas y melasma, limpieza facial médica. **Nada de medicina vascular** (várices, arañitas,
eco-doppler, cuperosis): esas páginas existen en la web pero esta agencia no escribe sobre ellas.

Lector: mujeres y hombres de Pereira y su área (Dosquebradas, Santa Rosa de Cabal, La Virginia,
Cartago) que están averiguando un tratamiento, casi siempre desde el celular, y que se preguntan
cuánto vale, cuánto dura, si se va a notar, si duele y en quién confiar.

**Meta: 1 artículo nuevo al día** (o 1 actualización de uno viejo), en el orden de `temas.md`.

## 1. Marca (tono)

- Manual de marca: "claro, cercano, seguro"; "playful pero sofisticada". "Sofisticación sin distancia."
- Ideas que repite la marca: "Belleza que se acompaña, no que se impone", "Primero te escuchamos.
  Luego recomendamos", "Menos, mejor puesto", resultados sutiles y armónicos.
- Tuteo. Frases cortas. Párrafos de 2 a 4 líneas. Nada de exclamaciones, emojis ni "¡increíble!".
- Hablar con la persona, nunca con su inseguridad: nada de "arregla tus defectos", "luce 10 años
  menor", "cara perfecta".
- CTA de la marca: "Agenda tu valoración". El WhatsApp y el cierre los pone la plantilla.
- Firma: "Equipo médico The Skin Haus". **No hay nombres de médicos confirmados**: no inventar
  nombres, títulos, años de experiencia ni registros.

## 2. Reglas de oro médicas y legales (contenido de salud, YMYL)

1. **Nada inventado.** Solo cifras, tiempos y datos que estén en `hechos.md` (con fuente) o en
   `../datos.py` (lo que ya publica la web). Si no está, no se escribe o se dice de forma general.
2. **Nunca precios** de The Skin Haus (no están definidos) ni rangos de precios del mercado.
   Si el tema es costo: qué define el valor, qué debería incluir, señales de alerta de lo "muy
   barato", y que el valor exacto se da en la valoración, antes de empezar.
3. Nunca prometer resultados ni decir "sin riesgo", "sin dolor", "garantizado", "permanente".
   "Todo procedimiento tiene riesgos y los resultados varían en cada persona."
4. **Nada de antes y después como promesa** (regla del manual de marca). No describir casos ni
   pacientes. **Nunca** testimonios ni "lo que vemos en consulta".
5. La valoración es **presencial**. Por WhatsApp se agenda y se resuelven dudas generales; no se
   diagnostica ni se indica tratamiento a distancia.
6. Los procedimientos los realiza o supervisa directamente el equipo médico (así lo dice la web).
7. No nombrar ni comparar con otras clínicas o médicos. No descalificar a nadie.
8. Marcas comerciales (Botox, Sculptra, Radiesse, Profhilo, Dermapen): se pueden nombrar para
   explicar qué es cada cosa, pero **nunca afirmar que The Skin Haus usa una marca concreta**.
   Fórmula segura: "en la valoración te decimos qué producto conviene para tu caso".

## 3. SEO (cómo posicionar)

- **1 keyword principal por artículo** + 3 a 5 secundarias. Debe ir en `title`, `h1`, primer
  párrafo (`entrada`), un `<h2>` y la `descripcion`.
- `title` ≤ 60 caracteres (la plantilla añade " · The Skin Haus" solo si cabe). `descripcion`
  140–160 caracteres, con un dato concreto, distinta en cada artículo.
- Keyword como la escribe alguien en Colombia: "bótox" (con o sin tilde) más que "toxina
  botulínica"; "cuánto vale", "cuánto dura", "es lo mismo", "precio". Las preguntas reales que
  Google muestra en Pereira están en `estrategia.md`.
- **Pereira** aparece natural en el primer párrafo, en un `<h2>` y en la descripción cuando la
  keyword es local. Señales locales verdaderas (de `hechos.md`): el sol y la altitud del Eje
  Cafetero, Dosquebradas y Santa Rosa a pocos minutos, la Torre Médica Oval, la cita entre semana.
- **Cada búsqueda tiene UNA página dueña. El blog no le roba la keyword a la página que vende.**
  "Bótox en Pereira", "ácido hialurónico en Pereira", "relleno de labios en Pereira", etc. son de
  las páginas de tratamiento (`../datos.py`: ESTETICA y BUSQUEDAS). Un artículo nunca lleva como
  `title` o `keyword` solo "<tratamiento> en Pereira": siempre suma un ángulo ("precio", "cuánto
  dura", "o", "¿es lo mismo?", "cuántas sesiones"). Antes de escribir, revisa `registro.md`,
  `articulos/` y `../datos.py`.
- **Enlace a la página que vende, dentro del texto**, en el primer tercio: p. ej.
  `<a href="toxina-botulinica">bótox</a>`. Las direcciones internas van sin `.html` y sin `/`
  inicial (la web usa `<base href="/">`): tratamientos = `toxina-botulinica`, `acido-hialuronico`,
  `bioestimuladores`, `skinboosters`, `peelings-medicos`, `microagujas`, `manchas-y-melasma`,
  `limpieza-facial-medica`, `relleno-de-labios`, `tratamiento-de-ojeras`, `armonizacion-facial`,
  `hiperhidrosis`, `cicatrices-de-acne`, `valoracion`; otros artículos = `blog/<slug>`.
- **Fuentes oficiales:** cada artículo con datos de salud enlaza al menos 1 fuente oficial que esté
  en `hechos.md` (INVIMA, MinSalud, RETHUS, FDA, AAD, etc.).
- **Enlaces internos:** 1–3 tratamientos en `tratamientos` (la plantilla pone las tarjetas) + en el
  texto 1–2 artículos hermanos cuando existan.
- **FAQ:** 3 a 6 preguntas reales (como se escriben en Google). La plantilla genera el JSON-LD
  (`FAQPage`, `BlogPosting`, `BreadcrumbList`). No lo escribas a mano.
- Slug en minúsculas con guiones, sin tildes: `cuanto-dura-el-botox`.

## 4. Que suene a persona, no a IA

Prohibido: raya larga (—) como muletilla (máx. 1 por artículo), "En este artículo te contamos",
"Te contamos", "Es importante destacar", "Cabe resaltar", "En conclusión", "En resumen",
"no solo… sino también", "sumérgete", "descubre", "el secreto de", "en el mundo actual",
"transforma tu piel", listas de 3 adjetivos por costumbre, párrafos todos del mismo largo,
cierres que repiten lo dicho, preguntas retóricas en cadena.
Sí: situaciones reales del lector en Pereira (la foto del grado o del matrimonio, la reunión del
lunes, el sol de mediodía, salir del trabajo y llegar a la cita, el miedo a "quedar rara"),
opiniones claras de la clínica respaldadas por §2 ("preferimos quedarnos cortos y completar en el
control"), y honestidad sobre límites ("el melasma no se cura: se controla").

## 5. Formato de cada artículo

Un archivo por artículo en `_agencia/articulos/<slug>.html`. Ver `plantilla-articulo.html`.
Cabecera JSON dentro de `<!-- -->` + cuerpo HTML (solo `<p>`, `<h2>`, `<h3>`, `<ul>`, `<ol>`,
`<li>`, `<strong>`, `<em>`, `<a>`, `<blockquote>` y el bloque `<div class="dato">`). Nada de
estilos, clases inventadas ni scripts. Primer párrafo con `class="entrada"`. Largo: 700–1.200
palabras. `"estado": "publicado"` para que salga; `"borrador"` no se publica.

## 6. Publicar

```
cd <carpeta del repositorio>
python3 build.py                      # genera páginas, blog, sitemap.xml, robots.txt y llms.txt
git add -A && git commit -m "blog: <título>"
git pull --rebase && git push
```
Luego verificar que `https://theskinhaus.com.co/blog/<slug>` responde 200 (1–3 min) y anotar en
`registro.md`. Fase: **automática** (aprobada por Laura el 19-oct-2026), ver `pipeline.md`.

## 7. Si algo no rinde

Política: **actualizar, no borrar.** Si en 3 meses un artículo no tiene impresiones en Search
Console, se mejora (título, profundidad, enlaces) y se cambia `actualizado`.
