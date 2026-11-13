# ADR-007: Usar RAG, y no fine-tuning ni prompt largo, para darle la normativa al LLM

**Estado:** propuesta · **Fecha:** 2026-11-12 · **Tarea:** INV-002

> Pasa a `aceptada` cuando se añadan a `investigacion/INV-002-entrenar-vs-rag.md`
> los resultados de INV-012 e INV-013 y confirmen la decisión. Si no la
> confirman, se avisa al docente antes de cerrar INV-002.

## Contexto

El asistente tiene que responder preguntas sobre la normativa de la UAB con
**la cita textual del artículo** (documento y página) y decir "no lo encuentro"
cuando la normativa no lo dice (`docs/VISION.md`). Los LLM no conocen esta
normativa, así que hay que dársela de alguna forma. Hay tres opciones:
fine-tuning, prompt largo y RAG.

Restricciones: sin presupuesto (plan gratuito de Groq con `openai/gpt-oss-120b`,
ADR-009), un equipo de estudiantes que debe entender cada pieza, y una
normativa que cambia con el tiempo.

## Decisión

Usamos **RAG**: troceamos la normativa por artículos, buscamos los más
relevantes para cada pregunta (unos 5) y solo esos se le pasan al modelo, que
debe responder con ellos y citarlos. **No** hacemos fine-tuning ni pegamos toda
la normativa en el prompt.

## Por qué

1. **Cita verificable.** Cada fragmento lleva documento, artículo y página, así
   que la respuesta se puede comprobar contra el texto original. Con
   fine-tuning el modelo no sabe de dónde viene lo que responde.
2. **Cabe en lo que tenemos.** Diez reglamentos como el Estudiantil son unos
   131.434 tokens: no caben en la ventana de 131.072 de `gpt-oss-120b` y superan
   de sobra el límite de 8.000 tokens por minuto del plan gratuito. Con RAG cada
   pregunta lleva unos 800 tokens de normativa.
3. **Actualizar es barato.** Si cambia un reglamento, se vuelve a indexar; no
   hay que reentrenar nada.
4. **Lo hacen así los demás.** Los 5 sistemas revisados en
   `investigacion/INV-002-estado-del-arte.md` usan búsqueda en documentos; los
   que probaron fine-tuning (Unipa-GPT, ChatLaw) no lo usaron solo, y en
   Unipa-GPT no mejoró.
5. **El equipo lo puede explicar.** Cada pieza (ingesta, BM25, búsqueda
   vectorial, prompt) es pequeña y ya tiene su tarea.

Detalle y cálculo en `investigacion/INV-002-entrenar-vs-rag.md`.

## Alternativas descartadas

| Alternativa | Por qué no |
|---|---|
| **Fine-tuning** | No permite citar el artículo de forma fiable, hay que reentrenar con cada cambio de la normativa, necesita datos de entrenamiento y GPU que no tenemos, y en Unipa-GPT no mejoró y produjo alucinaciones |
| **Prompt largo** (toda la normativa en cada pregunta) | Con 10 documentos (unos 131.434 tokens) no cabe en la ventana de `gpt-oss-120b` y supera el límite por minuto de Groq gratuito. En un modelo con ventana mayor (Gemini 3.8 Flash) costaría unos 0,10 USD por pregunta, y su plan gratuito usa los datos para mejorar sus productos (descartado en ADR-009). Además, con mucho texto el modelo cita peor |

## Consecuencias

- **Más fácil:** citar el artículo exacto, actualizar la normativa (volver a
  indexar), mantenernos en el plan gratuito y repartir el trabajo en piezas
  pequeñas.
- **Más difícil:** la calidad depende de la **búsqueda**. Si no encontramos el
  artículo correcto, el modelo no puede responder bien. Por eso hay que medir la
  recuperación (artículo correcto en el top-5) con el golden set, y cuidar el
  troceado por artículo (IA-002).
- **Riesgo que sigue:** RAG no elimina las alucinaciones (17-33 % en
  herramientas legales comerciales, según Stanford). Mantenemos la regla "cero
  respuestas sin cita" y el campo `rechazada`.
- **Señal para revisar la decisión:** si con el golden set el artículo correcto
  no aparece en el top-5 en la mayoría de las preguntas aun mejorando la
  búsqueda, o si cambiamos a un proveedor con ventana muy grande, coste bajo y
  privacidad aceptable, volveríamos a comparar con el prompt largo.
