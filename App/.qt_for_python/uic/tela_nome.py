# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Projeto integrador\Aplicativo_zurica\App\tela_nome.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(434, 534)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.antl = QtWidgets.QPushButton(self.centralwidget)
        self.antl.setGeometry(QtCore.QRect(30, 390, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.antl.setFont(font)
        self.antl.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;")
        self.antl.setObjectName("antl")
        self.pt = QtWidgets.QPushButton(self.centralwidget)
        self.pt.setGeometry(QtCore.QRect(250, 390, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pt.setFont(font)
        self.pt.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;")
        self.pt.setObjectName("pt")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 150, 421, 61))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 20, 291, 121))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("e:\\Projeto integrador\\Aplicativo_zurica\\App\\logo.jpg"))
        self.label_3.setObjectName("label_3")
        self.nomel = QtWidgets.QLineEdit(self.centralwidget)
        self.nomel.setGeometry(QtCore.QRect(20, 240, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.nomel.setFont(font)
        self.nomel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:black;")
        self.nomel.setObjectName("nomel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionABRIR = QtWidgets.QAction(MainWindow)
        self.actionABRIR.setObjectName("actionABRIR")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.antl.setText(_translate("MainWindow", "Anterior"))
        self.pt.setText(_translate("MainWindow", "Proxima Tela"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Qual e o apelido da empresa?</span></p></body></html>"))
        self.actionABRIR.setText(_translate("MainWindow", "ABRIR"))
