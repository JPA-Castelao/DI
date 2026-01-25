from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.graphics.shapes import Drawing, Rect
from reportlab.lib.units import cm

doc = SimpleDocTemplate("factura.pdf", pagesize=A4)
styles = getSampleStyleSheet()
story = []


