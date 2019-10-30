#-*-coding:utf-8-*-
import math

from PyQt5.QtWidgets import *
import numpy as np
from scipy import stats
from scipy.special import comb, perm
from uiView.binomialDialog import binomialDialog

import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

class binomialShow(binomialDialog, QDialog):
    def __init__(self):
        super(binomialDialog, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("binomial_distribution")
        self.setMinimumSize(0,0)

        self.figure = plt.figure(num = 1, figsize=(15, 8),facecolor='#FFD7C4')
        self.canves = FigureCanvas(self.figure)

        # plt.connect('motion_notify_event', self.mouse_move)

        QGridLayout(self.groupBox).addWidget(self.canves)

        self.pushButton_drawing.clicked.connect(self.draw)
        self.pushButton_clear.clicked.connect(self.clear)

    def clear(self):
        plt.clf()
        self.canves.draw()

    def draw(self):
        n = self.lineEdit_n.text()
        p = self.lineEdit_p.text()
        a = self.lineEdit_a.text()
        b = self.lineEdit_b.text()

        if n != '' and p != '':
            n = float(n)
            p = float(p)
            x = np.arange(0, n)
            y = stats.binom.pmf(x, n, p)
            print(type(x))

            if self.comboBox_style.currentText() == 'pdf':
                plt.plot(x, y, 'ro-')
                plt.xlabel('number')
                plt.ylabel('probalility')
                plt.grid(b=True, which='major', axis='both', alpha=0.5, color='skyblue', linestyle='--', linewidth=1)

                k1 = (n + 1) * p
                k2 = (n + 1) * p - 1
                k3 = math.floor(k1)

                if k3 == k1:
                    vertex1 = comb(n, k1) * math.pow(p, k1) * math.pow(1 - p, n - k1)
                    plt.text((k1 + k2) / 2, vertex1, '(%.2f or %.2f, %.3f)' % (k2, k1, vertex1),
                             color='mediumvioletred')
                else:
                    vertex2 = comb(n, k3) * math.pow(p, k3) * math.pow(1 - p, n - k3)
                    print(vertex2)
                    plt.text(k3, vertex2, '(%.2f, %.3f)' % (k3, vertex2), color='mediumvioletred')

                if self.comboBox_area.currentText() == 'x<=a' and a != '':
                    a = float(a)
                    self.draw_area(x, n, p, a, 0, 0)
                elif self.comboBox_area.currentText() == 'a<=x<=b' and a != '' and b != '':
                    a = float(a)
                    b = float(b)
                    self.draw_area(x, n, p, a, b, 1)
                elif self.comboBox_area.currentText() == 'x>=b' and b != '':
                    b = float(b)
                    self.draw_area(x, n, p, 0, b, 2)

                self.canves.draw()
            elif self.comboBox.currentText() == 'cdf':
                CY = np.cumsum(y * 1)
                plt.plot(x, CY, 'ro-')
                plt.grid(b=True, which='major', axis='both', alpha=0.5, color='skyblue', linestyle='--', linewidth=2)
                self.canves.draw()

    def func(self, x):
        return 0 * x

    def draw_area(self, x, n, p, a, b, category):
        if(category == 0):          #x<=a
            xf = x[np.where((x >= 0) & (x <= a))]
            plt.fill_between(xf, self.func(xf), stats.binom.pmf(xf, n, p), color='blue', alpha=0.25)
        elif(category == 1):
            xf = x[np.where((x >= a) & (x <= b))]
            plt.fill_between(xf, self.func(xf), stats.binom.pmf(xf, n, p), color='blue', alpha=0.25)
        elif(category == 2):
            xf = x[np.where((x >= b) & (x <= n))]
            plt.fill_between(xf, self.func(xf), stats.binom.pmf(xf, n, p), color='blue', alpha=0.25)