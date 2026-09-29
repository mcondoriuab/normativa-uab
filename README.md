# Asistente de Normativa UAB

Proyecto de la Sociedad Estudiantil de Investigación de Ingeniería de Sistemas
(SE.ING - UAB). Objetivo: que cualquier estudiante pueda preguntar en lenguaje
natural sobre la normativa de su carrera y obtenga una respuesta **con la cita
textual del artículo** del que sale.

Este repositorio es, ante todo, **el histórico del trabajo del equipo**: qué se
investigó, qué se decidió, qué se construyó, qué falló y qué se aprendió. El
código se va construyendo tarea a tarea, desde cero.

> **Aviso:** herramienta de apoyo. El texto oficial y vinculante es el documento
> publicado por la universidad.

## Estado actual

**Fase 0 — Arranque.** Todavía no hay código. El primer MVP responde preguntas
sobre la normativa de **una sola carrera** (Ingeniería de Sistemas). Ver
[`docs/VISION.md`](docs/VISION.md).

## Quiero empezar a trabajar

1. Lee [`docs/VISION.md`](docs/VISION.md) (5 min) y
   [`docs/ARQUITECTURA.md`](docs/ARQUITECTURA.md) (10 min).
2. Abre el tablero **Normativa UAB** en GitHub Projects (pestaña *Projects* del
   repositorio) y elige un issue en la columna *Disponible*.
3. Sigue el flujo de [`CONTRIBUTING.md`](CONTRIBUTING.md).
4. Si trabajas con un asistente de IA, pídele que lea primero
   [`AGENTS.md`](AGENTS.md) y el archivo de la tarea.

Si es tu primera vez, empieza por **SET-001** y **SET-002**.

## Mapa del repositorio

Las carpetas de código (`ia/`, `apps/`, `eval/`, `corpus/`, `db/`) se suben
cuando empiezan las fases que las usan.

| Carpeta | Qué contiene |
|---|---|
| `backlog/` | Especificación de cada tarea (el estado se lleva en GitHub Projects) |
| `historial/` | Bitácora de sesiones, decisiones (ADR) y resultados de evaluación |
| `investigacion/` | Informes de las tareas de investigación (INV) |
| `docs/` | Visión, arquitectura, glosario, corpus, evaluación y ética |
| `corpus/` | Normativa de cada carrera (los PDF no se suben a git) |
| `ia/` | Ingesta, índice, búsqueda y generación |
| `apps/api/` | API HTTP (FastAPI) |
| `apps/web/` | Interfaz web (HTML, CSS y JS sin framework) |
| `eval/` | Golden set y script de métricas |
| `db/` | Migraciones SQL de la base de datos (Supabase) |

## Despliegue

La web y la API se despliegan en **Render** y la base de datos vive en
**Supabase**, ambos en plan gratuito y manejables desde Claude Code con sus
conectores. URL pública: _(pendiente, tarea BE-006)_. Detalle en
[`docs/DESPLIEGUE.md`](docs/DESPLIEGUE.md).

## Documentación

- [`docs/VISION.md`](docs/VISION.md): qué problema resolvemos y qué entra en el MVP
- [`docs/ARQUITECTURA.md`](docs/ARQUITECTURA.md): cómo encajan las piezas y los contratos entre ellas
- [`docs/GLOSARIO.md`](docs/GLOSARIO.md): vocabulario de IA que usamos
- [`docs/CORPUS.md`](docs/CORPUS.md): qué documentos, de qué versión y con qué permiso
- [`docs/EVALUACION.md`](docs/EVALUACION.md): cómo medimos si funciona
- [`docs/ETICA.md`](docs/ETICA.md): privacidad, sesgos y aviso legal
- [`docs/DESPLIEGUE.md`](docs/DESPLIEGUE.md): Render, Supabase, secretos y conectores

El documento formal del proyecto ante la Sociedad (alcance, firmas) está en la
carpeta de proyectos de Drive. El día a día se registra aquí, en `historial/`.
