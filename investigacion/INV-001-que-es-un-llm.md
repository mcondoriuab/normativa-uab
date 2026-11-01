# INV-001: Qué es un LLM, un token y por qué alucina

**Autor(es):** Sarzuri Mamani Joas Jason · **Fecha:** 2026-10-25

## Pregunta

¿Cómo genera texto un LLM, qué son los tokens y la temperatura, y por qué
puede responder con seguridad algo falso?

## Lo que encontramos

### LLM y generación de texto

Un modelo de lenguaje grande (LLM) es un programa entrenado con muchos
ejemplos de texto. Al generar una respuesta, va prediciendo qué token podría
venir a continuación según el texto anterior y las instrucciones recibidas.
Repite ese proceso hasta formar una respuesta. Esto le permite producir texto
fluido, pero predecir una continuación probable no es lo mismo que comprobar
si una afirmación es cierta.

El conocimiento aprendido durante el entrenamiento suele llamarse
*conocimiento paramétrico*: está reflejado en los parámetros del modelo, no
guardado como una colección de artículos que pueda consultar y verificar.
Puede ser incompleto, estar desactualizado o no incluir una norma concreta.

### Tokens

Un token es una pieza de texto que el modelo procesa. Puede ser una palabra,
parte de una palabra, espacios o signos de puntuación. Por eso no hay una
equivalencia fija entre palabras, caracteres y tokens, y la división depende
del tokenizador del modelo.

**Experimento:** el corpus del proyecto todavía no contiene normativa en PDF.
Para tener un ejemplo reproducible, usamos un fragmento del artículo 5.1.a
del Reglamento General de Protección de Datos de la Unión Europea:

> Los datos personales serán: a) tratados de manera lícita, leal y transparente
> en relación con el interesado («licitud, lealtad y transparencia»);

Lo introdujimos en el [tokenizador de OpenAI](https://platform.openai.com/tokenizer),
con la opción «GPT-5.x & O1/3» seleccionada. La herramienta indicó:

| Texto | Caracteres | Tokens | Caracteres por token |
|---|---:|---:|---:|
| Fragmento del reglamento (español) | 145 | 34 | 4,26 |

Separación que mostró la herramienta:

```text
Los | datos | personales | serán | : | a | ) | tratados | de | manera |
lí | c | ita | , | le | al | y | transparente | en | relación | con |
el | interesado | (« | licit | ud | , | le | alt | ad | y |
transparencia | » | );
```

En la vista del tokenizador, los espacios que preceden a algunas piezas no se
aprecian siempre; los separadores `|` se añadieron aquí para distinguirlas.
En este ejemplo, 145 ÷ 34 da aproximadamente 4,26 caracteres por token. Es un
resultado de este texto y tokenizador, no una regla para todo el español.
Además, `lícita`, `licitud` y otras palabras aparecen divididas en varias
piezas.

### Temperatura

La temperatura controla cuánto se favorecen las opciones más probables al
elegir el siguiente token. En general, una temperatura más baja hace que la
salida varíe menos y una más alta permite más variación. No es un medidor de
verdad: bajar la temperatura no comprueba los datos ni elimina las respuestas
falsas. No hicimos una prueba comparando temperaturas; aquí explicamos el
concepto, no presentamos un resultado experimental.

### Por qué puede alucinar

Llamamos alucinación a una respuesta que parece razonable, pero contiene
información falsa o que no está respaldada por el contexto. Como el objetivo
de generación es construir una continuación que encaje con lo anterior, el
modelo puede completar un dato que no conoce con una respuesta plausible en
vez de detenerse. El tono seguro no es una garantía ni una medida de certeza.

**Ejemplo inventado, no referido a una norma real:** alguien pregunta qué
artículo regula el préstamo de calculadoras. Un modelo podría responder
«artículo 18» porque suena a una cita normativa posible, aunque no haya visto
ningún documento que lo confirme.

Las instrucciones pueden permitir que el modelo admita que no tiene
información suficiente, y pedirle que base sus afirmaciones en citas directas
puede ayudar a detectar errores. Son medidas para reducir el riesgo, no una
garantía de que desaparezca.

## Evidencia

- [OpenAI, Key concepts: Tokens](https://developers.openai.com/api/docs/concepts):
  describe los tokens como secuencias comunes de caracteres, explica que se
  predice el siguiente token y advierte que la entrada y la salida comparten
  una ventana de contexto.
- [OpenAI, Tokenizer](https://platform.openai.com/tokenizer): herramienta
  pública usada para contar y ver la división del fragmento del experimento.
- [Reglamento (UE) 2016/679, artículo 5.1.a, EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=es):
  fuente del texto utilizado. Es un reglamento europeo, no normativa propia de
  la UAB.
- [Anthropic, Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations):
  recomienda permitir que el modelo exprese incertidumbre, fundamentar
  respuestas en citas y verificar afirmaciones; indica que estas prácticas
  reducen las alucinaciones, pero no las eliminan.
- [Hugging Face, LLM Course: Introduction](https://huggingface.co/learn/llm-course/chapter1/1):
  presenta los LLM como una parte del campo del procesamiento del lenguaje
  natural y ofrece una introducción al tema.

**Uso de IA:** se usó IA para preparar este borrador. El conteo y la división
de tokens se comprobaron en el tokenizador enlazado, y todas las fuentes citadas
fueron comprobadas antes de presentar el informe.

## Conclusión para el proyecto

La normativa concreta debe venir de documentos recuperados, no de lo que el
modelo parezca recordar. Para nuestro asistente, esto apoya el uso de RAG:
buscar fragmentos de la normativa, pedir al modelo que redacte con esa
evidencia y citar los fragmentos. Si no hay evidencia suficiente, debe poder
decir que no encontró la respuesta. Las citas facilitan la revisión, pero no
evitan por sí solas todos los errores. La temperatura baja puede ayudar a que
las respuestas varíen menos, pero tampoco verifica que sean correctas.

## Preguntas abiertas

- ¿Cuánto cambia la proporción de caracteres por token entre tokenizadores y
  textos distintos en español?
- ¿Qué pruebas servirán para detectar respuestas no respaldadas por los
  fragmentos recuperados?
