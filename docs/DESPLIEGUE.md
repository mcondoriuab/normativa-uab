# Despliegue

Dónde y cómo vive el asistente en producción. Decisión y alternativas en
[`historial/decisiones/ADR-002-despliegue-render-supabase.md`](../historial/decisiones/ADR-002-despliegue-render-supabase.md).

```
GitHub (main) ── push ──> Render (web service, plan free)
                           ├─ apps/web   archivos estáticos
                           ├─ apps/api   FastAPI
                           └─ ia/        búsqueda + generación
                                │              │
                                ▼              ▼
                     Supabase (Postgres     APIs externas
                      + pgvector)           ├─ embeddings (INV-009)
                                            └─ LLM (INV-010)

Claude Code ── conectores MCP ──> Render, Supabase
```

## 1. Configuración inicial (la hace el docente, una vez)

Usar la cuenta institucional en todo. Anotar en la tabla de abajo la fecha en
que se completa cada paso.

| # | Paso | Hecho |
|---|---|---|
| 1 | Crear el repositorio en GitHub y subir `main` | |
| 2 | Crear cuenta en [Render](https://render.com), entrando con GitHub | |
| 3 | Crear cuenta en [Supabase](https://supabase.com) y un proyecto `normativa-uab` en la región **São Paulo** (la más cercana) | |
| 4 | Crear la clave de API del proveedor de embeddings (INV-009) | |
| 5 | Crear la clave de API del LLM (INV-010) | |
| 6 | Instalar los conectores de Claude Code (sección 3) | |
| 7 | Compartir con el equipo, **por un canal privado**, los valores de `.env` para desarrollo | |

Las claves nunca se suben a git ni se pegan en issues, PRs o chats de grupo.

## 2. Variables de entorno

Plantilla en [`.env.ejemplo`](../.env.ejemplo). En local se copian a `.env`; en
producción se configuran en Render (*Environment*).

| Variable | Qué es | Dónde se obtiene |
|---|---|---|
| `DATABASE_URL` | Cadena de conexión a Postgres | Supabase → *Connect* → **Session pooler** (no la conexión directa: Render no tiene IPv6) |
| `EMBEDDINGS_API_KEY` | Clave del proveedor de embeddings | Panel del proveedor (INV-009) |
| `LLM_API_KEY`, `NORMATIVA_LLM_MODELO` | Clave y modelo del LLM | Panel del proveedor (INV-010) |

## 3. Conectores MCP para Claude Code

Permiten pedirle a Claude cosas como "¿por qué falló el último deploy?", "muestra
los logs de la API" o "¿cuántos fragmentos hay en la base?". Comandos según la
documentación oficial (verifícalos allí antes de ejecutarlos:
[Render](https://render.com/docs/mcp-server) ·
[Supabase](https://supabase.com/docs/guides/ai-tools/mcp)):

```bash
# Render: crear antes una API key en Account Settings → API Keys
claude mcp add --transport http render https://mcp.render.com/mcp \
  --header "Authorization: Bearer <RENDER_API_KEY>"

# Supabase: limitado a nuestro proyecto; autenticar después con /mcp
claude mcp add --transport http supabase \
  "https://mcp.supabase.com/mcp?project_ref=<PROJECT_REF>"
```

Reglas de uso:

- Los conectores los tiene el **docente**. Los estudiantes trabajan con su `.env`
  y con los paneles web.
- Para consultas, añadir `&read_only=true` a la URL de Supabase. Los cambios de
  esquema **no** se hacen por el conector, sino con una migración en
  `db/migraciones/` revisada en un PR.
- Mantener activada la aprobación manual de cada llamada.

## 4. Cómo se despliega

- **Automático:** cada merge a `main` redespliega en Render (`render.yaml`, tarea
  BE-006).
- **Base de datos:** las migraciones de `db/migraciones/` se aplican en orden en
  el editor SQL de Supabase, y se anota en `db/README.md` cuándo se aplicó cada
  una.
- **Datos:** la ingesta y la indexación (IA-005, IA-008) se ejecutan en local y
  escriben en Supabase. No hace falta redesplegar al cambiar la normativa.

## 5. Límites del plan gratuito que hay que conocer

| Límite | Efecto | Qué hacemos |
|---|---|---|
| Render duerme tras 15 min sin uso | La primera visita tarda ~1 min | Aviso de "despertando…" en la web; abrirla antes de una demo |
| Render: 512 MB de RAM | No cabe un modelo de embeddings local | Embeddings por API (ADR-002) |
| Supabase pausa tras 7 días sin actividad | La API deja de encontrar la base | Tarea programada que la consulta (BE-009) |
| Supabase: 500 MB | Varios miles de fragmentos caben de sobra | Vigilar el tamaño si se añaden carreras |
| Cuotas gratuitas de embeddings y LLM | Pueden agotarse o limitar la velocidad | Indexar por lotes; vigilar el uso en el panel |

## 6. Registro de despliegues

| Fecha | Qué se desplegó | URL | Quién |
|---|---|---|---|
| | | | |
