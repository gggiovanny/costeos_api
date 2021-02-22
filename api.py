from fastapi import Depends, FastAPI, HTTPException
from pony.orm import db_session
import time
from typing import List
import models_db as models
import crud as crud
import schemas as schemas
import status_messages as msgs
from api_response_tools import *

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
@db_session
def update_costo_fijo(id: int, updatedata: schemas.CostoFijoUpdate):
    try:
        costofijo_updating = models.CostosFijos[id]
    except:
        raise HTTPException(status_code=400, detail=msgs.notFoundMsg(id, "CostosFijos"))
    if updatedata.concepto:
        costofijo_updating.concepto = updatedata.concepto
    if updatedata.costo_mensual:
        costofijo_updating.costo_mensual = updatedata.costo_mensual
    return costofijo_updating

@app.delete("/costosfijos/{id}")
@db_session
def delete_costo_fijo(id: int):
    try:
        costo_deleting = models.CostosFijos[id]
    except:
        raise HTTPException(status_code=400, detail=msgs.notFoundMsg(id, "CostosFijos"))
    costo_deleting.delete()
    return costo_deleting

@app.get("/unidades/", response_model=List[schemas.Unidad])
@db_session
def get_unidades(skip: int = 0, limit: int = 100):
    return ponylist(models.Unidades.select()[skip:limit])

@app.get("/insumos/", response_model=List[schemas.Insumo])
@db_session
def get_insumos(skip: int = 0, limit: int = 100):
    lstinsumos = ponylist(models.Insumos.select()[skip:limit])
    return lstinsumos


