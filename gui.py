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
        self.setFixedSize(QSize(280, 280))
        self.label = QtWidgets.QLabel()
        canvas = QPixmap(280, 280)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, a0: QMouseEvent) -> None:
        """Draw on canvas when mouse is moved while clicking"""
        canvas = self.label.pixmap()
        painter = QPainter(canvas)
        print(a0.buttons())
        if a0.buttons() == Qt.MouseButton.LeftButton:
            painter.setBrush(QBrush(Qt.BrushStyle.SolidPattern))
            painter.setPen(Qt.GlobalColor.black)
            painter.setBrush(Qt.GlobalColor.black)
        else:

            painter.setBrush(QBrush(Qt.BrushStyle.SolidPattern))
            painter.setPen(Qt.GlobalColor.white)
            painter.setBrush(Qt.GlobalColor.white)

        x = int(a0.position().x())
        y = int(a0.position().y())
        painter.drawEllipse(x - 2, y - 2, 4, 4)
        painter.end()
        self.label.setPixmap(canvas)


app = QtWidgets.QApplication(sys.argv)
window = Window()
window.show()
app.exec()
