from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def Main_window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setGeometry(540,810, 300,300)
    win.setWindowTitle("learning qt")
    
    label = QtWidgets.QLabel(win)
    label.setText("first test app")
    label.move(50,50)
    
    win.show()
    sys.exit(app.exec_())

Main_window()