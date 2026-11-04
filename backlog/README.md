# Backlog

Todas las tareas del proyecto, autocontenidas. Cada una se puede resolver
leyendo solo su archivo, los contratos de `docs/ARQUITECTURA.md` y los archivos
que lista en *Entradas*. Tamaños: S ≤ 2 h, M ≤ 4 h, L ≤ 8 h (dos tardes).

Cada tarea tiene una `fecha_limite`: la presentación del MVP es el
**19 de noviembre de 2026** y todo tiene que estar cerrado el 18 (ADR-005).

- **GitHub Projects, tablero "Normativa UAB"**: única fuente del **estado** y
  del **responsable** de cada tarea. Cada tarea es un issue.
- `tareas/<ID>.md`: la **especificación** de cada tarea y sus notas de cierre.
  El issue enlaza a este archivo; si hay diferencias, manda el archivo.
- `TABLERO.md`: índice de todas las tareas con sus dependencias, su fecha
  límite, su issue y el camino crítico. Todas las tareas tienen issue
  (ADR-004).
- `_plantilla-tarea.md`: para proponer tareas nuevas.

## Áreas

| Prefijo | Área | Qué se entrega normalmente |
|---|---|---|
| `SET` | Arranque | Entorno y primeros pasos con git |
| `INV` | Investigación | Informe en `investigacion/` y, si hay decisión, un ADR |
| `IA` | IA y datos | Código en `ia/` o `eval/`, datos, mediciones |
| `BE` | Backend | Código en `apps/api/`, base de datos (`db/`, `ia/db.py`) y despliegue |
| `FE` | Frontend | Código en `apps/web/` |

## Fases

| Fase | Meta | Se cierra cuando… |
|---|---|---|
| F0 Arranque | Entorno listo y conceptos base | Todos hicieron su primer PR |
| F1 Corpus | Normativa de la carrera reunida; API mínima desplegada en Render | Hay PDFs registrados, golden set v0 y `/salud` responde en la URL pública |
| F2 Ingesta | PDFs → fragmentos por artículo; base de datos creada | `data/fragmentos.json` revisado a mano y esquema aplicado en Supabase |
| F3 Búsqueda | Encontrar el artículo correcto | recall@5 medido en los tres modos |
| F4 Generación | Respuesta con citas y rechazo | La web responde de verdad con citas |
| F5 Cierre MVP | Desplegado y documentado | URL pública + informe del MVP |

Las áreas avanzan en paralelo: mientras IA trabaja la ingesta, backend y
frontend construyen la API y la web contra el mock. Desde ADR-005 todas las
fases están abiertas a la vez y se solapan: lo que ordena el trabajo es la
**fecha límite** de cada tarea y sus dependencias, no la fase.

## Estados

Columnas del tablero: *Backlog* (su fase aún no empezó) → *Bloqueada* (le
faltan dependencias) → *Disponible* → *En curso* → *En revisión* → *Hecha*.

Desde ADR-005 no queda nada en *Backlog*: cada tarea está en *Disponible* o
en *Bloqueada*, según sus dependencias.

Cuando una tarea se cierra, quien la cerró revisa en `TABLERO.md` qué tareas
dependían de ella y mueve a *Disponible* las que ya tengan todas sus
dependencias cerradas.

## Reglas

- Máximo dos tareas `en-curso` por persona.
- Una tarea no se modifica mientras está `en-curso`, salvo *Notas de cierre*.
  Si la especificación está mal, se comenta en el PR y el docente la corrige.
- Una tarea que no llega a su fecha límite se avisa en su issue **antes** de
  esa fecha, para que el docente la reparta o la tome.
- Tarea nueva: copiar la plantilla, usar el siguiente número libre del área,
  añadir una fila a `TABLERO.md` y pedir al docente que cree su issue en cuanto
  se acepte.
