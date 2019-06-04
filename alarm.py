import sys, os, random
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QPushButton,QMessageBox,QLineEdit,QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
import pygame
import PyQt5.QtCore as QtCore
import winsound

font = QFont() 
font.setFamily('Comic Sans MS')
font.setBold(True)

class SwitchBtn(QWidget):
    #信号
    checkedChanged = pyqtSignal(bool)
    def __init__(self,parent=None):
        super(QWidget, self).__init__(parent)        
        self.checked = False
        self.bgColorOn = QColor(240, 128, 128)
        self.bgColorOff = QColor(119,136,153)
        self.sliderColorOn = QColor(100, 100, 100)
        self.sliderColorOff = QColor(240, 128, 128)
        self.textColorOn = QColor(255, 255, 255)
        self.textColorOff = QColor(255, 255, 255)
        self.textOff = "OFF"
        self.textOn = "ON"
        self.space = 2
        self.rectRadius = 5
        self.step = self.width() / 50
        self.startX = 0
        self.endX = 0
        self.timer = QTimer(self)  # 初始化一个定时器
        self.timer.timeout.connect(self.updateValue)  # 计时结束调用operate()方法
        #self.timer.start(5)  # 设置计时间隔并启动
        self.setFont(QFont("Microsoft Yahei", 10))
        #self.resize(55,22)

    def updateValue(self):
        if self.checked:
            if self.startX < self.endX:
                self.startX = self.startX + self.step
            else:
                self.startX = self.endX
                self.timer.stop()
        else:
            if self.startX  > self.endX:
                self.startX = self.startX - self.step
            else:
                self.startX = self.endX
                self.timer.stop()
        self.update()

    def mousePressEvent(self,event):
        self.checked = not self.checked
        #发射信号
        self.checkedChanged.emit(self.checked)
        # 每次移动的步长为宽度的50分之一
        self.step = self.width() / 50
        #状态切换改变后自动计算终点坐标
        if self.checked:
            self.endX = self.width() - self.height()
        else:
            self.endX = 0
        self.timer.start(5)

    def paintEvent(self, evt):
        #绘制准备工作, 启用反锯齿
            painter = QPainter()
            painter.begin(self)
            painter.setRenderHint(QPainter.Antialiasing)
            #绘制背景
            self.drawBg(evt, painter)
            #绘制滑块
            self.drawSlider(evt, painter)
            #绘制文字
            self.drawText(evt, painter)
            painter.end()

    def drawText(self, event, painter):
        painter.save()
        if self.checked:
            painter.setPen(self.textColorOn)
            painter.drawText(0, 0, self.width() / 2 + self.space * 2, self.height(), Qt.AlignCenter, self.textOn)
        else:
            painter.setPen(self.textColorOff)
            painter.drawText(self.width() / 2, 0,self.width() / 2 - self.space, self.height(), Qt.AlignCenter, self.textOff)
        painter.restore()

    def drawBg(self, event, painter):
        painter.save()
        painter.setPen(Qt.NoPen)
        if self.checked:
            painter.setBrush(self.bgColorOn)
        else:
            painter.setBrush(self.bgColorOff)

        rect = QRect(0, 0, self.width(), self.height())
        #半径为高度的一半
        radius = rect.height() / 2
        #圆的宽度为高度
        circleWidth = rect.height()

        path = QPainterPath()
        path.moveTo(radius, rect.left())
        path.arcTo(QRectF(rect.left(), rect.top(), circleWidth, circleWidth), 90, 180)
        path.lineTo(rect.width() - radius, rect.height())
        path.arcTo(QRectF(rect.width() - rect.height(), rect.top(), circleWidth, circleWidth), 270, 180)
        path.lineTo(radius, rect.top())

        painter.drawPath(path)
        painter.restore()

    def drawSlider(self, event, painter):
        painter.save()

        if self.checked:
            painter.setBrush(self.sliderColorOn)
        else:
            painter.setBrush(self.sliderColorOff)

        rect = QRect(0, 0, self.width(), self.height())
        sliderWidth = rect.height() - self.space * 2
        sliderRect = QRect(self.startX + self.space, self.space, sliderWidth, sliderWidth)
        painter.drawEllipse(sliderRect)

        painter.restore()


