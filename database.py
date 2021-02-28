from pony.orm import *
# creando el objeto de la base de datos
db = Database()


def connect():
    # conectando a la base de datos
    db.bind(provider='sqlite', filename='cache.sqlite',
            create_db=True)  # file database
    # debug mode: show querys
    set_sql_debug(True)
    # mapeando modelos a la base de datos
    db.generate_mapping(create_tables=True)
    return db
