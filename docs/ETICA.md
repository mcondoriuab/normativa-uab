# Consideraciones éticas

## Por qué importa aquí más que en otros proyectos

Una respuesta equivocada sobre normativa no es un error cosmético: puede llevar
a un estudiante a no presentar un recurso a tiempo, a asumir que tiene una
convalidación que no tiene, o a creerse una sanción que no existe. El sistema se
diseña asumiendo que alguien va a actuar según lo que diga.

## Medidas adoptadas

| Riesgo | Medida |
|---|---|
| El sistema inventa normativa | El modelo solo redacta a partir de fragmentos recuperados; nunca se le pide que recuerde |
| Cita algo que no dice eso | La cita literal se muestra siempre, desplegable junto a la respuesta |
| Responde sin base | Filtro de relevancia + instrucción explícita de rechazo |
| Se toma como fuente oficial | Aviso visible en la interfaz y en cada respuesta de la API |
| Se usa para casos personales | El prompt prohíbe opinar sobre situaciones concretas o predecir decisiones |
| Normativa derogada | Versión y vigencia por documento en `CORPUS.md` |

## Privacidad

- **No se registra la identidad** de quien pregunta. No hay login ni cookies.
- Las consultas pueden guardarse **anonimizadas** para evaluar y mejorar. Si se
  hace, se avisa en la interfaz.
- Las preguntas sobre normativa son sensibles: alguien que pregunta por el
  reglamento disciplinario puede estar en un proceso. Tratar los registros en
  consecuencia, o no guardarlos.
- Si se comparte el informe de consultas frecuentes con la administración, va
  **agregado y anonimizado**: patrones, nunca preguntas individuales.

## Sesgos y límites

- El sistema solo sabe lo que hay en el corpus. Normativa de facultad no
  indexada no existe para él, y no lo advierte.
- Los modelos de embeddings funcionan peor con lenguaje muy coloquial o con
  vocabulario local; eso perjudica justo a quien no domina el registro formal.
  Medirlo con las preguntas de tipo `coloquial` del golden set.

## Autoría

El trabajo es de los estudiantes que lo construyen y va firmado por ellos.
Licencia y condiciones de uso: _(se decide en la tarea INV-003 y se anota aquí)_.

## Uso de IA en el propio desarrollo

Se permite usar asistentes de IA para programar, con una regla del grupo: **si
pegaste código generado, tienes que poder explicar cada línea en la siguiente
sesión**. Anotar en las *Notas de cierre* de cada tarea dónde se usó y qué hubo
que corregir — es material interesante para el informe final.
