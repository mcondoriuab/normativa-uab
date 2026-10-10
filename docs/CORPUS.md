# Corpus

Qué documentos indexa el sistema, en qué versión y de dónde salieron. Si esto no
está al día, las citas apuntan a normativa derogada — que es peor que no citar.

## Documentos

| Documento (nombre de archivo) | Carrera | Versión / año | Vigente desde | Origen (URL o persona) | ¿Público? | Tiene texto extraíble |
|---|---|---|---|---|---|---|
| _(rellenar en INV-004 / INV-005)_ | | | | | | |

## Procedencia

El MVP usa solo la normativa de **Ingeniería de Sistemas** y la normativa
general que le aplica. Es de dominio público, así que **no hace falta pedir
permiso** a la administración (decisión del 2026-10-09, que sustituye a la
gestión formal prevista al principio). Cada documento tiene que tener un origen
verificable: la URL donde se publica o la persona que lo facilitó y la fecha.

Si aparece un documento que no es público, no entra en el corpus: se anota
aparte (INV-004) y se avisa al docente. Pedir permiso solo volvería a hacer
falta al añadir normativa que no esté publicada.

## Corpus semilla

Se empieza con los documentos que el equipo ya tenía y con los del sitio web,
reunidos en la carpeta de Drive del corpus (INV-016), no en git. Los PDF van
en `corpus/ingenieria-sistemas/` (tareas INV-004 e INV-005). Añadir normativa
después es copiar PDFs en la carpeta de la carrera y volver a ejecutar la
ingesta y el índice.

## Calidad de la extracción

Revisar después de cada ingesta y anotar aquí:

- Documentos sin texto extraíble (escaneados, necesitan OCR): _(rellenar)_
- Documentos donde la detección de artículos falla: _(rellenar)_
- Fragmentos totales / con artículo identificado: _(rellenar)_

## Actualización

La normativa cambia. Cada vez que se sustituya un documento: actualizar la tabla,
reconstruir el índice y anotarlo en la bitácora de sesiones
(`historial/sesiones/`).
