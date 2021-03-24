# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'App_UI_LOG_final.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import (QAreaSeries, QBarSet, QChart, QChartView,
                           QLineSeries, QPieSeries, QScatterSeries, QSplineSeries,
                           QStackedBarSeries)
from PyQt5.QtCore import pyqtSlot, QPointF, Qt
from PyQt5.QtGui import QColor, QPainter, QPalette
from PyQt5.QtWidgets import (QCheckBox, QComboBox, QGridLayout, QHBoxLayout,
                             QLabel, QSizePolicy, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 600)
        MainWindow.setMinimumSize(QtCore.QSize(950, 600))
        MainWindow.setMaximumSize(QtCore.QSize(950, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(180, 10, 750, 550))
        self.stackedWidget.setMinimumSize(QtCore.QSize(750, 550))
        self.stackedWidget.setMaximumSize(QtCore.QSize(750, 550))
        self.stackedWidget.setObjectName("stackedWidget")
        self.Login = QtWidgets.QWidget()
        self.Login.setObjectName("Login")
        self.label_Login = QtWidgets.QLabel(self.Login)
        self.label_Login.setGeometry(QtCore.QRect(350, 40, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_Login.setFont(font)
        self.label_Login.setStyleSheet("")
        self.label_Login.setObjectName("label_Login")
        self.label_Password = QtWidgets.QLabel(self.Login)
        self.label_Password.setGeometry(QtCore.QRect(221, 215, 84, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Password.setFont(font)
        self.label_Password.setObjectName("label_Password")
        self.lineEdit_Addpad = QtWidgets.QLineEdit(self.Login)
        self.lineEdit_Addpad.setGeometry(QtCore.QRect(318, 291, 171, 31))
        self.lineEdit_Addpad.setStyleSheet("QLineEdit{ \n"
" border-radius:15px;\n"
" border-color: rgb(140, 140, 140);\n"
" border-style: inset;\n"
" border-width: 2px;\n"
" background-color: rgb(255, 255, 255);\n"
" font: 12pt \"Impact\";\n"
" color: rgb(0, 0, 0);\n"
" padding-left: 10px;\n"
"}")
        self.lineEdit_Addpad.setObjectName("lineEdit_Addpad")
        self.lineEdit_Username = QtWidgets.QLineEdit(self.Login)
        self.lineEdit_Username.setGeometry(QtCore.QRect(318, 139, 171, 31))
        self.lineEdit_Username.setStyleSheet("QLineEdit{ \n"
" border-radius:15px;\n"
" border-color: rgb(140, 140, 140);\n"
" border-style: inset;\n"
" border-width: 2px;\n"
" background-color: rgb(255, 255, 255);\n"
" font: 12pt \"Impact\";\n"
" color: rgb(0, 0, 0);\n"
" padding-left: 10px;\n"
"}")
        self.lineEdit_Username.setObjectName("lineEdit_Username")
        self.label_Username = QtWidgets.QLabel(self.Login)
        self.label_Username.setGeometry(QtCore.QRect(221, 139, 90, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Username.setFont(font)
        self.label_Username.setObjectName("label_Username")
        self.label_ADD = QtWidgets.QLabel(self.Login)
        self.label_ADD.setGeometry(QtCore.QRect(221, 291, 73, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_ADD.setFont(font)
        self.label_ADD.setObjectName("label_ADD")
        self.lineEdit_Password = QtWidgets.QLineEdit(self.Login)
        self.lineEdit_Password.setGeometry(QtCore.QRect(318, 215, 171, 31))
        self.lineEdit_Password.setStyleSheet("QLineEdit{ \n"
" border-radius:15px;\n"
" border-color: rgb(140, 140, 140);\n"
" border-style: inset;\n"
" border-width: 2px;\n"
" background-color: rgb(255, 255, 255);\n"
" font: 12pt \"Impact\";\n"
" color: rgb(0, 0, 0);\n"
" padding-left: 10px;\n"
"}")
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.Login)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(290, 340, 221, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_Addpad = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_Addpad.setFont(font)
        self.pushButton_Addpad.setStyleSheet("QPushButton {\n"
"  font: 15pt \"Impact\";\n"
"  background-color: qlineargradient(spread:reflect, x1:1, y1:0.505318, x2:1, y2:1, stop:0.4375 rgba(234, 234, 234, 255), stop:1 rgba(192, 192, 192, 255));\n"
"  color: rgb(65, 65, 65);\n"
"  border: 2px solid #ffffff;\n"
"  border-style: solid;\n"
"  border-radius:20;\n"
"  padding: 3px;\n"
"}\n"
"QPushButton:pressed {\n"
" font: 15pt \"Impact\";\n"
" color: rgb(255, 255, 255);\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.159091 rgba(0, 180, 219, 255), stop:1 rgba(97, 218, 223, 255));\n"
"}")
        self.pushButton_Addpad.setObjectName("pushButton_Addpad")
        self.horizontalLayout_2.addWidget(self.pushButton_Addpad)
        self.pushButton_Login = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_Login.setFont(font)
        self.pushButton_Login.setStyleSheet("QPushButton {\n"
"  font: 15pt \"Impact\";\n"
"  background-color: qlineargradient(spread:reflect, x1:1, y1:0.505318, x2:1, y2:1, stop:0.4375 rgba(234, 234, 234, 255), stop:1 rgba(192, 192, 192, 255));\n"
"  color: rgb(65, 65, 65);\n"
"  border: 2px solid #ffffff;\n"
"  border-style: solid;\n"
"  border-radius:20;\n"
"  padding: 3px;\n"
"}\n"
"QPushButton:pressed {\n"
" font: 15pt \"Impact\";\n"
" color: rgb(255, 255, 255);\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.159091 rgba(0, 180, 219, 255), stop:1 rgba(97, 218, 223, 255));\n"
"}")
        self.pushButton_Login.setObjectName("pushButton_Login")
        self.horizontalLayout_2.addWidget(self.pushButton_Login)
        self.comboBox_IP_PAD = QtWidgets.QComboBox(self.Login)
        self.comboBox_IP_PAD.setGeometry(QtCore.QRect(300, 440, 200, 28))
        self.comboBox_IP_PAD.setMinimumSize(QtCore.QSize(200, 28))
        self.comboBox_IP_PAD.setMaximumSize(QtCore.QSize(200, 28))
        self.comboBox_IP_PAD.setObjectName("comboBox_IP_PAD")
        self.stackedWidget.addWidget(self.Login)
        self.Dashbord_page = QtWidgets.QWidget()
        self.Dashbord_page.setObjectName("Dashbord_page")
        self.label_All = QtWidgets.QLabel(self.Dashbord_page)
        self.label_All.setGeometry(QtCore.QRect(590, 20, 61, 21))
        self.label_All.setObjectName("label_All")
        self.label_Visito = QtWidgets.QLabel(self.Dashbord_page)
        self.label_Visito.setGeometry(QtCore.QRect(290, 20, 61, 21))
        self.label_Visito.setObjectName("label_Visito")
        self.label_Employee = QtWidgets.QLabel(self.Dashbord_page)
        self.label_Employee.setGeometry(QtCore.QRect(120, 20, 61, 21))
        self.label_Employee.setObjectName("label_Employee")
        self.label_Blacklist = QtWidgets.QLabel(self.Dashbord_page)
        self.label_Blacklist.setGeometry(QtCore.QRect(430, 20, 61, 21))
        self.label_Blacklist.setObjectName("label_Blacklist")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.Dashbord_page)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 50, 601, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lcdNumber_Employee = QtWidgets.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_Employee.setObjectName("lcdNumber_Employee")
        self.horizontalLayout.addWidget(self.lcdNumber_Employee)
        self.lcdNumber_Visito = QtWidgets.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_Visito.setObjectName("lcdNumber_Visito")
        self.horizontalLayout.addWidget(self.lcdNumber_Visito)
        self.lcdNumber_Blacklist = QtWidgets.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_Blacklist.setObjectName("lcdNumber_Blacklist")
        self.horizontalLayout.addWidget(self.lcdNumber_Blacklist)
        self.lcdNumber_ALL = QtWidgets.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_ALL.setObjectName("lcdNumber_ALL")
        self.horizontalLayout.addWidget(self.lcdNumber_ALL)
        self.gridLayoutWidget = QtWidgets.QWidget(self.Dashbord_page)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(90, 150, 571, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_graph3_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_graph3_2.setMinimumSize(QtCore.QSize(550, 210))
        self.label_graph3_2.setMaximumSize(QtCore.QSize(550, 210))
        self.label_graph3_2.setStyleSheet("QLabel{ \n"
" \n"
" border-color: rgb(140, 140, 140);\n"
" border-radius:15;\n"
"    padding: 3px;\n"
"    border-style: solid; \n"
" border-width: 2px;\n"
"}")
        # self.baseLayout = QGridLayout()
        self.label_graph3_2.setText("")
        self.label_graph3_2.setObjectName("label_graph3_2")
        self.gridLayout_2.addWidget(self.label_graph3_2, 0, 0, 0, 3)
        # self.baseLayout.addLayout(gridLayout_2, 0, 0, 0, 3)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Dashbord_page)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(90, 380, 571, 161))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_blacklist = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_blacklist.setMinimumSize(QtCore.QSize(0, 0))
        self.label_blacklist.setMaximumSize(QtCore.QSize(800, 300))
        self.label_blacklist.setStyleSheet("QLabel{ \n"
" \n"
" border-color: rgb(140, 140, 140);\n"
" border-radius:15;\n"
"    padding: 3px;\n"
"    border-style: solid; \n"
" border-width: 2px;\n"
"}")
        self.label_blacklist.setText("")
        self.label_blacklist.setObjectName("label_blacklist")
        self.verticalLayout_3.addWidget(self.label_blacklist)
        self.stackedWidget.addWidget(self.Dashbord_page)
        self.Employee_page = QtWidgets.QWidget()
        self.Employee_page.setObjectName("Employee_page")
        self.tableWidget_information = QtWidgets.QTableWidget(self.Employee_page)
        self.tableWidget_information.setGeometry(QtCore.QRect(90, 30, 581, 501))
        self.tableWidget_information.setRowCount(100)
        self.tableWidget_information.setColumnCount(9)
        self.tableWidget_information.setObjectName("tableWidget_information")
        self.stackedWidget.addWidget(self.Employee_page)
        self.Config_page = QtWidgets.QWidget()
        self.Config_page.setObjectName("Config_page")
        self.label_7 = QtWidgets.QLabel(self.Config_page)
        self.label_7.setGeometry(QtCore.QRect(190, 50, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.Config_page)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(190, 80, 236, 131))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.timeEdit_End_config_2 = QtWidgets.QTimeEdit(self.gridLayoutWidget_3)
        self.timeEdit_End_config_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.timeEdit_End_config_2.setObjectName("timeEdit_End_config_2")
        self.gridLayout_4.addWidget(self.timeEdit_End_config_2, 1, 1, 1, 1)
        self.label_End_2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_End_2.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_End_2.setFont(font)
        self.label_End_2.setObjectName("label_End_2")
        self.gridLayout_4.addWidget(self.label_End_2, 1, 0, 1, 1)
        self.timeEdit_start_config_2 = QtWidgets.QTimeEdit(self.gridLayoutWidget_3)
        self.timeEdit_start_config_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.timeEdit_start_config_2.setObjectName("timeEdit_start_config_2")
        self.gridLayout_4.addWidget(self.timeEdit_start_config_2, 0, 1, 1, 1)
        self.label_start_2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_start_2.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_start_2.setFont(font)
        self.label_start_2.setObjectName("label_start_2")
        self.gridLayout_4.addWidget(self.label_start_2, 0, 0, 1, 1)
        self.pushButton_Setshift_2 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_Setshift_2.setObjectName("pushButton_Setshift_2")
        self.gridLayout_4.addWidget(self.pushButton_Setshift_2, 2, 1, 1, 1)
        self.label_Removepad_2 = QtWidgets.QLabel(self.Config_page)
        self.label_Removepad_2.setGeometry(QtCore.QRect(190, 260, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Removepad_2.setFont(font)
        self.label_Removepad_2.setObjectName("label_Removepad_2")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.Config_page)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(310, 310, 101, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_Removepad_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_Removepad_2.setObjectName("pushButton_Removepad_2")
        self.horizontalLayout_3.addWidget(self.pushButton_Removepad_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.Config_page)
        self.comboBox_2.setGeometry(QtCore.QRect(190, 290, 221, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.stackedWidget.addWidget(self.Config_page)
        self.Report = QtWidgets.QWidget()
        self.Report.setObjectName("Report")
        self.label_Start = QtWidgets.QLabel(self.Report)
        self.label_Start.setGeometry(QtCore.QRect(140, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Start.setFont(font)
        self.label_Start.setObjectName("label_Start")
        self.dateEdit_start = QtWidgets.QDateEdit(self.Report)
        self.dateEdit_start.setGeometry(QtCore.QRect(20, 230, 121, 21))
        self.dateEdit_start.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.dateEdit_start.setObjectName("dateEdit_start")
        self.calendarWidget_start = QtWidgets.QCalendarWidget(self.Report)
        self.calendarWidget_start.setGeometry(QtCore.QRect(20, 40, 391, 183))
        self.calendarWidget_start.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.calendarWidget_start.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.calendarWidget_start.setObjectName("calendarWidget_start")
        self.label_End_3 = QtWidgets.QLabel(self.Report)
        self.label_End_3.setGeometry(QtCore.QRect(140, 260, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_End_3.setFont(font)
        self.label_End_3.setObjectName("label_End_3")
        self.dateEdit_End = QtWidgets.QDateEdit(self.Report)
        self.dateEdit_End.setGeometry(QtCore.QRect(20, 480, 121, 22))
        self.dateEdit_End.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.dateEdit_End.setObjectName("dateEdit_End")
        self.calendarWidget_End = QtWidgets.QCalendarWidget(self.Report)
        self.calendarWidget_End.setGeometry(QtCore.QRect(20, 290, 391, 183))
        self.calendarWidget_End.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.calendarWidget_End.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.calendarWidget_End.setObjectName("calendarWidget_End")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.Report)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(440, 70, 291, 151))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.radioButton_personal = QtWidgets.QRadioButton(self.gridLayoutWidget_4)
        self.radioButton_personal.setObjectName("radioButton_personal")
        self.gridLayout_5.addWidget(self.radioButton_personal, 1, 1, 1, 1)
        self.label_Employee_2 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_Employee_2.setFont(font)
        self.label_Employee_2.setObjectName("label_Employee_2")
        self.gridLayout_5.addWidget(self.label_Employee_2, 0, 0, 1, 1)
        self.radioButton_Allemployee = QtWidgets.QRadioButton(self.gridLayoutWidget_4)
        self.radioButton_Allemployee.setObjectName("radioButton_Allemployee")
        self.gridLayout_5.addWidget(self.radioButton_Allemployee, 2, 1, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.gridLayoutWidget_4)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 205, 242))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_12 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_12.setObjectName("checkBox_12")
        self.verticalLayout_2.addWidget(self.checkBox_12)
        self.checkBox_11 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_11.setObjectName("checkBox_11")
        self.verticalLayout_2.addWidget(self.checkBox_11)
        self.checkBox_5 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_2.addWidget(self.checkBox_5)
        self.checkBox_4 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_2.addWidget(self.checkBox_4)
        self.checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_2.addWidget(self.checkBox_2)
        self.checkBox_15 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_15.setObjectName("checkBox_15")
        self.verticalLayout_2.addWidget(self.checkBox_15)
        self.checkBox_3 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_2.addWidget(self.checkBox_3)
        self.checkBox_14 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_14.setObjectName("checkBox_14")
        self.verticalLayout_2.addWidget(self.checkBox_14)
        self.checkBox_13 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_13.setObjectName("checkBox_13")
        self.verticalLayout_2.addWidget(self.checkBox_13)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_5.addWidget(self.scrollArea, 0, 1, 1, 1)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.Report)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(450, 400, 195, 71))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_CSV = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_CSV.setObjectName("pushButton_CSV")
        self.horizontalLayout_4.addWidget(self.pushButton_CSV)
        self.pushButton_PDF = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_PDF.setObjectName("pushButton_PDF")
        self.horizontalLayout_4.addWidget(self.pushButton_PDF)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.Report)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(460, 310, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_OT = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_OT.setObjectName("radioButton_OT")
        self.verticalLayout.addWidget(self.radioButton_OT)
        self.radioButton_Timeattendance = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_Timeattendance.setObjectName("radioButton_Timeattendance")
        self.verticalLayout.addWidget(self.radioButton_Timeattendance)
        self.stackedWidget.addWidget(self.Report)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(19, 96, 170, 380))
        self.label_5.setMinimumSize(QtCore.QSize(170, 380))
        self.label_5.setMaximumSize(QtCore.QSize(170, 380))
        self.label_5.setStyleSheet("QLabel{ \n"
" \n"
" border-color: rgb(140, 140, 140);\n"
" border-radius:15;\n"
"    padding: 3px;\n"
"    border-style: solid; \n"
" border-width: 2px;\n"
"}")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.pushButton_Report_dash = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Report_dash.setGeometry(QtCore.QRect(30, 410, 150, 50))
        self.pushButton_Report_dash.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton_Report_dash.setMaximumSize(QtCore.QSize(150, 50))
        self.pushButton_Report_dash.setStyleSheet("QPushButton {\n"
"  font: 9pt \"Impact\";\n"
"  background-color: qlineargradient(spread:reflect, x1:1, y1:0.505318, x2:1, y2:1, stop:0.4375 rgba(234, 234, 234, 255), stop:1 rgba(192, 192, 192, 255));\n"
"  color: rgb(65, 65, 65);\n"
"  border: 2px solid #ffffff;\n"
"  border-style: solid;\n"
"  border-radius:20;\n"
"  padding: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
" font: 9pt \"Impact\";\n"
" color: rgb(255, 255, 255);\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.159091 rgba(0, 180, 219, 255), stop:1 rgba(97, 218, 223, 255));\n"
"}")
        self.pushButton_Report_dash.setObjectName("pushButton_Report_dash")
        self.pushButton_EmployeeInfo_dash = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_EmployeeInfo_dash.setGeometry(QtCore.QRect(30, 210, 150, 50))
        self.pushButton_EmployeeInfo_dash.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton_EmployeeInfo_dash.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_EmployeeInfo_dash.setFont(font)
        self.pushButton_EmployeeInfo_dash.setStyleSheet("QPushButton {\n"
"  font: 9pt \"Impact\";\n"
"  background-color: qlineargradient(spread:reflect, x1:1, y1:0.505318, x2:1, y2:1, stop:0.4375 rgba(234, 234, 234, 255), stop:1 rgba(192, 192, 192, 255));\n"
"  color: rgb(65, 65, 65);\n"
"  border: 2px solid #ffffff;\n"
"  border-style: solid;\n"
"  border-radius:20;\n"
"  padding: 1px;\n"
"}\n"
"QPushButton:pressed {\n"
" font: 9pt \"Impact\";\n"
" color: rgb(255, 255, 255);\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.159091 rgba(0, 180, 219, 255), stop:1 rgba(97, 218, 223, 255));\n"
"}")
        self.pushButton_EmployeeInfo_dash.setObjectName("pushButton_EmployeeInfo_dash")
        self.pushButton_Dashbord_dash = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Dashbord_dash.setGeometry(QtCore.QRect(30, 110, 150, 50))
        self.pushButton_Dashbord_dash.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton_Dashbord_dash.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_Dashbord_dash.setFont(font)
        self.pushButton_Dashbord_dash.setStyleSheet("QPushButton {\n"
"  font: 12pt \"Impact\";\n"
"  background-color: qlineargradient(spread:reflect, x1:1, y1:0.505318, x2:1, y2:1, stop:0.4375 rgba(234, 234, 234, 255), stop:1 rgba(192, 192, 192, 255));\n"
"  color: rgb(65, 65, 65);\n"
"  border: 2px solid #ffffff;\n"
"  border-style: solid;\n"
"  border-radius:20;\n"
"  padding: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
" font: 12pt \"Impact\";\n"
" color: rgb(255, 255, 255);\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.159091 rgba(0, 180, 219, 255), stop:1 rgba(97, 218, 223, 255));\n"
"}")
        self.pushButton_Dashbord_dash.setObjectName("pushButton_Dashbord_dash")
        self.pushButton_Config_table = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Config_table.setGeometry(QtCore.QRect(30, 310, 150, 50))
        self.pushButton_Config_table.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton_Config_table.setMaximumSize(QtCore.QSize(150, 50))
        self.pushButton_Config_table.setStyleSheet("QPushButton {\n"
"  font: 12pt \"Impact\";\n"
"  background-color: qlineargradient(spread:reflect, x1:1, y1:0.505318, x2:1, y2:1, stop:0.4375 rgba(234, 234, 234, 255), stop:1 rgba(192, 192, 192, 255));\n"
"  color: rgb(65, 65, 65);\n"
"  border: 2px solid #ffffff;\n"
"  border-style: solid;\n"
"  border-radius:20;\n"
"  padding: 3px;\n"
"}\n"
"QPushButton:pressed {\n"
" font: 12pt \"Impact\";\n"
" color: rgb(255, 255, 255);\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.159091 rgba(0, 180, 219, 255), stop:1 rgba(97, 218, 223, 255));\n"
"}")
        self.pushButton_Config_table.setObjectName("pushButton_Config_table")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 950, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(4)
        self.calendarWidget_start.activated['QDate'].connect(self.dateEdit_start.setDate)
        self.calendarWidget_End.activated['QDate'].connect(self.dateEdit_End.setDate)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_Login.setText(_translate("MainWindow", "Login"))
        self.label_Password.setText(_translate("MainWindow", "Password"))
        self.label_Username.setText(_translate("MainWindow", "Username"))
        self.label_ADD.setText(_translate("MainWindow", "Add Pad"))
        self.pushButton_Addpad.setText(_translate("MainWindow", "Add"))
        self.pushButton_Login.setText(_translate("MainWindow", "Login"))
        self.label_All.setText(_translate("MainWindow", "All"))
        self.label_Visito.setText(_translate("MainWindow", "Visito"))
        self.label_Employee.setText(_translate("MainWindow", "Employee"))
        self.label_Blacklist.setText(_translate("MainWindow", "Blacklist"))
        self.label_7.setText(_translate("MainWindow", "Shift Hours Fill"))
        self.label_End_2.setText(_translate("MainWindow", "End: Time"))
        self.label_start_2.setText(_translate("MainWindow", "Start: Time"))
        self.pushButton_Setshift_2.setText(_translate("MainWindow", "Set Shift  "))
        self.label_Removepad_2.setText(_translate("MainWindow", "Remove Pad"))
        self.pushButton_Removepad_2.setText(_translate("MainWindow", "Remove Pad "))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "192.168.0.11"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "192.168.1.23"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "192.168.1.99"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "192.168.1.46"))
        self.label_Start.setText(_translate("MainWindow", "Start Date"))
        self.label_End_3.setText(_translate("MainWindow", "End Date"))
        self.radioButton_personal.setText(_translate("MainWindow", "personal"))
        self.label_Employee_2.setText(_translate("MainWindow", "Employee "))
        self.radioButton_Allemployee.setText(_translate("MainWindow", "All Employee"))
        self.checkBox_12.setText(_translate("MainWindow", "มีนา คาแคร์ 59001452"))
        self.checkBox_11.setText(_translate("MainWindow", "มีนา หมูกระทะ 5878562"))
        self.checkBox_5.setText(_translate("MainWindow", " ง่วงนอน ขี้เกียจคิด 8887554"))
        self.checkBox_4.setText(_translate("MainWindow", "สมชาย ขายกัญ"))
        self.checkBox.setText(_translate("MainWindow", "กัญชัน วันหยุด"))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_15.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_3.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_14.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_13.setText(_translate("MainWindow", "CheckBox"))
        self.pushButton_CSV.setText(_translate("MainWindow", "CSV"))
        self.pushButton_PDF.setText(_translate("MainWindow", "PDF"))
        self.radioButton_OT.setText(_translate("MainWindow", "OT"))
        self.radioButton_Timeattendance.setText(_translate("MainWindow", "Time attendance"))
        self.pushButton_Report_dash.setText(_translate("MainWindow", "Report exportation"))
        self.pushButton_EmployeeInfo_dash.setText(_translate("MainWindow", "Employee Information"))
        self.pushButton_Dashbord_dash.setText(_translate("MainWindow", "Dashbord"))
        self.pushButton_Config_table.setText(_translate("MainWindow", "Configulation"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
