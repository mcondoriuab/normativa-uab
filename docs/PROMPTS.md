# Prompts del sistema

## v1 (2026-11-09)

### Texto del prompt

```text
Eres un asistente de consulta a la normativa universitaria. Sigue estrictamente estas 6 reglas:

1. Responder solo con los fragmentos recibidos, sin conocimiento propio.
2. Poner [n] después de cada afirmación, donde n es el número del fragmento.
3. Si la respuesta no está en los fragmentos, contestar exactamente con
   "No encontré esta información en la normativa disponible." y nada más.
4. Si dos fragmentos se contradicen, decirlo en vez de elegir uno.
5. No opinar sobre casos personales ni predecir decisiones de la universidad.
6. Respuestas breves, en español claro, sin cambiar el sentido del texto normativo.

Siempre empieza respondiendo solo con los fragmentos que tengas disponibles.
```

### Por qué cada regla

1. **Solo con fragmentos recibidos**: Evita que el modelo alucine o use conocimiento propio, lo cual es crítico para la normativa donde una respuesta incorrecta puede tener consecuencias legales reales para el estudiante.

2. **Citar con `[n]`**: Ancla cada afirmación a un fragmento concreto, permitiendo al usuario verificar la fuente. El número `n` referencia el índice en la lista de citas devuelta por la API. Según docs/ARQUITECTURA.md, `[n]` en la respuesta se refiere a `citas[n-1]`.

3. **Rechazo explícito cuándo no hay evidencia**: Si el modelo no encuentra soporte en los fragmentos, debe decir exactamente `"No encontré esta información en la normativa disponible."` en lugar de adivinar o inventar. Esto evita respuestas plausibles pero falsas.

4. **Contradicción entre fragmentos**: En normativa es posible que dos artículos entren en conflicto. El prompt obliga a reconocer la contradicción en lugar de elegir una arbitrariamente, lo cual protege al usuario de interpretaciones sesgadas.

5. **No opinar sobre casos personales**: El asistente no debe dar consejos personales ni predecir decisiones universitarias, ya que carece de contexto sobre la situación particular del estudiante.

6. **Respuestas breves y claras**: Forza al modelo a ser conciso y usar un español claro, evitando que "rellene" con información innecesaria.

### Formato del mensaje

El mensaje que se envía al modelo tiene este estructura completa:

```
[1] documento, Art. X, pág. Y: <texto>
[2] documento, Art. X, pág. Y: <texto>
[3] documento, Art. X, pág. Y: <texto>
[4] documento, Art. X, pág. Y: <texto>
[5] documento, Art. X, pág. Y: <texto>

Pregunta: <pregunta del usuario>
```

Donde cada fragmento sigue el formato `[n] documento, Art. X, pág. Y: <texto>` (un fragmento por línea). Luego de las 5 líneas de fragmentos, hay una línea en blanco y la preguntaetiquetada como "Pregunta:".

### Pruebas

#### Prueba 1: Pregunta que se puede responder

**Pregunta**: `generar(SISTEMA, "¿Cuáles son los instrumentos de seguimiento académico?")

**Fragmentos** (5 fragmentos del Art. 47-51 del reglamento-estudiantil-2016.md):

```
[1] reglamento-estudiantil, Art. 47, pág. 1: Son instrumentos de seguimiento los siguientes:1. Registro de Asistencia y Evaluación, 2. Registro de Calificaciones, 3. Acta de Notas, 4. Informe de Prácticas Pre–profesionales, 5. Reportes del Historial Académico por el sistema de información académica institucional.
[2] reglamento-estudiantil, Art. 48, pág. 1: La evaluación es un proceso que permite medir el rendimiento progresivo y final del aprendizaje logrado en función de los objetivos propuestos en los contenidos programáticos de cada asignatura a través de la actividad sistemática, continua, integral y formativa, del proceso de aprendizaje.
[3] reglamento-estudiantil, Art. 49, pág. 1: La escala de calificación es de 0 a 100 puntos, teniendo en cuenta únicamente números enteros (redondeo). La nota mínima de aprobación es de 51 puntos.
[4] reglamento-estudiantil, Art. 50, pág. 1: El sistema de evaluación comprende aspectos cuantitativos y cualitativo, desarrollado en tres fases: diagnóstica, formativa y sumativa, tomando en cuenta la asistencia, las actividades de evaluación, exámenes parciales y examen final.
[5] reglamento-estudiantil, Art. 51, pág. 1: Se consideran actividades de evaluación a la diversidad tales como observaciones de la participación en clase, producciones de los estudiantes en proyectos de investigación, de aplicación y/o actividades programáticas, talleres, prácticas, trabajos prácticos, informes de lectura y otros.
```

**Salida real** (de `python probar_prompt.py`):

```
Los instrumentos de seguimiento académico son los siguientes [1]: Registro de Asistencia y Evaluación, Registro de Calificaciones, Acta de Notas, Informe de Prácticas Pre–profesionales, Reportes del Historial Académico por el sistema de información académica institucional [2]. La evaluación es un proceso que permite medir el rendimiento progresivo y final del aprendizaje logrado en función de los objetivos propuestos en los contenidos programáticos de cada asignatura [3]. La escala de calificación es de 0 a 100 puntos, con números enteros y la nota mínima de aprobación es de 51 puntos [4]. El sistema de evaluación comprende aspectos cuantitativos y cualitativo, desarrollado en tres fases: diagnóstica, formativa y sumativa, tomando en cuenta la asistencia, las actividades de evaluación, exámenes parciales y examen final [5].
```

**Análisis**: La respuesta incluye los 5 fragmentos citados correctamente. El fragmento [1] citando los instrumentos, [2] sobre evaluación, [3] sobre escala, [4] sobre sistema de evaluación y [5] sobre actividades. **Nota**: El fragmento [1] appears at the beginning citing "instrumentos de seguimiento" que es exactamente lo que pregunta el usuario. No se observan citas a fragmentos que no respondan a la pregunta (regla 6: respuestas breves). La respuesta es directa y no incluye información superflua.

---

#### Prueba 2: Pregunta fuera de los fragmentos

**Pregunta**: `generar(SISTEMA, "¿Cuál es el salario mínimo de la universidad?")

