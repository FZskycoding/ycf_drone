from PyQt5.QtCore import QTimer
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import get_px4_information

class GyroscopeSimulator(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100, connection = None):
        # 初始化圖形窗口
        self.fig, self.ax = plt.subplots(figsize=(width, height), dpi=dpi)
        self.circle = plt.Circle((0.5, 0.5), 0.4, color='lightgray', ec='black', lw=2)
        self.ax.add_patch(self.circle)
        self.horizontal_line, = self.ax.plot([], [], color='blue', lw=2)
        self.vertical_line, = self.ax.plot([], [], color='red', lw=2)
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 1)
        self.ax.set_aspect('equal')
        self.ax.plot(0.5, 0.5, marker='o', color='black', markersize=5)
        self.x_offset = 0
        self.y_offset = 0
        super().__init__(self.fig)
        self.connection = connection
        # 設置定時器
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_plot)  # 每次定時器觸發時更新圖像
        self.timer.start(50)  # 每 100 毫秒更新一次

    def update_plot(self):
        # 從實際數據源（如 get_px4_information）獲取數據
        if self.connection != None:
            attitude_data = get_px4_information.get_attitude(self.connection)
            roll, pitch, _ = attitude_data
            self.x_offset = roll / 45.0 * 0.4  # 假設 Roll 範圍是 ±45°
            self.y_offset = pitch / 45.0 * 0.4  # 假設 Pitch 範圍是 ±45°

            # 更新十字交叉線的位置
            self.horizontal_line.set_data([0.1, 0.9], [0.5 + self.y_offset, 0.5 + self.y_offset])
            self.vertical_line.set_data([0.5 + self.x_offset, 0.5 + self.x_offset], [0.1, 0.9])

            # 刷新圖形
            self.draw()
            
    def close_spiritlevel(self):
        """關閉圖形窗口"""
        self.connection = None
        # 關閉窗口
        self.close()  # 調用 QWidget 的 close 方法來關閉窗口
