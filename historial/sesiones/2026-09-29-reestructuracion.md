# Sesión 2026-09-29: reestructuración del repositorio

**Asistentes:** Miguel Ángel Condori (docente) · **Fase:** 0, preparación

## Qué se trabajó

- Se revisó el prototipo que había preparado el docente y se decidió
  descartarlo para que el equipo construya el sistema desde cero (ADR-001).
- Se reorganizó el repositorio como monorepo e histórico del proyecto:
  `backlog/`, `historial/`, `investigacion/`, `docs/`, `ia/`, `apps/`,
  `corpus/` y `eval/`.
- Se fijaron los contratos entre piezas en `docs/ARQUITECTURA.md`, para que las
  áreas (IA, backend, frontend) puedan avanzar en paralelo.
- Se definió el primer MVP: la normativa de una sola carrera, Ingeniería de
  Sistemas (`docs/VISION.md`).
- Se escribió el backlog inicial en `backlog/`.
- La bitácora pasa de Drive a este repositorio. Drive queda solo para el
  documento formal ante la Sociedad.
- Se decidió que el mismo repositorio es lo que se despliega: web y API en
  Render, base de datos en Supabase, con embeddings por API porque el plan
  gratuito de Render no tiene RAM para un modelo local (ADR-002). Se añadieron
  `docs/DESPLIEGUE.md`, `db/`, `.env.ejemplo` y las tareas BE-008 a BE-010; se
  reescribieron BE-006, BE-007, INV-009 e IA-008 a IA-010.
- El estado de las tareas pasa a GitHub Projects (tablero "Normativa UAB"), con
  un issue por tarea (ADR-003). F0 se dividió en 11 tareas pequeñas para que
  los 5 estudiantes confirmados tengan trabajo en paralelo desde el primer día.

## Decisiones

- [ADR-001](../decisiones/ADR-001-monorepo-y-backlog.md): monorepo histórico,
  construcción desde cero y backlog en Markdown.
- [ADR-002](../decisiones/ADR-002-despliegue-render-supabase.md): despliegue en
  Render + Supabase, con embeddings por API.
- [ADR-003](../decisiones/ADR-003-tablero-github-projects.md): estado de las
  tareas en GitHub Projects; la especificación sigue en Markdown.

## Pendiente fuera del repo

- Gestión con la administración para obtener la normativa completa y el
  permiso de uso (ver `docs/CORPUS.md`).
- Presupuesto para el modelo de lenguaje: sin decidir; lo trata INV-010.
- Cuentas de GitHub, Render, Supabase y del proveedor de embeddings con la
  cuenta institucional (`docs/DESPLIEGUE.md`, sección 1).

## Para la próxima sesión

- [ ] Presentar el proyecto, la visión y el flujo de trabajo al equipo
- [ ] Todos: SET-002 (primer PR)
- [ ] Repartir las tareas disponibles de F0 en el tablero: una por persona
