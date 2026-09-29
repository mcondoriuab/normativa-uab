# ADR-002: Desplegar en Render + Supabase, con embeddings por API

**Estado:** aceptada · **Fecha:** 2026-09-29 · **Tarea:** —

## Contexto

El repositorio no solo guarda el histórico: también es lo que se despliega. Se
necesita una plataforma **gratuita**, fácil de usar y que se pueda manejar desde
Claude (conectores MCP) para las cuatro piezas: web, API, motor de IA y base de
datos.

Datos consultados el 2026-09-29 en la documentación oficial de cada servicio:

| Opción | Lo bueno | Lo que la descarta o limita |
|---|---|---|
| **Render** (plan free) | Web service Python gratis, autodeploy desde GitHub, conector MCP oficial (crear servicios, desplegar, logs, variables) | 512 MB de RAM y 0.1 CPU; se duerme tras 15 min sin uso (~60 s en despertar); su Postgres gratis caduca a los 30 días |
| **Supabase** (plan free) | Postgres + pgvector, 500 MB, conector MCP oficial | El proyecto se pausa tras 7 días sin actividad |
| Hugging Face Spaces | 16 GB de RAM | Los Spaces Docker ya exigen plan de pago |
| Railway | Conector MCP | Solo 1 USD de crédito al mes tras la prueba |
| Vercel | Conector MCP, no se duerme | FastAPI en funciones serverless es menos directo de entender |

## Decisión

- **Render** (un solo *web service* Python) sirve la API y la web (`apps/web`
  como archivos estáticos). Se despliega solo con cada push a `main`, con un
  `render.yaml` en la raíz.
- **Supabase** es la base de datos: fragmentos con su embedding (pgvector) y
  registro anónimo de consultas. El esquema se versiona en `db/migraciones/`.
- **Los embeddings se calculan por API** (candidato: Voyage AI, que tiene tokens
  gratuitos), no con un modelo local: 512 MB de RAM no alcanzan para cargar uno.
  El modelo exacto se elige en INV-009.
- El LLM sigue siendo intercambiable y se elige en INV-010.
- Se despliega **desde la fase 1** (un `/salud` en producción) y no al final,
  para descubrir pronto los problemas de despliegue.

## Por qué

- Las dos plataformas son gratuitas, se conectan a Claude y dejan el backend en
  Python, que es lo que el equipo aprende.
- Con la base de datos, los fragmentos y los vectores sobreviven a los reinicios
  (el disco de Render es efímero) y no hace falta subir datos generados a git.
- pgvector sigue siendo transparente: la búsqueda es una consulta SQL de pocas
  líneas (`ORDER BY embedding <=> :pregunta`).

## Alternativas descartadas

| Alternativa | Por qué no |
|---|---|
| NumPy + `.npy` en el servidor (ADR previo implícito) | El disco de Render es efímero y los datos no están en git |
| Modelo de embeddings local | No cabe en 512 MB junto con la API |
| Postgres de Render | Caduca a los 30 días en el plan gratuito |

## Consecuencias

- La primera visita tras 15 minutos sin uso tarda ~1 minuto. Para la demo, abrir
  la web un rato antes.
- Hay que evitar que Supabase se pause: una tarea programada lo consulta cada
  pocos días (BE-009).
- Render solo tiene IPv4: hay que conectarse a Supabase con la cadena del
  **pooler**, no con la conexión directa.
- Dependemos de dos APIs externas (embeddings y LLM) y de sus cuotas gratuitas.
- Revisar esta decisión si el arranque en frío molesta a los usuarios o si se
  superan las cuotas gratuitas.
