"""Búsqueda vectorial: los fragmentos más cercanos a la pregunta (pgvector)."""

from ia.db import conectar, vector_a_texto
from ia.embeddings import codificar_pregunta

# <=> es la distancia coseno de pgvector; 1 - distancia = similitud coseno.
SQL_BUSCAR = """
    select id, documento, articulo, pagina, texto,
           1 - (embedding <=> %(v)s::vector) as puntaje
    from fragmentos
    order by embedding <=> %(v)s::vector
    limit %(k)s
"""


def buscar_vectorial(pregunta: str, k: int = 5) -> list[dict]:
    vector = vector_a_texto(codificar_pregunta(pregunta))
    with conectar() as conexion:
        filas = conexion.execute(SQL_BUSCAR, {"v": vector, "k": k}).fetchall()

    resultados = []
    for fila in filas:
        fragmento = {
            "id": fila["id"],
            "documento": fila["documento"],
            "articulo": fila["articulo"],
            "pagina": fila["pagina"],
            "texto": fila["texto"],
        }
        resultados.append({"id": fila["id"], "puntaje": fila["puntaje"], "fragmento": fragmento})
    return resultados
