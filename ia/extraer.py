"""Extrae el texto de un PDF, página por página."""

import sys

import pypdf


def extraer_paginas(ruta_pdf: str) -> list[str]:
    """Devuelve el texto de cada página. El índice 0 es la página 1."""
    reader = pypdf.PdfReader(ruta_pdf)
    paginas = []
    for pagina in reader.pages:
        texto = pagina.extract_text()
        # Una página escaneada (solo imagen) no tiene texto: devuelve None o "".
        if texto is None:
            texto = ""
        paginas.append(texto)
    return paginas


if __name__ == "__main__":
    ruta = sys.argv[1]
    paginas = extraer_paginas(ruta)
    print("Páginas:", len(paginas))
    if paginas:
        print(paginas[0][:500])
