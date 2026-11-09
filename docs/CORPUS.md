# Corpus

Qué documentos indexa el sistema, en qué versión y de dónde salieron. Si esto no
está al día, las citas apuntan a normativa derogada — que es peor que no citar.

## Documentos

| Documento (nombre de archivo) | Carrera | Versión / año | Vigente desde | Origen (URL o persona) | ¿Público? | Tiene texto extraíble |
|---|---|---|---|---|---|---|
| reglamento-estudiantil-2016.pdf | General | 2016 | febrero 2016 | https://drive.google.com/file/d/1k6uMRlLGA8hLTub1rJZpKoWhwhlfNKlI/view (enlazado en https://paginanueva.uab.edu.bo/reglamentos-uab/) | sí | |
| reglamento-de-graduacion-2016.pdf | General | 2016 | febrero 2016 | https://drive.google.com/file/d/1icpU6V0iTDmAC9ANxSKcpNbuG0cFzaTH/view (enlazado en https://paginanueva.uab.edu.bo/reglamentos-uab/) | sí | |
| reglamento-de-becas-2016.pdf | General | 2016 | febrero 2016 | https://drive.google.com/file/d/190sR7nWnbP78TD1aWV1tkuRkRm8mhnGd/view (enlazado en https://paginanueva.uab.edu.bo/reglamentos-uab/) | sí | |
| reglamento-de-investigacion-2021.pdf | General | 2021 (vigencia dudosa: la portada dice 2021 y el cierre, 2016) | — | https://www.uab.edu.bo/assets/pdf/REGLAMENTO-DE-INVESTIGACION%202016.pdf | sí | |
| reglamento-de-interaccion-social-y-difusion-cultural-2016.pdf | General | 2016 | febrero 2016 | https://drive.google.com/file/d/1o_xpo1Vx84V4cRr-kX_cww-3G_ycFFbO/view (enlazado en https://paginanueva.uab.edu.bo/reglamentos-uab/) | sí | |

Quedan fuera, aunque son públicos, porque no regulan al estudiante: el
Reglamento Docente, el del Personal Administrativo y el de Autoevaluación
(misma página). La versión de 2016 del Reglamento de Investigación (Drive,
`1MG9axfNtsly_TJraaLy318oY37yVibaT`) se sustituye por la de 2021.

### Documentos no públicos

Ninguno. El *Reglamento Institucional* aparece en la lista de
https://paginanueva.uab.edu.bo/secretaria-general/, pero sin enlace: falta
conseguirlo. El plan de estudios de la carrera solo está como texto en
https://www.uab.edu.bo/carrers/systems-engineering, no como PDF.

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
reunidos en la carpeta de Drive del corpus (INV-004), no en git. Los PDF van
en `corpus/ingenieria-sistemas/` (tarea INV-004). Añadir normativa
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
