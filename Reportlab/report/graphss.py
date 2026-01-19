from reportlab.graphics.charts.barcharts import VerticalBarChart, HorizontalBarChart
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.rl_settings import strikeWidth

d = Drawing(400, 200)
datos = [(13.3, 8, 14.3, 25, 33.3, 37.5, 21.1, 28.6, 45.5, 38.1, 54.2, 36.0, 42.3)]
lendaDatos = ['11/12', '12/13', '13/14', '14/15', '15/16', '16/17', '17/18', '19/20', '20/21', '22/23', '23/24',
              '24/25']

graficoBarras = VerticalBarChart()
graficoBarras.x = 50
graficoBarras.y = 50
graficoBarras.height = 125
graficoBarras.width = 300
graficoBarras.data = datos
graficoBarras.valueAxis.valueMin = 0
graficoBarras.valueAxis.valueMax = 70
graficoBarras.valueAxis.valueStep = 10
# labels
graficoBarras.categoryAxis.labels.boxAnchor = 'ne'
graficoBarras.categoryAxis.labels.dx = 15
graficoBarras.categoryAxis.labels.dy = -5
graficoBarras.categoryAxis.labels.angle = 30
graficoBarras.categoryAxis.categoryNames = lendaDatos
graficoBarras.barSpacing = 5

# grafico lineas
d2 = Drawing(400, 500)
graficoLineas = HorizontalLineChart()

graficoLineas.x = 30
graficoLineas.y = 50
graficoLineas.height = 125
graficoLineas.width = 350
graficoLineas.data = datos
graficoLineas.categoryAxis.categoryNames = lendaDatos
graficoLineas.categoryAxis.labels.boxAnchor = 'n'
graficoLineas.valueAxis.valueMin = 0
graficoLineas.valueAxis.valueMax = 100
graficoLineas.valueAxis.valueStep = 20
graficoLineas.lines[0].strokeWidth = 2
graficoLineas.lines[0].symbol = makeMarker("FilledCircle")
graficoLineas.lines[1].strokeWidth = 1.5
d2.add(graficoLineas)

# doc = SimpleDocTemplate("exemploGraficos.pdf", pagesize=A4)
# doc.build([d])

# grafico tarta
d3 = Drawing(400, 200)
graficoTarta = Pie()
graficoTarta.x = 65
graficoTarta.y = 15
graficoTarta.height = 170
graficoTarta.width = 170
graficoTarta.data = [10, 20, 30, 40, 50]
graficoTarta.labels = ['Oppo', 'Pixel', 'Galaxy', 'Iphone', 'Xiaomi']

graficoTarta.slices.strokeWidth = 0.5
graficoTarta.slices[3].popout = 10
graficoTarta.slices[3].strokeDashArray = [2, 2]
graficoTarta.slices[3].labelRadius = 1.75
graficoTarta.slices[3].fontColor = colors.red
graficoTarta.sideLabels = 1

# colores
colores = [colors.blue, colors.red, colors.green, colors.yellow, colors.turquoise]

for i, color in enumerate(colores):
    graficoTarta.slices[i].fillColor = color

lenda = Legend()
lenda.colorNamePairs = [(graficoTarta.slices[i].fillColor,
                         graficoTarta.labels[i][0:20], '%0.2f' % (graficoTarta.data[i]))
                        for i in range(len(graficoTarta.data))]
lenda.x = 370
lenda.y = 5
lenda.fontName = 'Helvetica'
lenda.fontSize = 7
lenda.boxAnchor = 'n'
lenda.columnMaximum = 5
lenda.strokeWidth = 1
lenda.strokeColor = colors.black
lenda.deltax = 75
lenda.deltay = 20
lenda.autoXPadding = 5
lenda.dxTextSpace = 5
lenda.alignment = 'right'
lenda.dividerLines = 1 | 2 | 3 | 4 | 5
lenda.dividerLines = 7
lenda.dividerOffsY = 5.5
lenda.subCols.rpad = 10
# Constructor
d.add(graficoBarras)
d2.add(graficoLineas)
d3.add(lenda)
d3.add(graficoTarta)
doc = SimpleDocTemplate("exemploGraficos.pdf", pageSize=A4)
doc.build([d, Spacer(15, 15), d2, Spacer(15, 15), d3, Spacer(15, 15)])
