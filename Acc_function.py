import random
from PyQt5.QtCore import QTimer
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QThread
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import get_px4_information


class AccPlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=50, connection = None):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)  # 2D 折線圖
        super().__init__(fig)
        self.setParent(parent)
        self.connection = connection

        # 初始化數據
        self.x_angular_velocity_data, self.y_angular_velocity_data, self.z_angular_velocity_data = [], [], [] 
        self.max_points = 50  # 折線圖最多顯示的點數

        # 初始化折線圖
        self.line_angular_x, = self.axes.plot([], [], label="x-axis", color="r")
        self.line_angular_y, = self.axes.plot([], [], label="y-axis", color="g")
        self.line_angular_z, = self.axes.plot([], [], label="z-axis", color="b")

        # 設置圖表
        self.axes.set_title("IMU gyroscope data")
        self.axes.set_xlabel("Time")
        self.axes.set_ylabel("Angular velocity (mrad/s)")
        self.axes.legend()

        # 設置定時器更新數據
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_plot)  # 每次timeout時更新圖表
        self.timer.start(100)  # 每50ms更新一次數據

    def update_plot(self):
        # 獲取新數據
        if self.connection != None:
            angular_data = get_px4_information.get_angular_velocity(self.connection)
            if angular_data:
                x, y, z = angular_data
                # 添加新數據
                self.x_angular_velocity_data.append(x)
                self.y_angular_velocity_data.append(y)
                self.z_angular_velocity_data.append(z)

                # 保持數據數量在 max_points 以內
                if len(self.x_angular_velocity_data) > self.max_points:
                    self.x_angular_velocity_data = self.x_angular_velocity_data[-self.max_points:]
                    self.y_angular_velocity_data = self.y_angular_velocity_data[-self.max_points:]
                    self.z_angular_velocity_data = self.z_angular_velocity_data[-self.max_points:]

                # 更新折線圖數據
                self.line_angular_x.set_data(range(len(self.x_angular_velocity_data)), self.x_angular_velocity_data)
                self.line_angular_y.set_data(range(len(self.y_angular_velocity_data)), self.y_angular_velocity_data)
                self.line_angular_z.set_data(range(len(self.z_angular_velocity_data)), self.z_angular_velocity_data)

                # 更新 X 軸和 Y 軸範圍
                self.axes.set_xlim(0, self.max_points)
                self.axes.set_ylim(
                    min(min(self.x_angular_velocity_data), min(self.y_angular_velocity_data), min(self.z_angular_velocity_data)) - 2000,
                    max(max(self.x_angular_velocity_data), max(self.y_angular_velocity_data), max(self.z_angular_velocity_data)) + 2000,
                )
                # 重繪圖表
                self.draw()
    def close_acc(self):
        """關閉圖形窗口"""
        self.connection = None
        # 關閉窗口
        self.close()  # 調用 QWidget 的 close 方法來關閉窗口
