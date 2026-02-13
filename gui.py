"""
Docstring for gui
"""

import sys
from PyQt6 import QtWidgets
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPainter, QBrush, QPixmap, QMouseEvent
import model


class Window(QtWidgets.QMainWindow):
    """
    Qt MainWindow child that draws when clicked
    """

    def __init__(self):
        super().__init__()

        self.scale = 15
        self.grid = [[0 for _ in range(28)] for _ in range(28)]
        self.paint = 0
        self.trained_model = model.train_mnist()

        self.setWindowTitle("GUI")
        self.setFixedSize(QSize(28 * self.scale, 28 * self.scale))
        self.label = QtWidgets.QLabel()
        canvas = QPixmap(28 * self.scale, 28 * self.scale)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, a0: QMouseEvent) -> None:
        """
        Qt built in method that triggers when mouse is clicked and moved

        :param a0: Qt mouse event passed when window is clicked
        :type a0: QMouseEvent
        """
        if self.draw(a0):

            image = model.flatten_data([self.grid])
            prediction = self.trained_model.predict(image)
            print(prediction)

    def draw(self, a0: QMouseEvent) -> bool:
        """
        Draw on canvas when mouse is moved while clicking

        :return: Whether the grid changed or not
        :rtype: bool
        """

        painted = False
        canvas = self.label.pixmap()
        painter = QPainter(canvas)
        # Brush selection based on button clicked
        if a0.buttons() == Qt.MouseButton.LeftButton:
            painter.setBrush(QBrush(Qt.BrushStyle.SolidPattern))
            painter.setPen(Qt.GlobalColor.black)
            painter.setBrush(Qt.GlobalColor.black)
            self.paint = 255
        else:
            painter.setBrush(QBrush(Qt.BrushStyle.SolidPattern))
            painter.setPen(Qt.GlobalColor.white)
            painter.setBrush(Qt.GlobalColor.white)
            self.paint = 0

        x = int(a0.position().x())
        y = int(a0.position().y())
        smallx = int(x / self.scale)  # convert to 28x28 grid coords
        smally = int(y / self.scale)
        painter.drawRect(
            smallx * self.scale, smally * self.scale, self.scale - 1, self.scale - 1
        )
        if smallx in range(0, 28) and smally in range(0, 28):
            if self.grid[smallx][smally] != self.paint:
                self.grid[smallx][smally] = self.paint
                painted = True
        painter.end()
        self.label.setPixmap(canvas)
        return painted


def start_window() -> None:
    """
    Starts UI
    """
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()


if __name__ == "__main__":
    start_window()
