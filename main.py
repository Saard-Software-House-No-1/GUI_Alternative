import sys
import os.path
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtChart import (QAreaSeries, QBarSet, QChart, QChartView,
                           QLineSeries, QPieSeries, QScatterSeries, QSplineSeries,
                           QStackedBarSeries, QPieSlice)
from PyQt5.QtCore import pyqtSlot, QPointF, Qt, QMargins
from PyQt5.QtGui import QColor, QPainter, QPalette, QFont
from PyQt5.QtWidgets import (QCheckBox, QComboBox, QGridLayout, QHBoxLayout,
                             QLabel, QSizePolicy, QWidget)
from dataextraction.GetEmployeeInfo import getEmployeeInfo
from dataextraction.GetDashboardInfo import *
import datetime

from generate_csv.generate_csv import generate_csv

from App_UI_LOG import Ui_MainWindow
from ApiModule.TimeAttendaceAPI import *


config_dict = {'shift_start':(9,0),'shift_end':(18,0)}

class MainWindow:
    def __init__(self):
        
        if os.path.isfile('URL.txt'):
            f = open("URL.txt", "r")

        else:
            f = open("URL.txt","w+")

        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.P = 0
        self.url = []
        f=open("URL.txt", "r")
        line = f.readlines()
        
        for i in line:
            i = i.replace('\n','')
            self.url.append(i)
        f.close()

        self.User = str(self.ui.lineEdit_Username.text())
        self.Passwd = str(self.ui.lineEdit_Password.text())
        self.click = 0
        
        self.ui.stackedWidget.setCurrentWidget(self.ui.Login)
        self.ui.pushButton_Dashbord_dash.clicked.connect(self.Dashbord)
        self.ui.pushButton_EmployeeInfo_dash.clicked.connect(self.Employee)
        self.ui.pushButton_Config_table.clicked.connect(self.Config)
        self.ui.pushButton_Report_dash.clicked.connect(self.Report)
        self.ui.pushButton_Login.clicked.connect(self.log_in)
        self.ui.pushButton_Addpad.clicked.connect(self.Add_Pad)
        self.ui.pushButton_CSV.clicked.connect(self.export_csv)
        self.ui.pushButton_Setshift_2.clicked.connect(self.setShift)
        self.ui.pushButton_Removepad_2.clicked.connect(self.Remove_Pad)


    def show(self):
        self.main_win.show()
        # self.s = '\n'
        # self.url_show = self.s.join(self.url)
        count = 0
        for ip in self.url:
            self.ui.comboBox_IP_PAD.addItem("")
            self.ui.comboBox_IP_PAD.setItemText(count,ip)
            self.ui.comboBox_2.addItem("")
            self.ui.comboBox_2.setItemText(count,ip)
            count = count+1
        # self.ui.lineEdit_Addpad_show.setText(self.url_show)
        print(self.url)

    def Dashbord(self):
        if self.P == 1:
            self.ui.stackedWidget.setCurrentWidget(self.ui.Dashbord_page)

    def Config(self):
        if self.P == 1:
            self.ui.stackedWidget.setCurrentWidget(self.ui.Config_page)
            
    def Report(self):
        if self.P == 1:
            self.ui.stackedWidget.setCurrentWidget(self.ui.Report)

    def log_in(self):
        global df_person_input , df_record_input
        self.User = str(self.ui.lineEdit_Username.text())
        self.Passwd = str(self.ui.lineEdit_Password.text())

        ##### Test CSV #####
        datetime_input = '2021/02/15'
        df_record_input = pd.read_csv('exportAceesRecord2.csv')
        df_person_input = pd.read_csv('exportGetPerson.csv')
        # Dailay Data
        self.DailyTimeShow , self.user , self.Blacklist = daily_scan(df_record_input, df_person_input, datetime_input)
        # Monthly Data (Function Pending)
        self.MonthlyShow = monthly_scan(df_record_input, df_person_input, datetime_input)
        # self.MonthlyShow = self.DailyTimeShow

        # Yearly Data (Function Pending)
        # self.MonthlyShow = monthly_scan(df_record_input, df_person_input, datetime_input)
        self.YearlyShow = self.DailyTimeShow

        print("blacklist:",self.Blacklist)
        # Add Blacklist
        self.BlacklistText = ["{} : {} ".format(key, value) for key, value in self.Blacklist.items()]
        self.BlacklistShow = "\n".join(self.BlacklistText)
        self.ui.label_blacklist.setText(self.BlacklistShow)
        print(self.BlacklistShow)
        # LCD Show user number
        self.ui.lcdNumber_Employee.setProperty("value", self.user['Employee'])
        self.ui.lcdNumber_Visito.setProperty("value", self.user['Visitor'])
        self.ui.lcdNumber_Blacklist.setProperty("value", self.user['Blacklist'])
        self.All = self.user['Employee']+self.user['Visitor']+self.user['Blacklist']
        self.ui.lcdNumber_ALL.setProperty("value", self.All)
        # Add PieChart
        chartView = QChartView(self.Create_DailyPieChart())
        chartView.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.ui.gridLayout_2.addWidget(chartView)
        chartView2 = QChartView(self.Create_MonthlyPieChart())
        chartView2.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.ui.gridLayout_2.addWidget(chartView2)
        chartView3 = QChartView(self.Create_YearlyPieChart())
        chartView3.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.ui.gridLayout_2.addWidget(chartView3)
        # Login
        self.Log_Run()

        ###### API Test ######

        # self.result_login = get_seria_no(self.url,self.User,self.Passwd)
        # if self.result_login == True:
        # 	df_record_input = access_record('01/02/2021', datetime.today().strftime("%d/%m/%Y"),self.url,self.User,self.Passwd)
        # 	df_person_input = get_persons(self.url,self.User,self.Passwd)
        # 	print (df_person_input)
        # 	datetime_input = datetime.today().strftime("%Y/%m/%d")
        # 	# print (datetime_input)
        # # Daily Data
        # 	self.DailyTimeShow , self.user , self.Blacklist = daily_scan(df_record_input, df_person_input, datetime_input)
        # 	print(self.user,self.DailyTimeShow,self.Blacklist)
        # # Monthly Data
        # self.MonthlyShow = monthly_scan(df_record_input, df_person_input, datetime_input)

        # # Add Blacklist
        #     self.BlacklistText = ["{} : {} ".format(key, value) for key, value in self.Blacklist.items()]
        #     self.BlacklistShow = "\n".join(self.BlacklistText)
        #     self.ui.label_blacklist.setText(self.BlacklistShow)
        # # LCD Show user number
        # 	self.ui.lcdNumber_Employee.setProperty("value", self.user['Employee'])
        # 	self.ui.lcdNumber_Visito.setProperty("value", self.user['Visitor'])
        # 	self.ui.lcdNumber_Blacklist.setProperty("value", self.user['Blacklist'])
        # 	self.All = self.user['Employee']+self.user['Visitor']+self.user['Blacklist']
        # 	self.ui.lcdNumber_ALL.setProperty("value", self.All)
        # # Add PieChart
        #     chartView = QChartView(self.Create_DailyPieChart())
        #     chartView.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        #     self.ui.gridLayout_2.addWidget(chartView)
        #     chartView2 = QChartView(self.Create_MonthlyPieChart())
        #     chartView2.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        #     self.ui.gridLayout_2.addWidget(chartView2)
        #     chartView3 = QChartView(self.Create_YearlyPieChart())
        #     chartView3.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        #     self.ui.gridLayout_2.addWidget(chartView3)
        # 	self.Log_Run()
        # else:
        #     self.P =0

        em_df = getEmployeeInfo(df_person_input)
        em_list = em_df['Name'].unique()

        self.listEmployee = em_list.copy()
        for i,j in enumerate(em_list):
            self.listEmployee[i] = QtWidgets.QCheckBox(self.ui.scrollAreaWidgetContents)
            self.ui.verticalLayout_2.addWidget(self.listEmployee[i])
            self.listEmployee[i].setChecked(False)
            self.listEmployee[i].setText(em_list[i])

    def Employee(self):
        if self.P == 1:
            self.ui.stackedWidget.setCurrentWidget(self.ui.Employee_page)

            """
                Get information in dataframe and add to QTableWidgets
                
                :Param
                df (pandas.core.frame.DataFrame) : person dataframe   
                
            """
            em_df = getEmployeeInfo(df_person_input)

            nRows = len(em_df.index)
            nColumns = len(em_df.columns)
            self.ui.tableWidget_information.setRowCount(nRows)
            self.ui.tableWidget_information.setColumnCount(nColumns)

            for row in range(nRows):
                for column in range(nColumns):
                    data = em_df.iloc[row,column]
                    self.ui.tableWidget_information.setItem(row,column, QTableWidgetItem(data))

    def Add_Pad(self):
        self.url_input = str(self.ui.lineEdit_Addpad.text())
        self.exist = self.url_input in self.url
        if self.exist == False:
            self.ui.lineEdit_Addpad.setText('')
            self.url.append(self.url_input)
            print(self.url)
            f=open("URL.txt","a+")
            f.write(self.url_input + '\n')
            f.close()
            self.ui.comboBox_IP_PAD.addItem("")
            self.ui.comboBox_IP_PAD.setItemText(len(self.url)-1,self.url_input)
            self.ui.comboBox_2.addItem("")
            self.ui.comboBox_2.setItemText(len(self.url)-1,self.url_input)

    def Remove_Pad(self):
        self.select = self.ui.comboBox_2.currentText()
        self.select_index = self.url.index(self.select)
        del self.url[self.select_index]
        self.write = "\n".join(self.url)
        f=open("URL.txt","w+")
        f.write(self.write)
        f.close()
        self.ui.comboBox_IP_PAD.clear()
        self.ui.comboBox_2.clear()
        count = 0
        for ip in self.url:
            self.ui.comboBox_2.addItem("")
            self.ui.comboBox_2.setItemText(count,ip)
            count = count+1

        print(self.write)
            
        
    def Log_Run(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Dashbord_page)
        self.P=1
        
    def Create_DailyPieChart(self):
        self.DailyTimeShowPercent = self.DailyTimeShow
        self.total = self.DailyTimeShow['Ontime']+self.DailyTimeShow['Late']+self.DailyTimeShow['OT']+self.DailyTimeShow['Absence']
        self.DailyTimeShowPercent['Ontime'] = (self.DailyTimeShowPercent['Ontime']*100) / self.total
        self.DailyTimeShowPercent['Late'] = (self.DailyTimeShowPercent['Late']*100) / self.total
        self.DailyTimeShowPercent['OT'] = (self.DailyTimeShowPercent['OT']*100) / self.total
        self.DailyTimeShowPercent['Absence'] = (self.DailyTimeShowPercent['Absence']*100) / self.total
        series = QPieSeries()
        series.append("Ontime", self.DailyTimeShowPercent['Ontime'])
        series.append("Late", self.DailyTimeShowPercent['Late'])
        series.append("OT", self.DailyTimeShowPercent['OT'])
        series.append("Absence", self.DailyTimeShowPercent['Absence'])

        slice = QPieSlice()
        slice = series.slices()[0]
        slice.setLabelVisible(True)
        slice.setLabelFont(QFont('Arial', 7))
        slice = series.slices()[1]
        slice.setLabelVisible(True)
        slice.setLabelFont(QFont('Arial', 7))
        slice = series.slices()[2]
        slice.setLabelVisible(True)
        slice.setLabelFont(QFont('Arial', 7))
        slice = series.slices()[3]
        slice.setLabelVisible(True)
        slice.setLabelFont(QFont('Arial', 7))

        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Daily")
        chart.setMargins(QMargins(0, 0, 0, 0))
        # chart.setTitleFont(QFont('Arial', 5))

        chart.legend().setVisible(False)
        # chart.legend().setAlignment(Qt.AlignBottom)
        chart.legend().markers(series)[0].setLabel("Ontime")
        chart.legend().markers(series)[1].setLabel("Late")
        chart.legend().markers(series)[2].setLabel("OT")
        chart.legend().markers(series)[3].setLabel("Absence")
        return chart


    def Create_MonthlyPieChart(self):
        print(self.MonthlyShow)
        self.MonthlyTimeShowPercent = self.MonthlyShow
        # self.month_total = self.MonthlyShow['Ontime']+self.MonthlyShow['Late']+self.MonthlyShow['OT']+self.MonthlyShow['Absence']
        # print(self.total)
        # self.MonthlyTimeShowPercent['Ontime'] = (self.MonthlyTimeShowPercent['Ontime']*100) / self.month_total
        # self.MonthlyTimeShowPercent['Late'] = (self.MonthlyTimeShowPercent['Late']*100) / self.month_total
        # self.MonthlyTimeShowPercent['OT'] = (self.MonthlyTimeShowPercent['OT']*100) / self.month_total
        # self.MonthlyTimeShowPercent['Absence'] = (self.MonthlyTimeShowPercent['Absence']*100) / self.month_total
        series = QPieSeries()
        series.append("Ontime", float(self.MonthlyShow['Ontime']))
        series.append("Late", float(self.MonthlyShow['Late']))
        series.append("OT", float(self.MonthlyShow['OT']))
        series.append("Absence", float(self.MonthlyShow['Absence']))

        slice = QPieSlice()
        slice = series.slices()[0]
        slice.setLabelVisible(True)
        slice.setLabelFont(QFont('Arial', 7))
        slice = series.slices()[1]
        slice.setLabelVisible(True)
        slice.setLabelFont(QFont('Arial', 7))
        slice = series.slices()[2]
        slice.setLabelVisible(True)
        slice.setLabelFont(QFont('Arial', 7))
        slice = series.slices()[3]
        slice.setLabelVisible(True)
        slice.setLabelFont(QFont('Arial', 7))

        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Monthly")
        chart.setMargins(QMargins(0, 0, 0, 0))
        # chart.setTitleFont(QFont('Arial', 5))

        chart.legend().setVisible(False)
        # chart.legend().setAlignment(Qt.AlignBottom)
        chart.legend().markers(series)[0].setLabel("Ontime")
        chart.legend().markers(series)[1].setLabel("Late")
        chart.legend().markers(series)[2].setLabel("OT")
        chart.legend().markers(series)[3].setLabel("Absence")
        return chart

    def Create_YearlyPieChart(self):
        print(self.YearlyShow)
        self.YearlyTimeShowPercent = self.YearlyShow
        self.year_total = self.YearlyShow['Ontime']+self.YearlyShow['Late']+self.YearlyShow['OT']+self.YearlyShow['Absence']
        print(self.total)
        self.YearlyTimeShowPercent['Ontime'] = (self.YearlyTimeShowPercent['Ontime']*100) / self.year_total
        self.YearlyTimeShowPercent['Late'] = (self.YearlyTimeShowPercent['Late']*100) / self.year_total
        self.YearlyTimeShowPercent['OT'] = (self.YearlyTimeShowPercent['OT']*100) / self.year_total
        self.YearlyTimeShowPercent['Absence'] = (self.YearlyTimeShowPercent['Absence']*100) / self.year_total
        series = QPieSeries()
        series.append("Ontime", self.YearlyTimeShowPercent['Ontime'])
        series.append("Late", self.YearlyTimeShowPercent['Late'])
        series.append("OT", self.YearlyTimeShowPercent['OT'])
        series.append("Absence", self.YearlyTimeShowPercent['Absence'])

        slice = QPieSlice()
        slice = series.slices()[0]
        slice.setLabelVisible(True)
        slice.setLabelFont(QFont('Arial', 7))
        slice = series.slices()[1]
        slice.setLabelVisible(True)
        slice.setLabelFont(QFont('Arial', 7))
        slice = series.slices()[2]
        slice.setLabelVisible(True)
        slice.setLabelFont(QFont('Arial', 7))
        slice = series.slices()[3]
        slice.setLabelVisible(True)
        slice.setLabelFont(QFont('Arial', 7))

        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Yearly")
        chart.setMargins(QMargins(0, 0, 0, 0))
        # chart.setTitleFont(QFont('Arial', 5))

        chart.legend().setVisible(False)
        # chart.legend().setAlignment(Qt.AlignBottom)
        chart.legend().markers(series)[0].setLabel("Ontime")
        chart.legend().markers(series)[1].setLabel("Late")
        chart.legend().markers(series)[2].setLabel("OT")
        chart.legend().markers(series)[3].setLabel("Absence")
        return chart

        self.setCentralWidget(chartview)
    
    def export_csv(self):

        global config_dict 

        csv_checklist = []
        all_employee = []
        
        for i in self.listEmployee:
            print("person " + str(i.text()) + " ischeck " + str(i.isChecked()))
            if(i.isChecked()):
                
                csv_checklist.append(i.text())
            all_employee.append(i.text())

        start_date = self.ui.dateEdit_start.text().split('/')
        start_date_dt = datetime(year=int(start_date[2]), month=int(start_date[0]), day=int(start_date[1]))
        end_date = self.ui.dateEdit_End.text().split('/')
        end_date_dt = datetime(year=int(end_date[2]), month=int(end_date[0]), day=int(end_date[1]))

        print('csv_checklist = '+str(csv_checklist))
        if (self.ui.radioButton_personal.isChecked() and self.ui.radioButton_OT.isChecked()):
            print('personal and ot')
            generate_csv(df_record_input,df_person_input,start_date_dt,end_date_dt,'OT',config_dict,csv_checklist,isAllEmployee = False)
        elif (self.ui.radioButton_personal.isChecked() and self.ui.radioButton_Timeattendance.isChecked()):
            print('personal and time attendance')
            generate_csv(df_record_input,df_person_input,start_date_dt,end_date_dt,'Time attendance',config_dict,csv_checklist,isAllEmployee = False)
        elif (self.ui.radioButton_Allemployee.isChecked() and self.ui.radioButton_OT.isChecked()):
            print('all employee and ot')
            generate_csv(df_record_input,df_person_input,start_date_dt,end_date_dt,'OT',config_dict,all_employee,isAllEmployee = True)
        elif(self.ui.radioButton_Allemployee.isChecked() and self.ui.radioButton_Timeattendance.isChecked()):
            print('all employee and time attendance')
            generate_csv(df_record_input,df_person_input,start_date_dt,end_date_dt,'Time attendance',config_dict,all_employee,isAllEmployee = True)


    def setShift(self):

        global config_dict 
        
        
        shift_start = self.ui.timeEdit_start_config_2.text()
        shift_start_hour = int(shift_start.split(':')[0])
        shift_start_min = int(shift_start.split(':')[1].split(' ')[0])
        am_pm_start = shift_start.split(':')[1].split(' ')[1]

        if am_pm_start =='PM' and shift_start_hour < 12:
            shift_start_hour += 12
        elif am_pm_start =='AM' and shift_start_hour == 12:
            shift_start_hour = 0

        shift_end = self.ui.timeEdit_End_config_2.text()
        shift_end_hour = int(shift_end.split(':')[0])
        shift_end_min = int(shift_end.split(':')[1].split(' ')[0])
        am_pm_end = shift_end.split(':')[1].split(' ')[1]

        if am_pm_end =='PM' and shift_end_hour < 12:
           shift_end_hour += 12
        elif am_pm_end =='AM' and shift_end_hour == 12:
           shift_end_hour = 0
            
        config_dict = {'shift_start':(shift_start_hour,shift_start_min),'shift_end':(shift_end_hour,shift_end_min)}
        print("config_dict " + str(config_dict))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    widget = Ui_MainWindow()
    main_win.show()
    sys.exit(app.exec_())
