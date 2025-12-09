import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow, QGridLayout, QVBoxLayout, QHBoxLayout, QWidget,
                             QLabel, QListWidget, QPushButton, QComboBox, QLineEdit,
                             QRadioButton, QGroupBox, QTableView, QAbstractItemView, QTabWidget, QCheckBox, QDial)


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exame 24-11-2025")

        layoutPrincipal = QVBoxLayout()

        # riego
        self.gbpRiego = QGroupBox()
        layoutRiego = QGridLayout()
        self.gbpRiego.setLayout(layoutRiego)
        # zoa
        # self.gbpZoa = QGroupBox()
        # layoutZoa = QHBoxLayout()
        # self.gbpZoa.setLayout(layoutZoa)

        lblZoaActivada = QLabel("Zoa activada")
        self.chkZoaActivada = QCheckBox()

        # layoutZoa.addWidget(lblZoaActivada)
        # layoutZoa.addWidget(self.chkZoaActivada)

        lblHoraComezoRego = QLabel("Hora de comezo de rego")

        self.txtHoraComezoRego = QLineEdit()

        self.lblDuracionRego = QLabel("Duración rego")

        self.dilDuracionRego = QDial()
        self.dilDuracionRego.setRange(0, 400)

        layoutRiego.addWidget(lblZoaActivada, 0, 0)
        layoutRiego.addWidget(self.chkZoaActivada, 0, 1)

        # layoutRiego.addWidget(self.gbpZoa, 0, 0, 1, 1)
        layoutRiego.addWidget(lblHoraComezoRego, 1, 0)
        layoutRiego.addWidget(self.txtHoraComezoRego, 1, 1)
        layoutRiego.addWidget(self.lblDuracionRego, 2, 0)
        layoutRiego.addWidget(self.dilDuracionRego, 2, 1)
        # opcions de riego
        self.rbtDiario = QRadioButton("Diario")

        self.rbtSemanal = QRadioButton("Semanal")

        self.chkAntixiada = QCheckBox("Antixiada")

        self.chkChuvia = QCheckBox("Chuvia")

        self.gpbOpcionsRiego = QGroupBox("Opcións")
        layoutOpcionsRiego = QVBoxLayout()
        self.gpbOpcionsRiego.setLayout(layoutOpcionsRiego)

        layoutOpcionsRiego.addWidget(self.rbtDiario)
        layoutOpcionsRiego.addWidget(self.rbtSemanal)
        layoutOpcionsRiego.addWidget(self.chkAntixiada)
        layoutOpcionsRiego.addWidget(self.chkChuvia)

        layoutOpcionsRiego.addStretch()
        layoutRiego.addWidget(self.gpbOpcionsRiego, 0, 3, 2, 1)

        # Dias
        self.gbpDias = QGroupBox("Días")
        layoutDias = QHBoxLayout()
        self.gbpDias.setLayout(layoutDias)

        self.chkLuns = QCheckBox("Luns")
        self.chkMartes = QCheckBox("Martes")
        self.chkMercores = QCheckBox("Mércores")
        self.chkXoves = QCheckBox("Xoves")
        self.chkVenres = QCheckBox("Venres")
        self.chkSabado = QCheckBox("Sábado")
        self.chkDomingo = QCheckBox("Domingo")

        layoutDias.addWidget(self.chkLuns)
        layoutDias.addWidget(self.chkMartes)
        layoutDias.addWidget(self.chkMercores)
        layoutDias.addWidget(self.chkXoves)
        layoutDias.addWidget(self.chkVenres)
        layoutDias.addWidget(self.chkSabado)
        layoutDias.addWidget(self.chkDomingo)

        layoutPrincipal.addWidget(self.gbpRiego)
        layoutPrincipal.addWidget(self.gbpDias)

        # Aceptar

        self.btnAceptar = QPushButton("Aceptar")
        layoutPrincipal.addWidget(self.btnAceptar)

        self.widgetPrincipal = QWidget()
        self.setCentralWidget(self.widgetPrincipal)
        self.widgetPrincipal.setLayout(layoutPrincipal)

        # Controles

        self.dilDuracionRego.valueChanged.connect(self.duracionRego)
        self.chkZoaActivada.checkStateChanged.connect(self.zoaActivadaMetodo)

        self.rbtDiario.toggled.connect(self.diasDeRego)
        self.rbtSemanal.toggled.connect(self.semanaDeRego)

    def duracionRego(self):
        self.lblDuracionRego.setText(f"Dúracion rego:{self.dilDuracionRego.value()}min ")

    def zoaActivadaMetodo(self):
        valor = self.chkZoaActivada.isChecked()
        if valor:
            self.chkZoaActivada.setEnabled(True)
            self.gbpRiego.setDisabled(True)
            self.gbpDias.setDisabled(True)
            return
        else:
            self.gbpRiego.setDisabled(True)

            self.gbpRiego.setDisabled(False)
            self.gbpDias.setDisabled(False)

    def diasDeRego(self):
        if self.rbtDiario.isChecked:
            self.gbpDias.setEnabled(True)

    def semanaDeRego(self):
        if self.rbtSemanal.isChecked:
            self.gbpDias.setDisabled(True)


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    fiestra.show()
    sys.exit(aplicacion.exec())
