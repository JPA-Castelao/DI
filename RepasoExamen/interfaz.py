import sys
import PyQt6.QtWidgets

from PyQt6.QtWidgets import (
    QWidget, QMainWindow, QApplication, QPushButton, QLabel, QVBoxLayout, QLayout
)


class ventanaPrincial(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi app desde 0 para repasar tu sabe")
        self.setGeometry(0, 0, 300, 400)

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QVBoxLayout(central_widget)
        # Creacion de Widgetsss(botones y etiquetas)
        self.boton_principal = QPushButton("BOTON PRINCIPAL")
        self.boton_secundario = QPushButton("BOTON SECUNDARIO")
        self.etiqueta = QLabel("ETIQUETA")
        self.etiqueta.setGeometry(0, 0, 50, 40)
        # Adición de widgets
        self.main_layout.addWidget(self.boton_principal)
        self.main_layout.addWidget(self.boton_secundario)
        self.main_layout.addWidget(self.etiqueta)

        # conexion de eventos
        self.boton_principal.clicked.connect()
        self.boton_secundario.clicked.connect()
        # metodos

    def handle_principal_click(self):
        print("boton pulsado")
        self.etiqueta.setText("BOTON PRINCIPAL PULSADO")
        self.etiqueta.setStyleSheet("color:green")

    def handle_secundario_click(self):
        print("boton pulsado")
        self.etiqueta.setText("BOTON SECUNDARIO PULSADO")
        self.setStyleSheet("color:purple")

if __name__=="__main__":
    app=QApplication(sys.argv)
    ventanita= ventanaPrincial()
    ventanita.show()
    sys.exit(app.exec())

