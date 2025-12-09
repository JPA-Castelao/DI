import sys

from PyQt6.QtWidgets import (QApplication, QMainWindow, QGridLayout, QVBoxLayout, QHBoxLayout, QWidget,
                             QLabel, QListWidget, QPushButton, QComboBox, QLineEdit,
                             QRadioButton, QGroupBox, QTableView, QAbstractItemView, QTextEdit, QFormLayout)


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exame 17-11-2025 grupo B")
        self.setGeometry(100, 100, 400, 400)
        self.widgetCentral = QWidget()
        self.setCentralWidget(self.widgetCentral)

        self.layoutPrincipal = QVBoxLayout(self.widgetCentral)

        


        gpbCliente = QGroupBox("Cliente")

        self.layoutPrincipal.addWidget(gpbCliente)



        lblNumeroCliente = QLabel("Número Cliente")
        lblNomeCliente = QLabel("Nome")
        lblApelidosCliente = QLabel("Apelidos")
        lblDirección = QLabel("Dirección")
        lblCidade = QLabel("Cidade")
        lblProvinciaEstado = QLabel("Provincia")








        txtNumeroCliente = QLineEdit()
        txtNomeCliente = QLineEdit()
        txtApelidosCliente = QLineEdit()
        txtDireccion = QLineEdit()
        txtCidade = QLineEdit()
        cmbProvincia = QComboBox()

        self.txeClientes = QTextEdit()

        btnEngadir = QPushButton("Engadir")
        btnEditar = QPushButton("Editar")
        btnBorrar = QPushButton("Borrar")

        btnAceptar = QPushButton("Aceptar")
        btnCancelar = QPushButton("Cancelar")


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    fiestra.show()

    sys.exit(aplicacion.exec())
