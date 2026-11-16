"""Guarda en la base todos los fragmentos con su embedding.

Uso: python -m ia.indexar

Se puede repetir: los fragmentos que ya existen se actualizan, no se duplican.
"""

import json
import time

from ia.db import guardar_embeddings
from ia.embeddings import codificar_documentos


def main() -> None:
    inicio = time.time()
    with open("data/fragmentos.json", encoding="utf-8") as archivo:
        fragmentos = json.load(archivo)

    textos = []
    for fragmento in fragmentos:
        textos.append(fragmento["texto"])

    embeddings = codificar_documentos(textos)
    guardar_embeddings(fragmentos, embeddings)

    segundos = time.time() - inicio
    print(f"Guardados {len(fragmentos)} fragmentos en {segundos:.1f} s")


if __name__ == "__main__":
    main()
