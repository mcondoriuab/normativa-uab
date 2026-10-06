# ia/

El "motor" del asistente: ingesta, índice, búsqueda y generación. Todo en
Python, un archivo por responsabilidad. Hoy está vacío; lo llenan las tareas
`IA-*`.

| Archivo | Qué hace | Tarea |
|---|---|---|
| `extraer.py` | PDF → texto por página | IA-002 |
| `trocear.py` | Texto → fragmentos por artículo o por longitud | IA-003, IA-004 |
| `ingestar.py` | CLI: carpeta de PDFs → `data/fragmentos.json` | IA-005 |
| `bm25.py` | Búsqueda por palabras | IA-007 |
| `db.py` | Conexión a Supabase y lectura de fragmentos | BE-008 |
| `embeddings.py` | Embeddings por API (documentos y preguntas) | IA-008 |
| `indexar.py` | Fragmentos → embeddings por API → tabla `fragmentos` | IA-008 |
| `vectorial.py` | Búsqueda por embeddings con pgvector | IA-009 |
| `hibrida.py` | Fusión RRF de ambas búsquedas | IA-010 |
| `buscar.py` | CLI de búsqueda, sin LLM | IA-011 |
| `llm.py` | Capa que aísla qué modelo de lenguaje se usa | IA-014 |
| `prompts.py` | Prompt del sistema | IA-015 |
| `responder.py` | Pregunta → respuesta con citas (o rechazo) | IA-016, IA-017 |

Se ejecuta desde la raíz del repo: `python -m ia.ingestar corpus/ingenieria-sistemas`.
Formatos de datos: `docs/ARQUITECTURA.md`.
