import sys

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint, choices
from template import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        try:
            center = QPoint(randint(70, 630), randint(70, 530))
            r = randint(15, 70)
            color = QColor(*choices(range(256), k=3))
            self.circle_lst.append((center, r, color))
            for center, r, color in self.circle_lst:
                qp.setBrush(color)
                qp.drawEllipse(center, r, r)
            self.draw_flag = False
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
