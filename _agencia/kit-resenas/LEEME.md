# Kit de reseñas · The Skin Haus (27-oct-2026)

Las reseñas de Google son lo que más pesa para salir en el MAPA cuando alguien busca
"medicina estética Pereira". Hoy las 3 clínicas que salen ahí tienen 62, 67 y 175 reseñas.
Meta: **20 reseñas antes del 30 de noviembre**.

## Qué hay en esta carpeta

| Archivo | Para qué |
|---|---|
| `tarjeta-resena.pdf` / `.png` | Tarjeta para imprimir (10,5 × 14,8 cm, tamaño A6). Va en recepción y en el consultorio. |
| `qr-resena.png` | El código QR solo, para pegarlo en otras piezas (factura, sticker, historia de Instagram). |

El QR lleva a **theskinhaus.com.co/resena**. Esa página ya está en la web:

- **Hoy** (sin ficha de Google): muestra "¿Cómo te fue?" y un botón para contarnos por WhatsApp.
- **Cuando exista la ficha de Google Maps**: se pega el enlace "Pedir reseñas" de la ficha en `datos.py`
  (`RESENA_URL = "https://g.page/r/.../review"`), se publica, y desde ese momento el QR lleva directo
  a escribir la reseña en Google. **No hay que reimprimir nada.**

## Mensajes de WhatsApp (copiar y pegar)

**El mismo día, al salir de la cita:**
> Hola, [nombre]. Gracias por venir hoy a The Skin Haus. Si tienes un minuto, nos ayudaría mucho que
> contaras cómo te fue: theskinhaus.com.co/resena
> Cualquier duda sobre tus cuidados, escríbenos por aquí.

**A los 3 días, si no la dejó (solo una vez):**
> Hola, [nombre]. ¿Cómo sigues después de tu cita? Si quieres dejarnos tu opinión, es aquí:
> theskinhaus.com.co/resena. Gracias por confiar en nosotros.

**En el control de las 2 semanas (bótox) o cuando la paciente comente que está contenta:**
> Qué bueno que te sientas así. Si nos ayudas contándolo en Google, a otras personas de Pereira les
> sirve para decidir: theskinhaus.com.co/resena

## Reglas (normas de Google)

- Pedir reseña a **todas** las pacientes, no solo a las que creemos contentas (Google prohíbe filtrar).
- **Nunca** dar descuentos, regalos ni sorteos a cambio de una reseña.
- No escribir reseñas desde el equipo, familiares ni cuentas propias. No pedirlas todas el mismo día
  desde el mismo wifi de la clínica.
- Responder **todas** las reseñas en menos de 48 horas, con el nombre de la persona y sin datos de salud.

## Respuestas modelo

**Reseña buena:**
> Gracias, [nombre]. Nos alegra que te hayas sentido acompañada. Aquí estamos para tus controles.

**Reseña regular o mala:**
> [Nombre], gracias por contarnos. Lo sentimos. Queremos entender qué pasó y resolverlo:
> escríbenos al +57 317 441 2203 y te atendemos directamente.

(Nunca discutir en público ni mencionar el tratamiento que se hizo la paciente.)
