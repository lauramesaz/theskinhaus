# -*- coding: utf-8 -*-
# The Skin Haus · copias de 720 px de las fotos grandes, para celulares (9-nov-2026, ronda 3 · velocidad).
# Uso:  python3 _fotos_720.py      (necesita Pillow; solo hace falta correrlo cuando se agrega una foto nueva)
# Por cada assets/fotos/<nombre>.webp de más de 900 px de ancho crea assets/fotos/<nombre>-720.webp si no existe.
# build.py las usa solas (srcset) cuando existen; si una foto no tiene copia, la página sale con la foto de siempre.
import os, glob
from PIL import Image

AQUI = os.path.dirname(os.path.abspath(__file__))
for ruta in sorted(glob.glob(os.path.join(AQUI, "assets", "fotos", "*.webp"))):
    if ruta.endswith("-720.webp"):
        continue
    chica = ruta[:-5] + "-720.webp"
    with Image.open(ruta) as im:
        if im.width <= 900 or os.path.exists(chica):
            continue
        im.resize((720, round(im.height * 720 / im.width)), Image.LANCZOS).save(chica, "WEBP", quality=82, method=6)
    print("%s: %d KB -> %d KB" % (os.path.basename(ruta), os.path.getsize(ruta) // 1024, os.path.getsize(chica) // 1024))
