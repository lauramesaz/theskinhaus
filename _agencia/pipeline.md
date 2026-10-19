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

Semanal (lunes): `agentes/6-analista.md` lee `search-console.md` y mejora el artículo más flojo.

```
1 Redactor → 2 Policía → 3 Verificador ──(bloquea)──┐
                             │ aprueba                │
                             ▼                        │
                       4 Juez SEO → 2 Policía (control final) → 5 Publicador      vuelve a 1
```

Reglas de la cadena:
- El Redactor lee `notas-humanizador.md` (libreta de multas del Policía) antes de escribir.
- Cada día, además del artículo nuevo, el Policía humaniza 1 artículo viejo de `humanizados.md`;
  pasa por el Verificador y solo cambia `actualizado`.
- El Verificador manda sobre el Juez SEO: un dato dudoso se quita aunque baje la nota SEO.
- Si el Verificador bloquea dos veces el mismo tema, se marca `en pausa` en `temas.md` con el
  motivo y se toma el siguiente.
- Cada agente deja su nota en la línea del día de `registro.md`.

Fase actual: **automática** (aprobada por Laura el 19-oct-2026). La rutina diaria en la nube publica
sola con red de seguridad: se publica, se avisa a Laura y queda en el registro.
