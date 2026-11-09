"""Comando: python -m ia.ingestar <carpeta> → data/fragmentos.json"""

import json
import pathlib
import sys

from ia.extraer import extraer_paginas
from ia.trocear import trocear


def contar_con_articulo(fragmentos: list[dict]) -> int:
    total = 0
    for fragmento in fragmentos:
        if fragmento["articulo"] is not None:
            total += 1
    return total


def todas_vacias(paginas: list[str]) -> bool:
    for pagina in paginas:
        if pagina.strip():
            return False
    return True


def main():
    carpeta = sys.argv[1]
    todos = []

    for ruta in sorted(pathlib.Path(carpeta).glob("*.pdf")):
        documento = ruta.stem
        paginas = extraer_paginas(str(ruta))
        fragmentos = trocear(paginas, documento)
        todos.extend(fragmentos)

        print(
            f"{documento}: {len(paginas)} páginas, {len(fragmentos)} fragmentos, "
            f"{contar_con_articulo(fragmentos)} con artículo"
        )
        if todas_vacias(paginas):
            print("  AVISO: probablemente escaneado")

    pathlib.Path("data").mkdir(exist_ok=True)
    with open("data/fragmentos.json", "w", encoding="utf-8") as archivo:
        json.dump(todos, archivo, ensure_ascii=False, indent=2)

    print(f"Total: {len(todos)} fragmentos")


if __name__ == "__main__":
    main()
