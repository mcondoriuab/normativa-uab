# db/

Esquema de la base de datos (Postgres + pgvector en Supabase). Se versiona como
**migraciones**: archivos SQL numerados que se aplican en orden y **nunca se
editan** una vez aplicados. Para cambiar algo, se escribe una migración nueva.

| Migración | Qué hace | Tarea | Aplicada en Supabase |
|---|---|---|---|
| `001_inicial.sql` | Extensión `vector`, tablas `fragmentos` y `consultas` | BE-008 | _(fecha)_ |

Cómo aplicar una migración: Supabase → *SQL Editor* → pegar el archivo →
*Run*. Anotar la fecha en la tabla.

El acceso desde Python está en `ia/db.py` (BE-008) y lee `DATABASE_URL` del
entorno (ver `.env.ejemplo`).
