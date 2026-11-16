"""INV-009, Parte 2: comparar modelos de embeddings con nuestro golden set.

Para cada modelo, codifica todos los fragmentos y las preguntas del golden set
con `en_corpus: true`, ordena los fragmentos por similitud coseno y cuenta en
cuántas preguntas el `id_esperado` sale entre los 5 primeros.

Uso:
    pip install voyageai python-dotenv sentence-transformers
    python investigacion/INV-009-comparar-modelos.py

Necesita EMBEDDINGS_API_KEY (clave de Voyage AI) en el archivo .env.
"""

import json
import os
import time

import numpy as np
import voyageai
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

MODELOS_VOYAGE = ["voyage-4", "voyage-multilingual-2"]
MODELO_LOCAL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
# Lotes pequeños para que una sola petición no pase de 10K tokens.
TAMANO_LOTE = 20
# Sin método de pago, Voyage limita a 3 peticiones y 10K tokens por minuto:
# hay que esperar a que pase la ventana de un minuto.
ESPERA_SEGUNDOS = 60
MAX_REINTENTOS = 3
TOP = 5


def leer_fragmentos() -> list[dict]:
    with open("data/fragmentos.json", encoding="utf-8") as archivo:
        return json.load(archivo)


def leer_preguntas() -> list[dict]:
    preguntas = []
    with open("eval/preguntas.jsonl", encoding="utf-8") as archivo:
        for linea in archivo:
            pregunta = json.loads(linea)
            if pregunta["en_corpus"]:
                preguntas.append(pregunta)
    return preguntas


def codificar_con_voyage(cliente, textos: list[str], modelo: str, tipo: str):
    """Devuelve (vectores, tokens). `tipo` es "document" o "query"."""
    vectores = []
    tokens = 0
    for inicio in range(0, len(textos), TAMANO_LOTE):
        lote = textos[inicio:inicio + TAMANO_LOTE]
        for intento in range(MAX_REINTENTOS + 1):
            try:
                resultado = cliente.embed(lote, model=modelo, input_type=tipo)
                break
            except voyageai.error.RateLimitError:
                if intento == MAX_REINTENTOS:
                    raise
                print(f"  límite de velocidad; espero {ESPERA_SEGUNDOS} s...")
                time.sleep(ESPERA_SEGUNDOS)
        vectores.extend(resultado.embeddings)
        tokens += resultado.total_tokens
    return np.array(vectores), tokens


def contar_aciertos(vectores_fragmentos, vectores_preguntas, fragmentos, preguntas):
    """Devuelve cuántas preguntas tienen su id_esperado en el top-5, y el detalle."""
    # Normalizamos para que el producto punto sea directamente el coseno.
    normas_f = np.linalg.norm(vectores_fragmentos, axis=1, keepdims=True)
    normas_p = np.linalg.norm(vectores_preguntas, axis=1, keepdims=True)
    unitarios_f = vectores_fragmentos / normas_f
    unitarios_p = vectores_preguntas / normas_p

    aciertos = 0
    detalle = []
    for i, pregunta in enumerate(preguntas):
        similitudes = unitarios_f @ unitarios_p[i]
        mejores = np.argsort(similitudes)[::-1][:TOP]
        ids_top = [fragmentos[j]["id"] for j in mejores]
        acerto = pregunta["id_esperado"] in ids_top
        if acerto:
            aciertos += 1
        detalle.append((pregunta["tipo"], acerto))
    return aciertos, detalle


def aciertos_por_tipo(detalle) -> str:
    totales = {}
    buenos = {}
    for tipo, acerto in detalle:
        totales[tipo] = totales.get(tipo, 0) + 1
        if acerto:
            buenos[tipo] = buenos.get(tipo, 0) + 1
    partes = []
    for tipo in sorted(totales):
        partes.append(f"{tipo} {buenos.get(tipo, 0)}/{totales[tipo]}")
    return ", ".join(partes)


def imprimir_resultado(nombre, aciertos, total, detalle, tokens, segundos, dimension):
    print(f"{nombre}: {aciertos}/{total}  ({aciertos_por_tipo(detalle)})")
    print(f"  dimensión {dimension} · tokens {tokens} · {segundos:.1f} s\n")


def main() -> None:
    load_dotenv()
    fragmentos = leer_fragmentos()
    preguntas = leer_preguntas()
    textos_fragmentos = [f["texto"] for f in fragmentos]
    textos_preguntas = [p["pregunta"] for p in preguntas]
    print(f"{len(fragmentos)} fragmentos, {len(preguntas)} preguntas\n")

    # Referencia: modelo local, sin distinción entre documento y pregunta.
    inicio = time.time()
    local = SentenceTransformer(MODELO_LOCAL)
    v_frag = local.encode(textos_fragmentos)
    v_preg = local.encode(textos_preguntas)
    aciertos, detalle = contar_aciertos(v_frag, v_preg, fragmentos, preguntas)
    imprimir_resultado("local MiniLM-L12-v2", aciertos, len(preguntas), detalle,
                       "-", time.time() - inicio, v_frag.shape[1])

    cliente = voyageai.Client(api_key=os.environ["EMBEDDINGS_API_KEY"])
    for modelo in MODELOS_VOYAGE:
        inicio = time.time()
        try:
            v_frag, tokens_f = codificar_con_voyage(cliente, textos_fragmentos, modelo, "document")
            v_preg, tokens_p = codificar_con_voyage(cliente, textos_preguntas, modelo, "query")
        except voyageai.error.VoyageError as error:
            print(f"{modelo}: ERROR {type(error).__name__}: {error}\n")
            continue
        aciertos, detalle = contar_aciertos(v_frag, v_preg, fragmentos, preguntas)
        imprimir_resultado(modelo, aciertos, len(preguntas), detalle,
                           tokens_f + tokens_p, time.time() - inicio, v_frag.shape[1])


if __name__ == "__main__":
    main()
