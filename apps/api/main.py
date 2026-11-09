from fastapi import FastAPI

app = FastAPI(title="Asistente de Normativa UAB")


@app.get("/salud")
def salud():
    return {"estado": "ok"}
