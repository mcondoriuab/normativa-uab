"""Capa que aísla qué modelo de lenguaje se usa.

Esta es la única pieza que conoce el proveedor de LLM. El resto del código
llama a `generar(sistema, mensaje)` sin saber si detrás hay Groq, Ollama u otro.
Cumple el principio 3 de ARQUITECTURA.md: modelo intercambiable.
"""

import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

API_KEY = os.getenv("LLM_API_KEY")
MODELO = os.getenv("NORMATIVA_LLM_MODELO")


def _verificar_entorno() -> None:
    """Lanza error si faltan variables críticas."""
    if not API_KEY:
        raise ValueError(
            "Falta LLM_API_KEY en el entorno. Copia .env.ejemplo a .env y "
            "configura la clave de API."
        )
    if not MODELO:
        raise ValueError(
            "Falta NORMATIVA_LLM_MODELO en el entorno. Configúralo en .env "
            "ejemplo: NORMATIVA_LLM_MODELO=openai/gpt-oss-120b"
        )


def generar(sistema: str, mensaje: str) -> str:
    """Generar una respuesta del modelo de lenguaje.

    - Lee LLM_API_KEY y NORMATIVA_LLM_MODELO del entorno.
    - Llama al modelo con `sistema` como mensaje de sistema y `mensaje` como
      mensaje del usuario, con temperatura 0: en normativa queremos respuestas
      repetibles, no creativas.
    - Devuelve solo el texto de la respuesta.

    Args:
        sistema: Instrucciones del sistema (reglas, contexto).
        mensaje: Pregunta o mensaje del usuario.

    Returns:
        Texto plano de la respuesta del modelo.
    """
    _verificar_entorno()

    cliente = Groq(api_key=API_KEY)

    respuesta = cliente.chat.completions.create(
        model=MODELO,
        messages=[
            {"role": "system", "content": sistema},
            {"role": "user", "content": mensaje},
        ],
        temperature=0,
    )

    return respuesta.choices[0].message.content.strip()