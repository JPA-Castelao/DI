from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.graphics.shapes import Drawing, Rect, String, Image
from reportlab.lib.units import cm

doc = SimpleDocTemplate("Proforma.pdf", pagesize=A4)

styles = getSampleStyleSheet()

story = []

logo_canvas = Drawing(35, 35)
logo = Image(20, 100, 32, 32, "/report/images/equis23x23.jpg")

logo_canvas.add(logo)

logo_estilo = ParagraphStyle("estiloFactura", parent=styles['Heading1'], fontSize=26, textColor=colors.black)
logo_nombre = Paragraph("FACTURA Proforma", logo_estilo)

tabla_cabecera = Table([[logo_nombre, logo_canvas]], colWidths=50, rowHeights=50)
tabla_cabecera.setStyle(TableStyle([
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('ALIGN', (0, 0), (-1, -1), 'RIGHT')

]))

story.append(tabla_cabecera)
story.append(Spacer(1, 1 * cm))

datos_bloque_info = [
    ["FACTURAR A:", "Nº DE FACTURA"],
    ["", "FECHA"],
    ["Cliente", "Nº de pedido"],
    ["Domicilio", ""],
    ["Código postal/ciudad", "Fecha de vencimiento"],
    ["(NIF)", "Condiciones de pago"]

]

tabla_info = Table(datos_bloque_info, colWidths=9 * cm)
tabla_info.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (1, 0), colors.whitesmoke),
    ('FONTNAME', (0, 0), (1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (1, 5), 3),
    ('VALIGN', (0, 0), (-1, -1), 'TOP')
]))
story.append(tabla_info)
story.append(Spacer(1, 0.8 * cm))

# tabla de prodctos

header_productos = ["Pos.", "Concepto/Descripcion", "Cantidad", "Unidad", "Precio Unitario", "Importe"]
fila1 = ["1", "Descripción del producto o servicio", "1,00", "unidad", "100,00", "100,00"]
fila2 = ["2", "Otro concepto adicional", "2,00", "unidad", "50,00", "100,00"]
vacia = ["", "", "", "", "", ""]  #

data_tabla_prod = [header_productos, fila1, fila2, vacia, vacia]
tabla_prod = Table(data_tabla_prod, colWidths=10 * cm)
tabla_prod.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),  # Encabezado gris
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),  # Rejilla fina en toda la tabla
    ('ALIGN', (2, 0), (-1, -1), 'CENTER'),  # Centrar números
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('LEFTPADDING', (1, 1), (1, -1), 10),  # Margen extra para la descripción
    ('ROWHEIGHTS', (0, 0), (-1, -1), 20)
]))
story.append(tabla_prod)
story.append(Spacer(1, 1.5 * cm))

tabla_metodo = Table([["Metodo de pago:"]], colWidths=7 * cm, rowHeights=2.5 * cm)

tabla_metodo.setStyle(TableStyle([
    ('BOX', (0, 0), (0, 0), 0.5, colors.black),
    ('VALIGN', (0, 0), (0, 0), 'TOP'),
    ('FONTSIZE', (0, 0), (0, 0), 8),
]))

data_totales = [
    ["Importe neto", "200,00"],
    ["+ IVA de 21 %", "42,00"],
    ["- IRPF de 15 %", "30,00"],
    ["IMPORTE BRUTO", "212,00"]
]
tabla_totales = Table(data_totales, colWidths=[4 * cm, 3 * cm])
tabla_totales.setStyle(TableStyle([
    ('GRID', (0, 0), (1, 2), 0.5, colors.grey),  # Rejilla para los impuestos
    ('BACKGROUND', (0, 3), (1, 3), colors.lightgrey),  # Fondo para el total final
    ('FONTNAME', (0, 3), (1, 3), 'Helvetica-Bold'),
    ('ALIGN', (1, 0), (1, 3), 'RIGHT'),  # Números a la derecha
    ('BOX', (0, 3), (1, 3), 1, colors.black),  # Borde grueso al total
]))

# Metemos estas dos tablas en una sola para posicionarlas en la misma línea
bloque_final = Table([[tabla_metodo, tabla_totales]], colWidths=[10.5 * cm, 7 * cm])
bloque_final.setStyle(TableStyle([('ALIGN', (1, 0), (1, 0), 'RIGHT')]))
story.append(bloque_final)

# --- SECCIÓN 5: DESPEDIDA ---
story.append(Spacer(1, 1 * cm))
story.append(Paragraph("Gracias por su confianza.", styles['Normal']))
story.append(Spacer(1, 0.5 * cm))
story.append(Paragraph("Atentamente,", styles['Normal']))

# 3. GENERAR EL PDF
# El comando build() toma la lista de objetos y los "dibuja" en el archivo siguiendo el flujo.
doc.build(story)
print("¡Archivo 'Factura_Proforma_Explicada.pdf' generado!")
