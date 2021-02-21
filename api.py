from fastapi import Depends, FastAPI, HTTPException
from pony.orm import db_session
import time
from typing import List
import models_db as models
import crud as crud
import schemas as schemas

app = FastAPI()
models.connect()


@app.get("/")
async def root():
    return {'bienvenida': '¡Bienvenid@ a la API de costeos!'}


@app.get("/costosfijos/", response_model=List[schemas.CostoFijo])
def get_costos_fijos(skip: int = 0, limit: int = 100):
    return crud.read_costos_fijos(skip=skip, limit=limit)


@app.get("/costosfijos/{id}", response_model=schemas.CostoFijo)
def get_costo_fijo(id: int):
    return crud.read_costo_fijo(id)


@app.post("/costosfijos/", response_model=schemas.CostoFijo)
def create_costo_fijo(costofijo: schemas.CostoFijoCreate):
    duplicated = crud.read_costo_fijo_by_concepto(costofijo.concepto)
    if duplicated:
        raise HTTPException(status_code=400, detail="Concepto {} repetido".format(costofijo.concepto))
    return crud.create_costo_fijo(costofijo=costofijo)

@app.put("/costosfijos/{id}", response_model=schemas.CostoFijo)
def update_costo_fijo(id: int, updatedata: schemas.CostoFijoUpdate):
    return crud.update_costo_fijo(id, updatedata=updatedata)