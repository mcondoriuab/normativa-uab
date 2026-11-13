-- 001_inicial.sql (BE-008): tablas del contrato de docs/ARQUITECTURA.md.
-- La columna embedding de fragmentos la añade IA-008 en otra migración,
-- cuando se conozca la dimensión del modelo (INV-009).

-- En el esquema extensions, como recomienda Supabase; el tipo vector se sigue
-- pudiendo usar sin prefijo.
create extension if not exists vector with schema extensions;

create table fragmentos (
  id text primary key,
  documento text not null,
  articulo text,
  pagina integer not null,
  texto text not null
);

create table consultas (
  id bigint generated always as identity primary key,
  creada_en timestamptz default now(),
  pregunta text,
  rechazada boolean,
  ids_citados text[],
  latencia_ms integer
);

-- RLS sin políticas: la API pública de Supabase no puede leer ni escribir.
-- Nuestro backend entra con DATABASE_URL como dueño de las tablas y no le afecta.
alter table fragmentos enable row level security;
alter table consultas enable row level security;
