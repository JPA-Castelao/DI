from reportlab.pdfgen import canvas

texto = ('Jotaro', 'Joseph', 'Josuke', "Johnatan")
obxCanvas = canvas.Canvas("textoCanvas.pdf")
obxTexto = obxCanvas.beginText()
obxTexto.setTextOrigin(100, 500)
obxTexto.setFont("Courier", 15)

for linha in texto:
    obxTexto.textOut(linha)
    obxTexto.moveCursor(20, 15)

obxTexto.setFillGray(0.5)

textoLongo = """Outro Texto con varias liñas incorporadas
con retornos de carro incluidos"""

obxTexto.textLine("AWOOOOGA")
obxTexto.textLines(textoLongo)
obxTexto.setTextOrigin(20, 700)

for tipo_letra in obxCanvas.getAvailableFonts():
    obxTexto.setFont(tipo_letra, 16)
    obxTexto.textLine("ORA ORA ORA " + tipo_letra)
    obxTexto.moveCursor(10, 10)

obxTexto.setFillColorRGB(0.5, 0, 0.6)
obxTexto.setFont("Helvetica", 22)

for linha in texto:
    obxTexto.textOut(linha)
    obxTexto.moveCursor(20, 15)

obxTexto.setFillColor("Pink")

obxTexto.moveCursor(-60, 15)
espazoCaracteres = 0

for linha in texto:
    obxTexto.setCharSpace(espazoCaracteres)
    obxTexto.textLine("Espazo %s: %s" % (espazoCaracteres, linha))
    espazoCaracteres += 1

obxTexto.setFillColor("Green", 0.5)
obxTexto.textLines(texto)



obxCanvas.drawText(obxTexto)
obxCanvas.showPage()
obxCanvas.save()
