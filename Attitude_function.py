import random
from PyQt5.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import get_px4_information


class AttPlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=50, connection = None):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)  # 2D 折線圖
        super().__init__(fig)
        self.setParent(parent)
        self.connection = connection
        # 初始化數據
        self.x_attitude_data, self.y_attitude_data, self.z_attitude_data = [], [], []

        # 初始化繪圖
        self.init_plot()

        # 設置定時器更新數據
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_plot)  # 每次 timeout 時更新數據
        self.timer.start(100)  # 每 50ms 更新一次數據

    def init_plot(self):
        """初始化繪圖"""
        self.axes.clear()
        self.axes.set_title("IMU Attitude Data")
        self.axes.set_xlabel("Time")
        self.axes.set_ylabel("Amplitude (degrees)")
        self.line_attitude_x, = self.axes.plot([], [], label="X-axis", color="r")
        self.line_attitude_y, = self.axes.plot([], [], label="Y-axis", color="g")
        self.line_attitude_z, = self.axes.plot([], [], label="Z-axis", color="b")
        self.axes.legend()

    def update_plot(self):
        """更新繪圖數據"""
        # 獲取最新數據
        if self.connection != None:
            attitude_data = get_px4_information.get_attitude(self.connection)
            if attitude_data:
                x, y, z = attitude_data
                self.x_attitude_data.append(x)
                self.y_attitude_data.append(y)
                self.z_attitude_data.append(z)

                # 更新數據到曲線
                self.line_attitude_x.set_data(range(len(self.x_attitude_data)), self.x_attitude_data)
                self.line_attitude_y.set_data(range(len(self.y_attitude_data)), self.y_attitude_data)
                self.line_attitude_z.set_data(range(len(self.z_attitude_data)), self.z_attitude_data)

                # 動態調整 X 和 Y 軸範圍
                self.axes.set_xlim(max(0, len(self.x_attitude_data) - 50), len(self.x_attitude_data))
                self.axes.set_ylim(
                    min(min(self.x_attitude_data), min(self.y_attitude_data), min(self.z_attitude_data)) - 10,
                    max(max(self.x_attitude_data), max(self.y_attitude_data), max(self.z_attitude_data)) + 10,
                )

            # 刷新畫布
            self.draw()
    
    def close_att(self):
        """關閉圖形窗口"""
        self.connection = None
        # 關閉窗口
        self.close()  # 調用 QWidget 的 close 方法來關閉窗口
