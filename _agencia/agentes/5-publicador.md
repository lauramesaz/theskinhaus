# Agente 5 · Publicador-Auditor

1. En la carpeta del repositorio: `python3 build.py` (debe terminar sin error).
2. Revisa el HTML generado `blog/<slug>.html`: title, canonical, JSON-LD válido (cada bloque
   `<script type="application/ld+json">` debe pasar `json.loads`), que los enlaces internos existan
   como archivo (`<destino>.html` o `blog/<slug>.html`), que el artículo aparece en `blog/index.html`
   y en `sitemap.xml`.
3. Fase automática (aprobada por Laura el 19-oct-2026): publica directo.
4. `git add _agencia blog *.html sitemap.xml robots.txt llms.txt` (nunca `git add -A`), luego
   `git commit -m "blog: <título>" && git pull --rebase && git push origin HEAD:main`.
   Si al hacer `pull --rebase` chocan archivos generados, quédate con la versión de main, vuelve a correr
   `python3 build.py`, agrégalos y sigue. El detalle está en el encargo de `../rutina-diaria.md` (PUBLICAR).
5. A los 1–3 min verifica que `https://theskinhaus.com.co/blog/<slug>` da 200.
6. Marca el tema `publicado AAAA-MM-DD` en `temas.md` y agrega la línea en `registro.md`.
7. Aviso a Laura, sin jerga: título, enlace, qué búsqueda ataca, 1 línea de resumen.

Nunca: tocar `build.py`, `blog.py`, `assets/` ni páginas que no sean del blog; borrar artículos publicados.
`datos.py` solo en un día de mejora de una página de servicio, y solo sus campos `titulo=` y `desc=`
(ver `../rutina-diaria.md`).