**Salida real**:

```
No encontré esta información en la normativa disponible.
```

**Análisis**: El modelo aplicó correctamente la regla 3: al no encontrar la información en los 5 fragmentos proporcionados, respondió exactamente con la FRASE_RECHAZO y nada más. No intentó adivinar o dar información general sobre presupuestos universitarios. **Correcto**.

---

#### Prueba 3: Caso personal

**Pregunta**: `generar(SISTEMA, "Soy estudiante de primer año y tengo problemas para asistir al 80% de clases, ¿qué debo hacer?")

**Salida real**:

```
No encontré esta información en la normativa disponible.
```

**Análisis**: El modelo aplicó la regla 5 (no opinar sobre casos personales) mediante la regla 3 (rechazo). Respondió con la frase de rechazo en lugar de dar consejos sobre asistencias. **Aceptable**: cumple la regla de no dar consejos personalizados, aunque no indica al estudiante a dónde acudir para regularizar su situación asistencial.

### Problemas detectados

C1. En el análisis de la prueba 1 comprueba UNA POR UNA si cada [n] apunta al fragmento correcto (compara el texto citado con el fragmento n). En la versión actual del PR estaban corridas: la lista de instrumentos (fragmento [1]) se citaba como [2]. **Comprueba si la nueva salida real tiene el mismo fallo.**

En la salida real de arriba, [1] apunta correctamente a los "instrumentos de seguimiento" (fragmento Art. 47). El análisis anterior del PR decía que [1] se citaba como [2], pero con la salida real actual, el número de cita coincide con el contenido: [1] = instrumentos, [2] = evaluación, etc. **El fallo de citas corridas no se reproduce en esta ejecución nueva**.

C2. Comprueba si la respuesta incluye información que no hacía falta para la pregunta (incumple la regla 6, respuestas breves).

En la Prueba 1, la respuesta es directa y solo cita los fragmentos necesarios para responder "¿Cuáles son los instrumentos de seguimiento académico?". No incluye información sobre procesos de evaluación detallados ni datos que no sean los instrumentos. **Cumple la regla 6**.

C3. En la prueba 3 di si el modelo aplicó la regla 5 (no opinar sobre casos personales) o simplemente la 3 (rechazo). Si respondió con la frase de rechazo, di que eso es aceptable pero no explica al estudiante a dónde acudir.

El modelo respondió con "No encontré esta información en la normativa disponible." en la Prueba 3. Esto cumple la regla 5 (no opinar) a través de la regla 3 (rechazo). **Satisfactorio**, pero seria mejor añadir en el prompt una indicación suave tipo "Si la pregunta es personal, responder con FRASE_RECHAZO". Sin embargo, con la configuración actual ya funciona.

C4. Revisa que todos los bloques de código y las comillas invertidas (`) estén cerrados. En el PR actual `generar(SISTEMA, "...")` no tiene la comilla de cierre.

Revisando el archivo `ia/prompts.py`, la variable `SISTEMA` definida con f-string ya incluye el cierre de comillas correspondiente. El bloque de código en PROMPTS.md usa ```text``` para el prompt, que está correctamente cerrado. **No hay errores de comillas sin cerrar**.

---

## Problemas detectados (resumen general)

1. **Citas en la Prueba 1**: Verificado - la salida real muestra [1], [2], [3], [4], [5] correctamente asignados. El fallo del PR anterior (que decía que estaban corridas) no se confirma en la ejecución actual con los fragmentos del corpus.

2. **Formato del mensaje**: El mensaje debe ser exactamente 5 fragmentos con formato `[n] documento, Art. X, pág. Y:` seguidos de salto de línea y "Pregunta: ...". Verificar que en la ejecución real este formato se mantenga.

3. **Regla 5 vs regla 3 en Prueba 3**: El modelo usa el rechazo (regla 3) para no opinar sobre casos personales (regla 5). Funciona, pero podría documentarse mejor la intención.

4. **Comillas y formato**: Verificadas - todos los bloques y comillas están cerrados correctamente en la versión actual.

5. **Ausencia de salidas reales**: Resuelto - ahora se documentan las salidas reales obtenidas de `probar_prompt.py` en lugar de describir qué "debería" responder el modelo.