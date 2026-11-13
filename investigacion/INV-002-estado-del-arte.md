# INV-002: Estado del arte de los asistentes de normativa con IA

**Autor(es):** Sandra Condori · **Fecha:** 2026-11-12

> Este informe es la **Parte 1** de INV-002 (estado del arte). La Parte 2
> (fine-tuning frente a prompt largo frente a RAG, y el ADR-007) va en
> `INV-002-entrenar-vs-rag.md` y espera a INV-012 e INV-013.

## Pregunta

¿Quién ha construido ya asistentes de preguntas y respuestas sobre normativa
(universitaria, legal o institucional) con IA, cómo funcionan, cómo los
evaluaron y qué problemas encontraron? ¿Qué podemos aprender para nuestro
asistente?

## Lo que encontramos

Elegimos 5 ejemplos: 3 sobre **normativa universitaria** (los más parecidos a
nuestro proyecto) y 2 del **ámbito legal** (donde hay más trabajo publicado y
una evaluación independiente muy citada).

### Tabla resumen

| # | Sistema | Quién y año | Qué documentos usa | Cómo funciona | Cómo lo evaluaron | Problemas que reportan | Fuente primaria |
|---|---|---|---|---|---|---|---|
| 1 | **PoliChat** | Wojtasik, Berdowski, Okulska y Piasecki, Universidad Tecnológica de Breslavia (Polonia). ICCS 2025 | 2.350 documentos de la universidad (reglamentos, estatutos, resoluciones del rector, decanos y senado), en polaco, de 1995 a 2024 | **RAG** con cita de fuentes. Buscador (e5-large, BM25 y otros) + reordenador (*re-ranker*) + LLM abierto (Llama, Bielik, Command-R+). Propone un prompt en dos pasos, *Analyze & Answer* | 100 preguntas filtradas a mano (de casi 500 propuestas), con los fragmentos relevantes anotados. Miden recuperación (Acc@5, NDCG@10) y respuesta (palabras que deben aparecer o no, F1 de citas) | Documentos largos y resúmenes empeoran la recuperación y las citas; pedir citas a veces baja la exactitud; mucho contexto confunde al modelo; tablas difíciles de extraer de los PDF | [PDF ICCS 2025](https://www.iccs-meeting.org/archive/iccs2025/papers/159110266.pdf) |
| 2 | **REBot** | Ma, La, Le Huu, Nguyen y Pham Luu, Universidad de Can Tho (Vietnam). arXiv, 2025 | Reglamentos académicos de la universidad en PDF y páginas web, en vietnamita (no dicen cuántos) | **RAG + GraphRAG** (grafo de conocimiento de 250 nodos). Clasifica la pregunta por tema (fastText) y luego busca. Generan con gpt-4o-mini y Mistral. No hacen fine-tuning del LLM | 1.313 pares pregunta-respuesta escritos por personal de apoyo académico, de los cuales 404 son preguntas **fuera de tema**. Métrica F1: 98,89 % su versión con grafo frente a 98,67 % el RAG normal (gpt-4o-mini) | El grafo puede meter demasiado contexto y dar respuestas incoherentes; tarda unos 7 s por respuesta; el clasificador falla con preguntas largas | [arXiv:2510.01800](https://arxiv.org/abs/2510.01800) |
| 3 | **Unipa-GPT** | Siragusa y Pirrone, Universidad de Palermo (Italia). arXiv, 2024 (v3 de 2025) | 610 documentos de la web de la universidad (cursos, matrícula, becas, tasas, preguntas frecuentes), en italiano, descargados en verano de 2023 | **RAG** (fragmentos de 1.000 tokens, FAISS, gpt-3.5-turbo). Probaron **además fine-tuning** de gpt-3.5-turbo | Dos estudiantes de secundaria puntuaron 24 respuestas como "excelente", "buena" o "mala". Mejor configuración: 19 excelentes de 24. También una prueba en una feria con 165 preguntas | El modelo con fine-tuning **no mejoró** y generaba bucles y alucinaciones; una respuesta errónea en italiano fluido parece verdad; el coste de tokens les impidió evaluar más | [arXiv:2407.14246](https://arxiv.org/abs/2407.14246) |
| 4 | **ChatLaw** (v1) | Cui, Li, Yan, Chen y Yuan, Universidad de Pekín (China). arXiv, 2023 | Leyes, interpretaciones judiciales, consultas legales, preguntas de examen de abogacía y unas 930.000 sentencias, en chino | **Fine-tuning** (Ziya-LLaMA-13B con LoRA) **+ base de conocimiento externa** (busca artículos de ley parecidos con BERT y Faiss y se los pasa al modelo) | Unas 2.000 preguntas tipo test del examen judicial chino, comparando modelos por ranking Elo | Dicen que el fine-tuning solo no basta (lo vieron en un modelo anterior, LawGPT); la búsqueda por similitud falla con preguntas vagas; el razonamiento lógico es flojo. No miden cuánto bajan las alucinaciones | [arXiv:2306.16092v1](https://arxiv.org/abs/2306.16092v1) |
| 5 | **Herramientas legales comerciales** (Lexis+ AI, Westlaw AI-Assisted Research, Ask Practical Law AI), evaluadas por un equipo externo | Evaluación de Magesh, Surani, Dahl, Suzgun, Manning y Ho (Stanford y Yale). arXiv, 2024 | Las bases de datos legales de cada empresa (jurisprudencia, leyes, reglamentos, guías prácticas) | **RAG** comercial. Las empresas anunciaban que no alucinaba (*"hallucination-free"*) | Más de 200 preguntas legales preparadas y registradas antes de probar. Cuentan como alucinación tanto la información falsa como citar una fuente que **no dice** lo que se afirma | Alucinan **entre el 17 % y el 33 %** de las veces. Lexis+ AI acierta el 65 %; Westlaw el 42 %. Fallos: recuperar documentos parecidos en palabras pero que no aplican, y que el modelo siga lo que "sabe" en vez del texto recuperado | [arXiv:2405.20362](https://arxiv.org/abs/2405.20362) |

### Qué patrón se repite

- Los **5** usan búsqueda en documentos (RAG o algo equivalente). Ninguno confía
  solo en lo que el modelo aprendió.
- Los dos que probaron **fine-tuning** (Unipa-GPT y ChatLaw) lo combinaron con
  búsqueda. Unipa-GPT no vio mejora; ChatLaw dice que el fine-tuning solo no
  basta.
- Las **citas** son el punto fuerte y a la vez el punto débil: dejan verificar la
  respuesta, pero el modelo se equivoca al elegir qué citar, sobre todo cuando
  recibe mucho texto (PoliChat, Stanford).
- Casi todos evalúan con un **conjunto de preguntas propio** (100 en PoliChat,
  1.313 en REBot, 200 en Stanford), igual que nuestro golden set.

## Evidencia

Lo que **dice cada fuente**, en sus palabras (citas cortas) o resumido con
indicación de la sección. Todas se consultaron el 2026-11-12.

1. **PoliChat** — Wojtasik et al., *PoliChat: Retrieval Augmented Generation on
   University Documents and Regulations*, ICCS 2025 (DOI indicado en el PDF:
   10.1007/978-3-031-97570-7_21).
   [PDF](https://www.iccs-meeting.org/archive/iccs2025/papers/159110266.pdf).
   - Corpus de "2,350 documents, including regulations, bylaws, and official
     texts" (sec. 4.1).
   - Con fragmentos de 512 tokens, la mejor combinación (e5-large + bge-reranker)
     pone el fragmento correcto entre los 5 primeros en el 95 % de las
     preguntas; sin reordenador, el 78 % (tabla 1). Con BM25: 90 % con
     reordenador y 68 % sin él.
   - Con fragmentos de 4.000 tokens los resultados son peores, y con resúmenes
     todavía peores: los resúmenes "may remove key lexical or semantic cues"
     (sec. 6.1). La nota de la respuesta baja de 84,34 a 66,27 con resúmenes
     abstractivos (sec. 6.2).
   - Al recibir más fragmentos (top 5, 10, 20), "performance declines,
     particularly in citation F1" (sec. 6.3).
   - El sistema "refuses to answer when no relevant information is found"
     (sec. 3).
2. **REBot** — Ma et al., *REBot: From RAG to CatRAG with Semantic Enrichment
   and Graph Routing*, arXiv:2510.01800. Leímos la v2 (noviembre de 2025);
   existe una v3 posterior que no hemos revisado.
   [arXiv v2](https://arxiv.org/abs/2510.01800v2).
   - Los reglamentos están en PDF y páginas web "fragmented, unstructured"
     (sec. 2.1).
   - F1 de 98,89 % con gpt-4o-mini (tabla 2). Con Mistral y el umbral 0,6, el
     RAG normal sale **algo mejor** que su versión con grafo (98,95 % frente a
     98,73 %).
   - Limitaciones (sec. 5.4): el grafo "can introduce excessive context, leading
     to incoherent or inaccurate responses" y "the current average response time
     of about seven seconds is a significant bottleneck".
3. **Unipa-GPT** — Siragusa y Pirrone, *Unipa-GPT: Large Language Models for
   university-oriented QA in Italian*, arXiv:2407.14246.
   [arXiv](https://arxiv.org/abs/2407.14246).
   - RAG con gpt-3.5-turbo, fragmentos de 1.000 tokens con 50 de solape y
     embeddings text-embedding-ada-002 (sec. 4).
   - Sobre el fine-tuning: "No improvements in performances were found in the
     fine-tuned models" (sec. 5.1); sus respuestas "generate loops and
     hallucinations".
   - Avisan de que "an uninformed user can easily consider a wrong answer as
     truthful" porque el italiano es fluido.
   - El prompt le pide "non inventare risposte" (no inventar respuestas) y
     remitir a la web (tabla 3).
4. **ChatLaw** — Cui et al., *ChatLaw: Open-Source Legal Large Language Model
   with Integrated External Knowledge Bases*, arXiv:2306.16092 **v1** (junio de
   2023). [arXiv v1](https://arxiv.org/abs/2306.16092v1).
   - "People tend to believe that fine-tuning a model with specific domain
     knowledge would yield satisfactory results. However, ... this is not the
     case" (introducción).
   - Primero buscaron con MySQL y Elasticsearch con "unsatisfactory results";
     luego con embeddings BERT, que "often yields suboptimal results when the
     user's question is vague" (sec. 3.2).
   - **Cuidado:** las versiones v2 y v3 del mismo número de arXiv describen
     otro sistema (agentes y *mixture of experts*). Este informe resume solo la
     v1.
5. **Evaluación de Stanford** — Magesh et al., *Hallucination-Free? Assessing
   the Reliability of Leading AI Legal Research Tools*, arXiv:2405.20362.
   [arXiv](https://arxiv.org/abs/2405.20362).
   - Las herramientas "each hallucinate between 17% and 33% of the time"
     (resumen), y "the providers' claims are overstated".
   - Definición: "a response that contains either incorrect information or a
     false assertion that a source supports a proposition" (introducción).
   - Lexis+ AI responde bien el 65 %; Westlaw AI-AR el 42 % "but hallucinates
     nearly twice as often" (introducción).
   - "RAG systems are no panacea" (sec. 3.2). El modelo "may be more faithful
     to its training data than to the retrieval context" (sec. 3.2).

### Búsquedas hechas

Términos: "RAG chatbot university regulations", "university policy chatbot
LLM", "Hallucination-Free legal research tools", "Unipa-GPT", "ChatLaw legal
LLM". Descartamos resultados que solo tenían reseñas de terceros (por ejemplo,
un asistente de la Universidad de São Paulo del que solo encontramos un resumen
en una web de reseñas, no el artículo).

### Uso de IA

Usamos un asistente de IA (Claude) para buscar los artículos y leer los textos
completos. Para cada fuente se abrió el artículo original (arXiv o el PDF del
congreso) y se comprobó que las cifras y citas de la tabla aparecen allí. Al
comprobarlo encontramos detalles que corregimos: en REBot el texto dice 1.319
pares pero la tabla suma 1.313 (usamos el de la tabla), y en ChatLaw el enlace
"ar5iv" muestra la versión nueva, no la v1. Algunos números de Stanford solo
están en las figuras; en el informe usamos solo los que aparecen escritos en el
resumen y la introducción.

## Conclusión para el proyecto

Esto es lo que **concluimos nosotros** a partir de las fuentes.

### Tres lecciones

1. **Fragmentos pequeños por artículo, texto original y un reordenador.**
   PoliChat recupera mejor con fragmentos cortos que con largos, y mucho peor
   con resúmenes; el reordenador sube el acierto en el top-5 de 68 % a 90 % con
   BM25. Para nosotros: mantener el troceado **por artículo** de
   `docs/ARQUITECTURA.md`, **no resumir** los artículos antes de indexarlos y
   pasar al modelo pocos fragmentos (unos 5), no todos los que salgan. Un
   reordenador es una mejora candidata para después del MVP, a medir con el
   golden set.
2. **RAG reduce las alucinaciones, pero no las elimina: hay que medirlas y
   dejar que el sistema diga "no lo encuentro".** Herramientas comerciales con
   RAG siguen alucinando entre el 17 % y el 33 % de las veces, y una respuesta
   mal citada parece correcta. Para nosotros: la regla "cero respuestas sin
   cita", el campo `rechazada` y la cita textual son lo más importante del
   producto, no un extra. Nuestro golden set debería incluir, como REBot,
   preguntas **cuya respuesta no está** en la normativa, y comprobar que la cita
   **dice de verdad** lo que afirma la respuesta (lo que Stanford llama
   *misgrounded*).
3. **No empezar por el fine-tuning.** Los dos proyectos que lo probaron lo
   tuvieron que acompañar de búsqueda en documentos, y en Unipa-GPT no mejoró
   nada y además costó tokens. Ninguno de los tres proyectos universitarios lo
   necesitó. Para nosotros es un indicio fuerte a favor de RAG, que la Parte 2
   de esta tarea tiene que confirmar con nuestros propios experimentos
   (INV-012, INV-013) y registrar en el ADR-007.

## Preguntas abiertas

- ¿Cuánto ayuda un reordenador con reglamentos en español? PoliChat lo midió en
  polaco; habría que probarlo con nuestro golden set.
- ¿Cómo comprobamos de forma barata que una cita respalda la respuesta? PoliChat
  usa listas de palabras que deben aparecer o no; ¿nos sirve para el golden set?
- ¿Merece la pena un grafo de conocimiento (como REBot) para la normativa de la
  UAB, o con BM25 + búsqueda vectorial basta? En REBot la mejora fue muy
  pequeña y la respuesta, más lenta.
