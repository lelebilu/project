import sys
import pygame
import random
import alarm
import notes
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget,QMenu
from PyQt5.QtGui import QPixmap, QPainter, QBitmap, QCursor
import PyQt5.QtCore as QtCore
 
 
class PixWindow(QWidget):  # 不规则窗体
    
    windowWidth = 114
    windowHeight = 176
    def __init__(self):
        super().__init__()
 
        self.pix = QPixmap('xmq.png')
        self.resize(138, 191)
        self.pix = self.pix.scaled(int(114), int(176))
        self.setMask(self.pix.mask()) 
        self.setWindowFlags(Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)  # 设置无边框和置顶窗口样式
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - 210))
        
    def mousePressEvent(self, event):
        #鼠标左键按下
        if event.button() == Qt.LeftButton:
            self.pix.load('xmq2.png')
            self.pix = self.pix.scaled(int(138), int(191))
            self.setMask(self.pix.mask())
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))
            self.update()
        if event.button()==Qt.RightButton:
            contextMenu=QMenu(self)
            postitAct=contextMenu.addAction("Post it")
            alarmAct=contextMenu.addAction("Alarm")
            countdowndaysAct=contextMenu.addAction("CountdownDays")
            quitAct=contextMenu.addAction("Bye")
            action=contextMenu.exec_(self.mapToGlobal(event.pos()))
            if action==postitAct:
                self.p=notes.MainWindow()
                self.p.show()
            if action==alarmAct:
                self.a=alarm.alarmwindow()
                self.a.show()
            if action==quitAct:
                self.close()
            
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        screen = QDesktopWidget().screenGeometry()
        while(self.y() < (screen.height() - 210)):
            self.move((self.x()), self.y()+1)
        self.pix.load('xmq.png')
        self.pix = self.pix.scaled(int(114), int(176))
        self.setMask(self.pix.mask())
        self.m_drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))
        self.update()
        
    def paintEvent(self, event):
        paint = QPainter(self)
        paint.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)
      
def numbers_to_strings(argument):
    switcher = {
        0: "0.mp3",
        1: "1.mp3",
        2: "2.mp3",
    }
    return switcher.get(argument, "nothing")
        
        
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = PixWindow()
    win.show()
    sys.exit(app.exec_())