from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton, QHBoxLayout, QMessageBox, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
import sys


class Main(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.interfaceMain()

    def interfaceMain(self):
        self.mainLay = QGridLayout()
        showBtn = QPushButton("&Show", self)
        addBtn = QPushButton("&Add \u2795", self)
        searchBtn = QPushButton('&Search \U0001F50D', self)
        # view = []
        # kontakty = [{
        #         'name':'Janusz', # database['name'],
        #         'surname': 'Nowak', # database['surname'],
        #         'number': 198765432# database['number']
        #         }
        #     ]
        # kontakty.append({'name':'Wojciech',
        #                 'surname':'Kowalski',
        #                 'number': 987654321
        # })
        # for x in range(0, len(kontakty)):
        #     self.view[x] = QLabel(kontakty[x], self)
        #     uklad.addWidget(self.view[x],x,0)

        showBtn.clicked.connect(self.showCont)
        self.mainLay.addWidget(showBtn, 0, 0,1,0)
        self.mainLay.addWidget(addBtn, 1, 0,1,0)
        self.mainLay.addWidget(searchBtn, 2, 0,1,0)
        self.setLayout(self.mainLay)
        self.setFixedWidth(400)
        self.setFixedHeight(500)
        self.show()

    def showCont(self):
        showLay = QHBoxLayout()
        showBtn = QLabel("&Show", self)
        addBtn = QLabel("&Add \u2795", self)
        searchBtn = QLabel('&Search \U0001F50D', self)
        showLay.addWidget(showBtn, 0, 0)
        showLay.addWidget(addBtn, 1, 0)
        showLay.addWidget(searchBtn, 2, 0)

        self.layout().addLayout(showLay)
        self.layout().takeAt(self.showCont)







if __name__ == '__main__':
    app = QApplication(sys.argv)
    okno = Main()
    sys.exit(app.exec_())
