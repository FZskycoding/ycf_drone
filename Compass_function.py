import sys
import math
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
import get_px4_information

class Compass(QWidget):
    def __init__(self, parent=None, width=5, height=4, dpi=50, connection=None):
        super().__init__(parent)

        # 初始化 Matplotlib 畫布
        self.canvas = FigureCanvas(Figure(figsize=(5, 5)))
        self.ax = self.canvas.figure.add_subplot(111, polar=True)  # 使用極座標
        self.setup_plot()
        self.connection = connection
        self.direction_angle = 0
        # 將畫布添加到 PyQt 的布局中
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        # 初始設置指針方向為從數據獲取（如從 PX4 獲取）
        if self.connection != None:
            self.direction_angle = get_px4_information.get_compass(self.connection)  # 初始化航向角度
        
        # 動態更新羅盤的動畫，使用 blit=True 以提高性能
        self.animation = FuncAnimation(self.canvas.figure, self.update_compass, interval=50, blit=True)

    def setup_plot(self):
        """初始化羅盤圖表"""
        # 設置極座標
        self.ax.set_theta_zero_location("N")  # 設置北方為 0 度
        self.ax.set_theta_direction(-1)  # 順時針方向
        self.ax.set_ylim(0, 1)  # 半徑範圍

        # 添加圓環和標記
        self.ax.grid(True)
        self.ax.set_yticks([])  # 隱藏半徑標記
        self.ax.set_xticks([0, math.pi/2, math.pi, 3*math.pi/2])  # N, E, S, W
        self.ax.set_xticklabels(['N', 'E', 'S', 'W'])  # 設置標籤

        # 初始化指針
        self.pointer, = self.ax.plot([], [], color="red", linewidth=2)

    def update_compass(self, frame):
        """更新羅盤指針的方向"""
        if self.connection != None:
    
            yaw = get_px4_information.get_compass(self.connection)  # 從 PX4 獲取航向角
            self.direction_angle = yaw  # 更新航向角
            
            # 更新指針數據
            self.pointer.set_data([self.direction_angle, self.direction_angle], [0, 1])  # 起點與終點的數據
            
            # 返回更新的指針，使其與 blit=True 兼容
            return [self.pointer]
        self.pointer.set_data([0, 0], [0, 1])
        return [self.pointer]
    
    def close_compass(self):
        """關閉圖形窗口"""
        self.connection = None

        # 關閉窗口
        self.close()  # 調用 QWidget 的 close 方法來關閉窗口



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Compass()
    main_window.show()
    sys.exit(app.exec_())
