# Evaluación 2026-11-16: comparativa de búsqueda

**Tarea:** IA-012 · **Golden set:** 20 preguntas, 15 evaluadas · **Commit del motor y del script:** b417928

## Qué se cambió respecto a la medición anterior

Realicé la primera comparación integrada de BM25, vectorial e híbrida usando
`ia.hibrida.buscar()`, el mismo golden set y la misma base de Supabase.
INV-009 había comparado modelos de embeddings; aquí comparé los tres modos
de búsqueda ya implementados. No ajusté los buscadores para obtener mejores
resultados en estas preguntas.

## Datos y entorno

- Fecha de ejecución: 2026-11-16, hora de Bolivia.
- Golden set: `eval/preguntas.jsonl`, última modificación en bb6644c
  (2026-11-15). Evalué 5 preguntas literales, 7 coloquiales y 3 de varios
  artículos. Excluí las 5 preguntas con `en_corpus: false`.
- Corpus: 293 fragmentos de Supabase, todos con embeddings de 1024 dimensiones.
  Comprobé que todos los ids esperados existen en la base.
- Modelo: Voyage `voyage-4`, con `input_type="query"` para las preguntas.
- BM25: tokenización de IA-007, en minúsculas y sin tildes.
- Híbrida: RRF con `K=60`, 20 candidatos por buscador y 5 resultados finales.
- Entorno: Python 3.14.3, `rank-bm25==0.2.2`, `voyageai==0.6.0`,
  `psycopg==3.3.9`.
- Credenciales: variables de entorno temporales de los procesos. No las
  guardé en archivos ni en commits; solo ejecuté consultas de lectura.

Huellas SHA-256 para identificar los datos y el script:

| Elemento | SHA-256 |
|---|---|
| Archivo local `eval/preguntas.jsonl` | `28d4184ea9143e3c2fa0ead67288c6d48e3682e31a39cda0e3b345108344a05e` |
| Archivo local `eval/recall.py` | `5292996389cf70ba5a2c7094550f3159bd1b611c8219caaa184d2a0765e70470` |
| Fragmentos consultados, ordenados por id | `8bbd1be0d8716638d989e2f3e0c40afe5cd25d734df0d5caaefca66a0b26c7ba` |

La huella de los fragmentos corresponde a
`json.dumps(fragmentos, ensure_ascii=False, sort_keys=True)`, con los campos
del contrato Fragmento; no incluye los vectores.

## Resultados

| Modo | recall@5 global | literal | coloquial | multi-articulo |
|---|---|---|---|---|
| bm25 | 11/15 (73.3%) | 5/5 (100.0%) | 3/7 (42.9%) | 3/3 (100.0%) |
| vectorial | 13/15 (86.7%) | 5/5 (100.0%) | 5/7 (71.4%) | 3/3 (100.0%) |
| hibrida | 13/15 (86.7%) | 5/5 (100.0%) | 5/7 (71.4%) | 3/3 (100.0%) |

Rechazo correcto (fuera de corpus): no medido en IA-012.
Latencia p50/p95: no medida; las duraciones de las ejecuciones incluyen las
esperas por cuota de Voyage y no representan esas métricas.

Comprobé la repetibilidad ejecutando `python -m eval.recall` y
`python -m eval.recall --fallos`. Las tres filas globales y por tipo fueron
idénticas; los mensajes de espera del proveedor no forman parte de la métrica.
Las salidas completas y las duraciones están al final de este documento.

Cada celda es aciertos/preguntas de ese grupo. Un acierto significa que el
`id_esperado` aparece entre los cinco ids devueltos; no evalúo el texto de
una respuesta. En `multi-articulo` solo compruebo el artículo principal del
golden set, no la recuperación de todos los artículos que harían falta.

## Análisis de errores

Vectorial e híbrida fallaron las mismas dos preguntas, aunque devolvieron
rankings distintos. Las dos recuperaron los casos sobre proyecto de grado y
materias pendientes que BM25 había fallado. Los cuatro fallos de BM25 y los
dos de cada uno de los otros modos figuran en la salida de `--fallos`.

Todos los ids de la siguiente tabla pertenecen a
`reglamento-estudiantil-2016`; los números indican `#art-N`, en el orden
recuperado. Las etiquetas son diagnósticos propuestos a partir de la pregunta,
el fragmento esperado y los textos recuperados, no una prueba de la causa
interna del modelo.

