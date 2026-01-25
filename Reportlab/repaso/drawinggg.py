from reportlab.graphics.shapes import Image, Drawing

from reportlab.graphics import renderPDF

from reportlab.lib.pagesizes import A4

imagenes = []

imagen = Image(400, 0, 230, 250, r"E:\edits\emotional autarchy\jpg.jpg")

dibujo = Drawing(30, 30)

dibujo.add(imagen)

dibujo.translate(0, 700)

imagenes.append(dibujo)

dibujo = Drawing(30, 30)

dibujo.add(imagen)

dibujo.rotate(45)
dibujo.translate(-90, 300)
dibujo.scale(1.5, 0.5)

imagenes.append(dibujo)

dibujo = Drawing(30, 30)
dibujo.rotate(90)

dibujo.translate(-20, - 110)

dibujo.add(imagen)

imagenes.append(dibujo)

dibujo = Drawing(A4[0], A4[1])

for aux in imagenes:
    dibujo.add(aux)

renderPDF.drawToFile(dibujo, r"E:\DAM\DI\Reportlab\repaso\cap1.pdf")
