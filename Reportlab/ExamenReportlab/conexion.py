import sqlite3
import os
from pydoc import pager

from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.shapes import Drawing
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table
from reportlab.lib import colors
from reportlab.platypus import *
from reportlab.lib import *


def obter_produtos_mais_vendidos(self, limite=10):
    """Obter os produtos máis vendidos"""

    conn = sqlite3.connect(self)
    cursor = conn.cursor()

    cursor.execute("""
       SELECT 
        p.nome,
        SUM(If.cantidade) as total_vendido,
        SUM(If.cantidade*If.prezo_unitario*(1- If.desconto/100)) as facturacion
        FROM linhas_factura If
        JOIN produtos p on If.id_produto=p.id_produto
        GROUP BY p.id_produto,p.nome
        ORDER BY total_vendido DESC
        LIMIT ?             
     """, (limite,))

    resultados = cursor.fetchall()
    conn.close()
    return resultados


def grafica():
    d = Drawing(400, 400)

    produtos_lista = []
    cabecera = ['Posicion', 'Produto', 'Unidades vendidas', 'Facturacion']
    linha1 = [1, 'Memoria RAM DDR4 16GB', 81, '4324€']
    linha2 = [2, 'Memoria RAM DDR4 16GB', 81, '4324€']
    linha3 = [3, 'Memoria RAM DDR4 16GB', 81, '4324€']
    linha4 = [4, 'Memoria RAM DDR4 16GB', 81, '4324€']
    linha5 = [5, 'Memoria RAM DDR4 16GB', 81, '4324€']
    produtos_lista.append(cabecera)
    produtos_lista.append(linha1)
    produtos_lista.append(linha2)
    produtos_lista.append(linha3)
    produtos_lista.append(linha4)
    produtos_lista.append(linha5)

    datos = [(4324, 33648, 7429, 36269, 7632)]
    lendaDatos = ['Memoria RAM DDR4 16GB',
                  'Portátil HP Pavilion 15',
                  'Monitor Dell 24 polgadas',
                  'Torre de sobremesa Custom',
                  'Monitor LG 27 polgadas']

    graficoBarras = VerticalBarChart()
    graficoBarras.x = 0
    graficoBarras.y = 0
    graficoBarras.height = 100
    graficoBarras.width = 300
    graficoBarras.data = datos
    graficoBarras.valueAxis.valueMin = 0
    graficoBarras.valueAxis.valueMax = 40000
    graficoBarras.valueAxis.valueStep = 5000
    graficoBarras.categoryAxis.labels.boxAnchor = 'ne'
    graficoBarras.categoryAxis.labels.dx = 8
    graficoBarras.categoryAxis.labels.dy = -10
    graficoBarras.categoryAxis.labels.angle = 30
    graficoBarras.categoryAxis.categoryNames = lendaDatos
    graficoBarras.groupSpacing = 10

    graficoBarras.barSpacing = 3
    d.add(graficoBarras)
    return d


def adxuntar_datos():
    datos_columna = []
    colummnas_totales = []
    array_produtos = obter_produtos_mais_vendidos("/home/dam/DI/Reportlab/ExamenReportlab/bdTendaOrdeadoresBig.bd")
    for i in range(5):
        for sss in enumerate(array_produtos[i]):
            datos_columna.append(sss)
        colummnas_totales.append(datos_columna)

        print(colummnas_totales[i])
    return colummnas_totales


def crear_taboa():
    produtos_lista = []
    cabecera = ['Posicion', 'Produto', 'Unidades vendidas', 'Facturacion']
    linha1 = [1, 'Memoria RAM DDR4 16GB', 81, '4324€']
    linha2 = [2, 'Memoria RAM DDR4 16GB', 81, '4324€']
    linha3 = [3, 'Memoria RAM DDR4 16GB', 81, '4324€']
    linha4 = [4, 'Memoria RAM DDR4 16GB', 81, '4324€']
    linha5 = [5, 'Memoria RAM DDR4 16GB', 81, '4324€']
    produtos_lista.append(cabecera)
    produtos_lista.append(linha1)
    produtos_lista.append(linha2)
    produtos_lista.append(linha3)
    produtos_lista.append(linha4)
    produtos_lista.append(linha5)

    # taboa = Table(adxuntar_datos())#
    taboa = Table(produtos_lista)
    taboa.setStyle(([
        ('BACKGROUND', (0, 0), (4, 0), colors.red),
        ('TEXTCOLOR', (0, 0), (4, 0), colors.white),
        ("BOX", (0, 0), (-1, -1), 1, colors.black),

        ('BACKGROUND', (1, 1), (5, 1), colors.white),
        ('BACKGROUND', (0, 2), (5, 2), colors.gray),
        ('BACKGROUND', (0, 3), (5, 3), colors.white),
        ('BACKGROUND', (0, 4), (5, 4), colors.gray),

        ('INNERGRID', (0, 1), (4, -1), 1, colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ]))

    guion = []

    guion.append(taboa)
    guion.append(grafica())
    doc = SimpleDocTemplate("TaboaProdutos.pdf", pagesize=A4)
    doc.build(guion)


def xerar_factura():
    datos = obter_produtos_mais_vendidos("/home/dam/DI/Reportlab/ExamenReportlab/bdTendaOrdeadoresBig.bd", 10)

    cabeceira = ['Posicion', 'Produto', 'Unidades vendidas', 'Facturacion']
    datos_Taboa = []
    datos_Taboa.append(cabeceira)
    for orde, linha in enumerate(datos):
        datos_Taboa.append([orde + 1, linha[0], linha[1], f"{linha[2]:.0f}€"])
    print(datos_Taboa)
    t = Table(datos_Taboa)

    estilo_tabla = [
        # cabeceira
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkgreen),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        # Corpo
        ('GRID', (0, 1), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),

    ]

    for i in range(2, len(datos_Taboa), 2):
        estilo_tabla.append(('BACKGROUND', (0, i), (-1, i), colors.lightgrey))

    t.setStyle(estilo_tabla)

    doc = SimpleDocTemplate("InformeCliente.pdf", pagesize=A4)
    doc.build([t])


def xerar_tarta_pdf(datos):
    facturacion = []
    etiquetas = []
    for linha in datos:
        facturacion.append(linha[-1])
        etiquetas.append(linha[0])

    ancho = 400
    alto = 350
    debuxo = Drawing(ancho, alto)
    tarta = Pie()
    tarta.x = ancho / 2 - 100
    tarta.y = alto / 2 - 100
    tarta.width = 200
    tarta.height = 200
    tarta.data = facturacion
    tarta.labels = etiquetas
    doc = SimpleDocTemplate("informeCliente.pdf", pagesize=A4)
    debuxo.add(tarta)
    doc.build([debuxo.add(tarta)])


if __name__ == '__main__':
    xerar_factura()
    xerar_tarta_pdf()
