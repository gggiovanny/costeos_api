from typing import Any, List, Optional
from pony.orm import core
from pydantic import BaseModel
from pydantic.utils import GetterDict
from fastapi import Query
from pydantic_to_optional import *


class PonyOrmGetterDict(GetterDict):

    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, core.Query):
            lstdict = [r.to_dict() for r in res]
            return lstdict
        if isinstance(res, core.Entity):
            dct = res.to_dict()
            return dct
        return res


###### CostosFijos ######

class CostoFijoBase(BaseModel):
    concepto: str
    costo_mensual: str


class CostoFijoCreate(CostoFijoBase):
    pass


class CostoFijoUpdate(to_optional(CostoFijoBase)):
    pass


class CostoFijo(CostoFijoBase):
    id: int

    class Config:
        orm_mode = True
        getter_dict = PonyOrmGetterDict


###### Unidades ######

class UnidadBase(BaseModel):
    nombre: str
    abrev: str


class UnidadCreate(UnidadBase):
    pass


class UnidadUpdate(to_optional(UnidadBase)):
    pass


class Unidad(UnidadBase):
    id: int

    class Config:
        orm_mode = True
        getter_dict = PonyOrmGetterDict


###### Insumos ######

class InsumoBase(BaseModel):
    nombre: str
    unidad: int  # fk
    valor_de_compra: float
    merma: float = Query(0, ge=0, lt=1)  # decimal, rango [0, 1)


class InsumoCreate(InsumoBase):
    pass


class InsumoUpdate(to_optional(InsumoBase)):
    pass


class Insumo(InsumoBase):
    id: int
    # faltan propiedades calculadas por ponyorm

    class Config:
        orm_mode = True
        getter_dict = PonyOrmGetterDict

class InsumoDetailed(Insumo):
    unidad: Unidad


###### Ingredientes ######

class IngredienteBase(BaseModel):
    receta: Optional[int] = None
    insumo: int  # fk
    cantidad: float


class IngredienteCreate(IngredienteBase):
    pass


class IngredienteUpdate(to_optional(IngredienteBase)):
    pass


class Ingrediente(IngredienteBase):
    id: str
    # faltan propiedades calculadas por ponyorm

    class Config:
        orm_mode = True
        getter_dict = PonyOrmGetterDict


###### Recetas ######

class RecetaBase(BaseModel):
    nombre: str
    porciones: int
    tiempo_elaboracion: float
    # falta propiedad de costo


class RecetaCreate(RecetaBase):
    pass


class RecetaUpdate(to_optional(RecetaBase)):
    pass


class Receta(RecetaBase):
    id: int

    class Config:
        orm_mode = True
        getter_dict = PonyOrmGetterDict


class AnalisisReceta(BaseModel):
    costo_fijo_por_dia_laborado: float
    costo_variable: float
    costo_por_platillo: float
    precio_de_venta: float
    margen_de_contribucion: float
    porcentaje_utilidad: float
    porcentaje_de_costo: float
