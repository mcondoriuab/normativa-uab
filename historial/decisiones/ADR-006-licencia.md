# ADR-006: Licencia del proyecto

**Estado:** aceptada · **Fecha:** 2026-11-12 · **Tarea:** INV-003

## Contexto

El repositorio es público, pero sin licencia nadie puede reutilizarlo
legalmente: por defecto, todos los derechos quedan reservados a sus autores.
El código y la documentación los escriben los estudiantes y van firmados por
ellos (`docs/ETICA.md`, *Autoría*). Queremos que otra carrera, otra
universidad u otro grupo de estudiantes puedan aprovechar el trabajo.

No conocemos ninguna política de la UAB ni de la Sociedad sobre la propiedad
intelectual de los proyectos estudiantiles. Por eso el docente decide sin
esperarla.

## Decisión

- **Código** (Python, HTML, CSS, JavaScript, SQL, configuración): licencia
  **MIT**, en `LICENSE`.
- **Documentación y datos propios** (Markdown de `docs/`, `historial/`,
  `investigacion/`, `backlog/`, los README y el golden set de `eval/`):
  **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.es)**.
- **Fuera de las dos**: los PDF de normativa y los textos de `corpus/`. Son de
  la universidad, y su procedencia está en `docs/CORPUS.md`.

Los titulares son *los autores de normativa-uab*: quienes figuran en
`EQUIPO.md` y en el historial de git.

## Por qué

- MIT permite reutilizar el código con una sola condición: conservar el aviso
  de autoría. Cabe en una página, así que el equipo la puede leer y explicar
  entera. Comparación de MIT, Apache-2.0 y GPL-3.0 en
  <https://choosealicense.com/licenses/>.
- MIT está pensada para software. Para textos lo habitual es Creative Commons,
  y CC BY pide lo mismo que MIT: citar a los autores.

## Alternativas descartadas

| Alternativa | Por qué no |
|---|---|
| Apache-2.0 para el código | Permisiva como MIT, pero añade una concesión de patentes y la obligación de marcar los cambios. Aquí no hay patentes en juego, y es mucho más larga de leer |
| GPL-3.0 para el código | Copyleft: quien distribuya una versión modificada tiene que hacerlo con la misma licencia y entregar el código. Es más larga y difícil de cumplir, y en un servicio web casi no protege: ejecutarlo en un servidor no cuenta como distribuir (eso lo cubriría AGPL-3.0) |
| MIT también para la documentación | MIT habla de "software"; aplicada a textos es ambigua |
| CC BY-SA 4.0 para la documentación | Obliga a compartir las adaptaciones con la misma licencia; para material docente preferimos no poner condiciones |
| Sin licencia | Nadie podría reutilizar nada legalmente, aunque el repositorio sea público |

## Consecuencias

- Cualquiera puede copiar, modificar y usar el código y los textos, también
  con fines comerciales, siempre que cite a los autores.
- MIT y CC BY no dan garantías: si alguien despliega su propia copia, la
  responsabilidad es suya. Esto no cambia el aviso de la interfaz: el texto
  oficial y vinculante es el de la universidad.
- Revisaríamos esta decisión si la UAB o la Sociedad publican una política de
  propiedad intelectual que exija otra licencia o la cesión de derechos.
