from reportlab.platypus import Paragraph
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.rl_settings import showBoundary

guion = []

follaEstilo = getSampleStyleSheet()
# print(follaEstilo.list())

cabeceira = follaEstilo["Heading4"]
cabeceira.pageBreakbefore = 0
cabeceira.backColor = colors.aquamarine

cabeceiraCursiva = follaEstilo["Heading4"]
cabeceiraCursiva.fontName = "Helvetica-Oblique"
cabeceiraCursiva.pageBreakbefore = 0
cabeceiraCursiva.fontSize = 18
cabeceiraCursiva.aligment = 1

titulo = Paragraph("Titulo no documento", cabeceiraCursiva)
guion.append(titulo)

paragrafo = Paragraph("Cabeceira do documento", cabeceira)
guion.append(paragrafo)


texto = "Texto incluido no documento, e que forma o contido." * 50

corpoTexto = follaEstilo['BodyText']
corpoTexto.fontSize = 12
paragrafo2 = Paragraph(texto, corpoTexto)
guion.append(paragrafo2)
guion.append(Spacer(0, 30))

imaxe = Image("bloatlord.jpg", width=500, height=400)
guion.append(imaxe)

doc = SimpleDocTemplate("exemploPlatypus.pdf", pageisze=A4, showBoundary=1)
doc.build(guion)


import os
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                Image, Table, TableStyle, Frame)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas

import os
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                Image, Table, TableStyle, Frame)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas

# --- 1. CONFIGURACIÓN INICIAL Y ESTILOS ---
# SimpleDocTemplate es el contenedor de alto nivel (DocTemplate)
documento = SimpleDocTemplate("ejemplo_platypus.pdf", pagesize=A4, showBoundary=1)
estilos = getSampleStyleSheet()
story = []  # La "historia" es la lista de Flowables que formarán el PDF

# --- 2. CREACIÓN DE PÁRRAFOS (FLOWABLES) ---
# Definimos un estilo personalizado para la cabecera
estilo_cabecera = estilos['Heading4']
estilo_cabecera.backColor = colors.cyan  # Fondo color cian

# Creamos y añadimos elementos al story
story.append(Paragraph("CABECERA DEL DOCUMENTO", estilo_cabecera))
story.append(Spacer(1, 20))  # Espacio en blanco (ancho, alto)

cadena_texto = "El Viaje del Navegante " * 10
story.append(Paragraph(cadena_texto, estilos['BodyText']))

# --- 3. INSERCIÓN DE IMÁGENES ---
# Las imágenes son Flowables que requieren ruta, ancho y alto
try:
    ruta_img = os.path.realpath("elviajedelnavegante_png.png")
    imagen = Image(ruta_img, width=100, height=50)
    story.append(imagen)
except:
    print("Imagen no encontrada, saltando...")

story.append(Spacer(1, 20))

# --- 4. TABLAS Y ESTILOS DE TABLA ---
# Una tabla se define como una lista de listas (filas)
datos_tabla = [
    ['', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes'],
    ['Mañana', 'Estudiar', 'Cole', 'Gimnasio', '-', '-'],
    ['Tarde', 'Trabajar', 'Trabajar', 'Clases', 'Clases', 'Trabajar']
]

tabla = Table(datos_tabla)

# Los estilos de tabla usan coordenadas (columna, fila)
# (0,0) es el origen, (-1,-1) es la última celda
estilo_taboa = TableStyle([
    ('TEXTCOLOR', (1, 0), (-1, 0), colors.red),  # Días en rojo
    ('TEXTCOLOR', (0, 1), (0, -1), colors.blue),  # Mañana/Tarde en azul
    ('BACKGROUND', (1, 1), (-1, -1), colors.cyan),  # Fondo cian en datos
    ('GRID', (0, 0), (-1, -1), 0.25, colors.black),  # Rejilla completa
    ('BOX', (0, 0), (-1, -1), 1, colors.black)  # Borde exterior grueso
])

tabla.setStyle(estilo_taboa)
story.append(tabla)

# --- 5. CONSTRUCCIÓN FINAL ---
# build() procesa la lista 'story' y genera el archivo físico
documento.build(story)


# --- BONUS: USO DE FRAMES (MANUAL) ---
# Si no usas DocTemplate, puedes dibujar en un canvas usando Frames manualmente
def ejemplo_frame_manual():
    canv = Canvas("ejemplo_manual.pdf")
    # Frame(x, y, ancho, alto)
    marco = Frame(inch, inch, 4 * inch, 5 * inch, showBoundary=1)

    # Creamos una lista separada de elementos para este marco
    elementos_marco = [Paragraph("Texto dentro de un Frame manual", estilos['Normal'])]

    # addFromList "vierte" los elementos en el espacio del frame sobre el canvas
    marco.addFromList(elementos_marco, canv)
    canv.save()


ejemplo_frame_manual()