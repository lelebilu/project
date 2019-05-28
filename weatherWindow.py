# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WeatherWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WeatherWindow(object):
    def setupUi(self, WeatherWindow):
        WeatherWindow.setObjectName("WeatherWindow")
        WeatherWindow.resize(400, 200)
        self.centralwidget = QtWidgets.QWidget(WeatherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.city = QtWidgets.QLabel(self.centralwidget)
        self.city.setGeometry(QtCore.QRect(190, 50, 170, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.city.setFont(font)
        self.city.setAlignment(QtCore.Qt.AlignCenter)
        self.city.setObjectName("city")
        self.weather_icon = QtWidgets.QLabel(self.centralwidget)
        self.weather_icon.setGeometry(QtCore.QRect(20, 50, 128, 128))
        self.weather_icon.setText("")
        self.weather_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.weather_icon.setObjectName("weather_icon")
        self.temprature = QtWidgets.QLabel(self.centralwidget)
        self.temprature.setGeometry(QtCore.QRect(190, 100, 170, 72))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.temprature.setFont(font)
        self.temprature.setTextFormat(QtCore.Qt.PlainText)
        self.temprature.setAlignment(QtCore.Qt.AlignCenter)
        self.temprature.setObjectName("temprature")
        self.chooseCity = QtWidgets.QComboBox(self.centralwidget)
        self.chooseCity.setGeometry(QtCore.QRect(20, 10, 361, 22))
        self.chooseCity.setObjectName("chooseCity")
        WeatherWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(WeatherWindow)
        self.statusbar.setObjectName("statusbar")
        WeatherWindow.setStatusBar(self.statusbar)

        self.retranslateUi(WeatherWindow)
        QtCore.QMetaObject.connectSlotsByName(WeatherWindow)

    def retranslateUi(self, WeatherWindow):
        _translate = QtCore.QCoreApplication.translate
        WeatherWindow.setWindowTitle(_translate("WeatherWindow", "Weather"))
        self.city.setText(_translate("WeatherWindow", "Tainan"))
        self.temprature.setText(_translate("WeatherWindow", "30"))