class Timebox(QWidget):
    def __init__(self,parent=None):
        super(QWidget, self).__init__(parent)
        self.hour=QComboBox(self)
        hours=['00','01','02','03','04','05','06','07','08','09',
               '10','11','12','13','14','15','16','17',
               '18','19','20','21','22','23']
        self.hour.addItems(hours)
        self.hour.setMaxVisibleItems(8)
        self.hour.setFixedHeight(30)
        self.hour.setStyleSheet("border: 1px solid gray;border-radius:3px;min-width: 1em;selection-background-color:LightCoral;")
        self.hour.setFont(font) 
        self.colon=QLabel('    ：')
        self.colon.setFont(font)
        self.colon.setFixedHeight(30)
        self.min=QComboBox(self)
        mins=['00','01','02','03','04','05','06','07','08','09',
              '10','11','12','13','14','15','16','17',
              '18','19','20','21','22','23','24','25',
              '26','27','28','29','30','31','32','33',
              '34','35','36','37','38','39','40','41',
              '42','43','44','45','46','47','48','49',
              '50','51','52','53','54','55','56','57',
              '58','59']
        self.min.addItems(mins)
        self.min.setMaxVisibleItems(8)
        self.min.setFixedHeight(30)
        self.min.setFont(font)
        self.min.setStyleSheet("border: 1px solid gray;border-radius:3px;min-width: 1em;selection-background-color:LightCoral;")
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.hour)
        h_layout.addWidget(self.colon)
        h_layout.addWidget(self.min)
        self.setLayout(h_layout)

