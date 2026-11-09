# IA-002: cómo están escritos los PDF del corpus

**Autor(es):** Sandra · **Fecha:** 2026-11-09

## Pregunta

¿Los PDF de `corpus/ingenieria-sistemas/` tienen texto extraíble? ¿Cómo se
escriben los encabezados de artículo, capítulo y título, y qué rarezas hay
que tener en cuenta al trocear?

## Lo que encontramos

Los 5 PDF tienen texto (ninguno es escaneado). Todos siguen la misma plantilla:
`TÍTULO` → `CAPÍTULO` → `Artículo N.- (Nombre del artículo) Texto…`. No hay
índice al principio, así que ningún número de artículo se repite.

Los ejemplos son literales, sacados con `python -m ia.extraer` (la página es la
del PDF, empezando en 1).

### reglamento-de-becas-2016 (7 páginas)

| Aspecto | Valor |
|---|---|
| Texto extraíble | sí |
| Artículos | 50 (del 1 al 50, sin huecos) |
| Encabezados de artículo | `Artículo 1.- (Del Propósito del Reglamento)` (p. 2) · `Artículo 26.- (Del Porcentaje de la Beca) De` (p. 5) · `Artículo 50.- (De la Vigencia) El presente` (p. 7) |
| Capítulo | `CAPÍTULO ÚNICO` (p. 2), `CAPITULO I` (p. 3, sin tilde) |
| Título | `TITULO I` (p. 2, sin tilde), `TÍTULO II` (p. 3) |
| Rarezas | 7 líneas que **empiezan** por `Art. 6 del presente reglamento.` (pp. 5-7): son referencias dentro del texto, no encabezados. Pie de página `Reglamento de Becas Pag 2 de 7`. Muchos tabuladores en lugar de espacios (298). |

### reglamento-de-graduacion-2016 (13 páginas)

| Aspecto | Valor |
|---|---|
| Texto extraíble | sí |
| Artículos | 72 (del 1 al 72, sin huecos) |
| Encabezados de artículo | `Artículo 1.- (De la Normatividad Institucional)` (p. 2) · `Artículo 37.- (Del Informe de la Comisión` (p. 8) · `Artículo 72.- (De la Vigencia) El presente` (p. 13) |
| Capítulo | `CAPÍTULO I` (p. 2) |
| Título | `TITULO I` (p. 2, sin tilde), `TÍTULO II` (p. 4) |
| Rarezas | Pie de página `Reglamento de Graduación “UAB” Pag 2 de 13`. |

### reglamento-de-interaccion-social-y-difusion-cultural-2016 (6 páginas)

| Aspecto | Valor |
|---|---|
| Texto extraíble | sí |
| Artículos | 32 (del 1 al 32) |
| Encabezados de artículo | `Artículo 1.- (Del Órgano de Interacción Social y` (p. 2) · `Artículo 17.- (De la Modificación del Proyecto` (p. 4) · `Artículo 32.- (De la Vigencia) El presente` (p. 6) |
| Capítulo | `CAPÍTULO I` (p. 2), `CAPITULO III` (sin tilde) |
| Título | `TÍTULO I` (p. 2), `TÍTULO II` (p. 5) |
| Rarezas | **Errata en el original:** `Artículos 23.- (Participación de profesionales y` (p. 4), en plural. Pie de página `Reglamento de Interacción Social y Difusión Cultural “UAB” Pag 2 de 6`. |

### reglamento-de-investigacion-2021 (16 páginas)

| Aspecto | Valor |
|---|---|
| Texto extraíble | sí |
| Artículos | 57 (del 1 al 57, sin huecos) |
| Encabezados de artículo | `Artículo 1.- (Del Propósito de la Reglamentación) En concord…` (p. 2) · `Artículo 29.- (De la Evaluación del Proyecto` (p. 11) · `Artículo 57.- (De la Vigencia) El presente Reglamento…` (p. 16) |
| Capítulo | `CAPÍTULO I` (p. 2), `CAPÍTULO II` (p. 5) |
| Título | `TÍTULO I` (p. 2), `TÍTULO II` (p. 9) |
| Rarezas | **Encabezado** de página (arriba, no abajo) en 15 páginas: una línea `▬▬▬▬…` y `Reglamento de Investigación “UAB”   …   Página 4 de 16`. Es un formato distinto al de los otros cuatro (otra plantilla: versión 2021). |

