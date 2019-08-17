#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/16 17:06
# @Author  : Brown
# @FileName: login.py
# @Software: PyCharm

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPixmap, QPainter
from test import Ui_Form
import numpy as np
import sys


class mywindow(QWidget):
    def init(self):
        super(mywindow, self).init()
        self.setupUi(self)
        self.num = np.random.randint(10)
        self.setWindowTitle('    行人检测')
        print(self.num)

    def paintEvent(self, event):  # set background_img
        painter = QPainter(self)
        # painter.drawRect(self.rect())
        pixmap = QPixmap("i.jpg")  # 换成自己的图片的相对路径
        painter.drawPixmap(self.rect(), pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = mywindow()
    w.paintEngine()
    w.show()
    sys.exit(app.exec_())
