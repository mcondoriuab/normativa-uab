-- 002_embeddings.sql (IA-008): columna embedding de fragmentos.
-- Dimensión 1024 = voyage-4 (ADR-008). Si se cambia de modelo, hace falta una
-- migración nueva y reindexar todo.

-- Ya la creó 001; se repite por si esta migración se aplica en otra base.
create extension if not exists vector with schema extensions;

alter table fragmentos add column embedding vector(1024);
