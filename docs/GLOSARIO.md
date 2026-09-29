# Glosario

Definiciones cortas, en nuestras palabras. Si una definición no se entiende,
mejórala con un PR.

| Término | Qué es |
|---|---|
| **LLM** | Modelo de lenguaje grande. Predice el siguiente trozo de texto a partir de lo anterior. No "sabe" cosas: reproduce patrones de lo que leyó al entrenarse. |
| **Token** | Unidad en la que el modelo trocea el texto (más o menos, media palabra). Los límites y los precios se miden en tokens. |
| **Ventana de contexto** | Cuánto texto (en tokens) puede leer el modelo de una vez: instrucciones, fragmentos y pregunta. |
| **Alucinación** | Cuando el modelo produce algo falso con total seguridad. En normativa es el riesgo principal. |
| **Temperatura** | Cuánto azar se permite al generar. Con 0, la misma entrada da (casi) la misma salida. |
| **Prompt de sistema** | Instrucciones fijas que recibe el modelo antes de la pregunta (reglas de cita, de rechazo…). |
| **Entrenar / fine-tuning** | Cambiar los pesos de un modelo con datos nuevos. **No lo hacemos** (ver `docs/VISION.md`). |
| **RAG** | *Retrieval-Augmented Generation*: primero se buscan los textos relevantes y luego se le pide al modelo que responda solo con ellos. |
| **Corpus** | El conjunto de documentos sobre el que se busca. Aquí, la normativa de la carrera. |
| **Fragmento (chunk)** | Trozo del corpus que se indexa y se recupera; idealmente, un artículo. |
| **Embedding** | Lista de números (vector) que representa el significado de un texto. Textos parecidos tienen vectores cercanos. |
| **Similitud coseno** | Medida de cuán alineados están dos vectores: 1 = mismo sentido, 0 = sin relación. |
| **BM25** | Búsqueda clásica por palabras: puntúa según cuántas veces aparecen las palabras de la pregunta y cuán raras son. |
| **Búsqueda vectorial** | Buscar los fragmentos cuyo embedding está más cerca del embedding de la pregunta. |
| **Búsqueda híbrida** | Combinar BM25 y vectorial para tener lo mejor de ambas. |
| **RRF** | *Reciprocal Rank Fusion*: une dos rankings sumando `1/(K + posición)` de cada uno. No necesita que los puntajes estén en la misma escala. |
| **Top-k** | Los k mejores resultados de una búsqueda. |
| **Golden set** | Conjunto de preguntas con su respuesta correcta conocida, para medir el sistema. |
| **recall@k** | Proporción de preguntas en las que el fragmento correcto aparece entre los k primeros recuperados. |
| **Umbral de relevancia** | Puntaje mínimo que debe tener el mejor fragmento para intentar responder; por debajo, se rechaza. |
| **Base de datos vectorial / pgvector** | Base de datos que guarda embeddings y busca los más cercanos. pgvector es la extensión que añade eso a Postgres; es la que usamos, en Supabase. |
| **Variable de entorno** | Valor de configuración (como una clave) que el programa lee del sistema en vez de tenerlo escrito en el código. |
| **Despliegue (deploy)** | Publicar la aplicación en un servidor para que se pueda usar desde internet. Nosotros usamos Render. |
| **Arranque en frío** | Primera petición a un servidor que estaba dormido: tarda más porque primero tiene que arrancar. |
| **Migración** | Archivo SQL numerado que cambia el esquema de la base de datos de forma versionada y repetible. |
| **MCP** | *Model Context Protocol*: forma estándar de conectar un asistente de IA (como Claude) con servicios externos (Render, Supabase…). |
| **ADR** | *Architecture Decision Record*: documento corto que registra una decisión, sus alternativas y su porqué. |
