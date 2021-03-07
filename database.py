from pony.orm import *
from config import settings, dotenvsettings

# obteniendo la url de la base de datos definida como varible del sistema
DATABASE_URL = settings.database_url

# creando el objeto de la base de datos
db = Database()


def connect():
    # conectando a la base de datos
    if dotenvsettings.use_dev_api == "1":
        db.bind(provider='sqlite', filename='cache.sqlite',
                create_db=True)
    else:
        db.bind(provider='postgres', dsn=DATABASE_URL, sslmode='require')

    # debug mode: show querys
    set_sql_debug(True)
    # mapeando modelos a la base de datos
    db.generate_mapping(create_tables=True)
    return db
