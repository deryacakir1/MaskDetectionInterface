# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arayuz.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(321, 285)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.kameraAc = QtWidgets.QPushButton(self.centralwidget)
        self.kameraAc.setGeometry(QtCore.QRect(70, 130, 181, 71))
        self.kameraAc.setMaximumSize(QtCore.QSize(350, 250))
        self.kameraAc.setObjectName("kameraAc")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 321, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.kameraAc.setText(_translate("MainWindow", "Kamera"))

        #"Çıkış yapmak için 'Q' tuşuna basınız." yazısı için kod
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight)
        self.label.setGeometry(QtCore.QRect(45, 220, 200, 30))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">Çıkış yapmak için 'Q' tuşuna basınız.</span></p></body></html>"))

        #"BANDIRMA ONYEDİ EYLÜL ÜNİVERSİTESİ" yazısı için kod
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight)
        self.label.setGeometry(QtCore.QRect(25, 10, 260, 30))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#006aff;\"><b><font size=4>BANDIRMA ONYEDİ EYLÜL ÜNİVERSİTESİ</font></b></span></p></body></html>"))

        #"Tespit için "KAMERA" butonuna basınız." yazısı için kod
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight)
        self.label.setGeometry(QtCore.QRect(45, 80, 220, 30))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\"><b>Tespit için 'KAMERA' butonuna basınız.<b></span></p></body></html>"))





