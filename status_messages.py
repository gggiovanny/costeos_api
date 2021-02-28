from pydantic import BaseModel
from pony.orm.core import Entity


def notFoundMsg(fieldvalue: str, objectname: str = "registro", fieldname: str = "id"):
    return "No existe {} con {}: {}".format(
        objectname,
        fieldname,
        fieldvalue
    )


def duplicatedMsg(fieldvalue: str, objectname: str = "registro", fieldname: str = "id"):
    return "Ya existe {} con {}: {}".format(
        objectname,
        fieldname,
        fieldvalue
    )
