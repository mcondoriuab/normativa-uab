# ADR-010: conservar la búsqueda híbrida tras medir recall@5

**Estado:** propuesta · **Fecha:** 2026-11-16 · **Tarea:** IA-012

## Contexto

El sistema dispone de BM25, búsqueda vectorial con Voyage `voyage-4` y
búsqueda híbrida mediante RRF. La hipótesis inicial era que la híbrida
superaría a las otras dos. Medí los modos sobre el mismo golden set de
15 preguntas respondibles y 293 fragmentos de Supabase. Excluí las cinco
preguntas fuera del corpus, porque no tienen artículo esperado que recuperar.

La integración de IA-016 usa `puntaje_vectorial` para el umbral de rechazo;
la función `buscar()` añade ese campo en el modo híbrido. Cambiar el modo
obligaría a revisar esa integración con el docente.

## Decisión

Propongo conservar `hibrida` como modo del sistema: empata con vectorial
en recall@5 y mantiene la interfaz prevista para IA-016. No modifico los
buscadores, `ia/responder.py` ni su umbral de rechazo en esta tarea.

## Por qué

| Modo | Global | Literal | Coloquial | Multi-articulo |
|---|---|---|---|---|
| bm25 | 11/15 (73.3%) | 5/5 (100.0%) | 3/7 (42.9%) | 3/3 (100.0%) |
| vectorial | 13/15 (86.7%) | 5/5 (100.0%) | 5/7 (71.4%) | 3/3 (100.0%) |
| hibrida | 13/15 (86.7%) | 5/5 (100.0%) | 5/7 (71.4%) | 3/3 (100.0%) |

Los datos no confirman que la híbrida gane: empata con vectorial en los
cuatro grupos de la tabla. Tampoco confirman una ventaja de BM25 en las
literales: los tres modos aciertan las cinco. La diferencia global respecto
a BM25 viene de dos aciertos adicionales en preguntas coloquiales.

En el empate aplico como criterio de decisión la compatibilidad con el
sistema existente. No afirmo que la híbrida sea superior en calidad ni en
latencia; esta tarea no mide latencias ni respuestas del LLM.

La evidencia, los comandos, la repetición del experimento y el análisis de
errores están en la
[evaluación del 2026-11-16](../evaluaciones/2026-11-16-comparativa-busqueda.md).

## Alternativas descartadas

| Alternativa | Por qué no |
|---|---|
| BM25 como único modo | Baja a 11/15 global y 3/7 coloquial, aunque no necesita una API de embeddings. |
| Vectorial como único modo | Empata en recall con híbrida; no ofrece una mejora medida que justifique cambiar la interfaz del umbral de IA-016. |
| Ajustar pesos, tokenización o fragmentos | Corregir los fallos queda fuera del alcance de IA-012. |

## Consecuencias

- Mantengo el modo híbrido y su `puntaje_vectorial`; no hace falta cambiar la
  integración ni avisar de un cambio de modo en IA-016.
- El modo elegido todavía falla en 2/15 preguntas: recuperar resultados no
  garantiza que el artículo esperado esté presente, ni que el LLM responda
  correctamente.
- Conservo la dependencia de Voyage y sus límites de velocidad. En el
  experimento se aplicaron las esperas del código existente.
- La muestra de 15 preguntas es pequeña; una sola pregunta cambia el recall
  global en 6.7 puntos porcentuales. El empate no garantiza igualdad en otras
  consultas ni constituye una prueba de superioridad estadística.
- Revisaré esta propuesta si crece el golden set, cambia el corpus o el
  modelo, o una nueva medición separa a vectorial e híbrida.
