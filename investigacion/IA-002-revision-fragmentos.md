# IA-002: revisión manual de 30 fragmentos

**Autor(es):** Sandra · **Revisor (5 de 30):** Miguel Ángel Condori (con ayuda de Claude), 2026-11-12 · **Fecha:** 2026-11-09

## Pregunta

¿Los fragmentos de `data/fragmentos.json` están bien troceados? ¿Cada uno tiene
el artículo completo, la página correcta y nada de texto ajeno?

## Cómo se sacó la muestra

30 fragmentos al azar con `random.seed(42)` sobre los 293 de la ingesta
(comando del paso 18 de la tarea). Cualquiera puede repetirla y obtener los
mismos `id`.

## Primera ronda (comprobación automática, antes de corregir)

Antes de la revisión a mano se buscó en los textos de la muestra:

| Problema | Fragmentos de 30 | ¿> 20 %? |
|---|---|---|
| Pie o encabezado de página (`Pag N de M`, `Página N de M`, `▬▬▬`) | 8 | sí |
| `TÍTULO`/`CAPÍTULO` del bloque siguiente pegado al final | 6 | sí (6 o más) |

Ambos superan el umbral, así que se corrigió `ia/trocear.py` (paso 21):

- `quitar_pies_de_pagina`: borra las líneas con `Pag N de M`, `Página N de M`
  o solo `▬`, antes de trocear.
- `quitar_titulos_del_final`: corta el texto desde la primera línea
  `TÍTULO X` / `CAPÍTULO X` (mayúsculas, numeral romano o `ÚNICO`).

Tras volver a ejecutar la ingesta: 0 fragmentos con pie de página y 0 con
encabezados de estructura en todo el corpus (las 2 coincidencias restantes son
"Título Profesional", texto legítimo). La muestra no cambia porque los `id` y su
orden son los mismos.

## Segunda ronda (revisión a mano, contra el PDF)

Abrir cada fragmento junto al PDF en la página indicada. Responder `sí`/`no`.

| id | pág. | ¿artículo completo? | ¿página correcta? | ¿tiene basura? | ¿texto desordenado? | nota |
|---|---|---|---|---|---|---|
| `reglamento-de-graduacion-2016#art-8` | 4 | sí | sí | no | no | |
| `reglamento-de-becas-2016#art-13` | 3 | sí | sí | no | no | Sigue en la pág. 4; el texto está entero |
| `reglamento-de-interaccion-social-y-difusion-cultural-2016#art-19` | 4 | sí | sí | no | no | |
| `reglamento-de-interaccion-social-y-difusion-cultural-2016#art-4` | 2 | sí | sí | no | no | |
| `reglamento-de-graduacion-2016#art-65` | 12 | sí | sí | no | no | |
| `reglamento-de-graduacion-2016#art-22` | 6 | sí | sí | no | no | |
| `reglamento-de-graduacion-2016#art-3` | 2 | sí | sí | no | no | Sigue en la pág. 3; el texto está entero |
| `reglamento-estudiantil-2016#art-69` | 12 | sí | sí | no | no | |
| `reglamento-de-becas-2016#art-45` | 7 | sí | sí | no | no | |
| `reglamento-estudiantil-2016#art-6` | 2 | sí | sí | no | no | Sigue en la pág. 3; el texto está entero |
| `reglamento-de-becas-2016#art-17` | 4 | sí | sí | no | no | |
| `reglamento-de-becas-2016#art-16` | 4 | sí | sí | no | no | |
| `reglamento-de-becas-2016#art-48` | 7 | sí | sí | no | no | |
| `reglamento-de-graduacion-2016#art-62` | 11 | sí | sí | no | no | Sigue en la pág. 12; el texto está entero |
| `reglamento-de-graduacion-2016#art-70` | 12 | sí | sí | no | no | |
| `reglamento-estudiantil-2016#art-48` | 9 | sí | sí | no | no | |
| `reglamento-de-becas-2016#art-14` | 4 | sí | sí | no | no | |
| `reglamento-estudiantil-2016#art-77` | 14 | sí | sí | no | no | |
| `reglamento-de-graduacion-2016#art-52` | 10 | sí | sí | no | no | |
| `reglamento-estudiantil-2016#art-4` | 2 | sí | sí | no | no | |
| `reglamento-de-graduacion-2016#art-63` | 12 | sí | sí | no | no | |
| `reglamento-estudiantil-2016#art-19` | 4 | sí | sí | no | no | |
| `reglamento-de-interaccion-social-y-difusion-cultural-2016#art-21` | 4 | sí | sí | no | no | |
| `reglamento-de-becas-2016#art-4` | 2 | sí | sí | no | no | |
| `reglamento-de-graduacion-2016#art-32` | 7 | sí | sí | no | no | |
| `reglamento-de-investigacion-2021#art-21` | 9 | sí | sí | no | no | |
| `reglamento-de-graduacion-2016#art-30` | 7 | sí | sí | no | no | |
| `reglamento-de-graduacion-2016#art-61` | 11 | sí | sí | no | no | |
| `reglamento-de-investigacion-2021#art-19` | 9 | sí | sí | no | no | |
| `reglamento-de-investigacion-2021#art-41` | 12 | sí | sí | no | no | Sigue en la pág. 13; el texto está entero |

