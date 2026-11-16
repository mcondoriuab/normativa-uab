from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from ia.db import conectar

app = FastAPI(title="Asistente de Normativa UAB")

AVISO = "Herramienta de apoyo. El texto oficial y vinculante es el publicado por la universidad."

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
    # Respuesta simulada (mock) hasta que el motor real llegue en BE-003.
    if "rechazo" in peticion.pregunta.lower():
        return Respuesta(
            respuesta="No encontré esa información en la normativa disponible.",
            rechazada=True,
            citas=[],
            aviso=AVISO,
        )

    citas = [
        Cita(n=1, documento="ejemplo", articulo="1", pagina=1, texto="(respuesta simulada)"),
        Cita(n=2, documento="ejemplo", articulo=None, pagina=2, texto="(respuesta simulada)"),
    ]
    return Respuesta(
        respuesta="Esta es una respuesta simulada [1]. Más adelante vendrá del motor real [2].",
        rechazada=False,
        citas=citas,
        aviso=AVISO,
    )


# Va al final: si se monta antes, la web en "/" tapa las rutas de la API.
app.mount("/", StaticFiles(directory=CARPETA_WEB, html=True), name="web")
