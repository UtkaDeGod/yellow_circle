import sys

from PyQt5 import uic
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint as rdt


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('template.ui', self)
        self.setWindowTitle('Рисование')
        self.draw_flag = False
        self.circle_lst = []
        self.btn.clicked.connect(self.set_flag)

    def set_flag(self):
        self.draw_flag = True
        self.repaint()

    def paintEvent(self, event):
        if self.draw_flag:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        center = QPoint(rdt(70, 630), rdt(70, 530))
        r = rdt(15, 70)
        qp.setBrush(QColor('yellow'))
        self.circle_lst.append((center, r))
        for center, r in self.circle_lst:
            qp.drawEllipse(center, r, r)
        self.draw_flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
