# ADR-003: Estado de las tareas en GitHub Projects

**Estado:** aceptada; la creación fase a fase, reemplazada por ADR-004 · **Fecha:** 2026-09-29 · **Tarea:** —

## Contexto

ADR-001 puso todo el backlog en Markdown, incluido el estado de cada tarea en
`backlog/TABLERO.md`. El docente quiere además un **seguimiento visual** de
quién hace qué, y el repositorio ya está en GitHub
(`mcondoriuab/normativa-uab`), que ofrece tableros (GitHub Projects) gratis.

## Decisión

- **Estado y responsable** de cada tarea: tablero **"Normativa UAB"** de GitHub
  Projects, con un issue por tarea y columnas *Bloqueada*, *Disponible*,
  *En curso*, *En revisión* y *Hecha*.
- **Especificación** de cada tarea: sigue en `backlog/tareas/<ID>.md`,
  versionada con el código. El issue enlaza al archivo, y si difieren, manda
  el archivo.
- `backlog/TABLERO.md` pasa a ser un **índice** (ID, dependencias, issue), sin
  estado.
- Los issues se crean **fase a fase**, empezando por F0, para que el tablero
  muestre solo lo que se puede trabajar pronto.

## Por qué

- Evita llevar el estado en dos sitios, que es la forma más segura de que se
  desincronicen.
- Asignar un issue, moverlo de columna y cerrarlo con `Closes #n` desde el PR es
  justo lo que hace un equipo de desarrollo real: también es aprendizaje.
- La especificación en Markdown sigue siendo legible por cualquier IA sin
  acceso a GitHub y queda en el histórico del repositorio.

## Alternativas descartadas

| Alternativa | Por qué no |
|---|---|
| Solo Markdown (ADR-001) | No hay vista visual ni asignación |
| Especificación completa dentro del issue | Se pierde del histórico versionado y la IA necesitaría acceso a GitHub |
| Crear los 53 issues de golpe | Tablero ruidoso con tareas que tardarán semanas en poder empezarse |

## Consecuencias

- Crear los issues de cada fase es una tarea del docente al abrir la fase.
- Si se edita una tarea, hay que actualizar el archivo; el issue solo enlaza.
