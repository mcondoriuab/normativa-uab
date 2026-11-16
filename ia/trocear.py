"""Convierte el texto de las páginas de un PDF en fragmentos (contrato Fragmento)."""

import re

# Encabezado de artículo al inicio de una línea. Variantes reales del corpus
# (ver investigacion/IA-002-estructura-pdf.md):
#   "Artículo 12.- (...)", "Artículo 3.-  (...)", "Artículos 23.- (...)" (errata).
# Se exige ".-" tras el número para no confundirlo con referencias como
# "Art. 6 del presente reglamento.", que a veces caen a principio de línea.
PATRON_ARTICULO = re.compile(
    r"^\s*(art[íi]culos?)\s+(\d+(?:\s*bis)?)\s*\.\s*-",
    re.IGNORECASE | re.MULTILINE,
)


# Pies y encabezados de página: "Reglamento de Becas Pag 2 de 7",
# "Reglamento de Investigación “UAB”   Página 4 de 16" y la línea "▬▬▬▬".
PATRON_PIE_DE_PAGINA = re.compile(r"p[aá]g(ina)?\s+\d+\s+de\s+\d+|^\s*▬+\s*$", re.IGNORECASE)

# "TÍTULO II", "CAPITULO III", "CAPÍTULO ÚNICO": solo en mayúsculas y solos en
# su línea, para no confundirlos con un texto que empiece por "título".
PATRON_TITULO_O_CAPITULO = re.compile(r"^\s*(T[IÍ]TULO|CAP[IÍ]TULO)\s+([IVXLC]+|[ÚU]NICO)\s*$", re.MULTILINE)


def quitar_pies_de_pagina(texto: str) -> str:
    lineas_buenas = []
    for linea in texto.split("\n"):
        if not PATRON_PIE_DE_PAGINA.search(linea):
            lineas_buenas.append(linea)
    return "\n".join(lineas_buenas)


def quitar_titulos_del_final(texto: str) -> str:
    """Corta el TÍTULO/CAPÍTULO que precede al artículo siguiente y quedó al final."""
    encontrado = PATRON_TITULO_O_CAPITULO.search(texto)
    if encontrado is None:
        return texto
    return texto[:encontrado.start()]


def normalizar_numero(numero: str) -> str:
    """Deja el número como "47" o "47 bis" (un espacio, en minúsculas)."""
    numero = numero.lower().replace("bis", " bis")
    return " ".join(numero.split())


def nuevo_fragmento(documento: str, articulo, pagina: int, id_fragmento: str) -> dict:
    return {
        "id": id_fragmento,
        "documento": documento,
        "articulo": articulo,
        "pagina": pagina,
        "texto": "",
    }


def quedarse_con_el_mas_largo(fragmentos: list[dict]) -> list[dict]:
    """Si un id se repite (p. ej. por un índice), conserva el de texto más largo."""
    por_id = {}
    for fragmento in fragmentos:
        anterior = por_id.get(fragmento["id"])
        if anterior is None or len(fragmento["texto"]) > len(anterior["texto"]):
            por_id[fragmento["id"]] = fragmento
    return list(por_id.values())


def trocear_por_articulos(paginas: list[str], documento: str) -> list[dict]:
    fragmentos = []
    abierto = None  # El fragmento al que se va añadiendo texto.

    for numero_pagina, texto in enumerate(paginas, start=1):
        desde = 0  # Posición de la página a partir de la cual falta copiar texto.
        for encabezado in PATRON_ARTICULO.finditer(texto):
            if abierto is not None:
                abierto["texto"] += texto[desde:encabezado.start()]
                fragmentos.append(abierto)
            numero = normalizar_numero(encabezado.group(2))
            abierto = nuevo_fragmento(documento, numero, numero_pagina, f"{documento}#art-{numero}")
            desde = encabezado.start()
        # Lo que queda de la página es del fragmento abierto. Si aún no hay
        # ninguno, es portada o preámbulo y se descarta.
        if abierto is not None:
            abierto["texto"] += texto[desde:] + "\n"

    if abierto is not None:
        fragmentos.append(abierto)

    for fragmento in fragmentos:
        fragmento["texto"] = quitar_titulos_del_final(fragmento["texto"]).strip()
    return quedarse_con_el_mas_largo(fragmentos)


def partir_en_parrafos(texto: str) -> list[str]:
    partes = texto.split("\n\n")
    if len(partes) == 1:
        partes = texto.split("\n")
    parrafos = []
    for parte in partes:
        if parte.strip():
            parrafos.append(parte.strip())
    return parrafos


def trocear_por_longitud(paginas: list[str], documento: str, max_caracteres: int = 1500) -> list[dict]:
    fragmentos = []
    actual = None

    for numero_pagina, texto in enumerate(paginas, start=1):
        for parrafo in partir_en_parrafos(texto):
            # +1 por el salto de línea que separa los párrafos.
            if actual is not None and len(actual["texto"]) + 1 + len(parrafo) > max_caracteres:
                fragmentos.append(actual)
                actual = None
            if actual is None:
                n = len(fragmentos) + 1
                actual = nuevo_fragmento(documento, None, numero_pagina, f"{documento}#frag-{n}")
                actual["texto"] = parrafo
            else:
                actual["texto"] += "\n" + parrafo

    if actual is not None:
        fragmentos.append(actual)
    return fragmentos


def trocear(paginas: list[str], documento: str) -> list[dict]:
    paginas_limpias = []
    for texto in paginas:
        paginas_limpias.append(quitar_pies_de_pagina(texto))
    paginas = paginas_limpias

    fragmentos = trocear_por_articulos(paginas, documento)
    # Con menos de 3 artículos, el documento probablemente no está organizado
    # por artículos (o la detección falló): se trocea por longitud.
    if len(fragmentos) < 3:
        return trocear_por_longitud(paginas, documento)
    return fragmentos
