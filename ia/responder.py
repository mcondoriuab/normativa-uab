"""Responde preguntas con citas, o rechaza si no hay evidencia suficiente.

Une la búsqueda, el prompt del sistema y la capa del LLM, y devuelve el
diccionario con la forma exacta de la respuesta de `POST /preguntar`
(docs/ARQUITECTURA.md, sección *API*).
"""

import json
import re
import sys

from ia.hibrida import buscar
from ia.llm import generar
from ia.prompts import FRASE_RECHAZO, SISTEMA

MODO_BUSQUEDA = "hibrida"      # lo confirma o lo cambia el ADR de IA-012
UMBRAL_RELEVANCIA = 0.5       # calibrado en historial/evaluaciones/2026-11-16-umbral.md
AVISO = (
    "Herramienta de apoyo. El texto oficial y vinculante es el publicado por "
    "la universidad."
)


def armar_mensaje(pregunta: str, resultados: list[dict]) -> str:
    """Numera los fragmentos y termina con la pregunta del usuario."""
    partes = []
    for n, resultado in enumerate(resultados, start=1):
        fragmento = resultado["fragmento"]
        referencia = f"{fragmento['documento']}, "
        if fragmento["articulo"] is not None:
            referencia += f"Art. {fragmento['articulo']}, "
        referencia += f"pág. {fragmento['pagina']}"
        partes.append(f"[{n}] {referencia}:\n{fragmento['texto']}")

    partes.append(f"Pregunta: {pregunta}")
    return "\n\n".join(partes)


def extraer_citas(texto: str, resultados: list[dict]) -> list[dict]:
    """Devuelve una cita por cada `[n]` del texto, en orden y sin repetir."""
    citas = []
    vistos = set()
    for numero in re.findall(r"\[(\d+)\]", texto):
        n = int(numero)
        # Si el modelo cita un número que no existe, se ignora.
        if n in vistos or not 1 <= n <= len(resultados):
            continue
        vistos.add(n)

        fragmento = resultados[n - 1]["fragmento"]
        citas.append({
            "n": n,
            "documento": fragmento["documento"],
            "articulo": fragmento["articulo"],
            "pagina": fragmento["pagina"],
            "texto": fragmento["texto"],
        })

    return citas


def respuesta_rechazo() -> dict:
    """Respuesta del contrato cuando no hay evidencia suficiente."""
    return {
        "respuesta": FRASE_RECHAZO,
        "rechazada": True,
        "citas": [],
        "aviso": AVISO,
    }


def responder(pregunta: str) -> dict:
    """Busca, redacta con el modelo y devuelve la respuesta con sus citas."""
    resultados = buscar(pregunta, modo=MODO_BUSQUEDA, k=5)

    # Un resultado puede venir solo de BM25 y no traer puntaje vectorial.
    puntajes = [
        resultado["puntaje_vectorial"]
        for resultado in resultados
        if resultado.get("puntaje_vectorial") is not None
    ]
    if not puntajes or max(puntajes) < UMBRAL_RELEVANCIA:
        return respuesta_rechazo()

    texto = generar(SISTEMA, armar_mensaje(pregunta, resultados))

    if FRASE_RECHAZO in texto:
        return respuesta_rechazo()

    return {
        "respuesta": texto,
        "rechazada": False,
        "citas": extraer_citas(texto, resultados),
        "aviso": AVISO,
    }


if __name__ == "__main__":
    print(json.dumps(responder(sys.argv[1]), ensure_ascii=False, indent=2))
