import sys
import os.path
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtWidgets
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt

from dataextraction.GetEmployeeInfo import getEmployeeInfo
from dataextraction.GetDashboardInfo import *

from App_UI_LOG import Ui_MainWindow
# from ApiModule.TimeAttendaceAPI import *


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

        global df_person_input , df_record_input
        
        # df_record_input = access_record('01/01/2020', datetime.today().strftime("%d/%m/%Y"),self.url,self.User,self.Passwd)
        # df_person_input = get_persons(self.url,self.User,self.Passwd)
        # datetime_input = datetime.today().strftime("%Y/%m/%d")
        # self.TimeShow , self.user = daily_scan(df_record_input, df_person_input, datetime_input)

        # Test by CSV
        datetime_input = '2021/01/15'
        df_record_input = pd.read_csv('exportAceesRecord2.csv')
        df_person_input = pd.read_csv('exportGetPerson.csv')
        self.TimeShow , self.user = daily_scan(df_record_input, df_person_input, datetime_input)
        print(self.user)


        # Show User
        self.ui.lcdNumber_Employee.setProperty("value", self.user['Employee'])
        self.ui.lcdNumber_Visito.setProperty("value", self.user['Visitor'])
        self.ui.lcdNumber_Blacklist.setProperty("value", self.user['Blacklist'])
        self.All = self.user['Employee']+self.user['Visitor']+self.user['Blacklist']
        self.ui.lcdNumber_ALL.setProperty("value", self.All)


        self.ui.stackedWidget.setCurrentWidget(self.ui.Login)
        self.ui.pushButton_Dashbord_dash.clicked.connect(self.Dashbord)
        self.ui.pushButton_EmployeeInfo_dash.clicked.connect(self.Employee)
        self.ui.pushButton_Config_table.clicked.connect(self.Config)
        self.ui.pushButton_Report_dash.clicked.connect(self.Report)
        self.ui.pushButton_Login.clicked.connect(self.log_in)
        self.ui.pushButton_Addpad.clicked.connect(self.Add_Pad)
        self.ui.pushButton_CSV.clicked.connect(self.export_csv)


    def show(self):
        self.main_win.show()
        self.s = '\n'
        self.url_show = self.s.join(self.url)
        self.ui.lineEdit_Addpad_show.setText(self.url_show)
        print(self.url)

    def Dashbord(self):
        if self.P == 1:
            self.ui.stackedWidget.setCurrentWidget(self.ui.Dashbord_page)


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

    def Config(self):
        if self.P == 1:
            self.ui.stackedWidget.setCurrentWidget(self.ui.Config_page)
    def Report(self):
        if self.P == 1:

            self.ui.stackedWidget.setCurrentWidget(self.ui.Report)

            em_df = getEmployeeInfo(df_person_input)
            em_list = em_df['Name'].unique()

            self.listEmployee = em_list.copy()

            for i,j in enumerate(em_list):
                self.listEmployee[i] = QtWidgets.QCheckBox(self.ui.scrollAreaWidgetContents)
                self.ui.verticalLayout_2.addWidget(self.listEmployee[i])
                self.listEmployee[i].setText(em_list[i])
            
            
    def log_in(self):
        self.User = str(self.ui.lineEdit_Username.text())
        self.Passwd = str(self.ui.lineEdit_Password.text())
        self.Log_Run()
        # self.result_login = TimeAttendaceAPI.get_seria_no(self.url,self.User,self.Passwd)


        # if self.result_login == True:
        #     self.Log_Run()
        # else:
        #     self.P =0

    def Add_Pad(self):
        self.url_input = str(self.ui.lineEdit_Addpad.text())
        self.exist = self.url_input in self.url
        if self.exist == False:
            self.ui.lineEdit_Addpad.setText('')
            self.url.append(self.url_input)
            f=open("url.txt","a+")
            f.write(self.url_input + '\n')
            f.close()
            self.s = '\n'
            self.url_show = self.s.join(self.url)
            self.ui.lineEdit_Addpad_show.setText(self.url_show)

        
    def Log_Run(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Dashbord_page)
        self.P=1
        
    def create_piechart(self):
        print(self.user)
        series = QPieSeries()
        series.append("Ontime", self.TimeShow['Ontime'])
        series.append("Late", self.TimeShow['Late'])
        series.append("OT", self.TimeShow['OT'])
        series.append("Absence", self.TimeShow['Absence'])

        slice = QPieSlice()
        slice = series.slices()[0]
        slice.setLabelVisible(True)
        slice = series.slices()[1]
        slice.setLabelVisible(True)
        slice = series.slices()[2]
        slice.setLabelVisible(True)
        slice = series.slices()[3]
        slice.setLabelVisible(True)

        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Daily")

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
        chart.legend().markers(series)[0].setLabel("Ontime")
        chart.legend().markers(series)[1].setLabel("Late")
        chart.legend().markers(series)[2].setLabel("OT")
        chart.legend().markers(series)[3].setLabel("Absence")

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(chartview)
    
    def export_csv(self):
        
        csv_checklist = []
        
        for i in self.listEmployee:
            if(i.isChecked()):
                csv_checklist.append(i.text())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
