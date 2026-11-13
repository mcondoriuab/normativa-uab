# INV-002: ¿"Entrenar" la IA? Fine-tuning frente a prompt largo frente a RAG

**Autor(es):** Sandra Condori · **Fecha:** 2026-11-12

> Parte 2 de INV-002. La Parte 1 (estado del arte) está en
> [`INV-002-estado-del-arte.md`](INV-002-estado-del-arte.md).

## Pregunta

Decimos que vamos a "entrenar la IA con la normativa", pero hay tres formas de
darle a un LLM un conocimiento que no tiene. ¿Cuál nos conviene para un
asistente que responda sobre la normativa de la UAB **citando el artículo
exacto**?

## Lo que encontramos

### Los tres enfoques, en nuestras palabras

- **Fine-tuning (ajuste fino):** se toma un modelo ya entrenado y se le sigue
  entrenando con ejemplos nuestros (por ejemplo, pares pregunta-respuesta sobre
  la normativa). El conocimiento queda guardado *dentro* de los pesos del
  modelo, mezclado con todo lo demás que sabe. No se puede abrir el modelo para
  ver de qué artículo sacó una respuesta.
- **Prompt largo:** no se cambia el modelo. En cada pregunta se le pega
  **toda** la normativa en el prompt y se le pide que responda con ella. Es
  sencillo, pero cada pregunta "paga" por leer todos los reglamentos otra vez, y
  solo funciona si caben en la ventana de contexto.
- **RAG (generación aumentada por recuperación):** tampoco se cambia el modelo.
  La normativa se trocea por artículos y se indexa. Ante cada pregunta,
  **buscamos** los pocos artículos más relevantes (unos 5) y solo esos se le
  pasan al modelo, pidiéndole que responda con ellos y los cite.

### Tabla comparativa

| Criterio | Fine-tuning | Prompt largo | RAG |
|---|---|---|---|
| **Coste** | Alto al principio: hay que preparar cientos de ejemplos y pagar o tener GPU para entrenar. Luego cada pregunta es barata | Sin preparación, pero **muy caro por pregunta**: unos 131.000 tokens de entrada cada vez (ver cálculo). En el plan gratuito de Groq no cabe ni un reglamento por minuto | Coste medio al principio (trocear e indexar, una vez) y **barato por pregunta**: unos 800 tokens de normativa por pregunta |
| **Cuando cambia la normativa** | Hay que volver a generar ejemplos y **reentrenar**. Mientras tanto, el modelo responde con la versión vieja | Basta con cambiar el texto que se pega. Fácil | Basta con **volver a indexar** el reglamento cambiado. Fácil |
| **¿Puede citar el artículo exacto?** | **No de forma fiable.** El modelo no sabe de dónde viene lo que "sabe"; puede inventar el número de artículo | Sí, en teoría, porque el texto está en el prompt. Pero con mucho texto el modelo elige peor qué citar (PoliChat, Parte 1) | **Sí.** Cada fragmento lleva documento, artículo y página (contrato *Fragmento* de `docs/ARQUITECTURA.md`) y la cita se puede comprobar |
| **Riesgo de alucinar** | **Alto.** En Unipa-GPT el modelo ajustado "generate loops and hallucinations" y no mejoró (Parte 1) | Medio: tiene la información, pero se "pierde" entre mucho texto irrelevante | **Medio-bajo**, pero **no cero**: herramientas legales con RAG alucinan entre el 17 % y el 33 % (Stanford, Parte 1). Se reduce con cita obligatoria y rechazo |
| **Dificultad para el equipo** | **Alta**: preparar datos de entrenamiento, GPU, hiperparámetros. Poco que podamos explicar línea a línea | **Baja** de programar, pero choca con límites de tokens y coste | **Media**: trocear, buscar (BM25 y vectorial) y armar el prompt. Cada pieza es pequeña y se puede explicar, y ya está repartida en tareas (IA-002, IA-007, IA-008) |

### Cálculo: ¿cabe toda la normativa en un prompt?

Datos:

- Reglamento público de la UAB: **Reglamento Estudiantil (2016)**, texto en
  `corpus/ingenieria-sistemas/reglamento-estudiantil-2016.md` (convertido del
  PDF con markitdown). Lo contamos con Python (`len(texto)`):
  **55.991 caracteres**.
- Proporción de INV-001: **4,26 caracteres por token** (tokenizador de OpenAI,
  sobre un fragmento de reglamento en español).

Cálculo:

```text
Un reglamento:   55.991 caracteres ÷ 4,26 caracteres/token ≈ 13.143 tokens
10 documentos:   13.143 tokens × 10                         ≈ 131.434 tokens
```

Comparación con dos modelos actuales (consultados el 2026-11-12):

