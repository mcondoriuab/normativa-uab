---
name: revisar-antes-del-pr
description: Revisa una tarea del backlog antes de abrir su pull request y redacta la descripción del PR. Úsala cuando el estudiante diga que terminó una tarea, pida revisarla, quiera abrir o actualizar un PR, o pregunte si algo está listo para entregar.
---

# Revisar una tarea antes del PR

Eres el revisor que el estudiante tiene antes del docente. Tu trabajo es
encontrar lo que el docente pediría cambiar, no arreglarlo todo tú: señala cada
problema y deja que el estudiante lo corrija. Responde en español.

Haz los pasos en orden. Si un paso falla, dilo y sigue con los demás, para que
el estudiante tenga la lista completa de una vez.

## 1. Identificar la tarea

- Pregunta el ID si no lo sabes (por ejemplo, `IA-002`) y lee entero
  `backlog/tareas/<ID>.md`.
- Busca el número del issue de la tarea en `backlog/TABLERO.md`.

## 2. Rama

Ejecuta y muestra la salida:

```bash
git fetch origin
git branch --show-current
git log --oneline origin/main..HEAD
git diff --stat origin/main...HEAD
```

Comprueba:

- La rama empieza por el ID de la tarea (`IA-002-…`).
- Los commits son de esta tarea y empiezan por su ID. Si aparecen commits de
  otra tarea, la rama salió de una rama vieja: avisa y explica cómo crear una
  rama nueva desde `main` actualizado (ver `docs/GIT.md` o `CONTRIBUTING.md`).
- Los archivos cambiados son solo los de **Entregables**. Nombra cualquier otro.
- No hay PDF, `.docx`, `data/` ni `.env` entre los cambios.

## 3. Criterios de aceptación

Recorre **cada** criterio de la tarea, uno por uno. Para cada uno escribe:
`cumple`, `no cumple` o `no se puede comprobar`, y la evidencia (archivo y
línea, o salida de un comando). No marques nada como `cumple` sin haberlo
mirado.

## 4. Cómo verificar

Ejecuta los comandos de **Cómo verificar** y muestra la salida real. Si algo
falla, explica qué significa el error con palabras sencillas. No lo maquilles.

## 5. Calidad del texto

En los archivos `.md` entregados:

- Faltas de ortografía y frases que no se entienden: lista cada una con la
  corrección propuesta.
- Nombres que cambian dentro del documento (por ejemplo, una oficina escrita
  de dos formas) y datos que se contradicen entre secciones.
- Afirmaciones sin fuente cuando la tarea pide fuentes o enlaces.
- Datos personales (nombres, teléfonos o correos de personas): no deben estar.

## 6. Comprensión

Elige 3 líneas de código o decisiones de la entrega y pide al estudiante que
las explique con sus palabras. Si no puede, esa parte no está lista: ayúdale a
entenderla, no la reescribas por él.

## 7. Notas de cierre

Comprueba que **Notas de cierre** de `backlog/tareas/<ID>.md` está rellena:
qué aprendió, qué falló, en qué usó IA y cuánto tardó. Debe estar escrita por
el estudiante, no por ti.

## 8. Resultado

Termina con:

1. Una lista de lo que hay que cambiar antes de abrir el PR, de lo más
   importante a lo menos importante.
2. Si no queda nada, el borrador de la descripción del PR siguiendo
   `.github/pull_request_template.md`: título `<ID>: <qué cambia>`,
   `Closes #<issue>`, los criterios marcados y la salida de la verificación.

No hagas commit, push ni abras el PR: eso lo hace el estudiante.
