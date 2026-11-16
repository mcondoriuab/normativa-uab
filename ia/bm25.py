"""Búsqueda por palabras con BM25, sin distinguir mayúsculas ni tildes."""

import re
import unicodedata

from rank_bm25 import BM25Okapi


def tokenizar(texto: str) -> list[str]:
    """Separa palabras en minúsculas y sin tildes para comparar los textos."""
    texto = unicodedata.normalize("NFD", texto.lower())
    sin_tildes = ""
    for caracter in texto:
        if unicodedata.category(caracter) != "Mn":
            sin_tildes += caracter
    return re.findall(r"\w+", sin_tildes)


def crear_indice_bm25(fragmentos: list[dict]) -> BM25Okapi:
    """Prepara el índice que BM25 usará para puntuar cada fragmento."""
    textos_tokenizados = []
    for fragmento in fragmentos:
        textos_tokenizados.append(tokenizar(fragmento["texto"]))
    return BM25Okapi(textos_tokenizados)


def buscar_bm25(
    pregunta: str, fragmentos: list[dict], indice, k: int = 5
) -> list[dict]:
    """Devuelve los k mejores fragmentos, ordenados de mayor a menor puntaje."""
    puntajes = indice.get_scores(tokenizar(pregunta))
    posiciones = sorted(
        range(len(fragmentos)), key=lambda posicion: puntajes[posicion], reverse=True
    )

    resultados = []
    for posicion in posiciones[:k]:
        fragmento = fragmentos[posicion]
        resultados.append({
            "id": fragmento["id"],
            "puntaje": float(puntajes[posicion]),
            "fragmento": fragmento,
        })
    return resultados