| Modelo | Ventana de contexto | ¿Caben 131.434 tokens? | Fuente |
|---|---:|---|---|
| `openai/gpt-oss-120b` en Groq (el elegido en ADR-009) | 131.072 tokens | **No**: se pasa en unos 360 tokens (100,3 % de la ventana), y aún faltaría sitio para la pregunta y la respuesta | [Groq, ficha del modelo](https://console.groq.com/docs/model/openai/gpt-oss-120b) |
| `gemini-3.8-flash` (Google) | 1.048.576 tokens | **Sí**: ocupa el 12,5 % de la ventana | [Google AI, ficha del modelo](https://aistudio.google.com/docs/models/gemini-3.8-flash) |

Que quepa no significa que convenga:

- **Límite por minuto.** ADR-009 anota para Groq gratuito un límite de **8.000
  tokens por minuto** ([límites de Groq](https://console.groq.com/docs/rate-limits)).
  Un solo reglamento (unos 13.000 tokens) ya lo supera: con prompt largo no
  podríamos responder **ni una pregunta por minuto**.
- **Coste.** En Gemini 3.8 Flash de pago, la entrada cuesta 0,75 USD por millón
  de tokens hasta el 31/12/2026 y 1,50 USD desde 2027
  ([precios de Gemini](https://aistudio.google.com/docs/pricing)). Con prompt
  largo: 131.434 × 0,75 / 1.000.000 ≈ **0,10 USD por pregunta**, unos
  **99 USD por cada 1.000 preguntas**. El nivel gratuito existe, pero según esa
  misma página usa los datos "to improve our products", lo que ADR-009 ya
  descartó por privacidad.
- **Comparación con RAG** (estimación nuestra): el Reglamento Estudiantil tiene
  82 artículos, unos 683 caracteres por artículo, o sea unos 160 tokens.
  Cinco artículos son unos **800 tokens**: más de **160 veces menos** que el
  prompt largo.

Nota: hoy el corpus tiene 5 reglamentos y no 10 (172.602 caracteres, unos
40.517 tokens). La tarea pide el cálculo con 10 documentos porque el corpus
crecerá; con 5 ya superamos cinco veces el límite por minuto de Groq.

### Evidencia propia: INV-012 e INV-013

> **Pendiente de completar** cuando se integren los informes
> `investigacion/INV-012-alucinaciones.md` e `investigacion/INV-013-rag-a-mano.md`.
> No se rellena con datos supuestos: hay que copiar aquí sus resultados reales.

- **INV-012 (alucinaciones):** _cuántas preguntas sobre la normativa de la UAB
  se hicieron a chatbots sin documentos, y cuántas respuestas inventaron
  artículos, plazos o cifras._ Esto mide el riesgo de confiar en lo que el
  modelo "sabe" (lo más parecido a un fine-tuning sin datos nuestros).
- **INV-013 (RAG a mano):** _cuántas respuestas fueron correctas y con cita
  **sin** pasarle los artículos al modelo y cuántas **con** los artículos._ Es
  nuestra prueba directa de lo que aporta RAG.

## Evidencia

- Cálculo de caracteres: script de una línea con Python sobre los `.md` del
  corpus (`len(open(archivo, encoding="utf-8").read())`). Resultados: Becas
  20.882; Graduación 45.434; Interacción Social 16.419; Investigación 33.876;
  Estudiantil 55.991.
- [INV-001](INV-001-que-es-un-llm.md): 4,26 caracteres por token.
- [Groq, ficha de `openai/gpt-oss-120b`](https://console.groq.com/docs/model/openai/gpt-oss-120b)
  (consultado 2026-11-12): "CONTEXT WINDOW 131,072" y "MAX OUTPUT TOKENS 65,536".
- [Groq, límites](https://console.groq.com/docs/rate-limits) (consultado
  2026-11-12): fila de `openai/gpt-oss-120b` con 30 RPM, 1K RPD, 8K TPM, 200K
  TPD. La página tiene pestañas de plan *Free* y *Developer* y la extracción no
  dejó claro a cuál pertenece la tabla; coincide con lo que anotó ADR-009 para
  el plan gratuito.
- [Google AI, ficha de `gemini-3.8-flash`](https://aistudio.google.com/docs/models/gemini-3.8-flash)
  (consultado 2026-11-12): "Input token limit 1,048,576", "Output token limit
  65,536".
- [Google AI, precios](https://aistudio.google.com/docs/pricing) (consultado
  2026-11-12): Gemini 3.8 Flash, entrada de pago 0,75 USD por millón de tokens
  hasta el 31/12/2026.
- Parte 1 de esta tarea: Unipa-GPT (el fine-tuning no mejoró), ChatLaw (el
  fine-tuning solo no basta), PoliChat (mucho contexto empeora las citas),
  Stanford (RAG reduce pero no elimina las alucinaciones).

**Uso de IA:** usamos un asistente de IA (Claude) para leer las páginas de Groq
y Google y para hacer las cuentas. Las cifras de las fichas se comprobaron en
las páginas enlazadas y las cuentas se pueden repetir con los números de este
informe.

## Conclusión para el proyecto

Lo que **concluimos nosotros**:

- **RAG** es el único de los tres que cumple a la vez lo que pide
  `docs/VISION.md`: citar el artículo exacto, actualizarse sin reentrenar,
  funcionar dentro del plan gratuito y que el equipo pueda entender cada pieza.
- El **prompt largo** no es viable con el proveedor elegido (no cabe en la
  ventana y supera el límite por minuto), y con otro proveedor costaría unas 160
  veces más por pregunta.
- El **fine-tuning** no permite citar con fiabilidad, obliga a reentrenar con
  cada cambio y, en los proyectos que lo probaron, no mejoró los resultados.
- RAG **no** elimina las alucinaciones: por eso mantenemos la cita obligatoria,
  el rechazo ("no lo encuentro") y la medición con el golden set.

Decisión registrada en
[ADR-007](../historial/decisiones/ADR-007-enfoque-rag.md).

## Preguntas abiertas

- ¿La proporción de 4,26 caracteres por token vale también para el tokenizador
  de `gpt-oss-120b`? Se midió con un fragmento de 145 caracteres; con todo el
  reglamento podría variar.
- ¿Cuántos fragmentos (k) conviene pasar al modelo? Elegimos unos 5 por la
  Parte 1, pero hay que medirlo con el golden set.
- Si algún día hiciera falta, ¿tendría sentido un fine-tuning pequeño solo para
  el *estilo* de las respuestas (no para el contenido), manteniendo RAG?