## Recuento

| Problema | Fragmentos de 30 |
|---|---|
| Artículo incompleto | 0 |
| Página incorrecta | 0 |
| Con basura | 0 |
| Texto desordenado | 0 |

En la primera pasada se marcaron como incompletos 5 artículos que empiezan en
una página y terminan en la siguiente. Al compararlos de nuevo, el texto está
entero: el contrato guarda en `pagina` solo la página donde **empieza** el
artículo, así que cruzar de página no es un error.

## Revisión de 5 de 30 (revisor)

Se repitió la muestra con `random.seed(42)` (mismos 30 `id` y páginas) y se
eligieron 5 de los casos más difíciles: artículos que cruzan de página, el más
largo, texto a dos columnas y la plantilla de Investigación 2021. Cada
fragmento se comparó con el PDF abierto directamente, no con la salida de
`pypdf`.

| id | pág. | ¿artículo completo? | ¿página correcta? | ¿tiene basura? | ¿texto desordenado? | nota |
|---|---|---|---|---|---|---|
| `reglamento-de-becas-2016#art-13` | 3 | sí | sí | no | no | Sigue en la pág. 4; se quitaron bien el pie y el `CAPITULO I` |
| `reglamento-de-graduacion-2016#art-3` | 2 | sí | sí | no | no | El más largo: 3 columnas en 2 páginas, en el orden correcto |
| `reglamento-de-interaccion-social-y-difusion-cultural-2016#art-19` | 4 | sí | sí | no | no | |
| `reglamento-de-investigacion-2021#art-41` | 12 | sí | sí | no | no | Sigue en la pág. 13; quedan líneas en blanco donde estaba el pie |
| `reglamento-estudiantil-2016#art-77` | 14 | sí | sí | no | no | |

Los 5 coinciden con la revisión de arriba. Fuera de la muestra se vieron dos
detalles menores que no bloquean:

- `reglamento-estudiantil-2016` tiene un nivel más, `SECCIÓN I`/`SECCIÓN II`,
  que el patrón de `TÍTULO`/`CAPÍTULO` no quita: queda pegado al final de
  `#art-32`, `#art-73` y `#art-76`.
- Cuatro encabezados se escriben `Articulo`, sin tilde (Interacción Social
  art. 26; Investigación arts. 42, 43 y 49). El patrón los detecta, pero no
  están en la lista de variantes de `IA-002-estructura-pdf.md`.

## Conclusión para el proyecto

Después de la corrección del paso 21, los 30 fragmentos revisados tienen el
artículo completo, la página correcta, no traen basura y el texto está en
orden. Ningún problema supera el 20 %, así que no hacen falta más cambios en
`ia/trocear.py`. `data/fragmentos.json` sirve como entrada para la búsqueda
(IA-007, IA-008) y para INV-009.

Queda una limitación conocida: 5 de 30 fragmentos (17 %) cruzan de página y la
cita solo indica la página donde empiezan.

## Preguntas abiertas

- Al quitar `TÍTULO`/`CAPÍTULO` se pierde a qué capítulo pertenece cada
  artículo. ¿Serviría para la búsqueda o para las citas?
