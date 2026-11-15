# ADR-008: modelo de embeddings

**Estado:** propuesta · **Fecha:** 2026-11-15 · **Tarea:** INV-009

## Contexto

La búsqueda vectorial (IA-008) necesita convertir los fragmentos y las
preguntas en embeddings. La API corre en Render con 512 MB de RAM, donde no
cabe un modelo local (ADR-002), así que los embeddings se piden a una API
externa. El modelo tiene que funcionar en español y tener cuota gratuita
(presupuesto de IA = 0). Cambiarlo después obliga a reindexar todo.

## Decisión

Usamos **`voyage-4`** de Voyage AI con vectores de **1024 dimensiones** (el
valor por defecto). Al indexar fragmentos se llama con
`input_type="document"`; al buscar, la pregunta se codifica con
`input_type="query"`.

## Por qué

- En nuestro golden set (15 preguntas `en_corpus`) acierta **13/15** en el
  top-5, frente a 7/15 del modelo local de referencia (ver
  `investigacion/INV-009-embeddings.md`).
- Empata en aciertos con `voyage-multilingual-2`, pero gasta un 24 % menos de
  tokens (45.618 frente a 56.405 para el mismo corpus).
- Tiene **200 M de tokens gratis** por cuenta, según la página de precios
  (consultada el 2026-11-15). Indexar todo el corpus gasta unos 45 K.
- Es de la familia actual de Voyage; `voyage-multilingual-2` está en la lista
  de modelos antiguos.

## Alternativas descartadas

| Alternativa | Por qué no |
|---|---|
| `voyage-multilingual-2` | Mismos aciertos, más tokens, modelo antiguo y cuota gratuita poco clara. |
| `paraphrase-multilingual-MiniLM-L12-v2` (local) | 7/15 aciertos y no cabe en los 512 MB de Render. |

## Consecuencias

- La columna `embedding` de IA-008 será `vector(1024)`.
- `EMBEDDINGS_API_KEY` es una clave de Voyage AI.
- Sin método de pago, Voyage limita a 3 peticiones y 10 K tokens por minuto:
  `ia/indexar.py` tiene que usar lotes pequeños y esperar ante un error 429.
- Revisar esta decisión si se agota la cuota gratuita, si Voyage retira el
  modelo, o si un golden set más grande muestra diferencias entre modelos.
