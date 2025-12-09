import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel)
from PyQt6.QtCore import Qt


class colorBloc(QWidget):
    def __init__(self, color):
        super().__init__()
#para dar estilo al background
        self.setAttribute(Qt.WA_Stylebackground, True)
#poner la hoja de estilos para seleciionar color
        self.setStyleSheet(f"background-color:{color};margin:2px;")


