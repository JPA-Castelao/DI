from reportlab.platypus import Paragraph
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.rl_settings import showBoundary
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Table

cabecera = ['', 'Luns', 'Martes', 'Miercoles', 'Xoves', 'Venres', 'Sábado', 'Domingo']
actM = ['Mañán', "Cole", "Correr", '-', '-', '-', 'Estudar', 'Traballar', 'Correr', ]
actT = ['Tarde', 'Traballer', 'Cole', 'Cole', 'Clases', 'Clases', 'Traballar']
actN = ['Noite', '-', 'Traballar', 'Traballar', '-', '-', '-']
taboa = Table([[cabecera, actM, actT, actN]])
taboa.setStyle([('TEXTCOLOR', (1, -4), (7, -4), colors.red), ('TEXTCOLOR', (0, 0), (0, 3), colors.blue)])
guion = []

guion.append(taboa)
doc = SimpleDocTemplate("taboasPlatypus.py", pagesize=A4, showBoundary=0)
doc.build(guion)
