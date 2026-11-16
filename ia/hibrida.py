"""Entrada común para buscar por palabras, por significado o con ambas."""

from ia.bm25 import buscar_bm25, crear_indice_bm25
from ia.db import leer_fragmentos
from ia.vectorial import buscar_vectorial

_fragmentos = None
_indice = None


def fusionar_rrf(listas: list[list[dict]], k: int = 5, K: int = 60) -> list[dict]:
    """Combina las posiciones de los resultados y acumula puntos por id."""
    resultados_por_id = {}
    for lista in listas:
        for posicion, resultado in enumerate(lista, start=1):
            identificador = resultado["id"]
            if identificador not in resultados_por_id:
                resultados_por_id[identificador] = {
                    "id": identificador,
                    "puntaje": 0.0,
                    "fragmento": resultado["fragmento"],
                }
            resultados_por_id[identificador]["puntaje"] += 1 / (K + posicion)

    ordenados = sorted(
        resultados_por_id.values(),
        key=lambda resultado: resultado["puntaje"],
        reverse=True,
    )
    return ordenados[:k]


def cargar() -> None:
    """Carga los fragmentos de la base y conserva su índice BM25 en memoria."""
    global _fragmentos, _indice
    fragmentos = leer_fragmentos()
    indice = crear_indice_bm25(fragmentos)
    _fragmentos = fragmentos
    _indice = indice


def buscar(pregunta: str, modo: str = "hibrida", k: int = 5) -> list[dict]:
    """Busca con el modo elegido y reutiliza los fragmentos ya cargados."""
    if modo not in ("bm25", "vectorial", "hibrida"):
        raise ValueError("El modo debe ser bm25, vectorial o hibrida.")
    if _fragmentos is None:
        cargar()

    if modo == "bm25":
        return buscar_bm25(pregunta, _fragmentos, _indice, k=k)
    if modo == "vectorial":
        return buscar_vectorial(pregunta, k=k)

    resultados_bm25 = buscar_bm25(pregunta, _fragmentos, _indice, k=20)
    resultados_vectoriales = buscar_vectorial(pregunta, k=20)
    resultados = fusionar_rrf([resultados_bm25, resultados_vectoriales], k=k)

    puntajes_vectoriales = {}
    for resultado in resultados_vectoriales:
        puntajes_vectoriales[resultado["id"]] = resultado["puntaje"]
    for resultado in resultados:
        resultado["puntaje_vectorial"] = puntajes_vectoriales.get(resultado["id"])
    return resultados
