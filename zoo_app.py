import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import functionality as c


class App(QMainWindow):
    conn = c.conn()

    def __init__(self):
        super().__init__()
        self.title = "Zoo n' shit"
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(20, 20)
        self.textbox1.resize(280,40)

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(20, 100)
        self.textbox2.resize(280,40)


        # Create a button in the window
        self.button = QPushButton('Login', self)
        self.button.move(20,80)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        username = self.textbox1.text()
        password = self.textbox2.text()

        QMessageBox.question(self, username, password, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
