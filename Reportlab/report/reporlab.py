from reportlab.pdfgen import canvas

folla = canvas.Canvas("primeiroDocumento.pdf")

folla.drawString(0, 0, "Posición(x,y)=(0,0)")

folla.drawString(50, 100, "Posición(x,y)=(50,100)")

folla.drawString(150, 20, "Posición(x,y)=(150,20)")

folla.drawImage("Reportlab/images/equis23x23.jpg", 20, 700, 23, 23)
folla.drawImage("Reportlab/images/tick23x23.jpeg", 20, 650, 23, 23)

folla.showPage()
folla.save()
