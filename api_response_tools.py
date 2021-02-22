from pony.orm.core import Entity, QueryResult
from pony.utils.utils import cut_traceback

def ponylist(queryresult: QueryResult, related_objects=True, with_collections=False, **kwargs):
    return [recursive_to_dict(i, related_objects=related_objects, with_collections=with_collections, **kwargs) for i in queryresult]

def ponylistalt(queryresult: QueryResult, related_objects=True, with_collections=False, **kwargs):
    return [recursive_to_dict_alt(i, related_objects=related_objects, with_collections=with_collections, **kwargs) for i in queryresult]

def recursive_to_dict(dataset, _has_iterated=False, **kwargs):
    if isinstance(dataset, Entity):
        dataset = dataset.to_dict(**kwargs)
    delete_these = []
    for key, value in dataset.items():
        if _has_iterated:
            if isinstance(value, (list, tuple)):
                for iterable in value:
                    if isinstance(iterable, Entity):
                        delete_these.append(key)
                        break
                continue
        else:
            if isinstance(value, (list, tuple)):
                value_list = []
                for iterable in value:
                    if isinstance(iterable, Entity):
                        value_list.append(recursive_to_dict(iterable, True,
                                                            **kwargs))
                dataset[key] = value_list
        if isinstance(value, Entity) and not _has_iterated:
           dataset[key] = recursive_to_dict(value, True, **kwargs)
        elif isinstance(value, Entity) and _has_iterated:
            delete_these.append(key)
    for deletable_key in delete_these:
        del dataset[deletable_key]
    return dataset

@cut_traceback
def recursive_to_dict_alt(obj, only=None, exclude=None, with_collections=False, with_lazy=False, related_objects=False, depth=1):
    attrs = obj.__class__._get_attrs_(only, exclude, with_collections, with_lazy)
    result = {}
    for attr in attrs:
        value = attr.__get__(obj)
        if attr.is_collection:
            if related_objects:
                value = sorted(value)
            elif attr.reverse.entity._pk_is_composite_:
                value = sorted(item._get_raw_pkval_() for item in value)
            else:
                value = sorted(item._get_raw_pkval_()[0] for item in value)
        elif attr.is_relation and value is not None:
            if related_objects and depth - 1 >= 0:
                value = value.to_dict(with_collections=with_collections, with_lazy=with_lazy,
                                        related_objects=related_objects)
            else:
                value = value._get_raw_pkval_()
                if not obj._pk_is_composite_: value = value[0]
        result[attr.name] = value
    return result