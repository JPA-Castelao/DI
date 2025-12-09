import sys
from wsgiref.util import application_uri

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget)


# class NosaPrimeiraFiestra(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Miña primeria ventana QT")
#         self.setMinimumSize(500, 300)
#
#         self.txtSaudo = QLineEdit()
#         self.lblEtiqueta = QLabel("Ola a todos")
#
#         fonte = self.lblEtiqueta.font()
#         fonte.setPointSize(30)
#         self.lblEtiqueta.setFont(fonte)
#
#         layout = QVBoxLayout()
#         layout.addWidget(self.lblEtiqueta)
#         layout.addWidget(self.txtSaudo)
#
#         container = QWidget()
#         container.setLayout(layout)
#
#         self.CentralWidget(container)
#
#         set.lblEtiqueta.setAlignment(Qt.lblEtiqueta.AlignHCenter | Qt.lblEtiqueta.AlignVCenter)
#         self.show()
#
#
# if __name__ == "__main__":
#     aplicacion = QApplication(sys.argv)
#     fiestra = NosaPrimeiraFiestra()
#     aplicacion.exec()

class NosaPrimeiraFiestra(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("A miña primeira fiestra QT")
        self.setMinimumSize(500, 300)

        caixaV = QVBoxLayout()

        self.lblEtiqueta = QLabel("A miña primeria etiqueta")
        self.lblEtiqueta.setText("Henlooo")
        self.lblEtiqueta.setMinimumSize(100, 100)

        self.txtSaudo = QLineEdit()
        # self.txtSaudo.placeholderText("Introdue o teu nome")
        self.txtSaudo.placeholderText()
        self.txtSaudo.setPlaceholderText("Introduce o nome do teu capybara")
        self.txtSaudo.returnPressed.connect(self.on_btnSaudo_clicked)

        btnSaudo = QPushButton("Saudo")
        btnSaudo.clicked.connect(self.on_btnSaudo_clicked)

        caixaV.addWidget(self.lblEtiqueta)
        caixaV.addWidget(self.txtSaudo)
        caixaV.addWidget(btnSaudo)

        container = QWidget();
        container.setLayout(caixaV)

        self.setCentralWidget(container)

        self.showNormal()

    def on_btnSaudo_clicked(self):
        nome = self.txtSaudo.text()
        nome = nome.strip()

        if len(nome) != 0:
            self.txtSaudo.clear()
            self.txtSaudo.setText("")
            self.lblEtiqueta.setText("Ola " + nome + " encantado de coñecerte")
        else:
            self.lblEtiqueta.setText("Introduce un nome")

class NosaPrimeiraFiestra(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("A miña primeira fiestra QT")
        self.setMinimumSize(500, 300)

        caixaV = QVBoxLayout()

        self.lblEtiqueta = QLabel("A miña primeria etiqueta")
        self.lblEtiqueta.setText("Henlooo")
        self.lblEtiqueta.setMinimumSize(100, 100)

        # self.txtSaudo = QLineEdit()
        # # self.txtSaudo.placeholderText("Introdue o teu nome")
        # self.txtSaudo.placeholderText()
        # self.txtSaudo.setPlaceholderText("Introduce o nome do teu capybara")
        # self.txtSaudo.returnPressed.connect(self.on_btnSaudo_clicked)

        btnSaudo = QPushButton("Outra fiestra")
        btnSaudo.clicked.connect(self.on_btnSaudo_clicked)
        #
        # caixaV.addWidget(self.lblEtiqueta)
        # caixaV.addWidget(self.txtSaudo)
        caixaV.addWidget(btnSaudo)

        container = QWidget();
        container.setLayout(caixaV)

        self.setCentralWidget(container)

        self.showNormal()

    def on_btnSaudo_clicked(self):
        nome = self.txtSaudo.text()
        nome = nome.strip()

        if len(nome) != 0:
            self.txtSaudo.clear()
            self.txtSaudo.setText("")
            self.lblEtiqueta.setText("Ola " + nome + " encantado de coñecerte")
        else:
            self.lblEtiqueta.setText("Introduce un nome")

if __name__ == "__main__":
    application = QApplication(sys.argv)
    fiestra = NosaPrimeiraFiestra()
    #  fiestra.show()

    application.exec()
