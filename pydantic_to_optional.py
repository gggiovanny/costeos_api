# tomado de https://github.com/samuelcolvin/pydantic/issues/2272
from copy import deepcopy
from typing import Optional, Type, TypeVar
from pydantic import BaseModel, create_model

BaseModelT = TypeVar('BaseModelT', bound=BaseModel)


def to_optional(model: Type[BaseModelT], name: Optional[str] = None) -> Type[BaseModelT]:
    """
    Create a new BaseModel with the exact same fields as `model`
    but making them all optional
    """
    all_annotations = {}
    # Workaround to retrieve the passed type and not the resolved one
    # (e.g. `str` with constraints that resolved in `ConstrainedStrValue`)
    for base in reversed(model.__bases__):
        all_annotations.update(getattr(base, '__annotations__', {}))
    all_annotations.update(model.__annotations__)

    field_definitions = {}

    for name, field in model.__fields__.items():
        optional_field_info = deepcopy(field.field_info)
        # Do not change default value of fields that are already optional
        if optional_field_info.default is ...:
            optional_field_info.default = None

        field_type = all_annotations.get(name, field.outer_type_)
        field_definitions[name] = (field_type, optional_field_info)

    # type: ignore[arg-type]
    return create_model(name or f'Optional{model.__name__}', **field_definitions)


if __name__ == "__main__":
    class Model(BaseModel):
        a: str
        b: int

    print(Model.__fields__)
    # {'a': ModelField(name='a', type=str, required=True), 'b': ModelField(name='b', type=int, required=True)}
    print(to_optional(Model).__fields__)
    # {'a': ModelField(name='a', type=Optional[str], required=False, default=None), 'b': ModelField(name='b', type=Optional[int], required=False, default=None)}

    class Test(to_optional(Model)):
        x: bool

    print(Test.__fields__)
    # {'a': ModelField(name='a', type=Optional[str], required=False, default=None), 'b': ModelField(name='b', type=Optional[int], required=False, default=None), 'x': ModelField(name='x', type=bool, required=True)}
