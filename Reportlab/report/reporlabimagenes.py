from tabnanny import filename_only

from reportlab.graphics.shapes import Image, Drawing
from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import A4, A2

guion = []
imaxe = Image(20, 100, 200, 202, "bloatlord.jpg")
debuxo = Drawing(300, 12)
debuxo.add(imaxe)
guion.append(debuxo)

debuxo2 = Drawing()
debuxo2.add(imaxe)
debuxo2.translate(150, 350)
guion.append(debuxo2)

debuxo3 = Drawing()
debuxo3.add(imaxe)
debuxo3.rotate(45)
debuxo3.translate(600, 150)
guion.append(debuxo3)

debuxo4 = Drawing()
debuxo4.add(imaxe)
debuxo4.translate(150, 500)
debuxo4.scale(0.5, 0.5)
debuxo4.rotate(-115)
guion.append(debuxo4)

folla = Drawing(A4[0], A4[1])

for elemento in guion:
    folla.add(elemento)

renderPDF.drawToFile(folla, "exemploConDrawing.pdf")
