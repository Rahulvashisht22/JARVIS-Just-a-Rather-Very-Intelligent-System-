# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jarvisUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JarvisGUI(object):
    def setupUi(self, JarvisGUI):
        JarvisGUI.setObjectName("JarvisGUI")
        JarvisGUI.resize(1435, 950)
        self.centralwidget = QtWidgets.QWidget(JarvisGUI)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-120, -60, 1571, 1001))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/Black_Template.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 110, 911, 531))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/unnamed.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, -50, 551, 221))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("images/initial.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 130, 371, 121))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("images/box(1).jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 270, 371, 121))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("images/box(1).jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(-70, 520, 551, 421))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("images/Earth.gif"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.text_time = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_time.setGeometry(QtCore.QRect(60, 150, 291, 81))
        self.text_time.setStyleSheet("background-color: Transparent;\n"
"border-radius:none;\n"
"color: rgb(170, 255, 255);\n"
"font: 75 22pt \"Calibri\";")
        self.text_time.setObjectName("text_time")
        self.text_date = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_date.setGeometry(QtCore.QRect(60, 290, 291, 81))
        self.text_date.setStyleSheet("background-color: Transparent;\n"
"border-radius:none;\n"
"color: rgb(170, 255, 255);\n"
"font: 75 22pt \"Calibri\";")
        self.text_date.setObjectName("text_date")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(0, 410, 371, 121))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("images/box(1).jpg"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.text_temp = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_temp.setGeometry(QtCore.QRect(50, 430, 291, 81))
        self.text_temp.setStyleSheet("background-color: Transparent;\n"
"border-radius:none;\n"
"color: rgb(170, 255, 255);\n"
"font: 75 22pt \"Calibri\";")
        self.text_temp.setObjectName("text_temp")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(960, 10, 471, 341))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("images/brain.gif"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(980, 380, 411, 111))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("images/box(1).jpg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.text_cpu = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_cpu.setGeometry(QtCore.QRect(1070, 400, 291, 81))
        self.text_cpu.setStyleSheet("background-color: Transparent;\n"
"border-radius:none;\n"
"color: rgb(170, 255, 255);\n"
"font: 75 22pt \"Calibri\";")
        self.text_cpu.setObjectName("text_cpu")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(480, 690, 191, 111))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("images/btn.jpg"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(480, 710, 181, 71))
        self.pushButton.setStyleSheet("background-color: Transparent;\n"
"border-radius:none;\n"
"color: rgb(64, 240, 255);\n"
"font: 75 16pt \"Arial\";")
        self.pushButton.setObjectName("pushButton")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(720, 690, 191, 111))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("images/btn.jpg"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(720, 710, 181, 71))
        self.pushButton_2.setStyleSheet("background-color: Transparent;\n"
"border-radius:none;\n"
"color: rgb(64, 240, 255);\n"
"font: 75 16pt \"Arial\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(960, 540, 471, 361))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("images/B.G_Template_1.gif"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(580, 50, 381, 71))
        self.textBrowser.setStyleSheet("background-color: Transparent;\n"
"border-radius: none;")
        self.textBrowser.setObjectName("textBrowser")
        JarvisGUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(JarvisGUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1435, 26))
        self.menubar.setObjectName("menubar")
        JarvisGUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(JarvisGUI)
        self.statusbar.setObjectName("statusbar")
        JarvisGUI.setStatusBar(self.statusbar)

        self.retranslateUi(JarvisGUI)
        QtCore.QMetaObject.connectSlotsByName(JarvisGUI)

    def retranslateUi(self, JarvisGUI):
        _translate = QtCore.QCoreApplication.translate
        JarvisGUI.setWindowTitle(_translate("JarvisGUI", "MainWindow"))
        self.pushButton.setText(_translate("JarvisGUI", "START"))
        self.pushButton_2.setText(_translate("JarvisGUI", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JarvisGUI = QtWidgets.QMainWindow()
    ui = Ui_JarvisGUI()
    ui.setupUi(JarvisGUI)
    JarvisGUI.show()
    sys.exit(app.exec_())
