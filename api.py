from fastapi import Depends, FastAPI, HTTPException
from pony.orm import db_session
from typing import List

from pydantic.main import BaseModel
import models_db as models
import schemas as schemas
import status_messages as msgs
from api_response_tools import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
models.connect()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://localhost:3000",
        "https://gggiovanny.github.io",
        "https://costeosapp.netlify.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {'bienvenida': '¡Bienvenid@ a la API de costeos!'}


###### Costos Fijos ######

@app.get("/costosfijos/", response_model=List[schemas.CostoFijo])
@db_session
def get_costos_fijos(skip: int = 0, limit: int = 100):
    return ponylist(models.CostosFijos.select()[skip:limit])


@app.get("/costosfijos/{id}", response_model=schemas.CostoFijo)
@db_session
def get_costo_fijo(id: int):
    try:
        data = models.CostosFijos[id]
    except:
        raise HTTPException(400, msgs.notFoundMsg(id, "Costo fijo"))
    return data


@app.post("/costosfijos/", response_model=schemas.CostoFijo)
@db_session
def create_costo_fijo(costofijo: schemas.CostoFijoCreate):
    duplicated = models.CostosFijos.get(concepto=costofijo.concepto)
    if duplicated:
        raise HTTPException(
            status_code=400, detail=msgs.duplicatedMsg(costofijo.concepto, "Costo Fijo", "concepto"))
    return models.CostosFijos(
        concepto=costofijo.concepto,
        costo_mensual=costofijo.costo_mensual
    )


@app.put("/costosfijos/{id}", response_model=schemas.CostoFijo)
@db_session
def update_costo_fijo(id: int, updatedata: schemas.CostoFijoUpdate):
    costofijo_updating = get_costo_fijo(id)
    costofijo_updating.set(**cleandict(updatedata))
    return costofijo_updating


@app.delete("/costosfijos/{id}")
@db_session
def delete_costo_fijo(id: int):
    try:
        costo_deleting = models.CostosFijos[id]
    except:
        raise HTTPException(
            status_code=400, detail=msgs.notFoundMsg(id, "Costo Fijo"))
    costo_deleting.delete()
    return costo_deleting


###### Unidades ######

@app.get("/unidades/", response_model=List[schemas.Unidad])
@db_session
def get_unidades(skip: int = 0, limit: int = 100):
    return ponylist(models.Unidades.select()[skip:limit])


@app.get('/unidades/{id}', response_model=schemas.Unidad)
@db_session
def get_unidad(id: int):
    try:
        data = models.Unidades[id]
    except:
        raise HTTPException(400, msgs.notFoundMsg(id, "Unidad"))
    return data


@app.post("/unidades/", response_model=schemas.Unidad)
@db_session
def create_unidad(unidad: schemas.UnidadCreate):
    duplicated = models.Unidades.get(nombre=unidad.nombre)
    if duplicated:
        raise HTTPException(
            status_code=400, detail=msgs.duplicatedMsg(unidad.nombre, "Unidad", "nombre"))
    new = models.Unidades(
        nombre=unidad.nombre,
        abrev=unidad.abrev
    )
    return new


@app.delete("/unidades/{id}")
@db_session
def delete_unidad(id: int):
    data_del = get_unidad(id)
    data_del.delete()
    return data_del


@app.put("/unidades/{id}", response_model=schemas.Unidad)
@db_session
def update_unidad(id: int, updatedata: schemas.UnidadUpdate):
    data_updating = get_unidad(id)
    data_updating.set(**cleandict(updatedata))
    return data_updating


###### Insumos ######

@app.get("/insumos/", response_model=List[schemas.InsumoDetailed])
@db_session
def get_insumos(skip: int = 0, limit: int = 100):
    return ponylistrecursive(models.Insumos.select()[skip:limit])


@db_session
def _get_insumo(id: int):
    try:
        data = models.Insumos[id]
    except:
        raise HTTPException(400, msgs.notFoundMsg(id, "Insumo"))
    return data


@app.get("/insumos/{id}", response_model=schemas.InsumoDetailed)
@db_session
def get_insumo(id: int):
    return recursive_to_dict(_get_insumo(id))


@app.post("/insumos/", response_model=schemas.Insumo)
@db_session
def create_insumo(insumo: schemas.InsumoCreate):
    return models.Insumos(**insumo.dict()).to_dict()


@app.put("/insumos/{id}", response_model=schemas.Insumo)
@db_session
def update_insumo(id: int, updatedata: schemas.InsumoUpdate):
    data_updating = _get_insumo(id)
    data_updating.set(**cleandict(updatedata))
    return data_updating.to_dict()


@app.delete("/insumos/{id}")
@db_session
def delete_insumo(id: int):
    return _get_insumo(id).delete()


@app.get("/ingredientes/")
@db_session
def get_ingredientes(skip: int = 0, limit: int = 100):
    lst = ponylist(models.Ingredientes.select()[skip:limit])
    return lst
