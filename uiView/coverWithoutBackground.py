# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'coverWithoutBackground.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from uiView.utils import button_style, load_style


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(797, 702)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(120, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 0, 2, 2)
        spacerItem1 = QtWidgets.QSpacerItem(100, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 8, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(294, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 4, 7, 1, 5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_3.setMaximumSize(QtCore.QSize(60, 60))
        self.pushButton_3.setStyleSheet("QPushButton#pushButton_3 {\n"
"    color: white;\n"
"    font: bold 10pt;\n"
"    border:none;\n"
"    min-height: 60px;\n"
"    min-width: 60px;\n"
"    border-image:url(Icon.png) -60px 0px no-repeat;\n"
"}\n"
"QPushButton#pushButton_3:hover{\n"
"    color: lightgray;\n"
"    border-image:url(Icon.png) 0px 0px no-repeat;;\n"
"}\n"
"QPushButton#pushButton_3:pressed {\n"
"    color: lightgray;\n"
"    border-image:url(Icon.png) -120px 0px no-repeat;;\n"
"    padding-top: -15px;\n"
"    padding-bottom: -17px;\n"
"}")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_normal = QtWidgets.QPushButton(Form)
        self.pushButton_normal.setMinimumSize(QtCore.QSize(0, 40))
        load_style(self.pushButton_normal)
        button_style(self.pushButton_normal, "Lavender")

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_normal.setFont(font)
        self.pushButton_normal.setObjectName("pushButton_normal")
        self.horizontalLayout_2.addWidget(self.pushButton_normal)
        self.gridLayout.addLayout(self.horizontalLayout_2, 7, 2, 2, 5)
        spacerItem3 = QtWidgets.QSpacerItem(47, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 11, 11, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(100, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 2, 3, 1, 3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 62, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 13, 10, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(76, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 1, 10, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(174, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 9, 0, 1, 3)
        spacerItem8 = QtWidgets.QSpacerItem(17, 345, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 5, 10, 3, 1)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label_3 = QtWidgets.QLabel(self.splitter)
        self.label_3.setStyleSheet("QLabel#label_3{\n"
"color:rgb(220, 220, 220)\n"
"\n"
"}")
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.splitter)
        self.label_7.setStyleSheet("QLabel#label_7{\n"
"color:rgb(220, 220, 220)\n"
"\n"
"}")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.splitter, 8, 9, 5, 3)
        spacerItem9 = QtWidgets.QSpacerItem(20, 68, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem9, 12, 4, 2, 2)
        spacerItem10 = QtWidgets.QSpacerItem(209, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 9, 6, 1, 3)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        spacerItem11 = QtWidgets.QSpacerItem(492, 68, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.SpanningRole, spacerItem11)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.LabelRole, spacerItem12)
        self.label_6 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel#label_6{\n"
"color:rgb(220, 220, 220)\n"
"\n"
"}")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_6)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel#label_2{\n"
"color:rgb(220, 220, 220)\n"
"\n"
"}")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_2)
        self.gridLayout.addLayout(self.formLayout, 1, 1, 1, 9)
        spacerItem13 = QtWidgets.QSpacerItem(65, 128, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem13, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_2.setMaximumSize(QtCore.QSize(60, 60))
        self.pushButton_2.setMouseTracking(True)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("QPushButton#pushButton_2 {\n"
"    color: white;\n"
"    font: bold 10pt;\n"
"    border:none;\n"
"    min-height: 60px;\n"
"    min-width: 60px;\n"
"    border-image:url(Icon.png) -60px 0px no-repeat;\n"
"}\n"
"QPushButton#pushButton_2:hover{\n"
"    color: lightgray;\n"
"    border-image:url(Icon.png) 0px 0px no-repeat;;\n"
"}\n"
"QPushButton#pushButton_2:pressed {\n"
"    color: lightgray;\n"
"    border-image:url(Icon.png) -120px 0px no-repeat;;\n"
"    padding-top: -15px;\n"
"    padding-bottom: -17px;\n"
"}")
        self.pushButton_2.setText("")
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_binomail = QtWidgets.QPushButton(Form)
        self.pushButton_binomail.setMinimumSize(QtCore.QSize(20, 40))
        load_style(self.pushButton_binomail)
        button_style(self.pushButton_binomail, "Aqua")

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_binomail.setFont(font)
        self.pushButton_binomail.setObjectName("pushButton_binomail")
        self.horizontalLayout.addWidget(self.pushButton_binomail)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 2, 3, 5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_normal.setText(_translate("Form", "Normal Verteilung"))
        self.label_3.setText(_translate("Form", "Yukun Chen"))
        self.label_7.setText(_translate("Form", "Shaohua Tong"))
        self.label_6.setText(_translate("Form", "Wählen Sie die Form der Verteilung bitte "))
        self.label_2.setText(_translate("Form", "Willkommen bei Verteilungsanalyse Software"))
        self.pushButton_binomail.setText(_translate("Form", "Binomial Verteilung"))