### reglamento-estudiantil-2016 (15 páginas)

| Aspecto | Valor |
|---|---|
| Texto extraíble | sí |
| Artículos | 82 (del 1 al 82, sin huecos) |
| Encabezados de artículo | `Artículo 1.- (De la normatividad Institucional)` (p. 2) · `Artículo 42.- (De las obligaciones) Los estud…` (p. 8) · `Artículo 82.- (De la Vigencia) El presente` (p. 15) |
| Capítulo | `CAPÍTULO ÚNICO` (p. 2), `CAPÍTULO I` (p. 2) |
| Título | `TÍTULO I` (p. 2), `TÍTULO II` (p. 2) |
| Rarezas | Muchos tabuladores en lugar de espacios (677), p. ej. `Artículo 80.- (Apelación)\tEn\túltima\tinstancia,\tel`. Doble espacio tras el número en `Artículo 3.-  (De la inscripción)`. Pie de página con nombre inconsistente: `Reglamento Estudiantil “UAB” Pag 2 de 15` y `Reglamento de Estudiantil “UAB” Pag 3 de 15`. |

### Rarezas comunes a todos

- **No hay líneas en blanco** en el texto extraído (`"\n\n"` aparece 0 veces).
  El troceado por longitud tendrá que partir por `"\n"`.
- Cada línea del PDF es una línea del texto: los párrafos llegan cortados.
- No hay artículos "bis", ni numeración romana en artículos, ni `°`.
- Títulos y capítulos usan numeración romana y a veces van sin tilde
  (`TITULO`, `CAPITULO`).
- _(Pendiente de revisar a ojo abriendo cada PDF: tablas, notas al pie y texto
  en dos columnas. Desde el texto extraído no se ve.)_

### Todas las variantes de encabezado de artículo

1. `Artículo N.- (Nombre)` → la forma normal (292 de los 293 artículos).
2. `Artículo N.-  (Nombre)` → igual, con dos espacios.
3. `Artículo N.- (Nombre)\tTexto` → tabulador en lugar de espacio después.
4. `Artículos N.- (Nombre)` → errata en plural (Interacción Social, art. 23).

**No es un encabezado** aunque empiece la línea: `Art. 6 del presente
reglamento.` (referencia, Becas). Por eso el patrón exige `.-` después del
número y no acepta `Art.`.

## Evidencia

- Extracción con `pypdf` 7.0.0 (`ia/extraer.py`) y búsqueda con expresiones
  regulares sobre el texto de cada página.
- Total de encabezados encontrados al inicio de línea = total en cualquier
  posición (50, 72, 32, 57, 82): ningún encabezado aparece a mitad de línea.
- Se usó IA (Claude) para hacer el recuento automático y redactar el primer
  borrador; los ejemplos se copiaron de la salida real del script. _(Falta
  comprobarlos abriendo los PDF.)_

## Conclusión para el proyecto

- Los 5 PDF entran en la ingesta sin OCR.
- Patrón de artículo: `^\s*art[íi]culos?\s+(\d+(?:\s*bis)?)\s*\.\s*-`. Se deja
  el `bis` porque lo pide la tarea, aunque hoy no aparece.
- Esperamos 50 + 72 + 32 + 57 + 82 = **293 fragmentos**, todos con artículo.
- Los pies o encabezados de página (`Pag N de M`, `▬▬▬`) se colarán en los
  fragmentos que cruzan de página, y los `TÍTULO`/`CAPÍTULO` quedan pegados al
  final del artículo anterior. La revisión (Parte 5) confirmó que pasaba en más
  del 20 % y se corrigió: ver `investigacion/IA-002-revision-fragmentos.md`.

## Preguntas abiertas

- ¿Hay tablas, notas al pie o texto en dos columnas? Comprobarlo abriendo los
  PDF.
