from pydantic import BaseModel
from pony.orm.core import Entity


def notFoundMsg(fieldvalue: str, objectname: str = None, fieldname: str = "id"):
    if not objectname:
        return "No existe un registro con {}: {}".format(
            fieldname,
            fieldvalue
        )
    else:
        return "No existe un registro de {} con {}: {}".format(
            objectname,
            fieldname,
            fieldvalue
        )
