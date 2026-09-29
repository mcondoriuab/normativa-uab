# Cómo contribuir

## Flujo de una tarea

El estado de cada tarea se lleva en el tablero de GitHub Projects
**Normativa UAB**, donde cada tarea es un issue:

```
Bloqueada → Disponible → En curso → En revisión → Hecha
```

1. **Tomar.** En el tablero, elige un issue en *Disponible*, asígnatelo
   (*Assignees*) y muévelo a *En curso*. Una persona, máximo dos tareas en curso
   a la vez.
2. **Rama.** Crea una rama con el ID de la tarea:
   ```bash
   git switch main && git pull
   git switch -c IA-003-detectar-articulos
   ```
3. **Trabajar.** Sigue el archivo `backlog/tareas/<ID>.md`. Solo toca los
   entregables que lista.
4. **Verificar.** Ejecuta los comandos de *Cómo verificar* y comprueba cada
   criterio de aceptación.
5. **Cerrar notas.** Rellena *Notas de cierre* en el archivo de la tarea.
6. **Pull request.** Sube la rama y abre un PR titulado `IA-003: detectar
   artículos con regex` y escribe en la descripción `Closes #<número del
   issue>`. Mueve el issue a *En revisión*.
7. **Revisión.** Otra persona del equipo (no solo el docente) revisa el PR. Si
   está bien, se hace *merge*: el issue se cierra solo y pasa a *Hecha*.

## Mensajes de commit

Empiezan con el ID de la tarea y dicen qué cambia:

```
IA-003: detectar encabezados "Artículo N" con regex
FE-001: maqueta de la página con aviso legal
```

## Si te atascas

- Más de 30 minutos atascado: pregunta en el grupo. Atascarse es normal;
  quedarse atascado en silencio no.
- Si la tarea resulta ser más grande de lo que dice, no la estires: anótalo en
  sus *Notas de cierre* y propón dividirla.
- Si encuentras algo que falta, propón una tarea nueva copiando
  `backlog/_plantilla-tarea.md`.

## Uso de IA

Se permite usar asistentes de IA con una regla: **si pegaste código generado,
tienes que poder explicar cada línea en la siguiente sesión**. Anota en las
*Notas de cierre* dónde la usaste y qué tuviste que corregir.
