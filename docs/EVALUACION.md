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

El script de métricas se construye en la tarea IA-012 (`eval/recall.py`). Cada
corrida se registra en `historial/evaluaciones/` con su fecha y qué se cambió.

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
| bm25 | _(pendiente)_ | |
| vectorial | _(pendiente)_ | |
| híbrido | _(pendiente)_ | |

La hipótesis es que el híbrido gana, y que BM25 gana al vectorial en las
preguntas `literal` mientras pierde en las `coloquial`. Si los datos dicen otra
cosa, **se escribe lo que digan los datos** y se revisa el diseño.

## Historial de mediciones

Cada corrida, con la fecha y **qué se cambió**, va en
`historial/evaluaciones/AAAA-MM-DD-<cambio>.md`. Una medición sin contexto no
sirve para comparar.

## Análisis de errores

Más valioso que la media. Para cada fallo: qué se preguntó, qué se recuperó, qué
se respondió y **por qué falló** (troceado, recuperación, prompt o umbral). Los
patrones que salgan de aquí son lo que se corrige en la siguiente iteración.
