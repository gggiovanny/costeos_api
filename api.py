from fastapi import FastAPI
import models_db as models
import crud as crud
from pony.orm import db_session

app = FastAPI()
models.connect()


@app.get("/")
async def root():
    return {'bienvenida': '¡Bienvenid@ a la API de costeos!'}


@app.get("/costosfijos")
async def current_user():
    with db_session:
        return [c.to_dict() for c in models.CostosFijos.select()]


@app.get("/costosfijos/{id}")
async def get_costo_fijo(id: int):
    with db_session:
        return models.CostosFijos[id].to_dict()