| Pregunta fallada en híbrida | Esperado | Recuperados | Etiqueta |
|---|---|---|---|
| ¿Puedo cambiar de carrera sin perder las materias que ya aprobé? | art. 22 | 11, 15, 7, 17, 16 | `vocabulario` |
| ¿Me sancionan si falto a clase sin justificar? | art. 19 | 78, 55, 76, 71, 42 | `pregunta ambigua` |

### Cambio de carrera: vocabulario

El artículo 22, página 5, define la convalidación y el reconocimiento de
asignaturas entre carreras de la misma universidad. La pregunta expresa esa
necesidad como conservar materias aprobadas, sin usar «convalidación» ni
«reconocimiento».

El primer recuperado, artículo 11, menciona explícitamente el cambio de
carrera, pero trata de la obligación de pagar los créditos inscritos. Los
otros resultados tratan de planes, asignación de materias y arrastres. El
ranking recoge vocabulario relacionado y pierde el artículo que define el
reconocimiento. El fragmento esperado existe y contiene esa regla.

**Propuesta posterior al MVP:** probar reformulación o equivalencias de
vocabulario relacionadas con convalidación, conservando esta pregunta para
comparar antes y después. No implementé ese cambio en IA-012.

### Faltas a clase: pregunta ambigua

El golden set espera el artículo 19, página 4, sobre la asistencia regular
del 80 % y su valoración en las evaluaciones. La pregunta, en cambio, pone
el foco en sanción y justificación.

Los resultados incluyen faltas disciplinarias (78), clases de sanciones
(76), criterios disciplinarios (71), obligaciones (42) y postergación de
exámenes con justificación de inasistencia (55). Son temas que responden a
palabras de la consulta, pero no sustituyen la regla de asistencia esperada.
La frase puede interpretarse como régimen de asistencia o como procedimiento
disciplinario; el artículo 19 no establece por sí solo una sanción automática.

**Propuesta posterior al MVP:** revisar con el docente el alcance de esta
pregunta y ampliar los ejemplos coloquiales de asistencia y de disciplina.
Conservé su etiqueta y su id esperado para esta medición.

No cambié el golden set, los fragmentos, los pesos de RRF ni la tokenización.
Tampoco generé respuestas del LLM en este experimento.

## Conclusión

No confirmé la hipótesis de que la híbrida ganaría en conjunto: empató con
vectorial en las cuatro columnas. Tampoco encontré una ventaja de BM25 sobre
vectorial en las literales; los tres modos acertaron las cinco.

Propongo mantener `hibrida` por compatibilidad con la interfaz y el
`puntaje_vectorial` de IA-016. No atribuyo una mejora de calidad a ese
desempate. La decisión está en
[ADR-010](../decisiones/ADR-010-modo-de-busqueda.md).

La muestra es pequeña: una pregunta representa 6.7 puntos porcentuales del
recall global. Estos resultados no garantizan el mismo comportamiento en
preguntas nuevas ni evalúan respuestas, citas o rechazo del LLM.

## Guion para presentar en cinco minutos

1. **Minuto 1:** explicaré qué comprueba recall@5 y por qué usé 15 preguntas
   respondibles y excluí las otras cinco.
2. **Minuto 2:** mostraré 11/15 de BM25 y el empate 13/15 de vectorial e
   híbrida, destacando la diferencia en las coloquiales.
3. **Minuto 3:** presentaré las dos preguntas que falló la híbrida y las
   causas propuestas a partir de sus artículos y resultados.
4. **Minuto 4:** explicaré que mantengo híbrida por compatibilidad, no porque
   los números demuestren que supera a vectorial.
5. **Minuto 5:** señalaré la muestra pequeña y las mejoras pendientes para
   otra tarea, diferenciando recuperación y generación.


## Salidas completas de verificación

### Ejecución 1: python -m eval.recall

```text
modo | global | literal | coloquial | multi-articulo
bm25 | 11/15 (73.3%) | 5/5 (100.0%) | 3/7 (42.9%) | 3/3 (100.0%)
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
vectorial | 13/15 (86.7%) | 5/5 (100.0%) | 5/7 (71.4%) | 3/3 (100.0%)
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
hibrida | 13/15 (86.7%) | 5/5 (100.0%) | 5/7 (71.4%) | 3/3 (100.0%)
```

