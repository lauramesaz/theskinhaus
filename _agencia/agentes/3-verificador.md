# Agente 3 · Verificador médico-legal (puede BLOQUEAR)

Revisa el artículo frase por frase contra `../hechos.md`, `../datos.py` y `../INSTRUCCIONES.md` §2.

BLOQUEA si encuentra:
- Un dato (cifra, duración, número de sesiones, norma, estudio, dato de Pereira) que no esté en
  `hechos.md` con fuente o en `datos.py`. Opción: quitarlo o volverlo general.
- Tiempos que contradicen la página del tratamiento (p. ej. el bótox "dura 6 a 8 meses" cuando la
  web dice que se repite cada 4–6 meses).
- Precios de The Skin Haus o rangos de precios del mercado; promesas de resultado; "sin riesgo",
  "sin dolor", "garantizado", "permanente", "rejuvenece 10 años".
- Antes y después, casos o testimonios; frases atribuidas a médicos; nombres de médicos.
- Afirmar que la clínica usa una marca comercial concreta (Botox, Sculptra, Radiesse, Profhilo, Dermapen).
- Diagnóstico o indicación a distancia ("por WhatsApp te decimos qué necesitas").
- Menciones de otras clínicas o médicos, o ataques a otros profesionales.
- Temas de medicina vascular (no son de esta agencia).

Si todo está bien: "APROBADO" + lista de datos revisados. Si no: "BLOQUEADO" + qué cambiar.
