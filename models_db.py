from pony.orm import *
from database import *


class CostosFijos(db.Entity):
    concepto = Required(str)
    costo_mensual = Required(float)


class Unidades(db.Entity):
    # indica una relacion de una Unidad a muchos Insumos
    insumos = Set(lambda: Insumos)
    nombre = Required(str)
    abrev = Required(str)


class Insumos(db.Entity):
    # indica una relacion de un Insumo a muchos Ingredientes
    ingredientes = Set(lambda: Ingredientes)
    nombre = Required(str)
    unidad = Required(Unidades)
    valor_de_compra = Required(float)
    merma = Required(float)  # decimal, entre 0 y 1
    # valor calculado que representa el valor real aumentadole las perdidas por merma

    @property
    def valor_por_unidad(self):
        return (self.valor_de_compra * self.merma) + self.valor_de_compra
    # abreviatura de la unidad

    @property
    def unidad_abrev(self):
        return self.unidad.abrev
    # nombre de la unidad

    @property
    def unidad_nombre(self):
        return self.unidad.nombre


class Recetas(db.Entity):
    nombre = Required(str)
    porciones = Required(int)
    # en horas TODO: volverlo time y recibir el dato con un componente
    tiempo_elaboracion = Required(float)
    ingredientes = Set(lambda: Ingredientes)
    # costo total del platillo

    @property
    def costo(self):
        return sum(i.costo_por_unidad_utilizada for i in self.ingredientes)
    # Costo fijo por día laborado
    # Costo Variable
    # Costo por platillo
    # Precio de venta*
    # Margen de contribución
    # % de Utilidad


class Ingredientes(db.Entity):
    receta = Optional(Recetas)
    insumo = Required(Insumos)
    cantidad = Required(float)
    # heredado del insumo

    @property
    def unidad_abrev(self):
        return self.insumo.unidad_abrev
    # heredado del insumo

    @property
    def unidad_nombre(self):
        return self.insumo.unidad_nombre
    # heredado del insumo

    @property
    def valor_por_unidad(self):
        return self.insumo.valor_por_unidad
    # costo del ingrediente para la cantidad a usar en la receta

    @property
    def costo_por_unidad_utilizada(self):
        return self.insumo.valor_por_unidad * self.cantidad


@db_session
def analizarReceta(id, precio_de_venta, horas_jornada=8, dias_mes=30):
    receta = Recetas.get(id=id)
    total_costos_fijos = sum(c.costo_mensual for c in CostosFijos)
    analisis = {}
    analisis['costo_fijo_por_dia_laborado'] = total_costos_fijos/dias_mes
    analisis['costo_variable'] = receta.costo + \
        ((analisis['costo_fijo_por_dia_laborado'] /
          horas_jornada) * receta.tiempo_elaboracion)
    analisis['costo_por_platillo'] = analisis['costo_variable'] / \
        receta.porciones
    analisis['precio_de_venta'] = precio_de_venta
    analisis['margen_de_contribucion'] = precio_de_venta - \
        analisis['costo_por_platillo']
    analisis['porcentaje_utilidad'] = analisis['margen_de_contribucion'] / \
        precio_de_venta
    analisis['porcentaje_de_costo'] = precio_de_venta / \
        analisis['costo_por_platillo']
    return analisis
