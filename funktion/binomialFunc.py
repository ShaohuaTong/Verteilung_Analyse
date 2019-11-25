# -*-coding:utf-8-*-
import math

from PyQt5.QtWidgets import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy import stats
from scipy.special import comb, perm
from uiView.binomialDialog import BinomialDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

matplotlib.use("Qt5Agg")  # 声明使用QT5


class BinomialShow(BinomialDialog, QDialog):
    def __init__(self):
        super(BinomialDialog, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("binomial_distribution")
        self.setMinimumSize(0, 0)

        self.figure = plt.figure(num=1, figsize=(15, 8), facecolor='#FFFFFF')
        self.canves = FigureCanvas(self.figure)

        # plt.connect('motion_notify_event', self.mouse_move)

        QGridLayout(self.groupBox).addWidget(self.canves)

        self.pushButton_drawing.clicked.connect(self.draw)
        self.pushButton_clear.clicked.connect(self.clear)
        self.pushButton_return.clicked.connect(self.clear)

    def clear(self):
        plt.clf()
        self.canves.draw()
        self.hidden()
        self.lineEdit_a.clear()
        self.lineEdit_b.clear()
        self.lineEdit_point.clear()
        self.label_area_result.clear()


    def draw(self):
        n = self.lineEdit_n.text()
        p = self.lineEdit_p.text()
        a = self.lineEdit_a.text()
        b = self.lineEdit_b.text()
        point = self.lineEdit_point.text()

        self.hidden()
        self.label_area_result.clear()

        if n != '' and p != '':
            n = int(n)
            p = float(p)

            if p != 0 and p != 1:
                plt.clf()
                x = np.arange(0, n + 1)
                y = stats.binom.pmf(x, n, p)

                if self.comboBox_style.currentText() == 'pdf':
                    self.show_pdf()
                    for i in range(len(x)):
                        plt.scatter(x[i], y[i], color='black', s=5)
                        plt.plot([x[i], x[i]], [y[i], 0], label='sin')

                    plt.xlabel('number')
                    plt.ylabel('probality')
                    plt.grid(b=True, which='major', axis='both', alpha=0.5, color='skyblue', linestyle='--',
                             linewidth=1)

                    self.draw_highest_point(n, p, y)
                    self.draw_area(x, y, n, p, a, b)
                    self.canves.draw()
                elif self.comboBox_style.currentText() == 'cdf':
                    self.show_cdf()
                    cy = np.cumsum(y * 1)
                    for i in range(len(x) - 1):
                        plt.scatter(x[i], cy[i], color='black', s=5)
                        plt.plot([x[i], x[i]], [cy[i], cy[i + 1]], label='sin')
                        plt.plot([x[i], x[i + 1]], [cy[i + 1], cy[i + 1]], label='cos')
                    plt.scatter(x[len(x) - 1], cy[len(x) - 1], color='black', s=5)
                    plt.grid(b=True, which='major', axis='both', alpha=0.5, color='skyblue', linestyle='--',
                             linewidth=2)
                    if point != '':
                        point = int(point)
                        if 0 <= point <= n:
                            self.label_area_result.setText('Probability is %.3f' % cy[point])
                        else:
                            self.label_area_result.setText('invalid point')
                    self.canves.draw()

    def draw_area(self, x, y, n, p, a, b):
        cy = np.cumsum(y * 1)
        if a == '-' or a == '+' or a == '.' or b == '-' or b == '+' or b == '.':
            self.label_area_result.setText('invalid a or b')
        elif self.comboBox_area.currentText() == 'x=a':
            a = float(a)
            if a - math.floor(a) != 0 or a > n or a < 0:
                self.label_area_result.setText('invalid a')
            else:
                if a == 0:
                    self.label_area_result.setText('Probability of the point is %.3f' % (cy[0]))
                else:
                    self.label_area_result.setText('Probability of the point is %.3f' % (cy[int(a)] - cy[int(a) - 1]))

        elif self.comboBox_area.currentText() == 'x<=a':
            a = float(a)
            if 0 <= a <= n:
                a = int(math.floor(a))
                xf = x[np.where((x >= 0) & (x <= a))]
                plt.fill_between(xf, self.func(xf), stats.binom.pmf(xf, n, p), color='blue', alpha=0.25)
                if a == n:
                    area = cy[n]
                else:
                    area = cy[a]
                self.label_area_result.setText('Probability sum is %.3f' % area)
            elif a < 0:
                self.label_area_result.setText('Probability sum is 0.000')
            elif a > n:
                self.draw_area(x, y, n, p, n, b)
        elif self.comboBox_area.currentText() == 'x>=b':
            b = float(b)
            b = int(math.ceil(b))
            if 0 <= b <= n:
                xf = x[np.where((x >= b) & (x <= n))]
                plt.fill_between(xf, self.func(xf), stats.binom.pmf(xf, n, p), color='blue', alpha=0.25)
                if b == 0:
                    area = 1
                else:
                    area = 1 - cy[b - 1]
                self.label_area_result.setText('Probability sum is %.3f' % area)
            elif b > n:
                self.label_area_result.setText('Probability sum is 0.000')
            elif b < 0:
                self.draw_area(x, y, n, p, a, 0)
        elif self.comboBox_area.currentText() == 'a<=x<=b':
            a, b = float(a), float(b)
            if a > b:
                self.label_area_result.setText('b should bigger than a')
            elif a < 0:
                if b < 0:
                    self.label_area_result.setText('Probability sum is 0.000')
                elif 0 <= b <= n:
                    self.draw_area(x, y, n, p, 0, b)
                elif b > n:
                    self.draw_area(x, y, n, p, 0, n)
            elif 0 <= a <= n:
                if b <= n:
                    a = int(math.ceil(a))
                    b = int(math.floor(b))
                    xf = x[np.where((x >= a) & (x <= b))]
                    plt.fill_between(xf, self.func(xf), stats.binom.pmf(xf, n, p), color='blue', alpha=0.25)
                    if a == 0:
                        area = cy[b] - 0
                    else:
                        area = cy[b] - cy[a - 1]
                    self.label_area_result.setText('Probability sum is %.3f' % area)
                elif b > n:
                    self.draw_area(x, y, n, p, a, n)
            elif a > n:
                self.label_area_result.setText('Probability sum is 0.000')

    def func(self, x):
        return 0 * x

    def draw_highest_point(self, n, p, y):
        k1 = (n + 1) * p
        k2 = (n + 1) * p - 1
        k3 = math.floor(k1)

        if k3 == k1:
            # vertex1 = comb(n, k1) * math.pow(p, k1) * math.pow(1 - p, n - k1)
            plt.text((k1 + k2) / 2, y[k3], '(%.2f or %.2f, %.3f)' % (k2, k1, y[k3]), color='mediumvioletred')
        else:
            plt.text(k3, y[k3], '(%.2f, %.3f)' % (k3, y[k3]), color='mediumvioletred')

    def hidden(self):
        self.label_a.setHidden(True)
        self.label_b.setHidden(True)
        self.lineEdit_a.setHidden(True)
        self.lineEdit_b.setHidden(True)
        self.label_area.setHidden(True)
        self.comboBox_area.setHidden(True)
        self.label_point.setHidden(True)
        self.lineEdit_point.setHidden(True)

    def show_pdf(self):
        self.label_a.setHidden(False)
        self.label_b.setHidden(False)
        self.lineEdit_a.setHidden(False)
        self.lineEdit_b.setHidden(False)
        self.label_area.setHidden(False)
        self.comboBox_area.setHidden(False)

    def show_cdf(self):
        self.label_point.setHidden(False)
        self.lineEdit_point.setHidden(False)

# y1, y2 = y[int(math.floor(a / 2))], y[int(math.ceil(a / 2))]
# if y1 == y2:
#     y_left = y[int(a / 2 - 1)]
#     location_y = y1 if y1 <= y_left else y_left
#     plt.annotate('Probality of area is %.3f' % area, xy=(a / 2 - 0.5, location_y), xytext=(n * 0.6, y[k3]),
#                  # 添加标注，参数：注释文本、指向点、文字位置、箭头属性
#                  arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2')
#                  )
