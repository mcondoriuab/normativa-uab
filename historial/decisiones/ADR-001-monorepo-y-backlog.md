# ADR-001: Monorepo histórico, construcción desde cero y backlog en Markdown

**Estado:** aceptada (el punto 4 lo modifica ADR-003) · **Fecha:** 2026-09-29 · **Tarea:** —

## Contexto

Antes de empezar con el equipo, el docente tenía un prototipo casi completo del
asistente (ingesta, búsqueda híbrida, generación con citas, API y web). El
proyecto tiene dos objetivos de igual peso: un producto funcional y que los
estudiantes aprendan IA aplicada con el proceso documentado.

Entregar el prototipo hecho habría dado el producto, pero se habría perdido el
aprendizaje: los estudiantes habrían mantenido código que no escribieron ni
entienden.

## Decisión

1. **Se descarta el prototipo.** El código se construye desde cero, en tareas
   pequeñas que toma el equipo.
2. **Un solo repositorio (monorepo)** con todo: backlog, historial,
   investigación, documentación, motor de IA (`ia/`), API (`apps/api/`) y web
   (`apps/web/`).
3. **El repositorio es el histórico del trabajo**, no solo el código: la
   bitácora de sesiones, las decisiones y las evaluaciones viven en
   `historial/`.
4. **El backlog vive en Markdown** (`backlog/`), un archivo por tarea, escrito
   para que lo pueda seguir un estudiante o un asistente de IA sin contexto
   extra.
5. **Frontend sin framework** (HTML, CSS y JS), servido por la API.

## Por qué

- Construir cada pieza es el aprendizaje. Lo que valía del prototipo (el diseño)
  se conserva como pistas dentro de las tareas y como contratos en
  `docs/ARQUITECTURA.md`.
- Un monorepo evita que un equipo pequeño tenga que coordinar versiones entre
  repositorios.
- El backlog en Markdown no depende de ninguna herramienta externa, queda
  versionado junto al código y se puede migrar después a GitHub Issues.
- Sin npm, el equipo no pierde las primeras semanas peleando con herramientas
  de frontend.

## Alternativas descartadas

| Alternativa | Por qué no |
|---|---|
| Mantener el prototipo y extenderlo | Más rápido, pero el equipo no entendería el mecanismo |
| Guardar el prototipo en una rama de referencia | Tienta a copiar la solución en vez de construirla |
| Backlog en GitHub Issues / Jira | Otra herramienta que aprender; se puede migrar más adelante |
| React + Vite | Exige Node y npm desde la semana 1 |

## Consecuencias

- El MVP tardará más que si se hubiera entregado el prototipo.
- El orden de las tareas importa: `backlog/TABLERO.md` registra las
  dependencias.
- Revisar esta decisión si el backlog en Markdown genera conflictos frecuentes
  al editar `TABLERO.md` a la vez: entonces migrar a GitHub Issues + Projects.
