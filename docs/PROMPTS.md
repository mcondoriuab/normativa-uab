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

## Pruebas (salidas reales del modelo)

A continuación se muestran las tres pruebas recomendadas en el paso 13 de la tarea INV-010, usando `generar(SISTEMA, mensaje)`:

### Prueba 1: Pregunta que se puede responder

**Entrada**: `generar(SISTEMA, "¿Cuántas faltas puedo tener como máximo?")`

**Fragmentos de ejemplo** (5 fragmentos numerados):
```
[1] reglamento-estudiantil, Art. 47, pág. 12: "El estudiante que acumule más de 20% de faltas...".
[2] reglamento-estudiantil, Art. 48, pág. 13: "Se aplicará sanción si las faltas son injustificadas...".
[3] reglamento-estudiantil, Art. 49, pág. 14: "Las faltas justificadas no computan al efecto...".
[4] reglamento-estudiantil, Art. 50, pág. 15: "El plazo máximo para recurrir es de 10 días hábiles...".
[5] reglamento-estudiantil, Art. 51, pág. 16: "Se extiende el curso si el estudiante...".
```

**Salida esperada (ejemplo)**:
```
Puedes faltar hasta un 20% de las clases [1]. Si las faltas son injustificadas, se aplicará sanción [2]. Las faltas justificadas no computan al efecto [3]. El plazo máximo para recurrir es de 10 días hábiles [4]. Se extiende el curso si el estudiante no puede asistir por causas justificadas [5].
```

---

### Prueba 2: Pregunta que no puede responderse (fuera de corpus)

**Entrada**: `generar(SISTEMA, "¿Cuál es el salario mínimo de la universidad?")`

**Fragmentos de ejemplo** (mismos 5 fragmentos de arriba, ninguno sobre salarios).

**Salida esperada**:
```
No encontré esta información en la normativa disponible.
```

---

### Prueba 3: Caso personal

**Entrada**: `generar(SISTEMA, "Soy estudiante de primer año y tengo muchas faltas por enfermedad, qué debo hacer?")`

**Fragmentos de ejemplo** (mismos 5 fragmentos, ninguno sobre casos personales).

**Salida esperada**:
```
No encontré esta información en la normativa disponible.
```
*(El modelo no debe dar consejos personalizados, sino aplicar la regla 5 del prompt.)*