
import sys
import os
if hasattr(sys, 'frozen'):os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtWidgets import QApplication
from funktion.coverFun import CircleLineWindow
from funktion.binomialFunc import BinomialShow
from funktion.normalFunc import NormalShow
from funktion.hypergeometricFunc import HypergeometricShow
import warnings
import matplotlib.cbook


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cover = CircleLineWindow()
    binomial = BinomialShow()
    normal = NormalShow()
    hypergeometric = HypergeometricShow()

    cover.resize(900, 800)

    cover.pushButton_2.clicked.connect(cover.hide)
    cover.pushButton_2.clicked.connect(binomial.show)
    cover.pushButton_binomail.clicked.connect(cover.hide)
    cover.pushButton_binomail.clicked.connect(binomial.show)



    cover.pushButton_3.clicked.connect(cover.hide)
    cover.pushButton_3.clicked.connect(normal.show)
    cover.pushButton_normal.clicked.connect(cover.hide)
    cover.pushButton_normal.clicked.connect(normal.show)

    cover.pushButton_4.clicked.connect(cover.hide)
    cover.pushButton_4.clicked.connect(hypergeometric.show)
    cover.pushButton.clicked.connect(cover.hide)
    cover.pushButton.clicked.connect(hypergeometric.show)


    binomial.pushButton_return.clicked.connect(cover.show)
    binomial.pushButton_return.clicked.connect(binomial.hide)
    normal.pushButton_return.clicked.connect(cover.show)
    normal.pushButton_return.clicked.connect(normal.hide)
    hypergeometric.pushButton_return.clicked.connect(cover.show)
    hypergeometric.pushButton_return.clicked.connect(hypergeometric.hide)

    cover.show()
    warnings.filterwarnings("ignore", category=matplotlib.cbook.mplDeprecation)

    sys.exit(app.exec_())