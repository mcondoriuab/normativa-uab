# eval/

Cómo sabemos si el sistema funciona. Metodología en `docs/EVALUACION.md`.

| Archivo | Qué es | Tarea |
|---|---|---|
| `preguntas.jsonl` | Golden set: preguntas con su artículo correcto | IA-001 |
| `recall.py` | Calcula recall@5 por modo de búsqueda | IA-012 |

Los resultados de cada corrida **no** se guardan aquí, sino en
`historial/evaluaciones/`.
