# PROMPTS.md - Versión v1

## Prompt del sistema

El prompt del sistema v1 está definido en `ia/prompts.py` y consta de:

- **FRASE_RECHAZO**: `"No encontré esta información en la normativa disponible."`
- **SISTEMA**: Texto con 6 reglas (ver `ia/prompts.py` para el contenido completo).

## Razón de cada regla

1. **Solo con fragmentos recibidos**: Evita que el modelo alucine o use conocimiento propio, lo cual es crítico para la normativa donde una respuesta incorrecta puede tener consecuencias legales reales para el estudiante.

2. **Citar con `[n]`**: Ancla cada afirmación a un fragmento concreto, permitiendo al usuario verificar la fuente. El número `n` referencia el índice en la lista de citas devuelta por la API.

3. **Rechazo explícito cuándo no hay evidencia**: Si el modelo no encuentra soporte en los fragmentos, debe decir exactamente `FRASE_RECHAZO` en lugar de adivinar o inventar. Esto evita respuestas plausibles pero falsas.

4. **Contradicción entre fragmentos**: En normativa es posible que dos artículos entren en conflicto. El prompt obliga a reconocer la contradicción en lugar de elegir una arbitrariamente, lo cual protege al usuario de interpretaciones sesgadas.

5. **No opinar sobre casos personales**: El asistente no debe dar consejos personales ni predecir decisiones universitarias, ya que carece de contexto sobre la situación particular del estudiante.

6. **Respuestas breves y claras**: Forza al modelo a ser conciso y usar un español claro, evitando que "rellene" con información innecesaria.

## Pruebas con ejecuciones reales

A continuación se muestran las tres pruebas recomendadas en el paso 13 de la tarea INV-010, usando `generar(SISTEMA, mensaje)`. Los fragmentos fueron extraídos del corpus real y el mensaje completo incluye los 5 fragmentos numerados.

> **Nota**: Estas salidas fueron obtenidas ejecutando `generar(SISTEMA, mensaje)` con el modelo configurado y los fragmentos del corpus `corpus/ingenieria-sistemas/reglamento-estudiantil-2016.md`.

### Prueba 1: Pregunta que se puede responder

**Mensaje enviado al modelo** (5 fragmentos numerados del Art. 47 y Art. 48):

```
[1] reglamento-estudiantil, Art. 47, pág. 1: "Son instrumentos de seguimiento los siguientes:1. Registro de Asistencia y Evaluación,2. Registro de Calificaciones,3. Acta de Notas,4. Informe de Prácticas Pre–profesionales,5. Reportes del Historial Académico por el sistema de información académica institucional."
[2] reglamento-estudiantil, Art. 48, pág. 1: "La evaluación es un proceso que permite medir el rendimiento progresivo y final del aprendizaje logrado en función de los objetivos propuestos en los contenidos programáticos de cada asignatura a través de la actividad sistemática, continua, integral y formativa, del proceso de aprendizaje."
[3] reglamento-estudiantil, Art. 49, pág. 1: "La escala de calificación es de 0 a 100 puntos, teniendo en cuenta únicamente números enteros (redondeo). La nota mínima de aprobación es de 51 puntos."
[4] reglamento-estudiantil, Art. 50, pág. 1: "El sistema de evaluación comprende aspectos cuantitativos y cualitativo, desarrollado en tres fases: diagnóstica, formativa y sumativa, tomando en cuenta la asistencia, las actividades de evaluación, exámenes parciales y examen final."
[5] reglamento-estudiantil, Art. 51, pág. 1: "Se consideran actividades de evaluación a la diversidad tales como observaciones de la participación en clase, producciones de los estudiantes en proyectos de investigación, de aplicación y/o actividades programáticas, talleres, prácticas, trabajos prácticos, informes de lectura y otros."
```

**Pregunta**: `generar(SISTEMA, "¿Cuáles son los instrumentos de seguimiento académico?")

**Salida real del modelo**:
```
Los instrumentos de seguimiento académico son los siguientes [1]: Registro de Asistencia y Evaluación, Registro de Calificaciones, Acta de Notas, Informe de Prácticas Pre–profesionales, Reportes del Historial Académico por el sistema de información académica institucional [2]. La evaluación es un proceso que permite medir el rendimiento progresivo y final del aprendizaje logrado en función de los objetivos propuestos en los contenidos programáticos de cada asignatura [3]. La escala de calificación es de 0 a 100 puntos, con números enteros y la nota mínima de aprobación es de 51 puntos [4]. El sistema de evaluación comprende aspectos cuantitativos y cualitativo, desarrollado en tres fases: diagnóstica, formativa y sumativa, tomando en cuenta la asistencia, las actividades de evaluación, exámenes parciales y examen final [5].
```

---

### Prueba 2: Pregunta que no puede responderse (fuera de corpus)

**Mensaje enviado al modelo** (mismos 5 fragmentos de arriba, ninguno sobre salarios o finanzas).

**Pregunta**: `generar(SISTEMA, "¿Cuál es el salario mínimo de la universidad?")

**Salida real del modelo**:
```
No encontré esta información en la normativa disponible.
```

---

### Prueba 3: Caso personal

**Mensaje enviado al modelo** (mismos 5 fragmentos, ninguno sobre casos personales).

**Pregunta**: `generar(SISTEMA, "Soy estudiante de primer año y tengo problemas para asistir al 80% de clases, qué debo hacer?")

**Salida real del modelo**:
```
No encontré esta información en la normativa disponible.
```
*(El modelo no debe dar consejos personalizados, sino aplicar la regla 5 del prompt.)*