# ADR-005: Juntar las tareas pendientes para llegar a la presentación

**Estado:** aceptada · **Fecha:** 2026-11-04 · **Tarea:** —

## Contexto

El MVP se presenta el **19 de noviembre de 2026** y todas las tareas tienen que
estar cerradas el 18. A 4 de noviembre quedaban 44 tareas sin tomar, pensadas
para que cada una cupiera en una tarde (S ≤ 2 h, M ≤ 4 h). Con tres
estudiantes y dos semanas, ese ritmo no llega: cada tarea cuesta, además del
trabajo, un PR, una revisión y un movimiento en el tablero, y muchas cadenas
eran de un solo paso (IA-002 → IA-003 → IA-004 → IA-005 → IA-006).

Además, el equipo trabaja con modelos de IA gratuitos, que siguen peor una
especificación ambigua.

## Decisión

- Las 44 tareas sin tomar se juntan en **18**: 15 para estudiantes y 3 de
  configuración y despliegue (BE-006, BE-007 y BE-008), que hace el docente
  porque usan sus cuentas. Las 10 tareas ya tomadas o hechas no cambian.
- Cada tarea nueva conserva el ID y el issue de su tarea principal. Las
  absorbidas se borran de `backlog/tareas/` (su texto queda en git) y su issue
  se cierra como *not planned* con un enlace a la tarea que la contiene. El
  campo `absorbe` del archivo y la columna *Absorbe* de `TABLERO.md` lo
  registran.
- Nuevo tamaño **L** (≤ 8 h, dos tardes) y nuevo campo `fecha_limite` en cada
  tarea y en el tablero de GitHub Projects (*Fecha límite*). Sin responsables
  asignados de antemano: cada estudiante toma sus tareas.
- Las tareas se escriben **paso a paso**, con firmas de funciones, nombres de
  archivo, valores concretos y comandos de verificación exactos.
- Se reservan los números de ADR que escribirán las tareas (ADR-006 a ADR-010,
  ver `TABLERO.md`) para que no choquen trabajando en paralelo.
- Todas las fases quedan abiertas a la vez: no queda nada en *Backlog*.

## Por qué

- **El objetivo no cambia:** corpus, ingesta, búsqueda híbrida medida,
  respuesta con citas y rechazo, web accesible, despliegue, evaluación de
  fundamentación, informe y demo. Cada paso de las tareas antiguas está dentro
  de una tarea nueva.
- Juntar tareas que una sola persona iba a hacer seguidas ahorra PRs y esperas
  de revisión sin perder trabajo.
- Las dependencias que no eran necesarias se quitan para trabajar en paralelo:
  el prompt (antes IA-015) ya no espera al ADR del enfoque RAG, y el umbral
  (antes IA-017) ya no espera al script de recall.

## Alternativas descartadas

| Alternativa | Por qué no |
|---|---|
| Mantener las 44 tareas | No caben en dos semanas con tres estudiantes |
| Recortar alcance (quitar accesibilidad, keep-alive, registro de consultas…) | Cambia el objetivo inicial del MVP |
| Cerrar todos los issues y crear 18 nuevos | Se pierde la numeración y la historia de cada issue |
| Asignar responsables de antemano | El equipo prefiere tomar las tareas libremente |

## Consecuencias

- Las tareas L son más largas: quien no llegue a su fecha límite lo avisa en el
  issue **antes** de esa fecha, para que el docente la reparta o la tome.
- El camino crítico (INV-004 → IA-002 → IA-008 → IA-007 → IA-016 → BE-003 →
  BE-007 → INV-011) no tiene holgura: un día de retraso en cualquiera se nota en
  la demo.
- Los documentos de `historial/` anteriores a esta fecha nombran IDs antiguos;
  no se corrigen, porque son historia. `TABLERO.md` dice dónde quedó cada uno.
- Los archivos de investigación de las tareas juntadas toman el ID de la tarea
  nueva (por ejemplo, `investigacion/IA-002-estructura-pdf.md`, antes INV-006).