Código de salida: 0.
Duración de esta ejecución: 622.5 segundos.

### Ejecución 2: python -m eval.recall --fallos

```text
modo | global | literal | coloquial | multi-articulo
bm25 | 11/15 (73.3%) | 5/5 (100.0%) | 3/7 (42.9%) | 3/3 (100.0%)
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
vectorial | 13/15 (86.7%) | 5/5 (100.0%) | 5/7 (71.4%) | 3/3 (100.0%)
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
Límite de velocidad de la API; espero 20 s...
hibrida | 13/15 (86.7%) | 5/5 (100.0%) | 5/7 (71.4%) | 3/3 (100.0%)

Fallos de bm25:
- [coloquial] ¿Puedo cambiar de carrera sin perder las materias que ya aprobé?
  Esperado: reglamento-estudiantil-2016#art-22
  Recuperados: reglamento-estudiantil-2016#art-17, reglamento-estudiantil-2016#art-7, reglamento-estudiantil-2016#art-16, reglamento-de-graduacion-2016#art-34, reglamento-estudiantil-2016#art-15
- [coloquial] ¿Cuánto tiempo tengo para entregar mi proyecto de grado después de aprobar todo?
  Esperado: reglamento-de-graduacion-2016#art-22
  Recuperados: reglamento-de-graduacion-2016#art-10, reglamento-de-investigacion-2021#art-26, reglamento-de-investigacion-2021#art-27, reglamento-de-graduacion-2016#art-17, reglamento-estudiantil-2016#art-35
- [coloquial] ¿Puedo matricularme si todavía tengo materias pendientes del semestre pasado?
  Esperado: reglamento-estudiantil-2016#art-17
  Recuperados: reglamento-estudiantil-2016#art-10, reglamento-de-graduacion-2016#art-8, reglamento-estudiantil-2016#art-16, reglamento-estudiantil-2016#art-57, reglamento-estudiantil-2016#art-7
- [coloquial] ¿Me sancionan si falto a clase sin justificar?
  Esperado: reglamento-estudiantil-2016#art-19
  Recuperados: reglamento-de-graduacion-2016#art-5, reglamento-estudiantil-2016#art-56, reglamento-estudiantil-2016#art-55, reglamento-estudiantil-2016#art-51, reglamento-de-investigacion-2021#art-27

Fallos de vectorial:
- [coloquial] ¿Puedo cambiar de carrera sin perder las materias que ya aprobé?
  Esperado: reglamento-estudiantil-2016#art-22
  Recuperados: reglamento-estudiantil-2016#art-11, reglamento-estudiantil-2016#art-9, reglamento-estudiantil-2016#art-15, reglamento-estudiantil-2016#art-21, reglamento-estudiantil-2016#art-23
- [coloquial] ¿Me sancionan si falto a clase sin justificar?
  Esperado: reglamento-estudiantil-2016#art-19
  Recuperados: reglamento-estudiantil-2016#art-20, reglamento-estudiantil-2016#art-79, reglamento-de-graduacion-2016#art-50, reglamento-estudiantil-2016#art-76, reglamento-estudiantil-2016#art-78

Fallos de hibrida:
- [coloquial] ¿Puedo cambiar de carrera sin perder las materias que ya aprobé?
  Esperado: reglamento-estudiantil-2016#art-22
  Recuperados: reglamento-estudiantil-2016#art-11, reglamento-estudiantil-2016#art-15, reglamento-estudiantil-2016#art-7, reglamento-estudiantil-2016#art-17, reglamento-estudiantil-2016#art-16
- [coloquial] ¿Me sancionan si falto a clase sin justificar?
  Esperado: reglamento-estudiantil-2016#art-19
  Recuperados: reglamento-estudiantil-2016#art-78, reglamento-estudiantil-2016#art-55, reglamento-estudiantil-2016#art-76, reglamento-estudiantil-2016#art-71, reglamento-estudiantil-2016#art-42
```

Código de salida: 0.
Duración de esta ejecución: 853.4 segundos.

Repetibilidad: las dos ejecuciones produjeron tablas idénticas.
