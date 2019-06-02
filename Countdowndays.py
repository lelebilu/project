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
        self.date.setCalendarPopup(True)
        self.choosedatelabel.setText("Choose The Day:")
        self.memolabel.setText("Memo:")
        self.memo=QLineEdit(self)
        self.memo.setText('')
        self.setbtn=QPushButton('Set',self)
        self.setbtn.clicked.connect(self.setdate)
        layout.addWidget(self.choosedatelabel)
        layout.addWidget(self.date)
        layout.addWidget(self.memolabel)
        layout.addWidget(self.memo)
        layout.addWidget(self.setbtn)
        checkcd()

    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet("#MainWindow{background-color:white}")
    
    def setdate(self):
        now = QDate.currentDate()
        nowdate=now.toString(Qt.ISODate)
        a=nowdate.split("-")
        print(a[0],a[1],a[2])
        #print(self.date.text())
        dateset=str(self.date.text())
        b=dateset.split("/")
        print(b[0],b[1],b[2])
                                 
class showcd(QDialog):
    windowWidth = 350
    windowHeight = 132
    def __init__(self):
        super().__init__()
 
        self.pix = QPixmap('alarmbg.png')
        self.resize(350, 132)
        self.pix = self.pix.scaled(int(350), int(132))
        self.setMask(self.pix.mask()) 
        self.setWindowFlags(Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)  # 设置无边框和置顶窗口样式
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.setWindowOpacity(0.5)
        self.move((screen.width() - size.width()) / 2, (screen.height() - 210))
        self.setWindowFlags(Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.alarmtime=QLabel('',self)
        self.alarmtime.setGeometry(40,15,300,85)
        #self.init_ui()
        
    def paintEvent(self, event):
        paint = QPainter(self)
        paint.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)
    
    def init_ui(self,h,m):
        self.alarmtime.setFont(QFont('Comic Sans MS',36,QFont.Bold))
        self.alarmtime.setText("<font color=%s>%s</font>" %('#FFFFFF', h+" : "+m))
                                                            
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


def checkcd():
    my_file = Path("cdd.txt")
    if my_file.is_file():
        print("路徑是檔案。")
        f = open(my_file, 'r')
        line=f.readline()
        if line!="NONE":
            print(line)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = countdowndays()
    form.show()
    sys.exit(app.exec_())