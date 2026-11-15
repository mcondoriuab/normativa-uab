"""Embeddings con Voyage AI (modelo y forma de uso en ADR-008).

Los fragmentos se codifican como "document" y las preguntas como "query": si
no se indica, la calidad baja sin ningún error visible.
"""

import os
import time

import voyageai
from dotenv import load_dotenv

MODELO = "voyage-4"
TAMANO_LOTE = 50
ESPERA_SEGUNDOS = 20
MAX_REINTENTOS = 3


def _cliente() -> voyageai.Client:
    load_dotenv()
    return voyageai.Client(api_key=os.environ["EMBEDDINGS_API_KEY"])


def _codificar_lote(cliente, textos: list[str], tipo: str) -> list[list[float]]:
    """Pide un lote; si la API devuelve límite de velocidad, espera y reintenta."""
    for intento in range(MAX_REINTENTOS + 1):
        try:
            resultado = cliente.embed(textos, model=MODELO, input_type=tipo)
            return resultado.embeddings
        except voyageai.error.RateLimitError:
            if intento == MAX_REINTENTOS:
                raise
            print(f"Límite de velocidad de la API; espero {ESPERA_SEGUNDOS} s...")
            time.sleep(ESPERA_SEGUNDOS)


def codificar_documentos(textos: list[str]) -> list[list[float]]:
    cliente = _cliente()
    vectores = []
    for inicio in range(0, len(textos), TAMANO_LOTE):
        lote = textos[inicio:inicio + TAMANO_LOTE]
        vectores.extend(_codificar_lote(cliente, lote, "document"))
    return vectores


def codificar_pregunta(texto: str) -> list[float]:
    vectores = _codificar_lote(_cliente(), [texto], "query")
    return vectores[0]
