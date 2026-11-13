# Índice de tareas

Todas las tareas del proyecto con sus dependencias y su **fecha límite**. El
estado y el responsable se llevan en el tablero "Normativa UAB" de GitHub
Projects, no aquí. Flujo completo en `backlog/README.md`.

El **2026-11-04** se juntaron las 44 tareas que nadie había tomado en 18, para
llegar a la presentación del **19 de noviembre** con todo cerrado el 18
(ADR-005). La columna *Absorbe* dice qué tareas antiguas contiene cada una; sus
issues están cerrados y enlazan a la tarea nueva.

**Camino crítico** (si una se retrasa, se retrasa la demo): INV-004 → IA-002 →
IA-008 → IA-007 → IA-016 → BE-003 → BE-007 → INV-011. Las marcadas con ⚙ son de
configuración o despliegue y las hace el docente, porque usan sus cuentas.

## Ya tomadas antes de la reorganización

No cambian. Solo se les pone fecha límite.

| ID | Tarea | Área | Fecha límite | Issue |
|---|---|---|---|---|
| [SET-001](tareas/SET-001.md) | Guía de entorno para macOS y Linux | SET | hecha | [#1](https://github.com/mcondoriuab/normativa-uab/issues/1) |
| [SET-002](tareas/SET-002.md) | Primer pull request: añadirse al equipo (todos) | SET | hecha | [#2](https://github.com/mcondoriuab/normativa-uab/issues/2) |
| [SET-003](tareas/SET-003.md) | Guía de entorno para Windows | SET | hecha | [#3](https://github.com/mcondoriuab/normativa-uab/issues/3) |
| [SET-004](tareas/SET-004.md) | Guía de git para el equipo | SET | hecha | [#4](https://github.com/mcondoriuab/normativa-uab/issues/4) |
| [INV-001](tareas/INV-001.md) | Qué es un LLM, un token y por qué alucina | INV | hecha | [#5](https://github.com/mcondoriuab/normativa-uab/issues/5) |
| [BE-001](tareas/BE-001.md) | API mínima con `/salud` | BE | hecha | [#21](https://github.com/mcondoriuab/normativa-uab/issues/21) |
| [INV-003](tareas/INV-003.md) | Elegir licencia del proyecto | INV | hecha | [#6](https://github.com/mcondoriuab/normativa-uab/issues/6) |
| [INV-012](tareas/INV-012.md) | Experimento: cazar alucinaciones en chatbots | INV | 2026-11-07 | [#7](https://github.com/mcondoriuab/normativa-uab/issues/7) |
| [INV-013](tareas/INV-013.md) | RAG a mano: con y sin los artículos | INV | 2026-11-07 | [#8](https://github.com/mcondoriuab/normativa-uab/issues/8) |
| [INV-015](tareas/INV-015.md) | Mapa de actores y fuentes de la normativa | INV | 2026-11-07 | [#10](https://github.com/mcondoriuab/normativa-uab/issues/10) |

## Semana 1: del 4 al 10 de noviembre

| ID | Tarea | Área | Tamaño | Depende de | Fecha límite | Absorbe | Issue |
|---|---|---|---|---|---|---|---|
| [INV-004](tareas/INV-004.md) | Corpus de la carrera: reunir, inventariar y registrar los PDF | INV | L | — | hecha | INV-016, INV-005 | [#16](https://github.com/mcondoriuab/normativa-uab/issues/16) |
| [FE-001](tareas/FE-001.md) | Página estática: maqueta HTML y estilos responsive | FE | M | — | hecha | FE-002 | [#24](https://github.com/mcondoriuab/normativa-uab/issues/24) |
| [IA-001](tareas/IA-001.md) | Golden set a partir de preguntas reales | IA | L | INV-004 | 2026-11-09 | INV-007 | [#20](https://github.com/mcondoriuab/normativa-uab/issues/20) |
| [BE-002](tareas/BE-002.md) | `/preguntar` simulado y la web servida desde la API | BE | M | BE-001, FE-001 | 2026-11-09 | BE-005 | [#22](https://github.com/mcondoriuab/normativa-uab/issues/22) |
| [IA-002](tareas/IA-002.md) | Ingesta: de los PDF a fragmentos revisados | IA | L | INV-004 | 2026-11-10 | INV-006, IA-003, IA-004, IA-005, IA-006 | [#26](https://github.com/mcondoriuab/normativa-uab/issues/26) |
| [BE-006](tareas/BE-006.md) ⚙ | Primer despliegue en Render | BE | M | BE-001 | hecha | — | [#23](https://github.com/mcondoriuab/normativa-uab/issues/23) |
| [BE-008](tareas/BE-008.md) ⚙ | Supabase: esquema, `ia/db.py` y mantener la base activa | BE | L | BE-006, BE-001 (Parte 2) | 2026-11-10 | BE-009 | [#31](https://github.com/mcondoriuab/normativa-uab/issues/31) |

## Semana 2: del 11 al 18 de noviembre

| ID | Tarea | Área | Tamaño | Depende de | Fecha límite | Absorbe | Issue |
|---|---|---|---|---|---|---|---|
| [INV-009](tareas/INV-009.md) | Embeddings: experimento y elección del modelo | INV | L | IA-001, IA-002 | 2026-11-11 | INV-008 | [#35](https://github.com/mcondoriuab/normativa-uab/issues/35) |
| [INV-002](tareas/INV-002.md) | Estado del arte y por qué RAG | INV | L | INV-001, INV-012, INV-013 | 2026-11-12 | INV-014 | [#11](https://github.com/mcondoriuab/normativa-uab/issues/11) |
| [INV-010](tareas/INV-010.md) | LLM: elegir proveedor, capa `llm.py` y prompt del sistema | INV | L | INV-001 | 2026-11-12 | IA-014, IA-015 | [#47](https://github.com/mcondoriuab/normativa-uab/issues/47) |
| [FE-003](tareas/FE-003.md) | Interfaz completa: respuesta, citas, estados y accesibilidad | FE | L | BE-002 | 2026-11-13 | FE-004, FE-005, FE-006 | [#33](https://github.com/mcondoriuab/normativa-uab/issues/33) |
| [IA-008](tareas/IA-008.md) | Búsqueda vectorial: indexar en Supabase y buscar con pgvector | IA | L | INV-009, BE-008, IA-002 | 2026-11-13 | IA-009 | [#37](https://github.com/mcondoriuab/normativa-uab/issues/37) |
| [IA-007](tareas/IA-007.md) | Búsqueda BM25, búsqueda híbrida y comando `buscar` | IA | L | IA-002, IA-008 | 2026-11-14 | IA-010, IA-011 | [#36](https://github.com/mcondoriuab/normativa-uab/issues/36) |
| [IA-012](tareas/IA-012.md) | Medir recall@5 y elegir el modo de búsqueda | IA | L | IA-001, IA-007 | 2026-11-15 | IA-013 | [#41](https://github.com/mcondoriuab/normativa-uab/issues/41) |
| [IA-016](tareas/IA-016.md) | `responder()` con citas y umbral de rechazo calibrado | IA | L | IA-007, INV-010, IA-001 | 2026-11-15 | IA-017 | [#50](https://github.com/mcondoriuab/normativa-uab/issues/50) |
| [BE-003](tareas/BE-003.md) | Motor real en la API: carga al arrancar y registro anónimo | BE | L | BE-002, BE-008, IA-016 | 2026-11-16 | BE-004, BE-010 | [#53](https://github.com/mcondoriuab/normativa-uab/issues/53) |
| [BE-007](tareas/BE-007.md) ⚙ | Despliegue del MVP completo | BE | M | BE-003, BE-008, IA-008 | 2026-11-17 | — | [#56](https://github.com/mcondoriuab/normativa-uab/issues/56) |
| [INV-011](tareas/INV-011.md) | Evaluación final, informe y demo del MVP | INV | L | IA-012, IA-016, FE-003, BE-007 | 2026-11-18 | IA-018 | [#57](https://github.com/mcondoriuab/normativa-uab/issues/57) |

## Números de ADR reservados

Varias tareas escriben un ADR a la vez. Para que no choquen, cada una tiene su
número:

| ADR | Tema | Tarea |
|---|---|---|
| ADR-005 | Reorganización del backlog para la presentación | — |
| ADR-006 | Licencia del proyecto | INV-003 |
| ADR-007 | Enfoque RAG | INV-002 |
| ADR-008 | Modelo de embeddings | INV-009 |
| ADR-009 | Proveedor de LLM | INV-010 |
| ADR-010 | Modo de búsqueda | IA-012 |
