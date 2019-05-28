import sys, os, random
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QPushButton,QMessageBox,QLineEdit,QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap

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
        hours=['0','1','2','3','4','5','6','7','8','9',
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
        mins=['0','1','2','3','4','5','6','7','8','9',
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

class alarmwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.set_Ui()
    def set_Ui(self):
        icon=QIcon("alarm.png")
        self.setWindowIcon(icon)
        self.setWindowTitle('alarm')
        self.setup(self)
        self.resize(400, 500)
        
        self.timelabel=QLabel(self)
        self.timelabel.setGeometry(-143,-130,800,500)
        self.timelabel.setFont(QFont('Comic Sans MS',36,QFont.Bold))
        
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start()
        
        self.tb1=Timebox(self)
        self.switchBtn1 = SwitchBtn(self)
        self.switchBtn1.setGeometry(310,233,60,30)
        self.tb1.setGeometry(10,220,300,50)
        self.switchBtn1.checkedChanged.connect(self.getState)
        
        self.tb2=Timebox(self)
        self.switchBtn2 = SwitchBtn(self)
        self.switchBtn2.setGeometry(310,283,60,30)
        self.tb2.setGeometry(10,270,300,50)
        self.switchBtn2.checkedChanged.connect(self.getState)
        
        self.tb3=Timebox(self)
        self.switchBtn3 = SwitchBtn(self)
        self.switchBtn3.setGeometry(310,333,60,30)
        self.tb3.setGeometry(10,320,300,50)
        self.switchBtn3.checkedChanged.connect(self.getState)
        
        self.tb4=Timebox(self)
        self.switchBtn4 = SwitchBtn(self)
        self.switchBtn4.setGeometry(310,383,60,30)
        self.tb4.setGeometry(10,370,300,50)
        self.switchBtn4.checkedChanged.connect(self.getState)
        
        self.tb5=Timebox(self)
        self.switchBtn5 = SwitchBtn(self)
        self.switchBtn5.setGeometry(310,433,60,30)
        self.tb5.setGeometry(10,420,300,50)
        self.switchBtn5.checkedChanged.connect(self.getState)

    
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
            print(self.tb2.hour.currentIndex())
            print(self.tb2.min.currentIndex())
            time = QTime.currentTime()
            print(time.toString(Qt.DefaultLocaleLongDate))
    
def main():
    app = QApplication(sys.argv)
    form = alarmwindow()
    form.show()
    sys.exit(app.exec_())

#if __name__ == "__main__":
#    main()