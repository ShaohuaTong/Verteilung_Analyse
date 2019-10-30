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

            if self.comboBox_style.currentText() == 'pdf':
                plt.plot(x, y, 'ro-')
                plt.xlabel('number')
                plt.ylabel('probality')
                plt.grid(b=True, which='major', axis='both', alpha=0.5, color='skyblue', linestyle='--', linewidth=1)

                self.draw_highest_point(n, p, y)
                self.draw_area(x, y, n, p, a, b)

                self.canves.draw()
            elif self.comboBox_style.currentText() == 'cdf':
                cy = np.cumsum(y * 1)
                plt.plot(x, cy, 'ro-')
                plt.grid(b=True, which='major', axis='both', alpha=0.5, color='skyblue', linestyle='--', linewidth=2)
                self.canves.draw()

    def func(self, x):
        return 0 * x

    def draw_highest_point(self, n , p, y):
        k1 = (n + 1) * p
        k2 = (n + 1) * p - 1
        k3 = math.floor(k1)

        if k3 == k1:
            # vertex1 = comb(n, k1) * math.pow(p, k1) * math.pow(1 - p, n - k1)
            plt.text((k1 + k2) / 2, y[k3], '(%.2f or %.2f, %.3f)' % (k2, k1, y[k3]), color='mediumvioletred')
        else:
            plt.text(k3, y[k3], '(%.2f, %.3f)' % (k3, y[k3]), color='mediumvioletred')

    def draw_area(self, x, y, n, p, a, b):
        cy = np.cumsum(y * 1)
        k1 = (n + 1) * p
        k3 = math.floor(k1)

        if self.comboBox_area.currentText() == 'x<=a' and a != '':
            a = int(a)
            xf = x[np.where((x >= 0) & (x <= a))]
            plt.fill_between(xf, self.func(xf), stats.binom.pmf(xf, n, p), color='blue', alpha=0.25)
            area = cy[a]
            plt.annotate('Probality is %.3f' % area, xy=(a / 2, y[k3] /2), xytext=(n * 0.6, y[k3]),  # 添加标注，参数：注释文本、指向点、文字位置、箭头属性
                         arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2')
                         )
        elif self.comboBox_area.currentText() == 'a<=x<=b' and a != '' and b != '':
            a = int(a)
            b = int(b)
            xf = x[np.where((x >= a) & (x <= b))]
            plt.fill_between(xf, self.func(xf), stats.binom.pmf(xf, n, p), color='blue', alpha=0.25)
            area = cy[b] - cy[a - 1]
            plt.annotate('Probality is %.3f' % area, xy=((a + b) / 2, y[k3] / 2), xytext=(n * 0.6, y[k3]),
                         # 添加标注，参数：注释文本、指向点、文字位置、箭头属性
                         arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2')
                         )
        elif self.comboBox_area.currentText() == 'x>=b' and b != '':
            b = int(b)
            xf = x[np.where((x >= b) & (x <= n))]
            plt.fill_between(xf, self.func(xf), stats.binom.pmf(xf, n, p), color='blue', alpha=0.25)
            area = 1 - cy[b - 1]
            plt.annotate('Probality is %.3f' % area, xy=((n + b) / 2, y[k3] / 2), xytext=(n * 0.6, y[k3]),
                         # 添加标注，参数：注释文本、指向点、文字位置、箭头属性
                         arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2')
                         )