class alarmwindow(QDialog):
    dialogSignel=pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.set_Ui()
    def set_Ui(self):
        icon=QIcon("alarm.png")
        self.setWindowIcon(icon)
        self.setWindowTitle('Alarm')
        self.setup(self)
        self.resize(400, 570)
        
        self.timelabel=QLabel(self)
        self.timelabel.setFont(QFont('Comic Sans MS',36,QFont.Bold))
        
        self.alarmlabel=QLabel(self)
        self.alarmlabel.setFont(QFont('Comic Sans MS',12,QFont.Bold))
        self.alarmlabel.setText("<font color=%s>%s</font>" %('#F08080', "Alarm"))
                                                             
        self.cdlabel=QLabel(self)
        self.cdlabel.setFont(QFont('Comic Sans MS',12,QFont.Bold))
        self.cdlabel.setText("<font color=%s>%s</font>" %('#F08080', "CountDown"))
                                                          
        self.rtlabel=QLabel(self)
        self.rtlabel.setFont(QFont('Comic Sans MS',12,QFont.Bold))
        self.rtlabel.setText("<font color=%s>%s</font>" %('#F08080', "Ringtone"))
                                                          
        self.cdhour=QComboBox(self)
        hours=['00','01','02','03','04','05','06','07','08','09',
               '10','11','12','13','14','15','16','17',
               '18','19','20','21','22','23']                                                 
        self.cdhour.addItems(hours)
        self.cdhour.setMaxVisibleItems(8)
        self.cdhour.setFixedHeight(30)
        self.cdhour.setStyleSheet("border: 1px solid gray;border-radius:3px;min-width: 1em;selection-background-color:LightCoral;")
        self.cdhour.setFont(font)                                                   
        self.cdmin=QComboBox(self)
        mins=['00','01','02','03','04','05','06','07','08','09',
              '10','11','12','13','14','15','16','17',
              '18','19','20','21','22','23','24','25',
              '26','27','28','29','30','31','32','33',
              '34','35','36','37','38','39','40','41',
              '42','43','44','45','46','47','48','49',
              '50','51','52','53','54','55','56','57',
              '58','59']
        self.cdmin.addItems(mins)
        self.cdmin.setMaxVisibleItems(8)
        self.cdmin.setFixedHeight(30)
        self.cdmin.setFont(font)
        self.cdmin.setStyleSheet("border: 1px solid gray;border-radius:3px;min-width: 1em;selection-background-color:LightCoral;")                                                  
        self.cds=QComboBox(self)
        self.cds.addItems(mins)
        self.cds.setMaxVisibleItems(8)
        self.cds.setFixedHeight(30)
        self.cds.setFont(font)
        self.cds.setStyleSheet("border: 1px solid gray;border-radius:3px;min-width: 1em;selection-background-color:LightCoral;")
        
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start()
        
        self.tb1=Timebox(self)
        self.switchBtn1 = SwitchBtn(self)
        self.switchBtn1.checkedChanged.connect(self.getState)
        self.gobutton=QPushButton(self)
        self.gobutton.setText('GO!')
        self.gobutton.setFont(font) 
        self.gobutton.setStyleSheet("color:white;background-color:LightCoral;border-radius:4px;min-width: 3em;")
        self.gobutton.clicked.connect(self.setcd)
        self.setbutton=QPushButton(self)
        self.setbutton.setText('SET')
        self.setbutton.setFont(font) 
        self.setbutton.clicked.connect(self.setal)
        self.setbutton.setStyleSheet("color:white;background-color:LightCoral;border-radius:4px;min-width: 3em;")
        self.choosebutton=QPushButton(self)
        self.choosebutton.setText('CHOOSE')
        self.choosebutton.setFont(font) 
        self.choosebutton.setStyleSheet("color:white;background-color:LightCoral;border-radius:4px;min-width: 3em;")
        self.choosebutton.clicked.connect(self.song)
        self.colon1=QLabel(':',self)
        self.colon1.setFont(font)
        self.colon1.setFixedHeight(30)
        self.colon2=QLabel(':',self)
        self.colon2.setFont(font)
        self.colon2.setFixedHeight(30)
        self.file=QLabel('',self)
        self.file.setFont(font)
        self.file.setFixedHeight(30)
        
        self.timelabel.setGeometry(-143,-130,800,500)
        self.rtlabel.setGeometry(20,200,180,50)
        self.file.setGeometry(220,270,300,30)
        self.choosebutton.setGeometry(100,270,100,30)
        self.switchBtn1.setGeometry(20,270,70,30)
        self.alarmlabel.setGeometry(20,320,180,50)
        self.tb1.setGeometry(10,370,295,50)
        self.setbutton.setGeometry(310,383,60,30)
        self.cdlabel.setGeometry(20,435,180,50)
        self.gobutton.setGeometry(313,500,60,30)
        self.cdhour.setGeometry(22,500,75,30)
        self.cdmin.setGeometry(120,500,75,30)
        self.cds.setGeometry(218,500,75,30)
        self.colon1.setGeometry(103,500,70,30)
        self.colon2.setGeometry(202,500,70,30)
        self.musicon=0
    
    def setal(self):
        self.sal = showalarm()
        hh=self.tb1.hour.currentIndex()
        mm=self.tb1.min.currentIndex()
        if hh<10:
            h="0"+str(hh)
        else:
            h=str(hh)
        if mm<10:
            m="0"+str(mm)
        else:
            m=str(mm)
        self.sal.init_ui(h,m)
        self.sal.show()
        print('set')
        #workThread.setvalue(h,m)
        self.workThread=WorkThread()
        self.workThread.hour=h
        self.workThread.min=m
        self.workThread.start()
        self.workThread.trigger.connect(self.timesup)
        
    def setcd(self):
        self.c=countdown()
        self.hh=self.cdhour.currentIndex()
        self.mm=self.cdmin.currentIndex()
        self.ss=self.cds.currentIndex()
        if self.hh<10:
            self.h="0"+str(self.hh)
        else:
            self.h=str(self.hh)
        if self.mm<10:
            self.m="0"+str(self.mm)
        else:
            self.m=str(self.mm)
        if self.ss<10:
            self.s="0"+str(self.ss)
        else:
            self.s=str(self.ss)
        self.c.init_ui(self.h,self.m,self.s)
        self.c.show()
        self.cdtimer=QTimer(self)
        self.cdtimer.timeout.connect(self.timer_timeout)
        self.cdtimer.start(1000)
        print('set')
    
    def timer_timeout(self):
        self.ss=self.ss-1
        print(self.hh,self.mm,self.ss)
        if self.hh==0 and self.mm==0 and self.ss==-1:
            self.cdtimer.stop()
            self.timesupcd()
        else:    
            if self.ss==-1:
                self.ss=59
                self.mm=self.mm-1
                if self.mm==-1:
                    self.mm=59
                    self.hh=self.hh-1
            if self.hh<10:
                self.h="0"+str(self.hh)
            else:
                self.h=str(self.hh)
            if self.mm<10:
                self.m="0"+str(self.mm)
            else:
                self.m=str(self.mm)
            if self.ss<10:
                self.s="0"+str(self.ss)
            else:
                self.s=str(self.ss)
            self.c.init_ui(self.h,self.m,self.s)
            self.c.show()
        
    def stopthread(self,flag):
        if flag==1:
            print(flag)
              
    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet("#MainWindow{background-color:white}")
        #self.centralwidget =QWidget(MainWindow)
        #self.centralwidget.setObjectName("centralwidget")
        
    def showtime(self):
        time = QTime.currentTime()
        text = time.toString(Qt.DefaultLocaleLongDate)
        self.timelabel.setText("<font color=%s>%s</font>" %('#F08080', "     "+ text))
    
    def getState(self,checked):
        print("checked=", checked)
        if checked==True:
            self.musicon=1
        else:
            self.musicon=0
    def song(self):
        filename,  _ = QFileDialog.getOpenFileName(self, 'Open file', './')
        file=open(filename)
        self.ringsong=filename
        self.file.setText(filename.split("/")[-1] )
        
    def timesup(self):
        self.dialogSignel.emit(1)
        self.sal.close()
        self.tu=timesup()
        self.tu.show()
        if self.musicon==1:
            pygame.mixer.init()
            pygame.mixer.music.load(self.ringsong) 
            pygame.mixer.music.play(0)
        self.tu.tudialogSignel.connect(self.musicstop)
    
    def timesupcd(self):
        self.dialogSignel.emit(1)
        self.c.close()
        self.tu=timesup()
        self.tu.show()
        if self.musicon==1:
            pygame.mixer.init()
            pygame.mixer.music.load(self.ringsong) 
            pygame.mixer.music.play(0)
        self.tu.tudialogSignel.connect(self.musicstop)
    
    def musicstop(self,flag):
        if flag==1 and self.musicon==1:
            print('stop')
            pygame.mixer.music.stop()

