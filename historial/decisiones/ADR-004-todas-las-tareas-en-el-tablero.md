# ADR-004: Todas las tareas en el tablero, con columna Backlog

**Estado:** aceptada · **Fecha:** 2026-10-06 · **Tarea:** —

## Contexto

ADR-003 decidió crear los issues **fase a fase** para que el tablero mostrara
solo lo que se podía trabajar pronto. Una semana después, el docente quiere ver
en el tablero el proyecto entero: qué falta, cuánto queda y qué viene después.
Además, con solo los issues de F0, quien terminaba pronto no veía en qué podía
seguir.

## Decisión

- Se crea un issue para **cada tarea** del backlog, de todas las fases.
- El tablero tiene una columna nueva, **Backlog**, delante de las demás:
  *Backlog* → *Bloqueada* → *Disponible* → *En curso* → *En revisión* →
  *Hecha*.
- *Backlog* = la tarea es de una fase que todavía no empezó. *Bloqueada* sigue
  significando solo "le falta una dependencia".
- Al abrir una fase, el docente mueve sus tareas de *Backlog* a *Disponible* o
  *Bloqueada*, según sus dependencias.

Reemplaza la parte de ADR-003 que dice "los issues se crean fase a fase". El
resto de ADR-003 sigue vigente.

## Por qué

- El equipo ve el camino completo hasta el MVP, y el docente puede medir el
  avance.
- Separar *Backlog* de *Bloqueada* mantiene la regla actual: al cerrar una
  tarea, se pasan a *Disponible* las que dependían de ella. Si todo lo futuro
  estuviera en *Bloqueada*, esa columna no diría por qué está bloqueada cada
  cosa.
- El ruido que preocupaba en ADR-003 se controla plegando la columna *Backlog*
  o filtrando por el campo *Fase*.

## Alternativas descartadas

| Alternativa | Por qué no |
|---|---|
| Seguir fase a fase (ADR-003) | No se ve el proyecto entero |
| Todo lo futuro en *Bloqueada* | Mezcla "falta una dependencia" con "no es su fase" |

## Consecuencias

- Si se edita la especificación de una tarea en `backlog/tareas/`, el texto del
  issue queda desactualizado antes; sigue mandando el archivo.
- Una tarea nueva necesita su issue al crearse, no al abrir su fase.
- Revisar si la columna *Backlog* termina siendo un sitio donde se olvidan las
  tareas.
