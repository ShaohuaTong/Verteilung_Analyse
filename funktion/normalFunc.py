# -*-coding:utf-8-*-
import math

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import numpy as np
from scipy import stats
from scipy.special import comb, perm

from uiView.normalDialog import normalDialog
from basisVerteilung.binomial_distribution import count, binomial

import matplotlib

matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt


class normalShow(normalDialog, QDialog):
    def __init__(self):
        super(normalDialog, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("normal_distribution")
        self.setMinimumSize(0, 0)

        self.figure = plt.figure(num=1, figsize=(15, 8), facecolor='#FFD7C4')
        self.canves = FigureCanvas(self.figure)

        # plt.connect('motion_notify_event', self.mouse_move)

        QGridLayout(self.groupBox).addWidget(self.canves)

        self.pushButton_drawing.clicked.connect(self.draw)
        self.pushButton_clear.clicked.connect(self.clear)
        self.pushButton_return.clicked.connect(self.clear)

    # def mouse_move(self, event):
    #     x, y = event.xdata, event.ydata
    #     self.label_mouseX.setText("X: %.2f" % 1.233)
    #     self.label_mouseY.setText("Y: %.2f" % 2.444)
    #     print(x, y)

    def clear(self):
        plt.clf()
        self.canves.draw()
        self.hidden()
        self.lineEdit_a.clear()
        self.lineEdit_b.clear()
        self.label_output.clear()

    def draw(self):
        self.label_output.clear();
        μ = self.lineEdit_n.text()
        σσ = self.lineEdit_p.text()
        a = self.lineEdit_a.text()
        b = self.lineEdit_b.text()
        x = self.lineEdit_x.text()


        if μ != '' and σσ != '' and σσ != '0':
            plt.clf()
            self.hidden()
            μ = float(μ)
            σσ = float(σσ)

            X = np.arange(μ - 5 - σσ, μ + 5 + σσ, 0.01)
            Y = stats.norm.pdf(X, μ, math.sqrt(σσ))

            if self.comboBox_style.currentText() == 'pdf':
                self.show_pdf()
                plt.plot(X, Y, 'ro-')
                plt.xlabel('Durchschnittswert')
                plt.grid(b=True, which='major', axis='both', alpha=0.5, color='skyblue', linestyle='--', linewidth=1)

                vertex1 = math.sqrt(2 * math.pi * σσ)
                plt.text(μ, 1 / vertex1, '(%.2f, %.3f)' % (μ, 1 / vertex1), color='mediumvioletred')

                self.draw_area(X, Y, μ, σσ, a, b)

                self.canves.draw()
            elif self.comboBox_style.currentText() == 'cdf':
                self.show_cdf()
                CY = np.cumsum(Y * 1)
                plt.plot(X, CY, 'ro-')
                plt.grid(b=True, which='major', axis='both', alpha=0.5, color='skyblue', linestyle='--', linewidth=2)
                self.draw_punkt(x, μ, σσ, Y)
                self.canves.draw()

    def func(self, x):
        return 0 * x

    def draw_punkt(self, x, μ, σσ, Y):
        if x != '':
            x = float(x)
            cy = np.cumsum(Y * 1)
            if x > μ - 5 - σσ and x <= μ + 5 + σσ:
                sum = cy[int((x - μ + σσ + 5) * 100) - 1]
                sum = sum / 100
                self.label_output.setText('Probality  %.2f' % sum)
            if x > μ + 5 + σσ:
                self.label_output.setText('Probality  1.00')
            if x <= μ - 5 - σσ:
                self.label_output.setText('Probality  0.00')

    def draw_area(self, X, Y, μ, σσ, a, b):
        cy = np.cumsum(Y * 1)

        if a == '-' or b == '-':
            self.label_output.setText('Ungültiger wert')

        elif self.comboBox_area.currentText() == 'x<=a' and a != '':
            a = float(a)

            if a > μ - 5 - σσ and a <= μ + 5 + σσ:
                xf = X[np.where((X >= μ - 5 - σσ) & (X <= a))]
                plt.fill_between(xf, self.func(xf), stats.norm.pdf(xf, μ, math.sqrt(σσ)), color='blue', alpha=0.25)
                area = cy[int((a - μ + σσ + 5) * 100) - 1]
                area = area / 100
                self.label_output.setText('Probality  %.2f' % area)

            if a > μ + 5 + σσ:
                xf = X[np.where((X >= μ - 5) & (X <= μ + 5))]
                plt.fill_between(xf, self.func(xf), stats.norm.pdf(xf, μ, math.sqrt(σσ)), color='blue', alpha=0.25)
                self.label_output.setText('Probality  1.00')

            if a <= μ - 5 - σσ:
                self.label_output.setText('Probality  0.00')

        elif self.comboBox_area.currentText() == 'a<=x<=b' and a != '' and b != '':
            a, b = float(a), float(b)
            if a >= μ - 5 - σσ and a <= b and b <= μ + 5 + σσ:
                xf = X[np.where((X >= a) & (X <= b))]
                plt.fill_between(xf, self.func(xf), stats.norm.pdf(xf, μ, math.sqrt(σσ)), color='blue', alpha=0.25)
                area = cy[int((b - μ + σσ + 5) * 100) - 1] - cy[int((a - μ + σσ + 5) * 100)]
                area = area / 100
                self.label_output.setText('Probality  %.2f' % area)

            if b <= μ - 5 - σσ and a <= b:
                self.label_output.setText('Probality  0.00')

            if a < μ - 5 - σσ and a <= b and μ - 5 - σσ <= b <= μ + 5 + σσ:
                xf = X[np.where((X >= μ - 5 - σσ) & (X <= b))]
                plt.fill_between(xf, self.func(xf), stats.norm.pdf(xf, μ, math.sqrt(σσ)), color='blue', alpha=0.25)
                area = cy[int((b - μ + σσ + 5) * 100) - 1]
                area = area / 100
                self.label_output.setText('Probality  %.2f' % area)

            if a < μ - 5 - σσ and a <= b and b > μ + 5 + σσ:
                xf = X[np.where((X >= μ - 5 - σσ) & (X <= μ + 5 + σσ))]
                plt.fill_between(xf, self.func(xf), stats.norm.pdf(xf, μ, math.sqrt(σσ)), color='blue', alpha=0.25)
                self.label_output.setText('Probality  1.00')

            if μ - 5 - σσ < a < μ + 5 + σσ and a <= b and b > μ + 5 + σσ:
                xf = X[np.where((X >= a) & (X <= μ + 5 + σσ))]
                plt.fill_between(xf, self.func(xf), stats.norm.pdf(xf, μ, math.sqrt(σσ)), color='blue', alpha=0.25)
                area = cy[int((a - μ + σσ + 5) * 100)]
                area = 1 - area / 100
                self.label_output.setText('Probality  %.2f' % area)

            if μ + 5 + σσ <= a <= b:
                self.label_output.setText('Probality  0.00')

            if a > b:
                self.label_output.setText('ungültig a,b')

        elif self.comboBox_area.currentText() == 'x>=b' and b != '':
            b = float(b)
            if μ - 5 - σσ < b < μ + 5 + σσ:
                xf = X[np.where((X >= b) & (X <= μ + 5 + σσ))]
                plt.fill_between(xf, self.func(xf), stats.norm.pdf(xf, μ, math.sqrt(σσ)), color='blue', alpha=0.25)
                area = cy[int((b - μ + σσ + 5) * 100)]
                area = 1 - area / 100
                self.label_output.setText('Probality  %.2f' % area)
            if b >= μ + 5 + σσ:
                self.label_output.setText('Probality  0.00')
            if b <= μ - 5 - σσ:
                xf = X[np.where((X >= μ - 5 - σσ) & (X <= μ + 5 + σσ))]
                plt.fill_between(xf, self.func(xf), stats.norm.pdf(xf, μ, math.sqrt(σσ)), color='blue', alpha=0.25)
                self.label_output.setText('Probality  1.00')

    def hidden(self):
        self.label_a.setHidden(True)
        self.label_b.setHidden(True)
        self.lineEdit_a.setHidden(True)
        self.lineEdit_b.setHidden(True)
        self.label_x.setHidden(True)
        self.lineEdit_x.setHidden(True)
        self.comboBox_area.setHidden(True)
        self.label_area.setHidden(True)

    def show_pdf(self):
        self.label_a.setHidden(False)
        self.label_b.setHidden(False)
        self.lineEdit_a.setHidden(False)
        self.lineEdit_b.setHidden(False)
        self.comboBox_area.setHidden(False)
        self.label_area.setHidden(False)

    def show_cdf(self):
        self.label_output.setHidden(False)
        self.label_x.setHidden(False)
        self.lineEdit_x.setHidden(False)
