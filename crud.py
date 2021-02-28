from pony.orm import *
import models_db as models
import schemas as schemas
from api_response_tools import *

@db_session
def insertData():
    # insertando costos fijos
    models.CostosFijos(concepto="Nomina", costo_mensual=22000)
    models.CostosFijos(concepto="Pago de luz", costo_mensual=1500)
    models.CostosFijos(concepto="Pago de agua", costo_mensual=200)
    models.CostosFijos(concepto="Gas", costo_mensual=2000)
    models.CostosFijos(concepto="Alquiler", costo_mensual=3000)
    # insertando unidades
    KG = models.Unidades(nombre="Kilogramo", abrev="KG")
    LT = models.Unidades(nombre="Litro", abrev="LT")
    PAQ = models.Unidades(nombre="Paquete", abrev="PAQ")
    PZA = models.Unidades(nombre="Pieza", abrev="PZA")
    ATD = models.Unidades(nombre="Atado", abrev="ATD")
    # insertando insumos
    achiote = models.Insumos(
        nombre="ACHIOTE", valor_de_compra=100.00, merma=0.00, unidad=KG)
    agua = models.Insumos(nombre="AGUA", valor_de_compra=1.75,
                      merma=0.00, unidad=LT)
    ajo = models.Insumos(nombre="AJO", valor_de_compra=150.00,
                     merma=0.00, unidad=KG)
    ajonjoli = models.Insumos(
        nombre="AJONJOLÍ", valor_de_compra=98.00, merma=0.00, unidad=KG)
    almendra = models.Insumos(
        nombre="ALMENDRA", valor_de_compra=229.00, merma=0.00, unidad=KG)
    anis = models.Insumos(nombre="ANIS", valor_de_compra=520.00,
                      merma=0.00, unidad=KG)
    arandano_en_pasita = models.Insumos(
        nombre="ARÁNDANO EN PASITA", valor_de_compra=115.00, merma=0.00, unidad=KG)
    avena = models.Insumos(nombre="AVENA", valor_de_compra=20.00,
                       merma=0.00, unidad=KG)
    azucar = models.Insumos(
        nombre="AZÚCAR", valor_de_compra=29.00, merma=0.00, unidad=KG)
    azucar_glas = models.Insumos(nombre="AZÚCAR GLAS",
                             valor_de_compra=31.00, merma=0.00, unidad=KG)
    betabel = models.Insumos(
        nombre="BETABEL", valor_de_compra=21.90, merma=0.05, unidad=KG)
    bitartrato_de_potasio = models.Insumos(
        nombre="BITARTRATO DE POTASIO", valor_de_compra=199.00, merma=0.00, unidad=KG)
    cacahuate = models.Insumos(
        nombre="CACAHUATE", valor_de_compra=65.00, merma=0.00, unidad=KG)
    cacao = models.Insumos(nombre="CACAO", valor_de_compra=149.00,
                       merma=0.00, unidad=KG)
    cafe_molido = models.Insumos(nombre="CAFÉ MOLIDO.",
                             valor_de_compra=126.00, merma=0.00, unidad=KG)
    cafe_soluble = models.Insumos(nombre="CAFÉ SOLUBLE. ",
                              valor_de_compra=237.00, merma=0.00, unidad=KG)
    canela_en_raja = models.Insumos(
        nombre="CANELA EN RAJA.", valor_de_compra=288.00, merma=0.00, unidad=KG)
    canela_molida = models.Insumos(
        nombre="CANELA MOLIDA", valor_de_compra=199.00, merma=0.00, unidad=KG)
    cebolla = models.Insumos(
        nombre="CEBOLLA", valor_de_compra=19.90, merma=0.00, unidad=KG)
    chile_ancho = models.Insumos(nombre="CHILE ANCHO",
                             valor_de_compra=210.00, merma=0.03, unidad=KG)
    chile_chipotle = models.Insumos(
        nombre="CHILE CHIPOTLE", valor_de_compra=200.00, merma=0.03, unidad=KG)
    chile_costeño = models.Insumos(
        nombre="CHILE COSTEÑO", valor_de_compra=180.00, merma=0.03, unidad=KG)
    chile_güero = models.Insumos(nombre="CHILE GÜERO",
                             valor_de_compra=82.00, merma=0.03, unidad=KG)
    chile_guiajillo = models.Insumos(
        nombre="CHILE GUIAJILLO", valor_de_compra=118.67, merma=0.00, unidad=KG)
    chile_habanero = models.Insumos(
        nombre="CHILE HABANERO", valor_de_compra=140.00, merma=0.03, unidad=KG)
    chile_mulato = models.Insumos(nombre="CHILE MULATO",
                              valor_de_compra=190.00, merma=0.03, unidad=KG)
    chile_pasilla = models.Insumos(
        nombre="CHILE PASILLA", valor_de_compra=185.00, merma=0.03, unidad=KG)
    chocolate_amargo = models.Insumos(
        nombre="CHOCOLATE AMARGO", valor_de_compra=160.00, merma=0.00, unidad=KG)
    chocolate_blanco = models.Insumos(
        nombre="CHOCOLATE BLANCO", valor_de_compra=100.00, merma=0.00, unidad=KG)
    chocolate_con_leche = models.Insumos(
        nombre="CHOCOLATE CON LECHE", valor_de_compra=170.00, merma=0.00, unidad=KG)
    chocolate_semiamargo = models.Insumos(
        nombre="CHOCOLATE SEMIAMARGO", valor_de_compra=165.00, merma=0.00, unidad=KG)
    cilantro = models.Insumos(nombre="CILANTRO.",
                          valor_de_compra=7.90, merma=0.00, unidad=ATD)
    ciruela_amarilla = models.Insumos(
        nombre="CIRUELA AMARILLA.", valor_de_compra=80.00, merma=0.00, unidad=KG)
    clavo_de_olor = models.Insumos(
        nombre="CLAVO DE OLOR", valor_de_compra=250.00, merma=0.00, unidad=KG)
    coco_rallado = models.Insumos(nombre="COCO RALLADO",
                              valor_de_compra=85.00, merma=0.00, unidad=KG)
    cocoa_en_polvo = models.Insumos(
        nombre="COCOA EN POLVO", valor_de_compra=100.00, merma=0.00, unidad=KG)
    crema_de_avellanas = models.Insumos(
        nombre="CREMA DE AVELLANAS.", valor_de_compra=144.00, merma=0.00, unidad=KG)
    crema_para_batir = models.Insumos(
        nombre="CREMA PARA BATIR.", valor_de_compra=49.95, merma=0.00, unidad=LT)
    dextrosa = models.Insumos(
        nombre="DEXTROSA", valor_de_compra=85.00, merma=0.00, unidad=KG)
    esencia_de_nuez = models.Insumos(
        nombre="ESENCIA DE NUEZ", valor_de_compra=165.00, merma=0.00, unidad=LT)
    extracto_de_vainilla = models.Insumos(
        nombre="EXTRACTO DE VAINILLA", valor_de_compra=6.70, merma=0.00, unidad=LT)
    fondo_de_pollo = models.Insumos(
        nombre="FONDO DE POLLO.", valor_de_compra=54.00, merma=0.00, unidad=LT)
    fresa = models.Insumos(nombre="FRESA", valor_de_compra=111.00,
                       merma=0.00, unidad=KG)
    galletas_maria = models.Insumos(
        nombre="GALLETAS MARÍA.", valor_de_compra=11.00, merma=0.00, unidad=PAQ)
    granillo_de_chocolate = models.Insumos(
        nombre="GRANILLO DE CHOCOLATE.", valor_de_compra=44.50, merma=0.00, unidad=KG)
    grenetina = models.Insumos(
        nombre="GRENETINA", valor_de_compra=178.90, merma=0.00, unidad=KG)
    guayaba = models.Insumos(
        nombre="GUAYABA", valor_de_compra=34.90, merma=0.00, unidad=KG)
    harina_de_almendra = models.Insumos(
        nombre="HARINA DE ALMENDRA.", valor_de_compra=380.00, merma=0.00, unidad=KG)
    harina_de_trigo = models.Insumos(
        nombre="HARINA DE TRIGO.", valor_de_compra=10.50, merma=0.00, unidad=KG)
    hielo = models.Insumos(nombre="HIELO", valor_de_compra=4.26,
                       merma=0.00, unidad=KG)
    hojas_de_maiz = models.Insumos(
        nombre="HOJAS DE MAÍZ. ", valor_de_compra=0.83, merma=0.00, unidad=PZA)
    huevo = models.Insumos(nombre="HUEVO", valor_de_compra=1.96,
                       merma=0.05, unidad=PZA)
    jalea_de_manzana = models.Insumos(
        nombre="JALEA DE MANZANA", valor_de_compra=80.00, merma=0.00, unidad=KG)
    jitomate = models.Insumos(
        nombre="JITOMATE", valor_de_compra=14.90, merma=0.00, unidad=KG)
    leche = models.Insumos(nombre="LECHE", valor_de_compra=22.00,
                       merma=0.00, unidad=LT)
    leche_condensada = models.Insumos(
        nombre="LECHE CONDENSADA.", valor_de_compra=43.00, merma=0.00, unidad=KG)
    leche_en_polvo = models.Insumos(
        nombre="LECHE EN POLVO", valor_de_compra=87.00, merma=0.00, unidad=KG)
    limon = models.Insumos(nombre="LIMÓN", valor_de_compra=24.90,
                       merma=0.05, unidad=KG)
    maiz = models.Insumos(nombre="MAIZ. ", valor_de_compra=15.00,
                      merma=0.10, unidad=KG)
    mamey = models.Insumos(nombre="MAMEY", valor_de_compra=33.00,
                       merma=0.00, unidad=KG)
    manteca_de_cerdo = models.Insumos(
        nombre="MANTECA DE CERDO.", valor_de_compra=39.00, merma=0.00, unidad=KG)
    mantequilla = models.Insumos(nombre="MANTEQUILLA",
                             valor_de_compra=68.00, merma=0.00, unidad=KG)
    masa_de_maiz = models.Insumos(nombre="MASA DE MAÍZ.",
                              valor_de_compra=10.00, merma=0.00, unidad=KG)
    media_crema = models.Insumos(nombre="MEDIA CREMA.",
                             valor_de_compra=12.00, merma=0.00, unidad=PZA)
    naranja = models.Insumos(
        nombre="NARANJA", valor_de_compra=15.90, merma=0.00, unidad=KG)
    neutro_para_helado = models.Insumos(
        nombre="NEUTRO PARA HELADO.", valor_de_compra=72.57, merma=0.00, unidad=KG)
    nuez_de_castilla = models.Insumos(
        nombre="NUEZ DE CASTILLA", valor_de_compra=399.00, merma=0.00, unidad=KG)
    oregano_molido = models.Insumos(
        nombre="ORÉGANO MOLIDO.", valor_de_compra=149.00, merma=0.00, unidad=KG)
    pan_blanco = models.Insumos(nombre="PAN BLANCO.",
                            valor_de_compra=18.50, merma=0.00, unidad=PAQ)
    pan_de_sandwichon = models.Insumos(
        nombre="PAN DE SANDWICHON", valor_de_compra=18.50, merma=0.00, unidad=PAQ)
    pepita = models.Insumos(
        nombre="PEPITA", valor_de_compra=220.00, merma=0.00, unidad=KG)
    piloncillo = models.Insumos(nombre="PILONCILLO",
                            valor_de_compra=9.97, merma=0.00, unidad=PZA)
    pimienta = models.Insumos(nombre="PIMIENTA ",
                          valor_de_compra=300.00, merma=0.00, unidad=KG)
    piñon_rosa = models.Insumos(nombre="PIÑON ROSA",
                            valor_de_compra=1500.00, merma=0.00, unidad=KG)
    platano_macho = models.Insumos(
        nombre="PLÁTANO MACHO.", valor_de_compra=29.90, merma=0.05, unidad=KG)
    polvo_para_hornear = models.Insumos(
        nombre="POLVO PARA HORNEAR.", valor_de_compra=28.00, merma=0.00, unidad=KG)
    queso_crema = models.Insumos(nombre="QUESO CREMA",
                             valor_de_compra=122.00, merma=0.00, unidad=KG)
    queso_de_bola = models.Insumos(
        nombre="QUESO DE BOLA", valor_de_compra=350.00, merma=0.05, unidad=KG)
    queso_mascarpone = models.Insumos(
        nombre="QUESO MASCARPONE", valor_de_compra=350.00, merma=0.00, unidad=KG)
    rompope = models.Insumos(
        nombre="ROMPOPE", valor_de_compra=96.50, merma=0.00, unidad=LT)
    sal = models.Insumos(nombre="SAL", valor_de_compra=8.10, merma=0.00, unidad=KG)
    soletillas = models.Insumos(nombre="SOLETILLAS",
                            valor_de_compra=195.00, merma=0.00, unidad=PAQ)
    tejocote = models.Insumos(
        nombre="TEJOCOTE", valor_de_compra=42.00, merma=0.00, unidad=KG)
    tortilla_de_maiz = models.Insumos(
        nombre="TORTILLA DE MAÍZ.", valor_de_compra=16.00, merma=0.00, unidad=KG)
    uva_pasa = models.Insumos(
        nombre="UVA PASA", valor_de_compra=106.00, merma=0.00, unidad=KG)
    vino_tinto_afrutado = models.Insumos(
        nombre="VINO TINTO AFRUTADO.", valor_de_compra=75.00, merma=0.00, unidad=LT)
    vodka = models.Insumos(nombre="VODKA", valor_de_compra=149.00,
                       merma=0.00, unidad=LT)
    # registrando ingredientes para mazapan de chocolate
    ing_mazapan_chocolate = [
        models.Ingredientes(insumo=agua, cantidad=0.320),
        models.Ingredientes(insumo=azucar_glas, cantidad=0.100),
        models.Ingredientes(insumo=bitartrato_de_potasio, cantidad=0.175),
        models.Ingredientes(insumo=cocoa_en_polvo, cantidad=0.004),
        models.Ingredientes(insumo=huevo, cantidad=0.500),
        models.Ingredientes(insumo=pepita, cantidad=0.100)
    ]
    # registrando receta mazapan de chocolate
    mazapan_chocolate = models.Recetas(
        nombre="MAZAPAN DE CHOCOLATE",
        porciones=16,
        tiempo_elaboracion=0.6,
        ingredientes=ing_mazapan_chocolate
    )
