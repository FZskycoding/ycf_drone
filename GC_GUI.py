# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'groundc.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1279, 796)
        self.FunctionBtn_groupbox = QtWidgets.QGroupBox(Form)
        self.FunctionBtn_groupbox.setGeometry(QtCore.QRect(0, 0, 1281, 71))
        self.FunctionBtn_groupbox.setTitle("")
        self.FunctionBtn_groupbox.setObjectName("FunctionBtn_groupbox")
        self.pushButton = QtWidgets.QPushButton(self.FunctionBtn_groupbox)
        self.pushButton.setGeometry(QtCore.QRect(800, 10, 151, 51))
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.FunctionBtn_groupbox)
        self.pushButton_2.setGeometry(QtCore.QRect(960, 10, 151, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.connect_btn = QtWidgets.QPushButton(self.FunctionBtn_groupbox)
        self.connect_btn.setGeometry(QtCore.QRect(1120, 10, 151, 51))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.connect_btn.setFont(font)
        self.connect_btn.setIconSize(QtCore.QSize(16, 16))
        self.connect_btn.setObjectName("connect_btn")
        self.Time_label = QtWidgets.QLabel(self.FunctionBtn_groupbox)
        self.Time_label.setGeometry(QtCore.QRect(10, 10, 231, 51))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.Time_label.setFont(font)
        self.Time_label.setText("")
        self.Time_label.setObjectName("Time_label")
        self.Acc_groupbox = QtWidgets.QGroupBox(Form)
        self.Acc_groupbox.setGeometry(QtCore.QRect(0, 70, 400, 200))
        self.Acc_groupbox.setTitle("")
        self.Acc_groupbox.setObjectName("Acc_groupbox")
        self.Map_groupbox = QtWidgets.QGroupBox(Form)
        self.Map_groupbox.setGeometry(QtCore.QRect(400, 150, 521, 641))
        self.Map_groupbox.setTitle("")
        self.Map_groupbox.setObjectName("Map_groupbox")
        self.Gps_groupbox = QtWidgets.QGroupBox(Form)
        self.Gps_groupbox.setGeometry(QtCore.QRect(920, 70, 361, 200))
        self.Gps_groupbox.setTitle("")
        self.Gps_groupbox.setObjectName("Gps_groupbox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.Gps_groupbox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 301, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.GpsNum_fixed_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.GpsNum_fixed_label.setFont(font)
        self.GpsNum_fixed_label.setObjectName("GpsNum_fixed_label")
        self.horizontalLayout.addWidget(self.GpsNum_fixed_label)
        self.GpsNum_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.GpsNum_label.setFont(font)
        self.GpsNum_label.setText("")
        self.GpsNum_label.setObjectName("GpsNum_label")
        self.horizontalLayout.addWidget(self.GpsNum_label)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.Gps_groupbox)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 80, 301, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Lon_fixed_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont() 
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.Lon_fixed_label.setFont(font)
        self.Lon_fixed_label.setObjectName("Lon_fixed_label")
        self.horizontalLayout_2.addWidget(self.Lon_fixed_label)
        self.Lon_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.Lon_label.setFont(font)
        self.Lon_label.setText("")
        self.Lon_label.setObjectName("Lon_label")
        self.horizontalLayout_2.addWidget(self.Lon_label)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.Gps_groupbox)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 140, 301, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Lat_fixed_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.Lat_fixed_label.setFont(font)
        self.Lat_fixed_label.setObjectName("Lat_fixed_label")
        self.horizontalLayout_3.addWidget(self.Lat_fixed_label)
        self.Lat_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.Lat_label.setFont(font)
        self.Lat_label.setText("")
        self.Lat_label.setObjectName("Lat_label")
        self.horizontalLayout_3.addWidget(self.Lat_label)
        self.Attitude_groupbox = QtWidgets.QGroupBox(Form)
        self.Attitude_groupbox.setGeometry(QtCore.QRect(0, 270, 400, 200))
        self.Attitude_groupbox.setTitle("")
        self.Attitude_groupbox.setObjectName("Attitude_groupbox")
        self.Spiritlevel_groupbox = QtWidgets.QGroupBox(Form)
        self.Spiritlevel_groupbox.setGeometry(QtCore.QRect(0, 470, 400, 321))
        self.Spiritlevel_groupbox.setTitle("")
        self.Spiritlevel_groupbox.setObjectName("Spiritlevel_groupbox")
        self.Region_groupbox = QtWidgets.QGroupBox(Form)
        self.Region_groupbox.setGeometry(QtCore.QRect(400, 70, 521, 81))
        self.Region_groupbox.setTitle("")
        self.Region_groupbox.setObjectName("Region_groupbox")
        self.Region_label = QtWidgets.QLabel(self.Region_groupbox)
        self.Region_label.setGeometry(QtCore.QRect(10, 10, 501, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)
        self.Region_label.setFont(font)
        self.Region_label.setLineWidth(1)
        self.Region_label.setText("")
        self.Region_label.setObjectName("Region_label")
        self.Airpressure_groupBox = QtWidgets.QGroupBox(Form)
        self.Airpressure_groupBox.setGeometry(QtCore.QRect(920, 270, 361, 200))
        self.Airpressure_groupBox.setTitle("")
        self.Airpressure_groupBox.setObjectName("Airpressure_groupBox")
        self.Compass_groupbox = QtWidgets.QGroupBox(Form)
        self.Compass_groupbox.setGeometry(QtCore.QRect(920, 470, 361, 321))
        self.Compass_groupbox.setTitle("")
        self.Compass_groupbox.setObjectName("Compass_groupbox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.pushButton_2.setText(_translate("Form", "PushButton"))
        self.connect_btn.setText(_translate("Form", "Connect"))
        self.GpsNum_fixed_label.setText(_translate("Form", "衛星數量:"))
        self.Lon_fixed_label.setText(_translate("Form", "經度:"))
        self.Lat_fixed_label.setText(_translate("Form", "緯度:"))
