from pony.orm import *
import models_db as md
import schemas as schemas
from api_response_tools import *


@db_session
def read_costos_fijos(skip: int = 0, limit: int = 100):
    return ponylist(md.CostosFijos.select()[skip:limit])


@db_session
def read_costo_fijo(id: int):
    return md.CostosFijos[id]


@db_session
def read_costo_fijo_by_concepto(concepto: str):
    return md.CostosFijos.get(concepto=concepto)


@db_session
def create_costo_fijo(costofijo: schemas.CostoFijoCreate):
    newcostofijo = md.CostosFijos(
        concepto=costofijo.concepto,
        costo_mensual=costofijo.costo_mensual
    )
    return newcostofijo


@db_session
def update_costo_fijo(id: int, updatedata: schemas.CostoFijoUpdate):
    costofijo_updating = read_costo_fijo(id)
    if updatedata.concepto:
        costofijo_updating.concepto = updatedata.concepto
    if updatedata.costo_mensual:
        costofijo_updating.costo_mensual = updatedata.costo_mensual
    return costofijo_updating


@db_session
def insertData():
    # insertando costos fijos
    md.CostosFijos(concepto="Nomina", costo_mensual=22000)
    md.CostosFijos(concepto="Pago de luz", costo_mensual=1500)
    md.CostosFijos(concepto="Pago de agua", costo_mensual=200)
    md.CostosFijos(concepto="Gas", costo_mensual=2000)
    md.CostosFijos(concepto="Alquiler", costo_mensual=3000)
    # insertando unidades
    KG = md.Unidades(nombre="Kilogramo", abrev="KG")
    LT = md.Unidades(nombre="Litro", abrev="LT")
    PAQ = md.Unidades(nombre="Paquete", abrev="PAQ")
    PZA = md.Unidades(nombre="Pieza", abrev="PZA")
    ATD = md.Unidades(nombre="Atado", abrev="ATD")
    # insertando insumos
    achiote = md.Insumos(
        nombre="ACHIOTE", valor_de_compra=100.00, merma=0.00, unidad=KG)
    agua = md.Insumos(nombre="AGUA", valor_de_compra=1.75,
                      merma=0.00, unidad=LT)
    ajo = md.Insumos(nombre="AJO", valor_de_compra=150.00,
                     merma=0.00, unidad=KG)
    ajonjoli = md.Insumos(
        nombre="AJONJOLÍ", valor_de_compra=98.00, merma=0.00, unidad=KG)
    almendra = md.Insumos(
        nombre="ALMENDRA", valor_de_compra=229.00, merma=0.00, unidad=KG)
    anis = md.Insumos(nombre="ANIS", valor_de_compra=520.00,
                      merma=0.00, unidad=KG)
    arandano_en_pasita = md.Insumos(
        nombre="ARÁNDANO EN PASITA", valor_de_compra=115.00, merma=0.00, unidad=KG)
    avena = md.Insumos(nombre="AVENA", valor_de_compra=20.00,
                       merma=0.00, unidad=KG)
    azucar = md.Insumos(
        nombre="AZÚCAR", valor_de_compra=29.00, merma=0.00, unidad=KG)
    azucar_glas = md.Insumos(nombre="AZÚCAR GLAS",
                             valor_de_compra=31.00, merma=0.00, unidad=KG)
    betabel = md.Insumos(
        nombre="BETABEL", valor_de_compra=21.90, merma=0.05, unidad=KG)
    bitartrato_de_potasio = md.Insumos(
        nombre="BITARTRATO DE POTASIO", valor_de_compra=199.00, merma=0.00, unidad=KG)
    cacahuate = md.Insumos(
        nombre="CACAHUATE", valor_de_compra=65.00, merma=0.00, unidad=KG)
    cacao = md.Insumos(nombre="CACAO", valor_de_compra=149.00,
                       merma=0.00, unidad=KG)
    cafe_molido = md.Insumos(nombre="CAFÉ MOLIDO.",
                             valor_de_compra=126.00, merma=0.00, unidad=KG)
    cafe_soluble = md.Insumos(nombre="CAFÉ SOLUBLE. ",
                              valor_de_compra=237.00, merma=0.00, unidad=KG)
    canela_en_raja = md.Insumos(
        nombre="CANELA EN RAJA.", valor_de_compra=288.00, merma=0.00, unidad=KG)
    canela_molida = md.Insumos(
        nombre="CANELA MOLIDA", valor_de_compra=199.00, merma=0.00, unidad=KG)
    cebolla = md.Insumos(
        nombre="CEBOLLA", valor_de_compra=19.90, merma=0.00, unidad=KG)
    chile_ancho = md.Insumos(nombre="CHILE ANCHO",
                             valor_de_compra=210.00, merma=0.03, unidad=KG)
    chile_chipotle = md.Insumos(
        nombre="CHILE CHIPOTLE", valor_de_compra=200.00, merma=0.03, unidad=KG)
    chile_costeño = md.Insumos(
        nombre="CHILE COSTEÑO", valor_de_compra=180.00, merma=0.03, unidad=KG)
    chile_güero = md.Insumos(nombre="CHILE GÜERO",
                             valor_de_compra=82.00, merma=0.03, unidad=KG)
    chile_guiajillo = md.Insumos(
        nombre="CHILE GUIAJILLO", valor_de_compra=118.67, merma=0.00, unidad=KG)
    chile_habanero = md.Insumos(
        nombre="CHILE HABANERO", valor_de_compra=140.00, merma=0.03, unidad=KG)
    chile_mulato = md.Insumos(nombre="CHILE MULATO",
                              valor_de_compra=190.00, merma=0.03, unidad=KG)
    chile_pasilla = md.Insumos(
        nombre="CHILE PASILLA", valor_de_compra=185.00, merma=0.03, unidad=KG)
    chocolate_amargo = md.Insumos(
        nombre="CHOCOLATE AMARGO", valor_de_compra=160.00, merma=0.00, unidad=KG)
    chocolate_blanco = md.Insumos(
        nombre="CHOCOLATE BLANCO", valor_de_compra=100.00, merma=0.00, unidad=KG)
    chocolate_con_leche = md.Insumos(
        nombre="CHOCOLATE CON LECHE", valor_de_compra=170.00, merma=0.00, unidad=KG)
    chocolate_semiamargo = md.Insumos(
        nombre="CHOCOLATE SEMIAMARGO", valor_de_compra=165.00, merma=0.00, unidad=KG)
    cilantro = md.Insumos(nombre="CILANTRO.",
                          valor_de_compra=7.90, merma=0.00, unidad=ATD)
    ciruela_amarilla = md.Insumos(
        nombre="CIRUELA AMARILLA.", valor_de_compra=80.00, merma=0.00, unidad=KG)
    clavo_de_olor = md.Insumos(
        nombre="CLAVO DE OLOR", valor_de_compra=250.00, merma=0.00, unidad=KG)
    coco_rallado = md.Insumos(nombre="COCO RALLADO",
                              valor_de_compra=85.00, merma=0.00, unidad=KG)
    cocoa_en_polvo = md.Insumos(
        nombre="COCOA EN POLVO", valor_de_compra=100.00, merma=0.00, unidad=KG)
    crema_de_avellanas = md.Insumos(
        nombre="CREMA DE AVELLANAS.", valor_de_compra=144.00, merma=0.00, unidad=KG)
    crema_para_batir = md.Insumos(
        nombre="CREMA PARA BATIR.", valor_de_compra=49.95, merma=0.00, unidad=LT)
    dextrosa = md.Insumos(
        nombre="DEXTROSA", valor_de_compra=85.00, merma=0.00, unidad=KG)
    esencia_de_nuez = md.Insumos(
        nombre="ESENCIA DE NUEZ", valor_de_compra=165.00, merma=0.00, unidad=LT)
    extracto_de_vainilla = md.Insumos(
        nombre="EXTRACTO DE VAINILLA", valor_de_compra=6.70, merma=0.00, unidad=LT)
    fondo_de_pollo = md.Insumos(
        nombre="FONDO DE POLLO.", valor_de_compra=54.00, merma=0.00, unidad=LT)
    fresa = md.Insumos(nombre="FRESA", valor_de_compra=111.00,
                       merma=0.00, unidad=KG)
    galletas_maria = md.Insumos(
        nombre="GALLETAS MARÍA.", valor_de_compra=11.00, merma=0.00, unidad=PAQ)
    granillo_de_chocolate = md.Insumos(
        nombre="GRANILLO DE CHOCOLATE.", valor_de_compra=44.50, merma=0.00, unidad=KG)
    grenetina = md.Insumos(
        nombre="GRENETINA", valor_de_compra=178.90, merma=0.00, unidad=KG)
    guayaba = md.Insumos(
        nombre="GUAYABA", valor_de_compra=34.90, merma=0.00, unidad=KG)
    harina_de_almendra = md.Insumos(
        nombre="HARINA DE ALMENDRA.", valor_de_compra=380.00, merma=0.00, unidad=KG)
    harina_de_trigo = md.Insumos(
        nombre="HARINA DE TRIGO.", valor_de_compra=10.50, merma=0.00, unidad=KG)
    hielo = md.Insumos(nombre="HIELO", valor_de_compra=4.26,
                       merma=0.00, unidad=KG)
    hojas_de_maiz = md.Insumos(
        nombre="HOJAS DE MAÍZ. ", valor_de_compra=0.83, merma=0.00, unidad=PZA)
    huevo = md.Insumos(nombre="HUEVO", valor_de_compra=1.96,
                       merma=0.05, unidad=PZA)
    jalea_de_manzana = md.Insumos(
        nombre="JALEA DE MANZANA", valor_de_compra=80.00, merma=0.00, unidad=KG)
    jitomate = md.Insumos(
        nombre="JITOMATE", valor_de_compra=14.90, merma=0.00, unidad=KG)
    leche = md.Insumos(nombre="LECHE", valor_de_compra=22.00,
                       merma=0.00, unidad=LT)
    leche_condensada = md.Insumos(
        nombre="LECHE CONDENSADA.", valor_de_compra=43.00, merma=0.00, unidad=KG)
    leche_en_polvo = md.Insumos(
        nombre="LECHE EN POLVO", valor_de_compra=87.00, merma=0.00, unidad=KG)
    limon = md.Insumos(nombre="LIMÓN", valor_de_compra=24.90,
                       merma=0.05, unidad=KG)
    maiz = md.Insumos(nombre="MAIZ. ", valor_de_compra=15.00,
                      merma=0.10, unidad=KG)
    mamey = md.Insumos(nombre="MAMEY", valor_de_compra=33.00,
                       merma=0.00, unidad=KG)
    manteca_de_cerdo = md.Insumos(
        nombre="MANTECA DE CERDO.", valor_de_compra=39.00, merma=0.00, unidad=KG)
    mantequilla = md.Insumos(nombre="MANTEQUILLA",
                             valor_de_compra=68.00, merma=0.00, unidad=KG)
    masa_de_maiz = md.Insumos(nombre="MASA DE MAÍZ.",
                              valor_de_compra=10.00, merma=0.00, unidad=KG)
    media_crema = md.Insumos(nombre="MEDIA CREMA.",
                             valor_de_compra=12.00, merma=0.00, unidad=PZA)
    naranja = md.Insumos(
        nombre="NARANJA", valor_de_compra=15.90, merma=0.00, unidad=KG)
    neutro_para_helado = md.Insumos(
        nombre="NEUTRO PARA HELADO.", valor_de_compra=72.57, merma=0.00, unidad=KG)
    nuez_de_castilla = md.Insumos(
        nombre="NUEZ DE CASTILLA", valor_de_compra=399.00, merma=0.00, unidad=KG)
    oregano_molido = md.Insumos(
        nombre="ORÉGANO MOLIDO.", valor_de_compra=149.00, merma=0.00, unidad=KG)
    pan_blanco = md.Insumos(nombre="PAN BLANCO.",
                            valor_de_compra=18.50, merma=0.00, unidad=PAQ)
    pan_de_sandwichon = md.Insumos(
        nombre="PAN DE SANDWICHON", valor_de_compra=18.50, merma=0.00, unidad=PAQ)
    pepita = md.Insumos(
        nombre="PEPITA", valor_de_compra=220.00, merma=0.00, unidad=KG)
    piloncillo = md.Insumos(nombre="PILONCILLO",
                            valor_de_compra=9.97, merma=0.00, unidad=PZA)
    pimienta = md.Insumos(nombre="PIMIENTA ",
                          valor_de_compra=300.00, merma=0.00, unidad=KG)
    piñon_rosa = md.Insumos(nombre="PIÑON ROSA",
                            valor_de_compra=1500.00, merma=0.00, unidad=KG)
    platano_macho = md.Insumos(
        nombre="PLÁTANO MACHO.", valor_de_compra=29.90, merma=0.05, unidad=KG)
    polvo_para_hornear = md.Insumos(
        nombre="POLVO PARA HORNEAR.", valor_de_compra=28.00, merma=0.00, unidad=KG)
    queso_crema = md.Insumos(nombre="QUESO CREMA",
                             valor_de_compra=122.00, merma=0.00, unidad=KG)
    queso_de_bola = md.Insumos(
        nombre="QUESO DE BOLA", valor_de_compra=350.00, merma=0.05, unidad=KG)
    queso_mascarpone = md.Insumos(
        nombre="QUESO MASCARPONE", valor_de_compra=350.00, merma=0.00, unidad=KG)
    rompope = md.Insumos(
        nombre="ROMPOPE", valor_de_compra=96.50, merma=0.00, unidad=LT)
    sal = md.Insumos(nombre="SAL", valor_de_compra=8.10, merma=0.00, unidad=KG)
    soletillas = md.Insumos(nombre="SOLETILLAS",
                            valor_de_compra=195.00, merma=0.00, unidad=PAQ)
    tejocote = md.Insumos(
        nombre="TEJOCOTE", valor_de_compra=42.00, merma=0.00, unidad=KG)
    tortilla_de_maiz = md.Insumos(
        nombre="TORTILLA DE MAÍZ.", valor_de_compra=16.00, merma=0.00, unidad=KG)
    uva_pasa = md.Insumos(
        nombre="UVA PASA", valor_de_compra=106.00, merma=0.00, unidad=KG)
    vino_tinto_afrutado = md.Insumos(
        nombre="VINO TINTO AFRUTADO.", valor_de_compra=75.00, merma=0.00, unidad=LT)
    vodka = md.Insumos(nombre="VODKA", valor_de_compra=149.00,
                       merma=0.00, unidad=LT)
    # registrando ingredientes para mazapan de chocolate
    ing_mazapan_chocolate = [
        md.Ingredientes(insumo=agua, cantidad=0.320),
        md.Ingredientes(insumo=azucar_glas, cantidad=0.100),
        md.Ingredientes(insumo=bitartrato_de_potasio, cantidad=0.175),
        md.Ingredientes(insumo=cocoa_en_polvo, cantidad=0.004),
        md.Ingredientes(insumo=huevo, cantidad=0.500),
        md.Ingredientes(insumo=pepita, cantidad=0.100)
    ]
    # registrando receta mazapan de chocolate
    mazapan_chocolate = md.Recetas(
        nombre="MAZAPAN DE CHOCOLATE",
        porciones=16,
        tiempo_elaboracion=0.6,
        ingredientes=ing_mazapan_chocolate
    )
