import logging
import time
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from ia.db import conectar, guardar_consulta
from ia.hibrida import cargar
from ia.responder import responder

# Uvicorn configura este logger para que el mensaje de arranque sea visible.
registro = logging.getLogger("uvicorn.error")


@asynccontextmanager
async def ciclo_de_vida(app: FastAPI):
    """Prepara el índice antes de que la API acepte la primera pregunta."""
    inicio = time.perf_counter()
    cargar()
    registro.info("Índice BM25 cargado en %.3f segundos.", time.perf_counter() - inicio)
    yield


app = FastAPI(title="Asistente de Normativa UAB", lifespan=ciclo_de_vida)

# Se calcula desde este archivo para que funcione al arrancar desde cualquier carpeta.
CARPETA_WEB = Path(__file__).resolve().parent.parent / "web"


class Peticion(BaseModel):
    pregunta: str = Field(min_length=1, max_length=500)


class Cita(BaseModel):
    n: int
    documento: str
    articulo: str | None
    pagina: int
    texto: str


class Respuesta(BaseModel):
    respuesta: str
    rechazada: bool
    citas: list[Cita]
    aviso: str


@app.get("/salud")
def salud():
    try:
        with conectar() as conexion:
            conexion.execute("select 1")
    except Exception:
        # La respuesta es pública: no se dice por qué falló.
        return JSONResponse(
            status_code=503,
            content={"estado": "error", "base_de_datos": "error"},
        )
    return {"estado": "ok", "base_de_datos": "ok"}


@app.post("/preguntar", response_model=Respuesta)
def preguntar(peticion: Peticion):
    inicio = time.perf_counter()
    try:
        respuesta = responder(peticion.pregunta)
    except Exception:
        registro.exception("No se pudo generar la respuesta del asistente.")
        raise HTTPException(
            status_code=503,
            detail="El asistente no está disponible. Inténtalo más tarde.",
        )

    latencia_ms = int((time.perf_counter() - inicio) * 1000)
    ids_citados = []
    for cita in respuesta["citas"]:
        if cita["articulo"] is None:
            identificador = cita["documento"]
        else:
            identificador = f"{cita['documento']}#art-{cita['articulo']}"
        ids_citados.append(identificador)

    try:
        guardar_consulta(peticion.pregunta, respuesta["rechazada"], ids_citados, latencia_ms)
    except Exception:
        registro.exception("No se pudo guardar la consulta anónima.")
    return respuesta


# Va al final: si se monta antes, la web en "/" tapa las rutas de la API.
app.mount("/", StaticFiles(directory=CARPETA_WEB, html=True), name="web")
