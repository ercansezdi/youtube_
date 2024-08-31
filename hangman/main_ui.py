# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hak_sayi_frame = QtWidgets.QFrame(self.main_frame)
        self.hak_sayi_frame.setMinimumSize(QtCore.QSize(0, 50))
        self.hak_sayi_frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.hak_sayi_frame.setStyleSheet("#frame {\n"
"border: 1px solid #4CAF50; /* Yeşil kenarlık */\n"
"    border-radius: 5px; /* Kenarları yuvarlat */\n"
"}")
        self.hak_sayi_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hak_sayi_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hak_sayi_frame.setObjectName("hak_sayi_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.hak_sayi_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.hak_saiyisi_lable = QtWidgets.QLabel(self.hak_sayi_frame)
        self.hak_saiyisi_lable.setStyleSheet("QLabel {\n"
"    color: #333; /* Koyu gri yazı rengi */\n"
"    background-color: #f0f0f0; /* Hafif gri arka plan */\n"
"    padding: 10px; /* İç dolgu */\n"
"    font-size: 18px; /* Yazı boyutu */\n"
"    font-weight: bold; /* Kalın yazı */\n"
"    text-align: center; /* Yazıyı ortala */\n"
"}")
        self.hak_saiyisi_lable.setObjectName("hak_saiyisi_lable")
        self.horizontalLayout.addWidget(self.hak_saiyisi_lable, 0, QtCore.Qt.AlignHCenter)
        self.hak_sayisi = QtWidgets.QLabel(self.hak_sayi_frame)
        self.hak_sayisi.setStyleSheet("QLabel {\n"
"    color: #333; /* Koyu gri yazı rengi */\n"
"    background-color: #f0f0f0; /* Hafif gri arka plan */\n"
"    padding: 10px; /* İç dolgu */\n"
"    font-size: 18px; /* Yazı boyutu */\n"
"    font-weight: bold; /* Kalın yazı */\n"
"    text-align: center; /* Yazıyı ortala */\n"
"}")
        self.hak_sayisi.setObjectName("hak_sayisi")
        self.horizontalLayout.addWidget(self.hak_sayisi, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.hak_sayi_frame, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.tahminler_frame = QtWidgets.QFrame(self.main_frame)
        self.tahminler_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tahminler_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tahminler_frame.setObjectName("tahminler_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tahminler_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.tahminler_frame)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.dial = QtWidgets.QDial(self.tahminler_frame)
        self.dial.setObjectName("dial")
        self.horizontalLayout_2.addWidget(self.dial)
        self.label_3 = QtWidgets.QLabel(self.tahminler_frame)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 36pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.verticalLayout.addWidget(self.tahminler_frame, 0, QtCore.Qt.AlignHCenter)
        self.tahmin_frame = QtWidgets.QFrame(self.main_frame)
        self.tahmin_frame.setMinimumSize(QtCore.QSize(0, 50))
        self.tahmin_frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.tahmin_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tahmin_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tahmin_frame.setObjectName("tahmin_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tahmin_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tahmin_linedit = QtWidgets.QLineEdit(self.tahmin_frame)
        self.tahmin_linedit.setStyleSheet("QLineEdit {\n"
"    background-color: #f0f0f0; /* Hafif gri arka plan */\n"
"    color: #333; /* Koyu gri yazı rengi */\n"
"    border: 2px solid #4CAF50; /* Yeşil kenarlık */\n"
"    padding: 8px; /* İç dolgu */\n"
"    font-size: 16px; /* Yazı boyutu */\n"
"    border-radius: 5px; /* Kenarları yuvarlat */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #45a049; /* Odaklanıldığında daha koyu yeşil kenarlık */\n"
"    background-color: #e0e0e0; /* Daha koyu gri arka plan */\n"
"}")
        self.tahmin_linedit.setObjectName("tahmin_linedit")
        self.horizontalLayout_3.addWidget(self.tahmin_linedit)
        self.tahmin_butonu = QtWidgets.QPushButton(self.tahmin_frame)
        self.tahmin_butonu.setStyleSheet("QPushButton {\n"
"    background-color: #4CAF50; /* Yeşil arka plan rengi */\n"
"    color: white; /* Beyaz yazı rengi */\n"
"    border: none; /* Kenarlık yok */\n"
"    padding: 10px 20px; /* İç dolgu */\n"
"    text-align: center; /* Yazıyı ortala */\n"
"    font-size: 16px; /* Yazı boyutu */\n"
"    border-radius: 5px; /* Kenarları yuvarlat */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45a049; /* Hover durumunda daha koyu yeşil */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #388E3C; /* Tıklanınca daha koyu renk */\n"
"    border: none;\n"
"}")
        self.tahmin_butonu.setObjectName("tahmin_butonu")
        self.horizontalLayout_3.addWidget(self.tahmin_butonu)
        self.verticalLayout.addWidget(self.tahmin_frame, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.main_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.hak_saiyisi_lable.setText(_translate("MainWindow", "KALAN HAK : "))
        self.hak_sayisi.setText(_translate("MainWindow", "200"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label_3.setText(_translate("MainWindow", "_"))
        self.tahmin_butonu.setText(_translate("MainWindow", "TAHMIN ET"))
