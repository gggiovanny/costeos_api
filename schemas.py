from typing import Any, List, Optional
from pony.orm import core 
from pydantic import BaseModel
from pydantic.utils import GetterDict

class PonyOrmGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, core.Query):
            return [r.to_dict() for r in res]
        if isinstance(res, core.Entity):
            return res.to_dict
        return res

class CostoFijoBase(BaseModel):
    concepto: Optional[str] = None
    costo_mensual: Optional[float] = None

class CostoFijoCreate(CostoFijoBase):
    pass

class CostoFijoUpdate(CostoFijoBase):
    pass

class CostoFijo(CostoFijoBase):
    id: int
    class Config:
        orm_mode = True
        getter_dict = PonyOrmGetterDict

