# Corpus

Qué documentos indexa el sistema, en qué versión y con qué permiso. Si esto no
está al día, las citas apuntan a normativa derogada — que es peor que no citar.

## Documentos

| Documento (nombre de archivo) | Carrera | Versión / año | Vigente desde | Origen (URL o persona) | Permiso | Tiene texto extraíble |
|---|---|---|---|---|---|---|
| _(rellenar en INV-004 / INV-005)_ | | | | | | |

## Procedencia y permisos

- **Estado de la gestión con la administración:** _(pendiente / concedido / parcial)_
- **Persona de contacto:** _(rellenar)_
- **Qué se pidió exactamente:** _(rellenar)_
- **Qué se ofreció a cambio:** informe anonimizado de qué consulta realmente la
  comunidad universitaria — información que hoy no se tiene y que sirve para
  detectar qué normativa está mal comunicada.

## Corpus semilla

Mientras la solicitud formal avanza se trabaja con los documentos ya públicos
del sitio web. El MVP usa solo la normativa de **Ingeniería de Sistemas** y la
normativa general que le aplica, en `corpus/ingenieria-sistemas/` (tareas
INV-004 e INV-005). Añadir normativa después es copiar PDFs en la carpeta de la
carrera y volver a ejecutar la ingesta y el índice.

## Calidad de la extracción

Revisar después de cada ingesta y anotar aquí:

- Documentos sin texto extraíble (escaneados, necesitan OCR): _(rellenar)_
- Documentos donde la detección de artículos falla: _(rellenar)_
- Fragmentos totales / con artículo identificado: _(rellenar)_

## Actualización

La normativa cambia. Cada vez que se sustituya un documento: actualizar la tabla,
reconstruir el índice y anotarlo en la bitácora de sesiones
(`historial/sesiones/`).
