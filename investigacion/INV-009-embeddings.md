# INV-009: Embeddings: experimento y elección del modelo

**Autor(es):** Sandra Condori · **Fecha:** 2026-11-15

## Pregunta

¿Cómo se comportan los embeddings con frases parecidas a las que harán los
estudiantes sobre la normativa? ¿Dónde aciertan y dónde fallan? Y, con esos
datos, ¿qué modelo de embeddings por API usamos en el proyecto?

## Lo que encontramos

### Qué es la similitud coseno

Un embedding es una lista de números (un vector). La similitud coseno mide si
dos vectores **apuntan hacia el mismo lado**, sin importar lo largos que sean:

```
coseno(a, b) = (a · b) / (|a| × |b|)
```

Ejemplo con vectores de 2 dimensiones:

| a | b | a · b | \|a\| × \|b\| | coseno | Qué significa |
|---|---|---|---|---|---|
| (1, 0) | (2, 0) | 2 | 1 × 2 = 2 | **1.00** | misma dirección: "significan lo mismo" |
| (1, 0) | (1, 1) | 1 | 1 × 1.41 = 1.41 | **0.71** | parecidos |
| (1, 0) | (0, 1) | 0 | 1 × 1 = 1 | **0.00** | perpendiculares: sin relación |
| (1, 0) | (-1, 0) | -1 | 1 × 1 = 1 | **-1.00** | dirección opuesta |

La primera fila muestra que la longitud no importa: (2, 0) es el doble de largo
que (1, 0), pero el coseno es 1. Nuestro modelo usa vectores de 384 números en
vez de 2, pero la cuenta es la misma.

### Parte 1: experimento con un modelo local

Modelo: `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`
(multilingüe, vector de **384** dimensiones), ejecutado en el ordenador con
`investigacion/INV-009-experimento.py`.

Las 10 frases:

| Etiqueta | Frase | Grupo |
|---|---|---|
| P1a | me pueden echar por faltar mucho a clases | pareja 1 |
| P1b | pérdida de la condición de estudiante por inasistencias | pareja 1 |
| P2a | cuánto tengo que sacar para aprobar una materia | pareja 2 |
| P2b | nota mínima de aprobación de una asignatura | pareja 2 |
| P3a | me pueden dar una beca si tengo buenas notas | pareja 3 |
| P3b | requisitos para obtener una beca por rendimiento académico | pareja 3 |
| C1 | el banco de la plaza está recién pintado | comparten palabra |
| C2 | el banco me cobró una comisión por la transferencia | comparten palabra |
| S1 | mañana va a llover en Cochabamba | sin relación |
| S2 | la receta lleva dos huevos y harina | sin relación |

Matriz de similitud coseno:

|  | P1a | P1b | P2a | P2b | P3a | P3b | C1 | C2 | S1 | S2 |
|---|---|---|---|---|---|---|---|---|---|---|
| **P1a** | 1.00 | **0.62** | 0.34 | 0.23 | 0.55 | 0.44 | 0.05 | 0.20 | 0.05 | 0.00 |
| **P1b** | 0.62 | 1.00 | 0.36 | 0.44 | 0.25 | 0.61 | 0.02 | 0.14 | -0.04 | -0.13 |
| **P2a** | 0.34 | 0.36 | 1.00 | **0.57** | 0.33 | 0.55 | 0.03 | 0.37 | 0.04 | -0.01 |
| **P2b** | 0.23 | 0.44 | 0.57 | 1.00 | 0.37 | 0.44 | 0.05 | 0.25 | 0.05 | -0.00 |
| **P3a** | 0.55 | 0.25 | 0.33 | 0.37 | 1.00 | **0.42** | 0.21 | 0.26 | 0.13 | 0.19 |
| **P3b** | 0.44 | 0.61 | 0.55 | 0.44 | 0.42 | 1.00 | 0.04 | 0.15 | -0.03 | -0.07 |
| **C1** | 0.05 | 0.02 | 0.03 | 0.05 | 0.21 | 0.04 | 1.00 | **0.28** | 0.18 | 0.07 |
| **C2** | 0.20 | 0.14 | 0.37 | 0.25 | 0.26 | 0.15 | 0.28 | 1.00 | -0.06 | 0.04 |
| **S1** | 0.05 | -0.04 | 0.04 | 0.05 | 0.13 | -0.03 | 0.18 | -0.06 | 1.00 | 0.10 |
| **S2** | 0.00 | -0.13 | -0.01 | -0.00 | 0.19 | -0.07 | 0.07 | 0.04 | 0.10 | 1.00 |

Prueba extra: `"artículo 47"` frente a `"artículo 48"` → **0.877**.

#### Observaciones

<!-- TODO (Sandra): revisa estas observaciones y reescríbelas con tus palabras. -->

