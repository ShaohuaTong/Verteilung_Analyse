import sys
import os
from PyQt5.QtWidgets import QApplication
from funktion.coverFun import CircleLineWindow
from funktion.binomialFunc import binomialShow
from funktion.normalFunc import normalShow
import warnings
import matplotlib.cbook


if __name__ == '__main__':
    # os.system('cd %s' % os.path.abspath('.'))
    #
    # print(os.path.dirname(sys.executable))
    # print("\n")
    # print(os.path.dirname(os.path.abspath(__file__)))
    # print("\n")
    # print(os.path.dirname(__file__))

    app = QApplication(sys.argv)
    cover = CircleLineWindow()
    binomial = binomialShow()
    normal = normalShow()

    cover.resize(900, 800)

    cover.pushButton_2.clicked.connect(cover.hide)
    cover.pushButton_2.clicked.connect(binomial.show)
    cover.pushButton_binomail.clicked.connect(cover.hide)
    cover.pushButton_binomail.clicked.connect(binomial.show)
    cover.pushButton_normal.clicked.connect(cover.hide)
    cover.pushButton_normal.clicked.connect(normal.show)
    binomial.pushButton_return.clicked.connect(cover.show)
    binomial.pushButton_return.clicked.connect(binomial.hide)
    normal.pushButton_return.clicked.connect(cover.show)
    normal.pushButton_return.clicked.connect(normal.hide)

    cover.show()
    warnings.filterwarnings("ignore", category=matplotlib.cbook.mplDeprecation)

    sys.exit(app.exec_())