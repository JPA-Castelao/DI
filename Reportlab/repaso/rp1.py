from reportlab.pdfgen import canvas


folla = canvas.Canvas("Follaprimeira.pdf")
folla.drawString(0, 0, "Posición 0 0")
folla.drawString(10, 10, "Posicion 10,10")
folla.drawString(33, 33, "Posicion 33,33")

folla.drawImage(r"E:\DAM\DI\Reportlab\images\equis23x23.jpg", 50, 50, 23, 23)
folla.drawImage(r"E:\DAM\DI\Reportlab\images\tick23x23.jpeg", 20, 650, 23, 23)

folla.showPage()
folla.save()