1. **Acierto: entiende frases distintas que dicen lo mismo.** P1a ("me pueden
   echar por faltar") y P1b ("pérdida de la condición de estudiante por
   inasistencias") no comparten casi ninguna palabra y aun así dan 0.62. Igual
   con la pareja 2 (0.57). Esto es lo que BM25 no puede hacer.
2. **Fallo: el estilo pesa más que el tema.** La pareja de becas (P3a–P3b) solo
   da 0.42, y P3b se parece más a P1b (0.61), que habla de inasistencias. Las
   dos usan lenguaje formal de reglamento ("requisitos", "condición de
   estudiante"). Una pregunta coloquial puede quedar más lejos de su artículo
   que otro artículo cualquiera.
3. **Acierto: no se deja engañar por una palabra compartida.** C1 y C2 usan
   "banco" con dos significados distintos y dan solo 0.28. Las frases sin
   relación (S1, S2) quedan cerca de 0 con todo.
4. **Fallo importante para nosotros: los números no importan.** "artículo 47"
   y "artículo 48" dan 0.877, casi iguales. Si alguien pregunta por un
   artículo concreto, la búsqueda vectorial no lo distingue de sus vecinos.
   Por eso necesitamos también BM25 (IA-007).
5. **Los valores son bajos en general.** Ninguna pareja pasa de 0.62. No hay un
   umbral "mágico" universal; habrá que fijarlo con nuestros datos (IA-016).

### Parte 2: comparación de modelos por API

Con `investigacion/INV-009-comparar-modelos.py` codificamos los 293
fragmentos de `data/fragmentos.json` y las 15 preguntas del golden set con
`en_corpus: true`. Para cada pregunta ordenamos los fragmentos por coseno y
miramos si el `id_esperado` sale entre los 5 primeros.

| Modelo | Proveedor | Dimensión | Documento/pregunta | Aciertos top-5 | Tokens usados | Tiempo | Cuota gratuita |
|---|---|---|---|---|---|---|---|
| paraphrase-multilingual-MiniLM-L12-v2 (referencia local) | sentence-transformers | 384 | no | **7/15** | — | 9 s | local, sin cuota |
| `voyage-4` | Voyage AI | 1024 (también 256, 512, 2048) | sí (`input_type`) | **13/15** | 45.618 | 317 s | 200 M tokens |
| `voyage-multilingual-2` | Voyage AI | 1024 (fija) | sí (`input_type`) | **13/15** | 56.405 | 419 s | dudosa (ver abajo) |

Aciertos por tipo de pregunta:

| Modelo | Coloquial | Literal | Multi-artículo |
|---|---|---|---|
| local MiniLM | 2/7 | 4/5 | 1/3 |
| `voyage-4` | 5/7 | 5/5 | 3/3 |
| `voyage-multilingual-2` | 5/7 | 5/5 | 3/3 |

Lo que observamos:

<!-- TODO (Sandra): revisa y reescribe con tus palabras. -->

- **Los dos modelos de Voyage casi duplican al modelo local**, sobre todo en
  las preguntas coloquiales (5/7 frente a 2/7). Que distingan pregunta y
  documento (`input_type`) puede ser parte del motivo: es justo el fallo de
  estilo de la observación 2 de la Parte 1.
- **Los dos modelos de Voyage empatan en aciertos.** Con 15 preguntas, la
  diferencia de calidad entre ellos no se ve; decidimos por coste y cuota.
- **`voyage-multilingual-2` gasta un 24 % más de tokens** con los mismos
  textos (usa otro tokenizador).
- **El tiempo lo pone el límite de velocidad, no el modelo.** Sin método de
  pago, Voyage limita a **3 peticiones y 10.000 tokens por minuto** (lo dice el
  mensaje de error 429). Con lotes de 50 fragmentos `voyage-multilingual-2`
  fallaba siempre; con lotes de 20 y esperas de 60 s funcionó. Indexar todo
  tarda unos 5 minutos, pero solo se hace una vez (IA-008).
- **Cuota de `voyage-multilingual-2`:** la página de precios lo pone en la
  lista de 50 M tokens gratis, pero en la tabla de modelos antiguos dice que
  para esos modelos no hay tokens gratis. No está claro.

## Evidencia

- Experimento propio: `investigacion/INV-009-experimento.py` (2026-11-15).
  Cualquiera que lo ejecute obtiene la misma tabla.
- Documentación del modelo local:
  <https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2>
- Experimento propio: `investigacion/INV-009-comparar-modelos.py`
  (2026-11-15). Se ejecutó 3 veces; `voyage-4` dio 13/15 y 45.618 tokens en
  todas.
- Documentación de Voyage AI, consultada el 2026-11-15:
  - <https://docs.voyageai.com/docs/embeddings>: modelos, dimensiones,
    `input_type` (`"query"` / `"document"`) y máximo de 1.000 textos por
    llamada.
  - <https://docs.voyageai.com/docs/pricing>: `voyage-4` cuesta 0,06 USD por
    millón de tokens y los primeros 200 M son gratis en cada cuenta.
  - <https://docs.voyageai.com/docs/rate-limits>: límites con método de pago
    (`voyage-4`: 8 M tokens y 2.000 peticiones por minuto). Sin método de pago
    no lo documenta; el límite de 3 peticiones / 10K tokens por minuto sale del
    mensaje de error.

## Conclusión para el proyecto

Usaremos **`voyage-4` con vectores de 1024 dimensiones**, indicando
`input_type="document"` al indexar e `input_type="query"` al buscar. La
decisión está en
[ADR-008](../historial/decisiones/ADR-008-modelo-embeddings.md).

Los embeddings sirven para las preguntas coloquiales, pero fallan con
identificadores exactos como números de artículo. Esto confirma la búsqueda
híbrida (BM25 + vectorial) prevista en IA-007.

Para IA-008: con la cuenta gratuita hay que indexar en lotes pequeños y
esperar cuando la API devuelve 429.

## Preguntas abiertas

- ¿Qué 2 preguntas coloquiales fallan los dos modelos de Voyage? Mirarlas
  puede indicar si el problema está en la pregunta o en cómo troceamos los
  artículos (IA-012).
- Con solo 15 preguntas, un empate no dice mucho. Si el golden set crece,
  conviene repetir la comparación.

## Uso de IA

Se usó Claude Code para escribir el script del experimento y el borrador de
este informe. Los números de la tabla salen de ejecutar el script, no de la IA.
