from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QThread
from GC_GUI import Ui_Form
from Acc_function import AccPlotCanvas
from Attitude_function import AttPlotCanvas
from Spiritlevel_function import GyroscopeSimulator
from Map_function import MapViewer
from Compass_function import Compass
import get_px4_information
import Region_function

from pymavlink import mavutil
import datetime
from PyQt5.QtCore import QTimer

class TimeUpdater(QtCore.QThread):
    time_updated = QtCore.pyqtSignal(str)
    def run(self):
        while True:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.time_updated.emit(now)
            self.msleep(1000)  # 每秒更新一次


class MainWindow(QtWidgets.QMainWindow):

    #加入實時更新時間function
    def update_time_label(self, time_str):
        self.ui.Time_label.setText(time_str)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.connection = None
        self.timer = QTimer()
            

        #引入Map地圖
        map_plot = MapViewer(self.ui.Map_groupbox, width=5, height=4, dpi=100)
        layout = self.ui.Map_groupbox.layout()
        if layout is None:
            layout = QtWidgets.QVBoxLayout(self.ui.Map_groupbox)
            self.ui.Map_groupbox.setLayout(layout)
        layout.addWidget(map_plot)

        #加入實時更新時間
        self.time_updater = TimeUpdater()
        self.time_updater.time_updated.connect(self.update_time_label)
        self.time_updater.start()
        #
        self.ui.connect_btn.clicked.connect(self.toggle_connection)
   

    def toggle_connection(self):
        """Toggle connection to Pixhawk."""
        if self.connection:  # Currently connected, so disconnect
            self.disconnect_pixhawk()
        else:  # Currently disconnected, so connect
            self.connect_pixhawk()

    def connect_pixhawk(self):
        """Connect to the Pixhawk device."""
        try:
            
            self.connection = get_px4_information.connect_to_px4('COM4',115200)
            self.ui.connect_btn.setText("Disconnect")
            self.timer.start(500)
            self.timer.timeout.connect(self.update_gps)    
            self.compass_init()
            self.spiritlevel_init()
            self.acc_init()
            self.att_init()
        except Exception as e:
            print(f"Status: Connection failed ({e})")

    def disconnect_pixhawk(self):      
        if self.connection:
            self.connection.close()  # Close the MAVLink connection
            self.connection = None
            self.compass_plot.close_compass()
            self.spi_plot.close_spiritlevel()
            self.acc_plot.close_acc()
            self.att_plot.close_att()
            self.ui.connect_btn.setText("Connect")

    def compass_init(self):
        #引入Campass資訊
        self.compass_plot = Compass(self.ui.Compass_groupbox, width=5, height=4, dpi=50, connection=self.connection)
        
        layout = self.ui.Compass_groupbox.layout()
        if layout is None:
            layout = QtWidgets.QVBoxLayout(self.ui.Compass_groupbox)
            self.ui.Compass_groupbox.setLayout(layout)
        layout.addWidget(self.compass_plot)
        #

    #引入Region地區名稱
    def update_gps(self):
        self.lon, self.lat = get_px4_information.get_gps_position(self.connection)
        self.satellites = get_px4_information.get_satellites(self.connection)
        self.ui.Region_label.setText(Region_function.get_location_name(self.lat, self.lon))
        #引入Gps資訊
        self.ui.GpsNum_label.setText(str(self.satellites))
        self.ui.Lon_label.setText(str(self.lon))
        self.ui.Lat_label.setText(str(self.lat))
    #
    def spiritlevel_init(self):
        #引入spiritlevel水平儀
        self.spi_plot = GyroscopeSimulator(self.ui.Spiritlevel_groupbox, width=5, height=4, dpi=50, connection=self.connection)

        layout = self.ui.Spiritlevel_groupbox.layout()
        if layout is None:
            layout = QtWidgets.QVBoxLayout(self.ui.Spiritlevel_groupbox)
            self.ui.Spiritlevel_groupbox.setLayout(layout)
        layout.addWidget(self.spi_plot)
        #  
    def acc_init(self):
        #引入ACC折線圖
        self.acc_plot = AccPlotCanvas(self.ui.Acc_groupbox, width=5, height=4, dpi=50, connection=self.connection)
        layout = self.ui.Acc_groupbox.layout()
        if layout is None:
            layout = QtWidgets.QVBoxLayout(self.ui.Acc_groupbox)
            self.ui.Acc_groupbox.setLayout(layout)
        layout.addWidget(self.acc_plot)
        #

    def att_init(self):
        #引入Attitude折線圖
        self.att_plot = AttPlotCanvas(self.ui.Attitude_groupbox, width=5, height=4, dpi=50, connection=self.connection)
        layout = self.ui.Attitude_groupbox.layout()
        if layout is None:
            layout = QtWidgets.QVBoxLayout(self.ui.Attitude_groupbox)
            self.ui.Attitude_groupbox.setLayout(layout)
        layout.addWidget(self.att_plot)
        #  

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())





        
