from pony.orm import *

from traci import main

# creando el objeto de la base de datos
db = Database()

class CostosFijos(db.Entity):
    concepto = Required(str)
    costo_mensual = Required(float)

class Unidades(db.Entity):
    insumos = Set(lambda:Insumos) # indica una relacion de una Unidad a muchos Insumos
    nombre = Required(str)

class Insumos(db.Entity):
    ingredientes = Set(lambda:Ingredientes) # indica una relacion de un Insumo a muchos Ingredientes
    nombre = Required(str)
    unidad = Required(Unidades)
    valor_de_compra = Required(float)
    merma = Required(float) # decimal, entre 0 y 1
    # valor calculado que representa el valor real aumentadole las perdidas por merma
    @property
    def valor_por_unidad(self):
        return (self.valor_de_compra * self.merma) + self.valor_de_compra

class Recetas(db.Entity):
    nombre = Required(str)
    porciones = Required(int)
    tiempo_elaboracion = Required(float) # en horas
    ingredientes = Set(lambda:Ingredientes)
    # Costo fijo por día laborado
    # Costo Variable
    # Costo por platillo
    # Precio de venta*
    # Margen de contribución 
    # % de Utilidad


class Ingredientes(db.Entity):
    receta = Required(Recetas)
    insumo = Required(Insumos)
    cantidad = Required(int)
    # heredado del insumo
    @property
    def unidad(self):
        self.insumo.unidad
    # heredado del insumo
    @property
    def valor_por_unidad(self):
        self.insumo.valor_por_unidad
    # costo del ingrediente para la cantidad a usar en la receta
    @property
    def costo_por_unidad_utilizada(self):
        self.costo_de_compra * self.cantidad


def connect(in_memory_database = True):
    # conectando a la base de datos
    if in_memory_database:
        db.bind(provider='sqlite', filename=':memory:') # in memory database
    else:
        db.bind(provider='sqlite', filename='cache.sqlite', create_db=True) # file database
    # mapeando modelos a la base de datos
    db.generate_mapping(create_tables=True)
    

connect(False)