class showalarm(QDialog):
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
        #self.init_ui()
        
    def paintEvent(self, event):
        paint = QPainter(self)
        paint.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)
    
    def init_ui(self,h,m):
        self.alarmtime=QLabel(self)
        self.alarmtime.setFont(QFont('Comic Sans MS',36,QFont.Bold))
        self.alarmtime.setText("<font color=%s>%s</font>" %('#FFFFFF', h+" : "+m))
        self.alarmtime.setGeometry(40,10,300,100)
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

class countdown(QDialog):
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
        self.countdowntime=QLabel('',self)
        self.countdowntime.setGeometry(25,32,305,60)
        
    def paintEvent(self, event):
        paint = QPainter(self)
        paint.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)
    
    def init_ui(self,h,m,s):
        self.countdowntime.setFont(QFont('Comic Sans MS',24,QFont.Bold))
        self.countdowntime.setText("<font color=%s>%s</font>" %('#FFFFFF', h+" : "+m+" : "+s))
                                                                
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

class WorkThread(QThread): 
    trigger = pyqtSignal() 
    def __int__(self): 
        super(WorkThread,self).__init__() 
    def run(self): 
        while True:
            current_time = time.strftime('%H:%M', time.localtime())
            now = current_time.split(':')
            print(now)
            if self.hour == now[0] and self.min == now[1]:
                #winsound.Beep(600, 2000)
                break
        self.trigger.emit()
        #時間到時發出訊號 
        
class timesup(QDialog):
    tudialogSignel=pyqtSignal(int)
    windowWidth = 441
    windowHeight = 262
    def __init__(self):
        super().__init__()
 
        self.pix = QPixmap('tu.png')
        self.resize(441, 262)
        self.pix = self.pix.scaled(int(441), int(262))
        self.setMask(self.pix.mask()) 
        self.setWindowFlags(Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)  # 设置无边框和置顶窗口样式
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.setWindowOpacity(1)
        self.move((screen.width()/2/2)+20, (screen.height()/2/2)+60)
        self.setWindowFlags(Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.closebutton=QPushButton(self)
        self.closebutton.setText('X')
        self.closebutton.setFont(font) 
        self.closebutton.setStyleSheet("color:white;background-color:LightCoral;border-radius:4px;min-width: 1em;")
        self.closebutton.setGeometry(363,20,30,30)
        self.closebutton.clicked.connect(self.stopclose)
    def paintEvent(self, event):
        paint = QPainter(self)
        paint.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)
    
    def stopclose(self):
        self.tudialogSignel.emit(1)
        self.close()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = alarmwindow()
    form.show()
    sys.exit(app.exec_())