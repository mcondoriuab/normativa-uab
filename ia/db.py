"""Único acceso a la base de datos (Postgres en Supabase).

Todas las consultas van con parámetros (%s o %(nombre)s): psycopg envía los
valores aparte del SQL, así que un texto con comillas no puede cambiar la
consulta (inyección SQL).
"""

import os

import psycopg
from dotenv import load_dotenv
from psycopg.rows import dict_row


def conectar() -> psycopg.Connection:
    """Abre una conexión con DATABASE_URL. Úsala con `with`: al salir hace commit."""
    load_dotenv()
    url = os.getenv("DATABASE_URL")
    if not url:
        raise ValueError(
            "Falta DATABASE_URL en el entorno. Copia .env.ejemplo a .env y pon "
            "la cadena de Supabase → Connect → Session pooler (te la pasa el docente)."
        )
    return psycopg.connect(url, row_factory=dict_row)


def guardar_fragmentos(fragmentos: list[dict]) -> None:
    """Inserta los fragmentos; si un id ya existe, lo actualiza (upsert)."""
    sql = """
        insert into fragmentos (id, documento, articulo, pagina, texto)
        values (%(id)s, %(documento)s, %(articulo)s, %(pagina)s, %(texto)s)
        on conflict (id) do update set
            documento = excluded.documento,
            articulo = excluded.articulo,
            pagina = excluded.pagina,
            texto = excluded.texto
    """
    with conectar() as conexion:
        with conexion.cursor() as cursor:
            cursor.executemany(sql, fragmentos)


def leer_fragmentos() -> list[dict]:
    """Devuelve todos los fragmentos con las claves del contrato Fragmento."""
    with conectar() as conexion:
        filas = conexion.execute(
            "select id, documento, articulo, pagina, texto from fragmentos order by id"
        ).fetchall()
    return filas
