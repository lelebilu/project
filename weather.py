# -*- coding: utf-8 -*-
"""
Created on Mon May 27 13:38:17 2019

@author: 史家瑩
"""
import sys
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from weatherWindow import Ui_WeatherWindow
import requests

class WeatherWindow(QtWidgets.QMainWindow, Ui_WeatherWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent=parent)
        self.ui = Ui_WeatherWindow()
        self.ui.setupUi(self)
        icon=QIcon("weatherIcon.png")
        self.setWindowIcon(icon)
        self.setStyleSheet("background-color:white;");
        self.init_ui()
    
    def init_ui(self):
        self.call_api("Taipei")
        
        City = ["Taipei", "Taoyuan", "Hsinchu", "Miaoli", "Taichung",
                "Changhua", "Nantou", "Yunlin", "Chiayi", "Tainan",
                "Kaohsiung", "Pingtung", "Taitung", "Hualien", "Yilan",]
        self.ui.chooseCity.addItems(City)
        self.ui.chooseCity.activated[str].connect(self.call_api)
        
    def call_api(self, text):
        api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=1418a9a29d87b90bd6e3c904f01ae38d&q='
        url = api_address + text
        json_data = requests.get(url).json()


        self.ui.city.setText(text)
        self.ui.temprature.setText(str(round(json_data['main']['temp']-273.15)) + "°С")
        if json_data['weather'][0]['id'] >= 200 and json_data['weather'][0]['id'] < 300:
            self.ui.weather_icon.setPixmap(QtGui.QPixmap("weather/thunderstorm.png"))
        elif json_data['weather'][0]['id'] >= 300 and json_data['weather'][0]['id'] < 600:
            self.ui.weather_icon.setPixmap(QtGui.QPixmap("weather/rain.png"))
        elif json_data['weather'][0]['id'] >= 600 and json_data['weather'][0]['id'] < 700:
            self.ui.weather_icon.setPixmap(QtGui.QPixmap("weather/snow.png"))
        elif json_data['weather'][0]['id'] >= 700 and json_data['weather'][0]['id'] < 800:
            self.ui.weather_icon.setPixmap(QtGui.QPixmap("weather/sunny.png"))
        elif json_data['weather'][0]['id'] == 800:
            self.ui.weather_icon.setPixmap(QtGui.QPixmap("weather/sun.png"))
        elif json_data['weather'][0]['id'] > 800:
            self.ui.weather_icon.setPixmap(QtGui.QPixmap("weather/cloudy.png"))
        #print(json_data)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = WeatherWindow()
    w.show()
    sys.exit(app.exec_())
