# Pipeline diario · Agencia SEO The Skin Haus

Conocimiento compartido: `INSTRUCCIONES.md`, `estrategia.md`, `hechos.md`, `temas.md`,
`plantilla-articulo.html`, `registro.md`. Cada agente tiene su archivo en `agentes/`.

| # | Agente | Archivo | Qué hace |
|---|---|---|---|
| 1 | Investigador-Redactor | `agentes/1-investigador-redactor.md` | Elige el tema, investiga y escribe |
| 2 | Policía humanizador | `agentes/2-policia-humanizador.md` | Reescribe la forma (prueba de 10 puntos, aprueba con 8), pone multas, control final y limpia 1 artículo viejo por día |
| 3 | Verificador médico-legal | `agentes/3-verificador.md` | Cada dato contra `hechos.md` y las reglas de oro; puede BLOQUEAR |
| 4 | Juez SEO | `agentes/4-juez-seo.md` | Puntúa el SEO (≥ 85/100) y corrige |
| 5 | Publicador-Auditor | `agentes/5-publicador.md` | build, revisa la página generada, publica, verifica en vivo y registra |

Semanal (lunes, 9:50): la revisión de la nube (`rutina-lunes.md`, hace el papel de `agentes/6-analista.md`) lee
Search Console y escribe `search-console.md`, `mejoras.md` y `metas-90-dias.md`.

```
1 Redactor → 2 Policía → 3 Verificador ──(bloquea)──┐
                             │ aprueba                │
                             ▼                        │
                       4 Juez SEO → 2 Policía (control final) → 5 Publicador      vuelve a 1
```

Reglas de la cadena:
- El Redactor lee `notas-humanizador.md` (libreta de multas del Policía) antes de escribir.
- Ritmo desde el 9-nov-2026: esta cadena completa corre lunes, miércoles y viernes (artículo nuevo).
  Martes, jueves y sábado es día de mejora sobre `mejoras.md` (Policía, Verificador y Juez SEO sobre el texto que
  cambie; en páginas de servicio solo `titulo=` y `desc=` de `datos.py`). Domingo, solo la limpieza del Policía.
  Ver `estrategia.md` §5 y `rutina-diaria.md`.
- Si `humanizados.md` tiene algún `[pendiente]`, el Policía lo humaniza ese mismo día; pasa por el Verificador
  y solo cambia `actualizado`. El domingo, si no hay pendientes, revisa el artículo con `actualizado` más viejo.
- El Verificador manda sobre el Juez SEO: un dato dudoso se quita aunque baje la nota SEO.
- Si el Verificador bloquea dos veces el mismo tema, se marca `en pausa` en `temas.md` con el
  motivo y se toma el siguiente.
- Cada agente deja su nota en la línea del día de `registro.md`.

Fase actual: **automática** (aprobada por Laura el 19-oct-2026). La rutina diaria en la nube publica
sola con red de seguridad: se publica, se avisa a Laura y queda en el registro.
