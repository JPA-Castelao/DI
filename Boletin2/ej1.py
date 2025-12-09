import sys
from PyQt6.QtWidgets import *


class ventana2(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Elemento 2 do Layout")
        self.setMinimumSize(500, 300)

        caixaV = QVBoxLayout()

        stackedLayout = QStackedLayout()

        self.lblEtiqueta = QLabel("Etiqueta da ventana 2")
        self.lblEtiqueta.setMinimumSize(100, 200)

        btnVentana2 = QPushButton("Cambiar de ventana")
        btnVentana2.clicked.connect(self.on_button_clicked)

        caixaV.addWidget(self.lblEtiqueta)
        caixaV.addWidget(btnVentana2)

        container = QWidget();
        container.setLayout(caixaV)

        self.setCentralWidget(container)

        self.showNormal()

    # def set_other_window(self, other_window):
    #     self.otra_ventana = other_window
    #
    # def on_button_clicked(self):
    #     self.hide()
    #     if hasattr(self, 'otra_ventana'):
    #         self.otra_ventana.show()
    def on_button_clicked(self):
        self.hide()


class ventana1(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Elemento 1 do Layout")
        self.setMinimumSize(500, 300)

        caixaV = QVBoxLayout()
        caixa2= QVBoxLayout()

        



        self.lblEtiqueta = QLabel("Etiqueta da ventana 1")
        self.lblEtiqueta.setMinimumSize(100, 200)

        btnVentana1 = QPushButton("Cambiar de ventana")

        btnVentana1.clicked.connect(self.on_button_clicked)

        caixaV.addWidget(self.lblEtiqueta)
        caixaV.addWidget(btnVentana1)

        container = QWidget();
        container.setLayout(caixaV)











        self.setCentralWidget(container)

        self.showNormal()

    # def set_other_window(self, other_window):
    #     self.otra_ventana = other_window
    #
    # def on_button_clicked(self):
    #     self.hide()
    #     if hasattr(self, 'otra_ventana'):
    #         self.otra_ventana.show()
    def on_button_clicked(self):

        self.hide()


if __name__ == '__main__':
    application = QApplication(sys.argv)
    fiestra = ventana1()
    fiestra2 = ventana2()
    fiestra.show()

    application.exec()
