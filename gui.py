"""
Docstring for gui
"""

import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(280, 280)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.centralWidget()
        self.draw_something()

    def draw_something(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        painter.drawLine(10, 10, 10, 0)
        painter.end()
        self.label.setPixmap(canvas)


app = QtWidgets.QApplication(sys.argv)
window = Window()
window.show()
app.exec()
