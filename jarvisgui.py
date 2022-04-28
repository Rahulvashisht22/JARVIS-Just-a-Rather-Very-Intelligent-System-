import sys

from jarvisUi import Ui_JarvisGUI
from PyQt5 import QtCore , QtGui , QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QTime, QDate
from PyQt5.uic import loadUiType
import jarvis
import psutil
import os
import requests
from requests import get
from bs4 import BeautifulSoup

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()
    def run(self):
        jarvis.taskexecution()

startexe = MainThread()

class Gui_Start(QMainWindow):
    def __init__(self):
        super().__init__()

        self.gui = Ui_JarvisGUI()
        self.gui.setupUi(self)

        self.gui.pushButton.clicked.connect(self.startTask)
        self.gui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.gui.label2 = QtGui.QMovie("images//unnamed.gif")
        self.gui.label_2.setMovie(self.gui.label2)
        self.gui.label2.start()

        self.gui.label3 = QtGui.QMovie("images//initial.gif")
        self.gui.label_3.setMovie(self.gui.label3)
        self.gui.label3.start()

        self.gui.label6 = QtGui.QMovie("images//Earth.gif")
        self.gui.label_6.setMovie(self.gui.label6)
        self.gui.label6.start()

        self.gui.label7 = QtGui.QMovie("images//brain.gif")
        self.gui.label_7.setMovie(self.gui.label7)
        self.gui.label7.start()

        self.gui.label12 = QtGui.QMovie("images//B.G_Template_1.gif")
        self.gui.label_12.setMovie(self.gui.label12)
        self.gui.label12.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)

        timer.start(1000)
        #timer.timeout.connect(self.readtemp)

        startexe.start()



    def showTime(self):
        current_time = QTime.currentTime()
        label_time = current_time.toString('hh:mm:ss')
        current_date = QDate.currentDate()
        label_date = current_date.toString(Qt.ISODate)
        self.gui.text_time.setText("TIME : " + label_time)
        self.gui.text_date.setText("DATE : " + label_date)

        usage = str(psutil.cpu_percent())
        battery = psutil.sensors_battery()
        bat = str(battery.percent)
        self.gui.text_cpu.setText("BATTERY : " + bat +"%")
        self.gui.text_temp.setText("CPU USAGE : " + usage)




'''speak("battery is at")
        speak(battery.percent)

    def readtemp(self):

        search = "temperature in solan"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        self.gui.text_temp.setText("Temp: " + temp)'''



GuiApp = QApplication(sys.argv)
jarvis_gui = Gui_Start()
jarvis_gui.show()

exit(GuiApp.exec_())

