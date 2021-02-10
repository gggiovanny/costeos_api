from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from models_db import *
from pony.flask import Pony

app = FlaskAPI(__name__)
Pony(app) # para usar db_session automaticamente en las peticiones
connect()

@app.route("/", methods=['GET'])
def raiz():
    return {'bienvenida': '¡Bienvenid@ a la API de costeos!'}

@app.route('/costosfijos',  methods=['GET'])
def get_costos_fijos():
    return [c.to_dict() for c in CostosFijos.select()]

@app.route("/costosfijos/<int:id>/", methods=['GET'])
def get_costo_fijo(id):
    return CostosFijos[id].to_dict()

if __name__ == "__main__":
    app.run(debug=True)