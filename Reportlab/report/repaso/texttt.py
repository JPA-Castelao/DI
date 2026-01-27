from reportlab.pdfgen import canvas

oracion = ['Y en tu ausencia las paredes', 'se pintarán de tristeza',
           'y enjaularé mi corazón entre tus huesos.']

aux = canvas.Canvas(r"E:\DAM\DI\Reportlab\repaso\textt.pdf")

textobject = aux.beginText()
textobject.setTextOrigin(100, 500)
textobject.setFont("Courier", 14)
