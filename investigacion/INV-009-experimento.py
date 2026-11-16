"""INV-009, Parte 1: experimento con embeddings y similitud coseno.

Calcula el embedding de 10 frases con un modelo local multilingüe y muestra
la matriz de similitud coseno entre todas. Después compara "artículo 47" con
"artículo 48".

Uso:
    pip install sentence-transformers   (no va en requirements.txt)
    python investigacion/INV-009-experimento.py
"""

import numpy as np
from sentence_transformers import SentenceTransformer

MODELO = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

# Cada frase lleva una etiqueta corta para que la tabla quepa en pantalla.
FRASES = [
    # 3 parejas que dicen lo mismo con palabras distintas
    ("P1a", "me pueden echar por faltar mucho a clases"),
    ("P1b", "pérdida de la condición de estudiante por inasistencias"),
    ("P2a", "cuánto tengo que sacar para aprobar una materia"),
    ("P2b", "nota mínima de aprobación de una asignatura"),
    ("P3a", "me pueden dar una beca si tengo buenas notas"),
    ("P3b", "requisitos para obtener una beca por rendimiento académico"),
    # 2 frases que comparten palabras pero no significado
    ("C1", "el banco de la plaza está recién pintado"),
    ("C2", "el banco me cobró una comisión por la transferencia"),
    # 2 frases sin relación con las demás
    ("S1", "mañana va a llover en Cochabamba"),
    ("S2", "la receta lleva dos huevos y harina"),
]


def similitud_coseno(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


def imprimir_matriz(etiquetas: list[str], vectores: np.ndarray) -> None:
    print("       " + "".join(f"{e:>6}" for e in etiquetas))
    for i, fila in enumerate(etiquetas):
        celdas = ""
        for j in range(len(etiquetas)):
            celdas += f"{similitud_coseno(vectores[i], vectores[j]):6.2f}"
        print(f"{fila:>6} {celdas}")


def main() -> None:
    modelo = SentenceTransformer(MODELO)

    etiquetas = []
    textos = []
    for etiqueta, texto in FRASES:
        etiquetas.append(etiqueta)
        textos.append(texto)

    vectores = modelo.encode(textos)
    print(f"Modelo: {MODELO}")
    print(f"Dimensión del vector: {vectores.shape[1]}\n")

    for etiqueta, texto in FRASES:
        print(f"{etiqueta:>4}: {texto}")
    print("\nMatriz de similitud coseno:\n")
    imprimir_matriz(etiquetas, vectores)

    a47, a48 = modelo.encode(["artículo 47", "artículo 48"])
    print(f"\n'artículo 47' frente a 'artículo 48': {similitud_coseno(a47, a48):.3f}")


if __name__ == "__main__":
    main()
