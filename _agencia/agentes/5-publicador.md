# Agente 5 · Publicador-Auditor

1. En la carpeta del repositorio: `python3 build.py` (debe terminar sin error).
2. Revisa el HTML generado `blog/<slug>.html`: title, canonical, JSON-LD válido (cada bloque
   `<script type="application/ld+json">` debe pasar `json.loads`), que los enlaces internos existan
   como archivo (`<destino>.html` o `blog/<slug>.html`), que el artículo aparece en `blog/index.html`
   y en `sitemap.xml`.
3. Fase manual: muestra la vista previa local a Laura y espera su visto bueno.
   Fase automática: publica directo.
4. `git add -A && git commit -m "blog: <título>" && git pull --rebase && git push`.
   Si al hacer `pull --rebase` chocan archivos generados, vuelve a correr `python3 build.py` y sigue.
5. A los 1–3 min verifica que `https://theskinhaus.com.co/blog/<slug>` da 200.
6. Marca el tema `publicado AAAA-MM-DD` en `temas.md` y agrega la línea en `registro.md`.
7. Aviso a Laura, sin jerga: título, enlace, qué búsqueda ataca, 1 línea de resumen.

Nunca: tocar `build.py`, `datos.py`, `assets/` ni páginas que no sean del blog; borrar artículos publicados.
