"""Mide recall@5 por modo y tipo: python -m eval.recall --fallos."""

import argparse
import json

from ia.hibrida import buscar

MODOS = ("bm25", "vectorial", "hibrida")
TIPOS = ("literal", "coloquial", "multi-articulo")


def cargar_preguntas() -> list[dict]:
    """Lee el golden set y conserva solo las preguntas respondibles."""
    preguntas = []
    with open("eval/preguntas.jsonl", encoding="utf-8") as archivo:
        for linea in archivo:
            pregunta = json.loads(linea)
            if pregunta["en_corpus"]:
                preguntas.append(pregunta)
    return preguntas


def evaluar_modo(preguntas: list[dict], modo: str) -> tuple[dict, list[dict]]:
    """Cuenta los aciertos globales y por tipo, y conserva los fallos."""
    conteos = {}
    for categoria in ("global", *TIPOS):
        conteos[categoria] = {"aciertos": 0, "total": 0}
    fallos = []

    for pregunta in preguntas:
        resultados = buscar(pregunta["pregunta"], modo=modo, k=5)
        ids_recuperados = [resultado["id"] for resultado in resultados]
        acierto = pregunta["id_esperado"] in ids_recuperados
        for categoria in ("global", pregunta["tipo"]):
            conteos[categoria]["total"] += 1
            if acierto:
                conteos[categoria]["aciertos"] += 1
        if not acierto:
            fallos.append({"pregunta": pregunta, "ids_recuperados": ids_recuperados})
    return conteos, fallos


def formatear_celda(conteo: dict) -> str:
    """Muestra los aciertos, el denominador y el porcentaje de cada grupo."""
    aciertos = conteo["aciertos"]
    total = conteo["total"]
    porcentaje = 100 * aciertos / total if total else 0
    return f"{aciertos}/{total} ({porcentaje:.1f}%)"


def mostrar_fallos(fallos_por_modo: dict) -> None:
    for modo, fallos in fallos_por_modo.items():
        print(f"\nFallos de {modo}:")
        if not fallos:
            print("Sin fallos.")
        for fallo in fallos:
            pregunta = fallo["pregunta"]
            print(f"- [{pregunta['tipo']}] {pregunta['pregunta']}")
            print(f"  Esperado: {pregunta['id_esperado']}")
            print("  Recuperados: " + ", ".join(fallo["ids_recuperados"]))


def main() -> None:
    argumentos = argparse.ArgumentParser(
        description="Compara recall@5 de BM25, vectorial e híbrida en el golden set."
    )
    argumentos.add_argument(
        "--fallos", action="store_true",
        help="Muestra las preguntas falladas y los ids recuperados en cada modo.",
    )
    opciones = argumentos.parse_args()
    preguntas = cargar_preguntas()
    print("modo | global | literal | coloquial | multi-articulo", flush=True)
    fallos_por_modo = {}
    for modo in MODOS:
        conteos, fallos = evaluar_modo(preguntas, modo)
        celdas = [formatear_celda(conteos[categoria]) for categoria in ("global", *TIPOS)]
        print(modo + " | " + " | ".join(celdas), flush=True)
        fallos_por_modo[modo] = fallos
    if opciones.fallos:
        mostrar_fallos(fallos_por_modo)


if __name__ == "__main__":
    main()
