"""
Docstring for gui
"""

import sys
from PyQt6 import QtWidgets
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPainter, QBrush, QPixmap, QMouseEvent


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GUI")
        self.scale = 15
        self.grid = [[0 for _ in range(28)] for _ in range(28)]
        self.paint = 1
        self.setFixedSize(QSize(28 * self.scale, 28 * self.scale))
        self.label = QtWidgets.QLabel()
        canvas = QPixmap(28 * self.scale, 28 * self.scale)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, a0: QMouseEvent) -> None:
        """Draw on canvas when mouse is moved while clicking"""

        canvas = self.label.pixmap()
        painter = QPainter(canvas)
        if a0.buttons() == Qt.MouseButton.LeftButton:
            painter.setBrush(QBrush(Qt.BrushStyle.SolidPattern))
            painter.setPen(Qt.GlobalColor.black)
            painter.setBrush(Qt.GlobalColor.black)
            self.paint = 1
        else:
            painter.setBrush(QBrush(Qt.BrushStyle.SolidPattern))
            painter.setPen(Qt.GlobalColor.white)
            painter.setBrush(Qt.GlobalColor.white)
            self.paint = 0

        x = int(a0.position().x())
        y = int(a0.position().y())
        smallx = int(x / self.scale)
        smally = int(y / self.scale)
        painter.drawRect(
            smallx * self.scale, smally * self.scale, self.scale - 1, self.scale - 1
        )
        if smallx in range(0, 28) and smally in range(0, 28):
            self.grid[smallx][smally] = self.paint
        painter.end()
        self.label.setPixmap(canvas)


app = QtWidgets.QApplication(sys.argv)
window = Window()
window.show()
app.exec()
