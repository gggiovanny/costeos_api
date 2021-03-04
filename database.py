from pony.orm import *
import os

# obteniendo la url de la base de datos definida como varible del sistema
DATABASE_URL = os.environ['DATABASE_URL']

# creando el objeto de la base de datos
db = Database()


def connect(use_sqlite=True):
    # conectando a la base de datos
    if use_sqlite:
        db.bind(provider='sqlite', filename='cache.sqlite',
                create_db=True)
    else:
        db.bind(provider='postgres', dsn=DATABASE_URL, sslmode='require')

    # debug mode: show querys
    set_sql_debug(True)
    # mapeando modelos a la base de datos
    db.generate_mapping(create_tables=True)
    return db
