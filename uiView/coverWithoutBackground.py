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
        Form.resize(795, 728)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(120, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
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
        self.pushButton_binomail.setMinimumSize(QtCore.QSize(350, 40))
        self.pushButton_binomail.setMaximumSize(QtCore.QSize(350, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_binomail.setFont(font)
        self.pushButton_binomail.setObjectName("pushButton_binomail")
        self.horizontalLayout.addWidget(self.pushButton_binomail)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
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
        self.pushButton_normal.setMinimumSize(QtCore.QSize(350, 40))
        self.pushButton_normal.setMaximumSize(QtCore.QSize(350, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_normal.setFont(font)
        self.pushButton_normal.setObjectName("pushButton_normal")
        self.horizontalLayout_2.addWidget(self.pushButton_normal)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setMaximumSize(QtCore.QSize(60, 60))
        self.pushButton.setStyleSheet("QPushButton#pushButton {\n"
"    color: white;\n"
"    font: bold 10pt;\n"
"    border:none;\n"
"    min-height: 60px;\n"
"    min-width: 60px;\n"
"    border-image:url(Icon.png) -60px 0px no-repeat;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"    color: lightgray;\n"
"    border-image:url(Icon.png) 0px 0px no-repeat;;\n"
"}\n"
"QPushButton#pushButton:pressed {\n"
"    color: lightgray;\n"
"    border-image:url(Icon.png) -120px 0px no-repeat;;\n"
"    padding-top: -15px;\n"
"    padding-bottom: -17px;\n"
"}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setMinimumSize(QtCore.QSize(350, 40))
        self.pushButton_4.setMaximumSize(QtCore.QSize(350, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 4, 2, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(174, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 7, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(209, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 7, 3, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(133, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 1, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem13, 0, 1, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem14, 2, 6, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem15, 4, 1, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem16, 2, 7, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(71, 125, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem17, 2, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
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
        spacerItem18 = QtWidgets.QSpacerItem(492, 68, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.SpanningRole, spacerItem18)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.LabelRole, spacerItem19)
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
        self.gridLayout.addLayout(self.formLayout, 1, 1, 2, 4)
        spacerItem20 = QtWidgets.QSpacerItem(101, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem20, 5, 6, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem21, 7, 7, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem22, 5, 5, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(20, 68, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem23, 8, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel#label_3{\n"
"color:rgb(220, 220, 220)\n"
"\n"
"}")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_7 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel#label_7{\n"
"color:rgb(220, 220, 220)\n"
"\n"
"}")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.gridLayout.addLayout(self.verticalLayout_2, 7, 6, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem24, 3, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        load_style(self.pushButton_normal)
        button_style(self.pushButton_normal, "Lavender")
        load_style(self.pushButton_binomail)
        button_style(self.pushButton_binomail, "Aqua")
        load_style(self.pushButton_4)
        button_style(self.pushButton_4, "MediumGray")
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_binomail.setText(_translate("Form", "Binomial distribution"))
        self.pushButton_normal.setText(_translate("Form", "Normal distribution"))
        self.pushButton_4.setText(_translate("Form", "hypergeometric distribution"))
        self.label_2.setText(_translate("Form", "Welcome to distribution analysis software"))
        self.label_6.setText(_translate("Form", "Please choose the form of distribution"))
        self.label_3.setText(_translate("Form", "Yukun Chen"))
        self.label_7.setText(_translate("Form", "Shaohua Tong"))

