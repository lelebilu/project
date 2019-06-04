# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TranslateWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTextEdit

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(620, 414)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 581, 161))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.txtDetect = QTextEdit(self.tab)
        self.txtDetect.resize(575,133);
        
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.txtZhTw = QTextEdit(self.tab_2)
        self.txtZhTw.resize(575,133)

        
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.txtEn = QTextEdit(self.tab_3)
        self.txtEn.resize(575,133);
        
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 180, 81, 28))
        self.pushButton.setObjectName("pushButton")
        
        self.tabWidget_2 = QtWidgets.QTabWidget(Form)
        self.tabWidget_2.setGeometry(QtCore.QRect(20, 220, 581, 161))
        self.tabWidget_2.setObjectName("tabWidget_2")
        
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.Entxt = QTextEdit(self.tab_4)
        self.Entxt.resize(575,133)
        self.Entxt.setReadOnly(True)
        
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget_2.addTab(self.tab_5, "")
        self.ZhTwtxt = QTextEdit(self.tab_5)
        self.ZhTwtxt.resize(575,133)
        self.ZhTwtxt.setReadOnly(True)
        
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget_2.addTab(self.tab_6, "")
        self.ZhCntxt = QTextEdit(self.tab_6)
        self.ZhCntxt.resize(575,133)
        self.ZhCntxt.setReadOnly(True)
        
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 390, 131, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Translate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "偵測語言"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "繁體中文"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "英文"))
        self.pushButton.setText(_translate("Form", "Enter"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("Form", "英文"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("Form", "繁體中文"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("Form", "简体中文"))
        self.label.setText(_translate("Form", "Translated by Google"))

