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
    abrev = Required(str)

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
    tiempo_elaboracion = Required(float) # en horas TODO: volverlo time y recibir el dato con un componente
    ingredientes = Set(lambda:Ingredientes)
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
    analisis['costo_variable'] = receta.costo + ((analisis['costo_fijo_por_dia_laborado'] / horas_jornada)* receta.tiempo_elaboracion)
    analisis['costo_por_platillo'] = analisis['costo_variable'] / receta.porciones
    analisis['precio_de_venta'] = precio_de_venta
    analisis['margen_de_contribucion'] = precio_de_venta - analisis['costo_por_platillo']
    analisis['porcentaje_utilidad'] = analisis['margen_de_contribucion'] / precio_de_venta
    analisis['porcentaje_de_costo'] = precio_de_venta / analisis['costo_por_platillo']
    return analisis

@db_session
def insertData():
    # insertando costos fijos
    CostosFijos(concepto="Nomina", costo_mensual=22000)
    CostosFijos(concepto="Pago de luz", costo_mensual=1500)
    CostosFijos(concepto="Pago de agua", costo_mensual=200)
    CostosFijos(concepto="Gas", costo_mensual=2000)
    CostosFijos(concepto="Alquiler", costo_mensual=3000)
    # insertando unidades
    KG = Unidades(nombre = "Kilogramo", abrev = "KG")
    LT = Unidades(nombre = "Litro", abrev = "LT")
    PAQ = Unidades(nombre = "Paquete", abrev = "PAQ")
    PZA = Unidades(nombre = "Pieza", abrev = "PZA")
    ATD = Unidades(nombre = "Atado", abrev = "ATD")
    # insertando insumos
    achiote = Insumos (nombre="ACHIOTE", valor_de_compra=100.00, merma=0.00, unidad=KG)
    agua = Insumos (nombre="AGUA", valor_de_compra=1.75, merma=0.00, unidad=LT)
    ajo = Insumos (nombre="AJO", valor_de_compra=150.00, merma=0.00, unidad=KG)
    ajonjoli = Insumos (nombre="AJONJOLÍ", valor_de_compra=98.00, merma=0.00, unidad=KG)
    almendra = Insumos (nombre="ALMENDRA", valor_de_compra=229.00, merma=0.00, unidad=KG)
    anis = Insumos (nombre="ANIS", valor_de_compra=520.00, merma=0.00, unidad=KG)
    arandano_en_pasita = Insumos (nombre="ARÁNDANO EN PASITA", valor_de_compra=115.00, merma=0.00, unidad=KG)
    avena = Insumos (nombre="AVENA", valor_de_compra=20.00, merma=0.00, unidad=KG)
    azucar = Insumos (nombre="AZÚCAR", valor_de_compra=29.00, merma=0.00, unidad=KG)
    azucar_glas = Insumos (nombre="AZÚCAR GLAS", valor_de_compra=31.00, merma=0.00, unidad=KG)
    betabel = Insumos (nombre="BETABEL", valor_de_compra=21.90, merma=0.05, unidad=KG)
    bitartrato_de_potasio = Insumos (nombre="BITARTRATO DE POTASIO", valor_de_compra=199.00, merma=0.00, unidad=KG)
    cacahuate = Insumos (nombre="CACAHUATE", valor_de_compra=65.00, merma=0.00, unidad=KG)
    cacao = Insumos (nombre="CACAO", valor_de_compra=149.00, merma=0.00, unidad=KG)
    cafe_molido = Insumos (nombre="CAFÉ MOLIDO.", valor_de_compra=126.00, merma=0.00, unidad=KG)
    cafe_soluble = Insumos (nombre="CAFÉ SOLUBLE. ", valor_de_compra=237.00, merma=0.00, unidad=KG)
    canela_en_raja = Insumos (nombre="CANELA EN RAJA.", valor_de_compra=288.00, merma=0.00, unidad=KG)
    canela_molida = Insumos (nombre="CANELA MOLIDA", valor_de_compra=199.00, merma=0.00, unidad=KG)
    cebolla = Insumos (nombre="CEBOLLA", valor_de_compra=19.90, merma=0.00, unidad=KG)
    chile_ancho = Insumos (nombre="CHILE ANCHO", valor_de_compra=210.00, merma=0.03, unidad=KG)
    chile_chipotle = Insumos (nombre="CHILE CHIPOTLE", valor_de_compra=200.00, merma=0.03, unidad=KG)
    chile_costeño = Insumos (nombre="CHILE COSTEÑO", valor_de_compra=180.00, merma=0.03, unidad=KG)
    chile_güero = Insumos (nombre="CHILE GÜERO", valor_de_compra=82.00, merma=0.03, unidad=KG)
    chile_guiajillo = Insumos (nombre="CHILE GUIAJILLO", valor_de_compra=118.67, merma=0.00, unidad=KG)
    chile_habanero = Insumos (nombre="CHILE HABANERO", valor_de_compra=140.00, merma=0.03, unidad=KG)
    chile_mulato = Insumos (nombre="CHILE MULATO", valor_de_compra=190.00, merma=0.03, unidad=KG)
    chile_pasilla = Insumos (nombre="CHILE PASILLA", valor_de_compra=185.00, merma=0.03, unidad=KG)
    chocolate_amargo = Insumos (nombre="CHOCOLATE AMARGO", valor_de_compra=160.00, merma=0.00, unidad=KG)
    chocolate_blanco = Insumos (nombre="CHOCOLATE BLANCO", valor_de_compra=100.00, merma=0.00, unidad=KG)
    chocolate_con_leche = Insumos (nombre="CHOCOLATE CON LECHE", valor_de_compra=170.00, merma=0.00, unidad=KG)
    chocolate_semiamargo = Insumos (nombre="CHOCOLATE SEMIAMARGO", valor_de_compra=165.00, merma=0.00, unidad=KG)
    cilantro = Insumos (nombre="CILANTRO.", valor_de_compra=7.90, merma=0.00, unidad=ATD)
    ciruela_amarilla = Insumos (nombre="CIRUELA AMARILLA.", valor_de_compra=80.00, merma=0.00, unidad=KG)
    clavo_de_olor = Insumos (nombre="CLAVO DE OLOR", valor_de_compra=250.00, merma=0.00, unidad=KG)
    coco_rallado = Insumos (nombre="COCO RALLADO", valor_de_compra=85.00, merma=0.00, unidad=KG)
    cocoa_en_polvo = Insumos (nombre="COCOA EN POLVO", valor_de_compra=100.00, merma=0.00, unidad=KG)
    crema_de_avellanas = Insumos (nombre="CREMA DE AVELLANAS.", valor_de_compra=144.00, merma=0.00, unidad=KG)
    crema_para_batir = Insumos (nombre="CREMA PARA BATIR.", valor_de_compra=49.95, merma=0.00, unidad=LT)
    dextrosa = Insumos (nombre="DEXTROSA", valor_de_compra=85.00, merma=0.00, unidad=KG)
    esencia_de_nuez = Insumos (nombre="ESENCIA DE NUEZ", valor_de_compra=165.00, merma=0.00, unidad=LT)
    extracto_de_vainilla = Insumos (nombre="EXTRACTO DE VAINILLA", valor_de_compra=6.70, merma=0.00, unidad=LT)
    fondo_de_pollo = Insumos (nombre="FONDO DE POLLO.", valor_de_compra=54.00, merma=0.00, unidad=LT)
    fresa = Insumos (nombre="FRESA", valor_de_compra=111.00, merma=0.00, unidad=KG)
    galletas_maria = Insumos (nombre="GALLETAS MARÍA.", valor_de_compra=11.00, merma=0.00, unidad=PAQ)
    granillo_de_chocolate = Insumos (nombre="GRANILLO DE CHOCOLATE.", valor_de_compra=44.50, merma=0.00, unidad=KG)
    grenetina = Insumos (nombre="GRENETINA", valor_de_compra=178.90, merma=0.00, unidad=KG)
    guayaba = Insumos (nombre="GUAYABA", valor_de_compra=34.90, merma=0.00, unidad=KG)
    harina_de_almendra = Insumos (nombre="HARINA DE ALMENDRA.", valor_de_compra=380.00, merma=0.00, unidad=KG)
    harina_de_trigo = Insumos (nombre="HARINA DE TRIGO.", valor_de_compra=10.50, merma=0.00, unidad=KG)
    hielo = Insumos (nombre="HIELO", valor_de_compra=4.26, merma=0.00, unidad=KG)
    hojas_de_maiz = Insumos (nombre="HOJAS DE MAÍZ. ", valor_de_compra=0.83, merma=0.00, unidad=PZA)
    huevo = Insumos (nombre="HUEVO", valor_de_compra=1.96, merma=0.05, unidad=PZA)
    jalea_de_manzana = Insumos (nombre="JALEA DE MANZANA", valor_de_compra=80.00, merma=0.00, unidad=KG)
    jitomate = Insumos (nombre="JITOMATE", valor_de_compra=14.90, merma=0.00, unidad=KG)
    leche = Insumos (nombre="LECHE", valor_de_compra=22.00, merma=0.00, unidad=LT)
    leche_condensada = Insumos (nombre="LECHE CONDENSADA.", valor_de_compra=43.00, merma=0.00, unidad=KG)
    leche_en_polvo = Insumos (nombre="LECHE EN POLVO", valor_de_compra=87.00, merma=0.00, unidad=KG)
    limon = Insumos (nombre="LIMÓN", valor_de_compra=24.90, merma=0.05, unidad=KG)
    maiz = Insumos (nombre="MAIZ. ", valor_de_compra=15.00, merma=0.10, unidad=KG)
    mamey = Insumos (nombre="MAMEY", valor_de_compra=33.00, merma=0.00, unidad=KG)
    manteca_de_cerdo = Insumos (nombre="MANTECA DE CERDO.", valor_de_compra=39.00, merma=0.00, unidad=KG)
    mantequilla = Insumos (nombre="MANTEQUILLA", valor_de_compra=68.00, merma=0.00, unidad=KG)
    masa_de_maiz = Insumos (nombre="MASA DE MAÍZ.", valor_de_compra=10.00, merma=0.00, unidad=KG)
    media_crema = Insumos (nombre="MEDIA CREMA.", valor_de_compra=12.00, merma=0.00, unidad=PZA)
    naranja = Insumos (nombre="NARANJA", valor_de_compra=15.90, merma=0.00, unidad=KG)
    neutro_para_helado = Insumos (nombre="NEUTRO PARA HELADO.", valor_de_compra=72.57, merma=0.00, unidad=KG)
    nuez_de_castilla = Insumos (nombre="NUEZ DE CASTILLA", valor_de_compra=399.00, merma=0.00, unidad=KG)
    oregano_molido = Insumos (nombre="ORÉGANO MOLIDO.", valor_de_compra=149.00, merma=0.00, unidad=KG)
    pan_blanco = Insumos (nombre="PAN BLANCO.", valor_de_compra=18.50, merma=0.00, unidad=PAQ)
    pan_de_sandwichon = Insumos (nombre="PAN DE SANDWICHON", valor_de_compra=18.50, merma=0.00, unidad=PAQ)
    pepita = Insumos (nombre="PEPITA", valor_de_compra=220.00, merma=0.00, unidad=KG)
    piloncillo = Insumos (nombre="PILONCILLO", valor_de_compra=9.97, merma=0.00, unidad=PZA)
    pimienta = Insumos (nombre="PIMIENTA ", valor_de_compra=300.00, merma=0.00, unidad=KG)
    piñon_rosa = Insumos (nombre="PIÑON ROSA", valor_de_compra=1500.00, merma=0.00, unidad=KG)
    platano_macho = Insumos (nombre="PLÁTANO MACHO.", valor_de_compra=29.90, merma=0.05, unidad=KG)
    polvo_para_hornear = Insumos (nombre="POLVO PARA HORNEAR.", valor_de_compra=28.00, merma=0.00, unidad=KG)
    queso_crema = Insumos (nombre="QUESO CREMA", valor_de_compra=122.00, merma=0.00, unidad=KG)
    queso_de_bola = Insumos (nombre="QUESO DE BOLA", valor_de_compra=350.00, merma=0.05, unidad=KG)
    queso_mascarpone = Insumos (nombre="QUESO MASCARPONE", valor_de_compra=350.00, merma=0.00, unidad=KG)
    rompope = Insumos (nombre="ROMPOPE", valor_de_compra=96.50, merma=0.00, unidad=LT)
    sal = Insumos (nombre="SAL", valor_de_compra=8.10, merma=0.00, unidad=KG)
    soletillas = Insumos (nombre="SOLETILLAS", valor_de_compra=195.00, merma=0.00, unidad=PAQ)
    tejocote = Insumos (nombre="TEJOCOTE", valor_de_compra=42.00, merma=0.00, unidad=KG)
    tortilla_de_maiz = Insumos (nombre="TORTILLA DE MAÍZ.", valor_de_compra=16.00, merma=0.00, unidad=KG)
    uva_pasa = Insumos (nombre="UVA PASA", valor_de_compra=106.00, merma=0.00, unidad=KG)
    vino_tinto_afrutado = Insumos (nombre="VINO TINTO AFRUTADO.", valor_de_compra=75.00, merma=0.00, unidad=LT)
    vodka = Insumos (nombre="VODKA", valor_de_compra=149.00, merma=0.00, unidad=LT)
    # registrando ingredientes para mazapan de chocolate
    ing_mazapan_chocolate = [
        Ingredientes (insumo=agua, cantidad=0.320),
        Ingredientes (insumo=azucar_glas, cantidad=0.100),
        Ingredientes (insumo=bitartrato_de_potasio, cantidad=0.175),
        Ingredientes (insumo=cocoa_en_polvo, cantidad=0.004),
        Ingredientes (insumo=huevo, cantidad=0.500),
        Ingredientes (insumo=pepita, cantidad=0.100)
    ]
    # registrando receta mazapan de chocolate
    mazapan_chocolate = Recetas(
        nombre="MAZAPAN DE CHOCOLATE",
        porciones=16,
        tiempo_elaboracion=0.6,
        ingredientes=ing_mazapan_chocolate
    )
    print(mazapan_chocolate.costo)
def connect():
    # conectando a la base de datos
    db.bind(provider='sqlite', filename='cache.sqlite', create_db=True) # file database
    # mapeando modelos a la base de datos
    db.generate_mapping(create_tables=True)
    

if __name__ == "__main__":
    connect()
    insertData()