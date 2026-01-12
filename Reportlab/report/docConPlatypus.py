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
