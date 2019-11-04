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
        self.label_a.setHidden(True)
        self.label_b.setHidden(True)
        self.lineEdit_a.setHidden(True)
        self.lineEdit_a.clear()
        self.lineEdit_b.clear()
        self.lineEdit_b.setHidden(True)
        self.label_area.setHidden(True)
        self.comboBox_area.setHidden(True)

        plt.clf()
        self.canves.draw()

    def draw(self):
        n = self.lineEdit_n.text()
        p = self.lineEdit_p.text()
        a = self.lineEdit_a.text()
        b = self.lineEdit_b.text()

        if n != '' and p != '':
            plt.clf()
            self.label_a.setHidden(False)
            self.label_b.setHidden(False)
            self.lineEdit_a.setHidden(False)
            self.lineEdit_b.setHidden(False)
            self.label_area.setHidden(False)
            self.comboBox_area.setHidden(False)

            n = int(n)
            p = float(p)
            x = np.arange(0, n + 1)
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
            if a >= 0:
                xf = x[np.where((x >= 0) & (x <= a))]
                plt.fill_between(xf, self.func(xf), stats.binom.pmf(xf, n, p), color='blue', alpha=0.25)
                area = cy[a]
                y1, y2= y[int(math.floor(a / 2))], y[int(math.ceil(a / 2))]
                if y1 == y2:
                    y_left = y[int(a / 2 - 1)]
                    location_y = y1 if y1 <= y_left else y_left
                    plt.annotate('Probality of area is %.3f' % area, xy=(a / 2 - 0.5, location_y), xytext=(n * 0.6, y[k3]),
                             # 添加标注，参数：注释文本、指向点、文字位置、箭头属性
                             arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2')
                             )
                else:
                    location_y = y1 if y1 <= y2 else y2
                    plt.annotate('Probality of area is %.3f' % area, xy=(a / 2, location_y), xytext=(n * 0.6, y[k3]),
                             arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2')
                             )
        elif self.comboBox_area.currentText() == 'a<=x<=b' and a != '' and b != '':
            a, b = int(a), int(b)
            if a >= 0 and a <= b and b <= n:
                xf = x[np.where((x >= a) & (x <= b))]
                plt.fill_between(xf, self.func(xf), stats.binom.pmf(xf, n, p), color='blue', alpha=0.25)
                area = cy[b] - cy[a - 1]
                temp = y[9]
                print(temp)
                y1, y2= y[int(math.floor((a + b) / 2))], y[int(math.ceil((a + b) / 2))]
                if y1 == y2:
                    y_left = y[int((a + b) / 2 - 1)]
                    location_y = y1 if y1 <= y_left else y_left
                    plt.annotate('Probality of area is %.3f' % area, xy=((a + b) / 2 - 0.5, location_y), xytext=(n * 0.4, 0.25),
                                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2')
                                 )
                else:
                    location_y = y1 if y1 <= y2 else y2
                    plt.annotate('Probality of area is %.3f' % area, xy=((a + b) / 2, location_y), xytext=(n * 0.6, y[k3]),
                             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2')
                             )
        elif self.comboBox_area.currentText() == 'x>=b' and b != '':
            b = int(b)
            if b <= n:
                xf = x[np.where((x >= b) & (x <= n))]
                plt.fill_between(xf, self.func(xf), stats.binom.pmf(xf, n, p), color='blue', alpha=0.25)
                area = 1 - cy[b - 1]
                print(cy[b])
                y1, y2 = y[int(math.floor((n + b) / 2))], y[int(math.ceil((n + b) / 2))]
                if y1 == y2:
                    y_right = y[int((n + b) / 2 + 1)]
                    location_y = y1 if y1 <= y_right else y_right
                    plt.annotate('Probality of area is %.3f' % area, xy=((n + b) / 2 + 0.5, location_y), xytext=(n * 0.6, y[k3]),
                                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2')
                                 )
                else:
                    location_y = y1 if y1 <= y2 else y2
                    plt.annotate('Probality of area is %.3f' % area, xy=((n + b) / 2, location_y), xytext=(n * 0.6, y[k3]),
                             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2')
                             )

  # pDoublevalidator = QDoubleValidator(self)
  #       pDoublevalidator.setRange(-99999999, 99999999)
  #       pDoublevalidator.setNotation(QDoubleValidator.StandardNotation)
  #       pDoublevalidator.setDecimals(2)
  #       self.lineEdit_a.setValidator(QDoubleValidator)
  #       self.lineEdit_b.setValidator(QDoubleValidator)
  #       self.lineEdit_n.setValidator(QDoubleValidator)
  #       self.lineEdit_p.setValidator(QDoubleValidator)
  #
  #       self.label_a.setHidden(True)
  #       self.label_b.setHidden(True)
  #       self.lineEdit_a.setHidden(True)
  #       self.lineEdit_a.clear()
  #       self.lineEdit_b.clear()
  #       self.lineEdit_b.setHidden(True)
  #       self.label_area.setHidden(True)
  #       self.comboBox_area.setHidden(True)