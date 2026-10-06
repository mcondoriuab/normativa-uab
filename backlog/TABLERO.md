# Índice de tareas

Todas las tareas del proyecto con sus dependencias. **El estado y el
responsable se llevan en el tablero "Normativa UAB" de GitHub Projects**, no
aquí. Cada tarea tiene su issue; las de fases futuras están en la columna
*Backlog*. Flujo completo en `backlog/README.md`.

## F0: Arranque

| ID | Tarea | Área | Tamaño | Depende de | Issue |
|---|---|---|---|---|---|
| [SET-001](tareas/SET-001.md) | Guía de entorno para macOS y Linux | SET | S | — | [#1](https://github.com/mcondoriuab/normativa-uab/issues/1) |
| [SET-002](tareas/SET-002.md) | Primer pull request: añadirse al equipo (todos) | SET | S | — | [#2](https://github.com/mcondoriuab/normativa-uab/issues/2) |
| [SET-003](tareas/SET-003.md) | Guía de entorno para Windows | SET | S | — | [#3](https://github.com/mcondoriuab/normativa-uab/issues/3) |
| [SET-004](tareas/SET-004.md) | Guía de git para el equipo | SET | S | — | [#4](https://github.com/mcondoriuab/normativa-uab/issues/4) |
| [INV-001](tareas/INV-001.md) | Qué es un LLM, un token y por qué alucina | INV | S | — | [#5](https://github.com/mcondoriuab/normativa-uab/issues/5) |
| [INV-012](tareas/INV-012.md) | Experimento: cazar alucinaciones en chatbots | INV | S | — | [#7](https://github.com/mcondoriuab/normativa-uab/issues/7) |
| [INV-013](tareas/INV-013.md) | RAG a mano: con y sin los artículos | INV | S | — | [#8](https://github.com/mcondoriuab/normativa-uab/issues/8) |
| [INV-014](tareas/INV-014.md) | Estado del arte: asistentes de normativa universitaria | INV | M | — | [#9](https://github.com/mcondoriuab/normativa-uab/issues/9) |
| [INV-015](tareas/INV-015.md) | Mapa de actores y fuentes de la normativa | INV | S | — | [#10](https://github.com/mcondoriuab/normativa-uab/issues/10) |
| [INV-003](tareas/INV-003.md) | Elegir licencia del proyecto | INV | S | — | [#6](https://github.com/mcondoriuab/normativa-uab/issues/6) |
| [INV-002](tareas/INV-002.md) | "Entrenar" vs fine-tuning vs RAG | INV | M | INV-001, INV-012, INV-013 | [#11](https://github.com/mcondoriuab/normativa-uab/issues/11) |

## F1: Corpus de la carrera, API desplegada y web vacía

| ID | Tarea | Área | Tamaño | Depende de | Issue |
|---|---|---|---|---|---|
| [INV-016](tareas/INV-016.md) | Reunir en Drive la normativa que ya tiene el equipo | INV | S | — | [#15](https://github.com/mcondoriuab/normativa-uab/issues/15) |
| [INV-004](tareas/INV-004.md) | Inventario de la normativa de la carrera | INV | M | — | [#16](https://github.com/mcondoriuab/normativa-uab/issues/16) |
| [INV-005](tareas/INV-005.md) | Reunir y registrar los PDF | INV | S | INV-004, INV-016 | [#17](https://github.com/mcondoriuab/normativa-uab/issues/17) |
| [INV-006](tareas/INV-006.md) | Analizar la estructura de los PDF | INV | M | INV-005 | [#18](https://github.com/mcondoriuab/normativa-uab/issues/18) |
| [INV-007](tareas/INV-007.md) | Recoger preguntas reales de estudiantes | INV | M | — | [#19](https://github.com/mcondoriuab/normativa-uab/issues/19) |
| [IA-001](tareas/IA-001.md) | Golden set v0 | IA | M | INV-005, INV-007 | [#20](https://github.com/mcondoriuab/normativa-uab/issues/20) |
| [BE-001](tareas/BE-001.md) | API mínima con `/salud` | BE | S | SET-001 | [#21](https://github.com/mcondoriuab/normativa-uab/issues/21) |
| [BE-002](tareas/BE-002.md) | `/preguntar` con respuesta simulada | BE | S | BE-001 | [#22](https://github.com/mcondoriuab/normativa-uab/issues/22) |
| [BE-006](tareas/BE-006.md) | Primer despliegue en Render | BE | M | BE-001 | [#23](https://github.com/mcondoriuab/normativa-uab/issues/23) |
| [FE-001](tareas/FE-001.md) | Maqueta HTML de la página | FE | S | — | [#24](https://github.com/mcondoriuab/normativa-uab/issues/24) |
| [FE-002](tareas/FE-002.md) | Estilos responsive | FE | S | FE-001 | [#25](https://github.com/mcondoriuab/normativa-uab/issues/25) |

## F2: Ingesta

| ID | Tarea | Área | Tamaño | Depende de | Issue |
|---|---|---|---|---|---|
| [IA-002](tareas/IA-002.md) | Extraer texto de un PDF por página | IA | S | SET-001, INV-005 | [#26](https://github.com/mcondoriuab/normativa-uab/issues/26) |
| [IA-003](tareas/IA-003.md) | Trocear por artículos con regex | IA | M | IA-002, INV-006 | [#27](https://github.com/mcondoriuab/normativa-uab/issues/27) |
| [IA-004](tareas/IA-004.md) | Troceado de respaldo por longitud | IA | S | IA-003 | [#28](https://github.com/mcondoriuab/normativa-uab/issues/28) |
| [IA-005](tareas/IA-005.md) | Comando `ingestar` | IA | S | IA-004 | [#29](https://github.com/mcondoriuab/normativa-uab/issues/29) |
| [IA-006](tareas/IA-006.md) | Revisión manual de fragmentos | IA | S | IA-005 | [#30](https://github.com/mcondoriuab/normativa-uab/issues/30) |
| [BE-008](tareas/BE-008.md) | Esquema inicial de la base de datos | BE | M | SET-001 | [#31](https://github.com/mcondoriuab/normativa-uab/issues/31) |
| [BE-005](tareas/BE-005.md) | Servir la web desde la API | BE | S | BE-002, FE-001 | [#32](https://github.com/mcondoriuab/normativa-uab/issues/32) |
| [FE-003](tareas/FE-003.md) | Enviar la pregunta y mostrar la respuesta | FE | M | BE-005 | [#33](https://github.com/mcondoriuab/normativa-uab/issues/33) |

## F3: Búsqueda

| ID | Tarea | Área | Tamaño | Depende de | Issue |
|---|---|---|---|---|---|
| [INV-008](tareas/INV-008.md) | Experimento: embeddings y similitud coseno | INV | M | SET-001 | [#34](https://github.com/mcondoriuab/normativa-uab/issues/34) |
| [INV-009](tareas/INV-009.md) | Elegir el modelo de embeddings | INV | M | INV-008, IA-005, IA-001 | [#35](https://github.com/mcondoriuab/normativa-uab/issues/35) |
| [IA-007](tareas/IA-007.md) | Búsqueda BM25 | IA | M | IA-005 | [#36](https://github.com/mcondoriuab/normativa-uab/issues/36) |
| [IA-008](tareas/IA-008.md) | Indexar embeddings en Supabase | IA | M | INV-009, BE-008, IA-005 | [#37](https://github.com/mcondoriuab/normativa-uab/issues/37) |
| [IA-009](tareas/IA-009.md) | Búsqueda vectorial con pgvector | IA | S | IA-008 | [#38](https://github.com/mcondoriuab/normativa-uab/issues/38) |
| [IA-010](tareas/IA-010.md) | Búsqueda híbrida con RRF | IA | S | IA-007, IA-009 | [#39](https://github.com/mcondoriuab/normativa-uab/issues/39) |
| [IA-011](tareas/IA-011.md) | Comando `buscar` | IA | S | IA-010 | [#40](https://github.com/mcondoriuab/normativa-uab/issues/40) |
| [IA-012](tareas/IA-012.md) | Script de recall@5 | IA | M | IA-001, IA-010 | [#41](https://github.com/mcondoriuab/normativa-uab/issues/41) |
| [IA-013](tareas/IA-013.md) | Experimento: BM25 vs vectorial vs híbrida | IA | M | IA-012, IA-006 | [#42](https://github.com/mcondoriuab/normativa-uab/issues/42) |
| [BE-009](tareas/BE-009.md) | Evitar que Supabase se pause | BE | S | BE-006, BE-008 | [#43](https://github.com/mcondoriuab/normativa-uab/issues/43) |
| [FE-004](tareas/FE-004.md) | Citas desplegables | FE | S | FE-003 | [#44](https://github.com/mcondoriuab/normativa-uab/issues/44) |
| [FE-005](tareas/FE-005.md) | Estados: cargando, error y rechazo | FE | S | FE-003 | [#45](https://github.com/mcondoriuab/normativa-uab/issues/45) |
| [FE-006](tareas/FE-006.md) | Accesibilidad básica | FE | S | FE-004, FE-005 | [#46](https://github.com/mcondoriuab/normativa-uab/issues/46) |

## F4: Generación

| ID | Tarea | Área | Tamaño | Depende de | Issue |
|---|---|---|---|---|---|
| [INV-010](tareas/INV-010.md) | Comparar proveedores de LLM | INV | M | INV-001 | [#47](https://github.com/mcondoriuab/normativa-uab/issues/47) |
| [IA-014](tareas/IA-014.md) | Capa `llm.py` | IA | S | INV-010 | [#48](https://github.com/mcondoriuab/normativa-uab/issues/48) |
| [IA-015](tareas/IA-015.md) | Prompt del sistema v1 | IA | S | IA-014, INV-002 | [#49](https://github.com/mcondoriuab/normativa-uab/issues/49) |
| [IA-016](tareas/IA-016.md) | Función `responder()` con citas | IA | M | IA-011, IA-015 | [#50](https://github.com/mcondoriuab/normativa-uab/issues/50) |
| [IA-017](tareas/IA-017.md) | Umbral de rechazo calibrado | IA | M | IA-016, IA-012 | [#51](https://github.com/mcondoriuab/normativa-uab/issues/51) |
| [IA-018](tareas/IA-018.md) | Caza-alucinaciones | IA | M | IA-017 | [#52](https://github.com/mcondoriuab/normativa-uab/issues/52) |
| [BE-003](tareas/BE-003.md) | Conectar `/preguntar` al motor real | BE | S | BE-002, IA-016 | [#53](https://github.com/mcondoriuab/normativa-uab/issues/53) |
| [BE-004](tareas/BE-004.md) | Cargar el índice una sola vez | BE | S | BE-003 | [#54](https://github.com/mcondoriuab/normativa-uab/issues/54) |
| [BE-010](tareas/BE-010.md) | Registro anónimo de consultas | BE | S | BE-003, BE-008 | [#55](https://github.com/mcondoriuab/normativa-uab/issues/55) |

## F5: Cierre del MVP

| ID | Tarea | Área | Tamaño | Depende de | Issue |
|---|---|---|---|---|---|
| [BE-007](tareas/BE-007.md) | Despliegue del MVP completo | BE | M | BE-004, BE-005, BE-009, BE-010, IA-017 | [#56](https://github.com/mcondoriuab/normativa-uab/issues/56) |
| [INV-011](tareas/INV-011.md) | Demo e informe del MVP | INV | M | IA-013, IA-018, BE-007, FE-006 | [#57](https://github.com/mcondoriuab/normativa-uab/issues/57) |
