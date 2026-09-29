# Índice de tareas

Todas las tareas del proyecto con sus dependencias. **El estado y el
responsable se llevan en el tablero "Normativa UAB" de GitHub Projects**, no
aquí. Los issues se crean fase a fase. Flujo completo en `backlog/README.md`.

## F0: Arranque

| ID | Tarea | Área | Tamaño | Depende de | Issue |
|---|---|---|---|---|---|
| [SET-001](tareas/SET-001.md) | Guía de entorno para macOS y Linux | SET | S | — | — |
| [SET-002](tareas/SET-002.md) | Primer pull request: añadirse al equipo (todos) | SET | S | — | — |
| [SET-003](tareas/SET-003.md) | Guía de entorno para Windows | SET | S | — | — |
| [SET-004](tareas/SET-004.md) | Guía de git para el equipo | SET | S | — | — |
| [INV-001](tareas/INV-001.md) | Qué es un LLM, un token y por qué alucina | INV | S | — | — |
| [INV-012](tareas/INV-012.md) | Experimento: cazar alucinaciones en chatbots | INV | S | — | — |
| [INV-013](tareas/INV-013.md) | RAG a mano: con y sin los artículos | INV | S | — | — |
| [INV-014](tareas/INV-014.md) | Estado del arte: asistentes de normativa universitaria | INV | M | — | — |
| [INV-015](tareas/INV-015.md) | Mapa de actores y fuentes de la normativa | INV | S | — | — |
| [INV-003](tareas/INV-003.md) | Elegir licencia del proyecto | INV | S | — | — |
| [INV-002](tareas/INV-002.md) | "Entrenar" vs fine-tuning vs RAG | INV | M | INV-001, INV-012, INV-013 | — |

## F1: Corpus de la carrera, API desplegada y web vacía

| ID | Tarea | Área | Tamaño | Depende de | Issue |
|---|---|---|---|---|---|
| [INV-004](tareas/INV-004.md) | Inventario de la normativa de la carrera | INV | M | — | — |
| [INV-005](tareas/INV-005.md) | Reunir y registrar los PDF | INV | S | INV-004 | — |
| [INV-006](tareas/INV-006.md) | Analizar la estructura de los PDF | INV | M | INV-005 | — |
| [INV-007](tareas/INV-007.md) | Recoger preguntas reales de estudiantes | INV | M | — | — |
| [IA-001](tareas/IA-001.md) | Golden set v0 | IA | M | INV-005, INV-007 | — |
| [BE-001](tareas/BE-001.md) | API mínima con `/salud` | BE | S | SET-001 | — |
| [BE-002](tareas/BE-002.md) | `/preguntar` con respuesta simulada | BE | S | BE-001 | — |
| [BE-006](tareas/BE-006.md) | Primer despliegue en Render | BE | M | BE-001 | — |
| [FE-001](tareas/FE-001.md) | Maqueta HTML de la página | FE | S | — | — |
| [FE-002](tareas/FE-002.md) | Estilos responsive | FE | S | FE-001 | — |

## F2: Ingesta

| ID | Tarea | Área | Tamaño | Depende de | Issue |
|---|---|---|---|---|---|
| [IA-002](tareas/IA-002.md) | Extraer texto de un PDF por página | IA | S | SET-001, INV-005 | — |
| [IA-003](tareas/IA-003.md) | Trocear por artículos con regex | IA | M | IA-002, INV-006 | — |
| [IA-004](tareas/IA-004.md) | Troceado de respaldo por longitud | IA | S | IA-003 | — |
| [IA-005](tareas/IA-005.md) | Comando `ingestar` | IA | S | IA-004 | — |
| [IA-006](tareas/IA-006.md) | Revisión manual de fragmentos | IA | S | IA-005 | — |
| [BE-008](tareas/BE-008.md) | Esquema inicial de la base de datos | BE | M | SET-001 | — |
| [BE-005](tareas/BE-005.md) | Servir la web desde la API | BE | S | BE-002, FE-001 | — |
| [FE-003](tareas/FE-003.md) | Enviar la pregunta y mostrar la respuesta | FE | M | BE-005 | — |

## F3: Búsqueda

| ID | Tarea | Área | Tamaño | Depende de | Issue |
|---|---|---|---|---|---|
| [INV-008](tareas/INV-008.md) | Experimento: embeddings y similitud coseno | INV | M | SET-001 | — |
| [INV-009](tareas/INV-009.md) | Elegir el modelo de embeddings | INV | M | INV-008, IA-005, IA-001 | — |
| [IA-007](tareas/IA-007.md) | Búsqueda BM25 | IA | M | IA-005 | — |
| [IA-008](tareas/IA-008.md) | Indexar embeddings en Supabase | IA | M | INV-009, BE-008, IA-005 | — |
| [IA-009](tareas/IA-009.md) | Búsqueda vectorial con pgvector | IA | S | IA-008 | — |
| [IA-010](tareas/IA-010.md) | Búsqueda híbrida con RRF | IA | S | IA-007, IA-009 | — |
| [IA-011](tareas/IA-011.md) | Comando `buscar` | IA | S | IA-010 | — |
| [IA-012](tareas/IA-012.md) | Script de recall@5 | IA | M | IA-001, IA-010 | — |
| [IA-013](tareas/IA-013.md) | Experimento: BM25 vs vectorial vs híbrida | IA | M | IA-012, IA-006 | — |
| [BE-009](tareas/BE-009.md) | Evitar que Supabase se pause | BE | S | BE-006, BE-008 | — |
| [FE-004](tareas/FE-004.md) | Citas desplegables | FE | S | FE-003 | — |
| [FE-005](tareas/FE-005.md) | Estados: cargando, error y rechazo | FE | S | FE-003 | — |
| [FE-006](tareas/FE-006.md) | Accesibilidad básica | FE | S | FE-004, FE-005 | — |

## F4: Generación

| ID | Tarea | Área | Tamaño | Depende de | Issue |
|---|---|---|---|---|---|
| [INV-010](tareas/INV-010.md) | Comparar proveedores de LLM | INV | M | INV-001 | — |
| [IA-014](tareas/IA-014.md) | Capa `llm.py` | IA | S | INV-010 | — |
| [IA-015](tareas/IA-015.md) | Prompt del sistema v1 | IA | S | IA-014, INV-002 | — |
| [IA-016](tareas/IA-016.md) | Función `responder()` con citas | IA | M | IA-011, IA-015 | — |
| [IA-017](tareas/IA-017.md) | Umbral de rechazo calibrado | IA | M | IA-016, IA-012 | — |
| [IA-018](tareas/IA-018.md) | Caza-alucinaciones | IA | M | IA-017 | — |
| [BE-003](tareas/BE-003.md) | Conectar `/preguntar` al motor real | BE | S | BE-002, IA-016 | — |
| [BE-004](tareas/BE-004.md) | Cargar el índice una sola vez | BE | S | BE-003 | — |
| [BE-010](tareas/BE-010.md) | Registro anónimo de consultas | BE | S | BE-003, BE-008 | — |

## F5: Cierre del MVP

| ID | Tarea | Área | Tamaño | Depende de | Issue |
|---|---|---|---|---|---|
| [BE-007](tareas/BE-007.md) | Despliegue del MVP completo | BE | M | BE-004, BE-005, BE-009, BE-010, IA-017 | — |
| [INV-011](tareas/INV-011.md) | Demo e informe del MVP | INV | M | IA-013, IA-018, BE-007, FE-006 | — |
