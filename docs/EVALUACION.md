# Evaluación

Esto es lo que separa "hicimos un chatbot" de "estudiamos si funciona". Sin
números, lo único que hay es la impresión de quien lo programó.

## Golden set

`eval/preguntas.jsonl`, una pregunta por línea:

```json
{"pregunta": "...", "id_esperado": "documento#art-47", "en_corpus": true,
 "tipo": "literal", "respuesta_esperada": "..."}
```

Formato exacto en `docs/ARQUITECTURA.md`. Se empieza con 20 preguntas (IA-001)
y el objetivo es llegar a **40–60**, construidas entre el docente (sabe qué se
pregunta de verdad en secretaría) y los estudiantes (saben qué dudas tienen).

Debe incluir los cuatro tipos a propósito:

| tipo | qué mide |
|---|---|
| `literal` | la pregunta usa las palabras del reglamento |
| `coloquial` | "¿me van a echar de la carrera?" — no comparte vocabulario con el texto |
| `multi-articulo` | la respuesta exige cruzar dos artículos |
| `fuera-de-corpus` | **el sistema debe rechazarla**; mide el guardrail |

Sin preguntas fuera de corpus no se mide lo más peligroso del sistema: que
invente.

## Cómo se ejecuta

Desde la raíz del repositorio, con las dependencias instaladas y
`DATABASE_URL` y `EMBEDDINGS_API_KEY` configuradas en el entorno:

```bash
python -m eval.recall
python -m eval.recall --fallos
```

El script `eval/recall.py` compara los tres modos y muestra los aciertos, el
total y el porcentaje global y por tipo. `--fallos` añade cada pregunta
fallada, su id esperado y los ids recuperados. Cada corrida se registra en
`historial/evaluaciones/` con su fecha y qué se cambió.

Solo cuentan las preguntas con `en_corpus: true`. En el golden set actual son
15: 5 literales, 7 coloquiales y 3 de varios artículos. Las otras 5 preguntas
no cuentan en los denominadores ni se envían a la búsqueda en esta medición.
Para `multi-articulo` se comprueba el artículo principal de `id_esperado`;
acertarlo no garantiza recuperar todos los artículos necesarios para responder.

## Métricas

| Métrica | Qué mide | Cómo |
|---|---|---|
| `recall@5` | ¿el artículo correcto está entre los 5 recuperados? | automático |
| Rechazo correcto | ¿dice "no sé" cuando debe? | automático, sobre fuera-de-corpus |
| Cobertura | ¿responde cuando sí puede? | automático, sobre en-corpus |
| Fundamentación | ¿toda afirmación tiene cita válida? | **manual**, 30 respuestas |
| Latencia p50/p95 | usabilidad real | automático |

`recall@5` es el techo del sistema: si el artículo correcto no se recupera, el
modelo no puede responder bien por muy buen prompt que tenga. Se mide primero.

La fundamentación se revisa a mano: abrir el PDF y comprobar que la cita
**existe literalmente**. Que suene bien no basta.

## Experimento comparativo

El resultado más presentable del proyecto. Mismo golden set, tres modos:

| modo | recall@5 | fecha |
|---|---|---|
| bm25 | 11/15 (73.3%) | 2026-11-16 |
| vectorial | 13/15 (86.7%) | 2026-11-16 |
| híbrido | 13/15 (86.7%) | 2026-11-16 |

La hipótesis es que el híbrido gana, y que BM25 gana al vectorial en las
preguntas `literal` mientras pierde en las `coloquial`. Si los datos dicen otra
cosa, **se escribe lo que digan los datos** y se revisa el diseño.

En la medición del 2026-11-16, vectorial e híbrida empatan: ambos aciertan
5/5 literales, 5/7 coloquiales y 3/3 de varios artículos. BM25 acierta
5/5, 3/7 y 3/3 respectivamente. No se confirma que la híbrida gane ni que
BM25 supere a la vectorial en las literales; en estas últimas hay un empate.

Con ese resultado se propone conservar `hibrida`, que mantiene la interfaz
actual y `puntaje_vectorial` para IA-016. La muestra es pequeña: una pregunta
representa 6.7 puntos porcentuales del recall global. La decisión se revisará
cuando crezca el golden set.

Resultados, salidas y análisis en la
[evaluación fechada](../historial/evaluaciones/2026-11-16-comparativa-busqueda.md).
Justificación de la elección en el
[ADR-010](../historial/decisiones/ADR-010-modo-de-busqueda.md).

## Historial de mediciones

Cada corrida, con la fecha y **qué se cambió**, va en
`historial/evaluaciones/AAAA-MM-DD-<cambio>.md`. Una medición sin contexto no
sirve para comparar.

## Análisis de errores

Más valioso que la media. Para cada fallo: qué se preguntó, qué se recuperó, qué
se respondió y **por qué falló** (troceado, recuperación, prompt o umbral). Los
patrones que salgan de aquí son lo que se corrige en la siguiente iteración.
