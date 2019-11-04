#-*-coding:utf-8-*-
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
        self.setMinimumSize(0,0)

        self.figure = plt.figure(num = 1, figsize=(15, 8),facecolor='#FFD7C4')
        self.canves = FigureCanvas(self.figure)

        # plt.connect('motion_notify_event', self.mouse_move)

        QGridLayout(self.groupBox).addWidget(self.canves)

        self.pushButton_drawing.clicked.connect(self.draw)
        self.pushButton_clear.clicked.connect(self.clear)

    # def mouse_move(self, event):
    #     x, y = event.xdata, event.ydata
    #     self.label_mouseX.setText("X: %.2f" % 1.233)
    #     self.label_mouseY.setText("Y: %.2f" % 2.444)
    #     print(x, y)

    def clear(self):
        plt.clf()
        self.canves.draw()

    def draw(self):
        μ = float(self.lineEdit.text())
        σσ = float(self.lineEdit_2.text())
        X = np.arange(μ-5, μ+5, 0.01)
        Y = stats.norm.pdf(X, μ, math.sqrt(σσ))


        if self.comboBox.currentText() == 'pdf':
            plt.plot(X, Y, 'ro-')
            plt.xlabel('Durchschnittswert')
            plt.ylabel('probalility')
            plt.grid(b=True, which='major', axis='both', alpha=0.5, color='skyblue', linestyle='--', linewidth=1)

            vertex1= math.sqrt(2 * math.pi * σσ)
            plt.text( μ, 1/vertex1, '(%.2f, %.3f)' % (μ, 1/vertex1), color='mediumvioletred')


            self.canves.draw()
        elif self.comboBox.currentText() == 'cdf':
            CY = np.cumsum(Y * 1)
            plt.plot(X, CY, 'ro-')
            plt.grid(b=True, which='major', axis='both', alpha=0.5, color='skyblue', linestyle='--', linewidth=2)
            self.canves.draw()