import sys, os, random
import time
import datetime
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QPushButton,QMessageBox,QLineEdit,QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
import PyQt5.QtCore as QtCore
from pathlib import Path 

font = QFont() 
font.setFamily('Comic Sans MS')
font.setBold(True)

class countdowndays(QWidget):
    def __init__(self):
        super().__init__()
        icon=QIcon("calendar.png")
        self.setWindowIcon(icon)
        self.setWindowTitle(' Countdowndays')
        self.resize(400, 170)
        self.set_Ui()
        self.setup(self)
        
    def set_Ui(self):
        layout=QVBoxLayout(self)
        self.choosedatelabel=QLabel(self)
        self.memolabel=QLabel(self)
        self.date=QDateTimeEdit(QDate.currentDate(), self)
        self.date.setFont(font)
        self.date.setCalendarPopup(True)
        self.choosedatelabel.setText("<font color=%s>%s</font>" %('#F08080',"Choose The Day :"))
        self.choosedatelabel.setFont(QFont('Comic Sans MS',10,QFont.Bold))
        self.memolabel.setText("<font color=%s>%s</font>" %('#F08080',"Memo :"))
        self.memolabel.setFont(QFont('Comic Sans MS',10,QFont.Bold))
        self.memo=QLineEdit(self)
        self.memo.setText('')
        self.memo.setFont(font)
        self.setbtn=QPushButton('Set',self)
        self.setbtn.setFont(font)
        self.setbtn.clicked.connect(self.setdate)
        self.setbtn.setStyleSheet("color:white;background-color:LightCoral;border-radius:4px;min-width: 3em;")
        layout.addWidget(self.choosedatelabel)
        layout.addWidget(self.date)
        layout.addWidget(self.memolabel)
        layout.addWidget(self.memo)
        layout.addWidget(self.setbtn)
        #checkcd()

    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet("#MainWindow{background-color:white}")
    
    def setdate(self):
        now = QDate.currentDate()
        nowdate=now.toString("yyyy-M-d")
        a=nowdate.split("-")
        #print(a[0],a[1],a[2])
        #print(self.date.text())
        dateset=str(self.date.text())
        b=dateset.split("/")
        #print(b[0],b[1],b[2])
       # print(self.memo.text())
        f = open('cdd.txt','w+')
        f.truncate()
        f.write(dateset+'\n')
        f.write(self.memo.text())
        f.close()
        self.countdays()
        
    def countdays(self):
        f = open('cdd.txt', 'r')
        thedate=f.readline()
        thememo=f.readline()
        #print('hello')
        print(thedate)
        print(thememo)
        b=thedate.split("/")
        y=int(b[0])
        m=int(b[1])
        d=int(b[2])
        t = (datetime.datetime(y,m,d,0,0,0) - datetime.datetime.now()).total_seconds()
        daysleft=int(t/86400)+1
        self.scd=showcd()
        self.scd.init_ui(daysleft,thememo,thedate)
        self.scd.show()
        
class showcd(QDialog):
    windowWidth = 300
    windowHeight = 301
    def __init__(self):
        super(showcd,self).__init__()
 
        self.pix = QPixmap('cddbg.png')
        self.resize(300, 301)
        self.pix = self.pix.scaled(int(300), int(301))
        self.setMask(self.pix.mask()) 
        self.setWindowFlags(Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnBottomHint)  # 设置无边框和置顶窗口样式
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.setWindowOpacity(0.9)
        self.setWindowFlags(Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnBottomHint)
        
    def paintEvent(self, event):
        paint = QPainter(self)
        paint.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)
    
    def init_ui(self,daysleft,thememo,thedate):
        self.days=QLabel(self)
        self.days.setFont(QFont('Comic Sans MS',60,QFont.Bold))
        self.days.setText("<font color=%s>%s</font>" %('#F08080',daysleft))
        self.thedate=QLabel(self)
        self.thedate.setText("<font color=%s>%s</font>" %('#FFFFFF',thedate))
        self.thedate.setFont(QFont('Comic Sans MS',18,QFont.Bold))
        self.thewords=QLabel(self)
        self.thewords.setText("<font color=%s>%s</font>" %('#F08080',thememo))
        self.thewords.setFont(QFont('Comic Sans MS',18,QFont.Bold))
        self.thedate.setGeometry(45,20,240,50)
        if daysleft>99:
            print('big')        
            self.days.setGeometry(40,70,260,200)
        elif 0<=daysleft<10:
            self.days.setGeometry(110,90,100,150)
        else:
            self.days.setGeometry(70,90,200,150)
            
        self.thewords.setGeometry(25,250,250,50)
                                                    
    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #獲取滑鼠相對視窗的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  #更改滑鼠圖示
        if event.button()==Qt.RightButton:
            self.close()
            
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:  
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改視窗位置
            QMouseEvent.accept()
            
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QCursor(Qt.ArrowCursor))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = countdowndays()
    form.show()
    sys.exit(app.exec_())