# -*- coding: utf-8 -*-
# The Skin Haus · ampliación de páginas (27-oct-2026). Se carga desde build.py después de datos.py.
from datos import SEO, BUSQUEDAS

POR_SLUG = {b["slug"]: b for b in BUSQUEDAS}

# Secciones largas (h2, html) que se agregan al final de /nosotros y de /valoracion.
NOSOTROS_TEXTO = []
VALORACION_TEXTO = []
