from xml.etree.ElementTree import QName

import PyQt6.QtWidgets as qtw;
import PyQt6.QtCore as qtc;
import sys;


class ExemploListasIntercambiables(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo con QListWidget")
        maia = qtw.QGridLayout()
        lblFollasVisibles = qtw.QLabel("Follas visibles")
        lblFollasocultas = qtw.QLabel("Follas ocultas")
        btnMostrar = qtw.QPushButton("<<Mostrar")
        btnOcultar = qtw.QPushButton("Ocultar>>")
        btnPechar = qtw.QPushButton("Pechar")
        lstOcultos = qtw.QLabel
