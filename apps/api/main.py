from fastapi import FastAPI
from fastapi.responses import JSONResponse

from ia.db import conectar

app = FastAPI(title="Asistente de Normativa UAB")


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
