# -*- coding: utf-8 -*-
"""
Created on Fri May 31 04:43:30 2019

@author: 105502506
"""

import sys

from googletrans import Translator
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTabWidget
from TranslateWindow import Ui_Form
from PyQt5.QtGui import QIcon

class TranslateWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent=parent)
        self.setWindowIcon(QIcon("Google_Translate_Icon.png"))
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.on_click)
        
    def on_click(self):
        n = self.ui.tabWidget.currentIndex()
        translator = Translator()
        if n==0:
            text = self.ui.txtDetect.toPlainText()
            lang = translator.detect(text).lang
            tabText = "偵測語言：" + lang
            self.ui.tabWidget.setTabText(0, tabText)
        elif n==1:
            self.ui.tabWidget.setTabText(0, "偵測語言")
            text = self.ui.txtZhTw.toPlainText()
            lang = 'zh-tw'
            
        elif n==2:
            text = self.ui.txtEn.toPlainText()
            lang = 'en'
            
        self.ui.Entxt.setPlainText(translator.translate(text, dest='en', src=lang).text)
        self.ui.ZhTwtxt.setPlainText(translator.translate(text, dest='zh-tw', src=lang).text)
        self.ui.ZhCntxt.setPlainText(translator.translate(text, dest='zh-cn', src=lang).text)
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = TranslateWindow()
    w.show()
    sys.exit(app.exec_())

