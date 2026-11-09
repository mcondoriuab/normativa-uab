# Provisional (BE-006): solo para probar el despliegue antes de que exista
# main.py (BE-001). Se borra cuando BE-001 se fusione en main.
from fastapi import FastAPI

app = FastAPI()


@app.get("/salud")
def salud():
    return {"estado": "ok"}
