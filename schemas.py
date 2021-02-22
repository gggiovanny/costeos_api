from typing import Any, List, Optional
from pony.orm import core 
from pydantic import BaseModel
from pydantic.utils import GetterDict
from pony.orm import db_session
import database as db

class PonyOrmGetterDict(GetterDict):
    
    @db_session
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, core.Query):
            lstdict = [r.to_dict() for r in res]
            return lstdict
        if isinstance(res, core.Entity):
            dct = res.to_dict()
            return dct
        return res

class CostoFijoBase(BaseModel):
    concepto: str
    costo_mensual: str

class CostoFijoCreate(BaseModel):
    concepto: Optional[str] = None
    costo_mensual: Optional[float] = None

class CostoFijoUpdate(CostoFijoBase):
    pass

class CostoFijo(CostoFijoBase):
    id: int
    class Config:
        orm_mode = True
        getter_dict = PonyOrmGetterDict

class Unidad(BaseModel):
    id: int
    nombre: str
    abrev: str
    class Config:
        orm_mode = True
        getter_dict = PonyOrmGetterDict
    
class Insumo(BaseModel):
    id: int
    # ingredientes = Set(lambda:Ingredientes) # indica una relacion de un Insumo a muchos Ingredientes
    nombre: str
    unidad: Unidad
    valor_de_compra: float
    merma: float # decimal, entre 0 y 1
    # valor_por_unidad: float # valor calculado que representa el valor real aumentadole las perdidas por merma
    # unidad_abrev: str # abreviatura de la unidad
    # unidad_nombre: str # nombre de la unidad
    class Config:
        orm_mode = True
        getter_dict = PonyOrmGetterDict

class Ingrediente(BaseModel):
    id: str
    receta: int
    insumo: Insumo
    cantidad: float
    
    # @property
    # def unidad_abrev(self):
    #     return self.insumo.unidad_abrev  # heredado del insumo
    # # heredado del insumo
    # @property
    # def unidad_nombre(self):
    #     return self.insumo.unidad_nombre
    # @property
    # def valor_por_unidad(self):
    #     return self.insumo.valor_por_unidad # heredado del insumo
    
    # costo del ingrediente para la cantidad a usar en la receta
    # @property
    # def costo_por_unidad_utilizada(self):
    #     return self.insumo.valor_por_unidad * self.cantidad

