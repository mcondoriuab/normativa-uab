# Visión

## El problema

La normativa de la universidad (reglamento estudiantil, régimen académico,
evaluación, convalidaciones, disciplina…) está repartida en PDFs largos que casi
nadie lee. Cuando un estudiante tiene una duda concreta ("¿cuántas faltas puedo
tener?", "¿hasta cuándo puedo pedir un examen de segunda instancia?") pregunta a
un compañero o hace fila en secretaría, y la respuesta que recibe no siempre es
la correcta.

## La propuesta

Un asistente web donde se escribe la pregunta en lenguaje natural y se recibe:

1. Una respuesta breve en español claro.
2. **La cita textual** del artículo que la respalda, con documento y página.
3. Si la normativa disponible no lo dice, un **"no lo encuentro"** honesto en
   vez de una respuesta inventada.

## Dos objetivos del mismo peso

1. **Producto:** una aplicación que funcione, desplegada y demostrable.
2. **Aprendizaje:** que el equipo entienda IA aplicada de verdad (embeddings,
   recuperación, evaluación, límites de los modelos) y que todo el proceso quede
   documentado en este repositorio.

Por eso, cuando hay que elegir, se prefiere la opción que el equipo puede leer y
explicar antes que la más sofisticada.

## ¿"Entrenar" la IA?

Decimos coloquialmente que vamos a "entrenar la IA con la normativa", pero
técnicamente **no vamos a entrenar ni ajustar (fine-tuning) ningún modelo**.
Haremos RAG (*Retrieval-Augmented Generation*):

- Guardamos la normativa troceada por artículos y la indexamos para poder
  buscarla.
- Ante una pregunta, **buscamos** los artículos relevantes.
- Le pasamos esos artículos a un modelo de lenguaje ya existente y le pedimos
  que responda **solo** con ellos y que cite de dónde saca cada cosa.

Así, el modelo no es la base de datos: si la normativa cambia, basta con volver
a indexar los PDFs, sin reentrenar nada, y cada respuesta es verificable contra
el texto original. Por qué se elige esto y no fine-tuning lo investiga y decide
el equipo en la tarea **INV-002**.

## MVP 1: una carrera

| Entra | No entra (todavía) |
|---|---|
| Normativa de **Ingeniería de Sistemas** más la normativa general que le aplica | Otras carreras |
| Preguntas en español | Otros idiomas |
| Respuesta + cita + página | Enlaces a trámites, formularios |
| Rechazo cuando no hay evidencia | Conversación con memoria de preguntas anteriores |
| Web usable en móvil, desplegada en una URL pública | Login, cuentas, historial por usuario |
| Métricas medidas con un golden set | Panel de analítica para la administración |

**Criterio de "MVP terminado":** con el golden set de la carrera, el sistema
recupera el artículo correcto en su top-5 en la mayoría de las preguntas, rechaza
las preguntas fuera de corpus, y cualquier persona puede usarlo desde el móvil.
Los números exactos se fijan tras la primera medición (IA-013).

## Después del MVP

Se crece por incrementos, cada uno con su propia tanda de tareas: añadir otra
carrera, comparar versiones de la normativa, informe anonimizado de dudas
frecuentes para la administración, etc.
