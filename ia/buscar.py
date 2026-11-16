"""Comando: python -m ia.buscar \"pregunta\" --modo hibrida --k 5."""

import argparse

from ia.hibrida import buscar


def main() -> None:
    """Lee las opciones de consola y muestra los fragmentos encontrados."""
    argumentos = argparse.ArgumentParser(
        description="Busca fragmentos de la normativa universitaria."
    )
    argumentos.add_argument("pregunta", help="Pregunta que se quiere buscar.")
    argumentos.add_argument(
        "--modo",
        choices=["bm25", "vectorial", "hibrida"],
        default="hibrida",
        help="Tipo de búsqueda (por defecto: hibrida).",
    )
    argumentos.add_argument(
        "--k",
        type=int,
        default=5,
        help="Cantidad de resultados que se mostrarán (por defecto: 5).",
    )
    opciones = argumentos.parse_args()

    resultados = buscar(opciones.pregunta, modo=opciones.modo, k=opciones.k)
    for posicion, resultado in enumerate(resultados, start=1):
        fragmento = resultado["fragmento"]
        print(
            f"{posicion}. Puntaje: {resultado['puntaje']:.3f} | "
            f"{resultado['id']} | Página: {fragmento['pagina']}"
        )
        print(fragmento["texto"][:200])
        print()


if __name__ == "__main__":
    main()
