
import sys
from PyQt5.QtWidgets import (QApplication, QMessageBox, QFrame, QVBoxLayout, QToolBar, QTextEdit,
                             QToolButton, QScrollArea)
from PyQt5 import QtGui
import copydata

class App(QFrame):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('MultiClipBoard')
        self.setBaseSize(1000, 540)
        self.setWindowIcon(QtGui.QIcon('mainlogo.png'))

        self.createApp()
        self.setTextToWidg()

        self.show()

    def createApp(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        toolbar = QToolBar()
        layout.addWidget(toolbar)

        refresh = QToolButton()
        refresh.setText('Refresh')
        toolbar.addWidget(refresh)
        refresh.clicked.connect(self.setTextToWidg)

        # delete all data in file
        deleteall = QToolButton()
        deleteall.setText('Delete all')
        toolbar.addWidget(deleteall)
        deleteall.clicked.connect(self.deleteAll)

        # about
        aboutbutton = QToolButton()
        aboutbutton.setText('About')
        toolbar.addWidget(aboutbutton)
        aboutbutton.clicked.connect(self.aboutAction)

        # copydata.fun()
        copydata.readData()
        copydata.startthread()

        self.scrollarea = QScrollArea()
        self.scrollarea.setLayout(QVBoxLayout())
        layout.addWidget(self.scrollarea)

        self.textedit = QTextEdit()
        self.textedit.setMinimumSize(600, 400)
        self.scrollarea.setWidget(self.textedit)

    def aboutAction(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle('About')
        msg.setText('MultiClipBoard \nVersion 18.1 \nDeveloped by Abhishek')
        msg.setWindowIcon(QtGui.QIcon('mainlogo.png'))
        msg.exec_()

    def deleteAll(self):
        copydata.deletedata()
        self.textedit.setPlainText('')

    def setTextToWidg(self):
        data = copydata.readData()
        self.textedit.setPlainText(data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()

    sys.exit(app.exec_())