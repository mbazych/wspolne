from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton, QHBoxLayout, QMessageBox, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
import sys


class Main(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.interface()
    def interface(self):
        uklad = QGridLayout()
        searchBtn = QPushButton("&Search", self)
        view = []
        kontakty = [{
                'name':'Janusz', # database['name'],
                'surname': 'Nowak', # database['surname'],
                'number': 198765432# database['number']
                }
            ]
        kontakty.append({'name':'Wojciech',
                        'surname':'Kowalski',
                        'number': 987654321
        })
        for x in range(0, len(kontakty)):
            self.view[x] = QLabel(kontakty[x], self)
            uklad.addWidget(self.view[x],x,0)
        uklad.addWidget(searchBtn, x+1, 0,1,1)
        self.setLayout(uklad)
        self.setFixedWidth(400)
        self.setFixedHeight(500)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    okno = Main()
    sys.exit(app.exec_())
