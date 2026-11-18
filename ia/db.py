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


def vector_a_texto(vector: list[float]) -> str:
    """Convierte [0.1, 0.2] en '[0.1,0.2]', el formato de texto de pgvector."""
    numeros = []
    for numero in vector:
        numeros.append(str(numero))
    return "[" + ",".join(numeros) + "]"


def guardar_embeddings(fragmentos: list[dict], embeddings: list[list[float]]) -> None:
    """Guarda cada fragmento con su embedding; si el id ya existe, lo actualiza."""
    sql = """
        insert into fragmentos (id, documento, articulo, pagina, texto, embedding)
        values (%(id)s, %(documento)s, %(articulo)s, %(pagina)s, %(texto)s,
                %(embedding)s::vector)
        on conflict (id) do update set
            documento = excluded.documento,
            articulo = excluded.articulo,
            pagina = excluded.pagina,
            texto = excluded.texto,
            embedding = excluded.embedding
    """
    filas = []
    for fragmento, embedding in zip(fragmentos, embeddings):
        fila = dict(fragmento)
        fila["embedding"] = vector_a_texto(embedding)
        filas.append(fila)
    with conectar() as conexion:
        with conexion.cursor() as cursor:
            cursor.executemany(sql, filas)


def leer_fragmentos() -> list[dict]:
    """Devuelve todos los fragmentos con las claves del contrato Fragmento."""
    with conectar() as conexion:
        filas = conexion.execute(
            "select id, documento, articulo, pagina, texto from fragmentos order by id"
        ).fetchall()
    return filas


def guardar_consulta(
    pregunta: str, rechazada: bool, ids_citados: list[str], latencia_ms: int
) -> None:
    """Guarda la pregunta y sus resultados sin datos de quien la envió."""
    sql = """
        insert into consultas (pregunta, rechazada, ids_citados, latencia_ms)
        values (%s, %s, %s, %s)
    """
    with conectar() as conexion:
        conexion.execute(sql, (pregunta, rechazada, ids_citados, latencia_ms))
