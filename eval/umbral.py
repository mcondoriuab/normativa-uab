"""Calibra el umbral de relevancia con el golden set.

Para cada pregunta busca con el modo híbrido, extrae el mayor
puntaje vectorial y muestra una tabla de umbrales candidatos
para elegir el que mejor separa las preguntas del corpus
de las que están fuera.

No llama al LLM: solo usa la búsqueda.
"""

import json
import pathlib

from ia.hibrida import buscar
from ia.responder import MODO_BUSQUEDA

RUTA_PREGUNTAS = pathlib.Path(__file__).with_name("preguntas.jsonl")
UMBRALES_CANDIDATOS = [0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6]


def cargar_preguntas() -> list[dict]:
    """Lee el golden set desde preguntas.jsonl."""
    preguntas = []
    for linea in RUTA_PREGUNTAS.read_text(encoding="utf-8").splitlines():
        linea = linea.strip()
        if linea:
            preguntas.append(json.loads(linea))
    return preguntas


def mayor_puntaje_vectorial(resultados: list[dict]) -> float | None:
    """Devuelve el mayor puntaje vectorial o None si no hay."""
    puntajes = [
        resultado["puntaje_vectorial"]
        for resultado in resultados
        if resultado.get("puntaje_vectorial") is not None
    ]
    if not puntajes:
        return None
    return max(puntajes)


def buscar_todas() -> list[dict]:
    """Busca cada pregunta y guarda el mayor puntaje vectorial."""
    preguntas = cargar_preguntas()
    resultados = []

    for pregunta in preguntas:
        fragmentos = buscar(pregunta["pregunta"], modo=MODO_BUSQUEDA, k=5)
        puntaje = mayor_puntaje_vectorial(fragmentos)
        resultados.append({
            "pregunta": pregunta["pregunta"],
            "en_corpus": pregunta["en_corpus"],
            "tipo": pregunta["tipo"],
            "mayor_puntaje": puntaje,
        })

    return resultados


def imprimir_tabla_puntajes(resultados: list[dict]) -> None:
    """Muestra los puntajes ordenados, separados por grupo."""
    print("=" * 70)
    print("PUNTAJES VECTORIALES DEL GOLDEN SET")
    print("=" * 70)

    en_corpus = [r for r in resultados if r["en_corpus"]]
    fuera_corpus = [r for r in resultados if not r["en_corpus"]]

    en_corpus_ordenados = sorted(en_corpus, key=lambda r: r["mayor_puntaje"] or -1, reverse=True)
    fuera_corpus_ordenados = sorted(fuera_corpus, key=lambda r: r["mayor_puntaje"] or -1, reverse=True)

    print(f"\nDentro del corpus ({len(en_corpus_ordenados)} preguntas):")
    print("-" * 70)
    for r in en_corpus_ordenados:
        puntaje = f"{r['mayor_puntaje']:.4f}" if r["mayor_puntaje"] is not None else "None"
        print(f"  {puntaje:>10}  [{r['tipo']}] {r['pregunta'][:60]}")

    print(f"\nFuera del corpus ({len(fuera_corpus_ordenados)} preguntas):")
    print("-" * 70)
    for r in fuera_corpus_ordenados:
        puntaje = f"{r['mayor_puntaje']:.4f}" if r["mayor_puntaje"] is not None else "None"
        print(f"  {puntaje:>10}  [{r['tipo']}] {r['pregunta'][:60]}")


def imprimir_tabla_umbral(resultados: list[dict]) -> None:
    """Muestra cuántas preguntas se rechazarían con cada umbral candidato."""
    en_corpus = [r for r in resultados if r["en_corpus"]]
    fuera_corpus = [r for r in resultados if not r["en_corpus"]]

    print("\n" + "=" * 70)
    print("TABLA DE UMBRALES CANDIDATOS")
    print("=" * 70)
    print(f"\n{'Umbral':>8}  {'Rechaza en corpus':>18}  {'Rechaza fuera corpus':>21}")
    print("-" * 70)

    for umbral in UMBRALES_CANDIDATOS:
        rechazadas_corpus = sum(
            1 for r in en_corpus
            if r["mayor_puntaje"] is None or r["mayor_puntaje"] < umbral
        )
        rechazadas_fuera = sum(
            1 for r in fuera_corpus
            if r["mayor_puntaje"] is None or r["mayor_puntaje"] < umbral
        )
        print(f"  {umbral:>8.4f}  {rechazadas_corpus:>18}  {rechazadas_fuera:>21}")

    print("\n" + "-" * 70)
    print("Nota: Se busca rechazar TODAS (o casi todas) las fuera de corpus")
    print("rechazando el MÍNIMO de las dentro de corpus.")
    print("-" * 70)


def main():
    """Ejecuta la calibración del umbral."""
    print("Cargando fragmentos y ejecutando búsqueda para cada pregunta...")
    resultados = buscar_todas()

    imprimir_tabla_puntajes(resultados)
    imprimir_tabla_umbral(resultados)


if __name__ == "__main__":
    main()
