import enum
from flask import Flask
from models_db import *
app = Flask(__name__)
connect()

@app.route('/')
def hello_world():
    return '¡Bienvenid@ a la API de costeos!'

@app.route('/costosfijos')
def get_costos_fijos():
    with db_session:
        res = {}
        costos = CostosFijos.select()[:]
        
        for val in costos:
            res['{}'.format(val.id)] = val.to_dict()
        return res
    
