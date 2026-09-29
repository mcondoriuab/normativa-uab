# Arquitectura

Arquitectura **objetivo** del MVP. Hoy no existe ningún código; cada pieza la
construye una tarea del backlog (entre paréntesis).

## Flujo

```
corpus/<carrera>/*.pdf                                  (en local)
        │
        ▼
[1] Ingesta        ia/extraer.py (IA-002) + ia/trocear.py (IA-003, IA-004)
        │          CLI: python -m ia.ingestar (IA-005)
        ▼
  data/fragmentos.json                                  (en local, no va a git)
        │
        ▼
[2] Índice         ia/indexar.py (IA-008): embeddings por API
        │          → tabla `fragmentos` en Supabase (esquema: BE-008)
        ▼
[3] Búsqueda       ia/bm25.py (IA-007) + ia/vectorial.py (IA-009, pgvector)
        │          fusión: ia/hibrida.py (IA-010) · CLI: python -m ia.buscar (IA-011)
        ▼
[4] Generación     ia/llm.py (IA-014) + ia/prompts.py (IA-015)
        │          ia/responder.py (IA-016, IA-017)
        ▼
[5] API            apps/api/main.py (BE-001…BE-005, BE-010)
        │
        ▼
[6] Web            apps/web/index.html, estilos.css, app.js (FE-001…FE-006)
```

Todos los comandos se ejecutan **desde la raíz del repositorio**. Las
dependencias de Python van en un único `requirements.txt` en la raíz. Los
secretos (conexión a la base, claves de API) se leen de variables de entorno;
plantilla en `.env.ejemplo`.

En producción, API y web corren en **Render** y la base de datos en
**Supabase**. Detalle en `docs/DESPLIEGUE.md` y en ADR-002.

## Contratos

Los contratos son el acuerdo entre piezas: si cada tarea los respeta, se pueden
construir en paralelo y encajan al final. **No se cambian sin un ADR** en
`historial/decisiones/`.

### Fragmento

`data/fragmentos.json` es una lista JSON de fragmentos:

```json
{
  "id": "reglamento-estudiantil#art-47",
  "documento": "reglamento-estudiantil",
  "articulo": "47",
  "pagina": 12,
  "texto": "Artículo 47. El estudiante que acumule ..."
}
```

- `documento`: nombre del PDF sin extensión, en minúsculas y con guiones.
- `articulo`: número como texto (`"47"`, `"47 bis"`), o `null` si el fragmento
  vino del troceado por longitud.
- `id`: `documento#art-<articulo>`; si no hay artículo,
  `documento#frag-<n>` con `n` correlativo dentro del documento.
- `pagina`: página del PDF (empezando en 1) donde **empieza** el fragmento.

### Base de datos

Postgres con la extensión `vector` (pgvector), en Supabase. Esquema en
`db/migraciones/` (BE-008); acceso desde Python solo a través de `ia/db.py`.

`fragmentos`: los mismos campos que el contrato *Fragmento*, más su embedding.

| Columna | Tipo | Nota |
|---|---|---|
| `id` | `text` primary key | `documento#art-47` |
| `documento` | `text` not null | |
| `articulo` | `text` | `null` si viene del troceado por longitud |
| `pagina` | `integer` not null | |
| `texto` | `text` not null | |
| `embedding` | `vector(N)` | `N` = dimensión del modelo elegido en INV-009 |

`consultas`: registro **anónimo** de uso, para evaluar y mejorar (ver
`docs/ETICA.md`). Nunca guarda IP, usuario ni nada que identifique a nadie.

| Columna | Tipo |
|---|---|
| `id` | `bigint` identity primary key |
| `creada_en` | `timestamptz` default `now()` |
| `pregunta` | `text` |
| `rechazada` | `boolean` |
| `ids_citados` | `text[]` |
| `latencia_ms` | `integer` |

### Resultado de búsqueda

Todas las funciones de búsqueda (`bm25`, `vectorial`, `hibrida`) devuelven una
lista ordenada de mejor a peor:

```json
[{"id": "reglamento-estudiantil#art-47", "puntaje": 0.83, "fragmento": { ... }}]
```

### API

`GET /salud` → `{"estado": "ok"}`

`POST /preguntar`

```json
// petición
{"pregunta": "¿cuántas faltas puedo tener?"}

// respuesta
{
  "respuesta": "Puedes faltar hasta el 20% de las clases [1].",
  "rechazada": false,
  "citas": [
    {"n": 1, "documento": "reglamento-estudiantil", "articulo": "47",
     "pagina": 12, "texto": "Artículo 47. ..."}
  ],
  "aviso": "Herramienta de apoyo. El texto oficial y vinculante es el publicado por la universidad."
}
```

- `rechazada: true` cuando no hay evidencia suficiente; en ese caso `citas` va
  vacía y `respuesta` explica que no se encontró.
- `[n]` en `respuesta` se refiere a `citas[n-1]`.
- Error de entrada (pregunta vacía o de más de 500 caracteres): HTTP 422.

### Golden set

`eval/preguntas.jsonl`, una pregunta por línea:

```json
{"pregunta": "...", "id_esperado": "reglamento-estudiantil#art-47", "en_corpus": true, "tipo": "literal", "respuesta_esperada": "..."}
```

`tipo` ∈ `literal` · `coloquial` · `multi-articulo` · `fuera-de-corpus`. Para
`fuera-de-corpus`, `id_esperado` es `null` y `en_corpus` es `false`. Detalle en
`docs/EVALUACION.md`.

## Principios

1. **Cero respuestas sin cita.** Toda afirmación se ancla a un fragmento
   recuperado.
2. **El modelo no es la base de datos.** Solo redacta a partir de lo recuperado.
3. **Modelo intercambiable.** El resto del código no sabe qué LLM hay detrás de
   `ia/llm.py`; así el presupuesto no bloquea el proyecto.
4. **Lo simple primero.** Postgres con pgvector es la única base de datos: no se
   añade una base vectorial dedicada ni otras piezas. Se añade complejidad solo
   si una medición lo justifica.
5. **Medir, no opinar.** Cada cambio de diseño se compara con el golden set.
