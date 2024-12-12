import sys
import random
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
import get_px4_information
import numpy as np


class Barometer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 初始化 Matplotlib 畫布
        self.canvas = FigureCanvas(Figure(figsize=(5, 5)))
        self.ax = self.canvas.figure.add_subplot(111, polar=True)  # 使用極座標
        self.setup_plot()

        # 將畫布添加到 PyQt 的布局中
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        # 初始化氣壓值
        self.pressure = 1013  # 預設氣壓值 (hPa)

        # 動態更新氣壓計的動畫
        self.animation = FuncAnimation(self.canvas.figure, self.update_barometer, interval=1000, blit=False)

    def setup_plot(self):
        """初始化氣壓計圖表"""
        # 設置極座標
        self.ax.set_theta_zero_location("N")  # 將北方設為 0 度
        self.ax.set_theta_direction(-1)  # 設置順時針方向

        # 設置儀表盤的刻度範圍（900 hPa ~ 1100 hPa）
        min_pressure = 900
        max_pressure = 1100
        num_ticks = 11  # 刻度數量

        # 設置刻度
        angles = np.linspace(0, 2 * np.pi, num_ticks, endpoint=False)
        labels = [f"{int(p)}" for p in np.linspace(min_pressure, max_pressure, num_ticks, endpoint=False)]
        self.ax.set_xticks(angles)
        self.ax.set_xticklabels(labels)

        # 添加圓環和網格
        self.ax.set_ylim(0, 1)
        self.ax.grid(True)

        # 初始化指針
        self.pointer, = self.ax.plot([], [], color="red", linewidth=2)

    def update_barometer(self, frame):
        """更新氣壓計的指針位置"""
        # 模擬氣壓數據（可替換為實際數據）
        self.pressure = random.uniform(900, 1100)  # 模擬氣壓範圍 (900~1100 hPa)

        # 計算指針的角度
        min_pressure = 900
        max_pressure = 1100
        pressure_range = max_pressure - min_pressure
        angle = (self.pressure - min_pressure) / pressure_range * 2 * np.pi  # 將氣壓數據映射到 0~2π 弧度範圍

        # 更新指針數據
        self.pointer.set_data([angle, angle], [0, 1])  # 起點與終點的數據
        return self.pointer,


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Barometer()
    main_window.show()
    sys.exit(app.exec_())
