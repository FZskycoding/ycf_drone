import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.animation import FuncAnimation

class GyroscopeSimulator:
    def __init__(self):
        # 创建一个绘图窗口
        self.fig, self.ax = plt.subplots(figsize=(6, 6))
        
        # 创建圆形表示陀螺仪面板
        self.circle = plt.Circle((0.5, 0.5), 0.4, color='lightgray', ec='black', lw=2)
        self.ax.add_patch(self.circle)
        
        # 创建两条交叉的线：一条表示横向（左右），一条表示纵向（上下）
        self.horizontal_line, = self.ax.plot([], [], color='blue', lw=2)
        self.vertical_line, = self.ax.plot([], [], color='red', lw=2)
        
        # 设置坐标轴范围
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 1)
        self.ax.set_aspect('equal')
        
        # 绘制圆心
        self.ax.plot(0.5, 0.5, marker='o', color='black', markersize=5)
        
        # 更新偏移数据的初始值
        self.x_offset = 0
        self.y_offset = 0
        
    def update_lines(self):
        # 根据当前的偏移数据更新两条线的位置
        # 水平线更新
        self.horizontal_line.set_data([0.1, 0.9], [0.5 + self.y_offset, 0.5 + self.y_offset])
        
        # 垂直线更新
        self.vertical_line.set_data([0.5 + self.x_offset, 0.5 + self.x_offset], [0.1, 0.9])
        
    def update_data(self, i):
        # 随机生成偏移量（模拟数据）
        self.x_offset = random.uniform(-0.4, 0.4)  # x方向的偏移，范围从-0.4到0.4
        self.y_offset = random.uniform(-0.4, 0.4)  # y方向的偏移，范围从-0.4到0.4
        
        # 更新线条位置
        self.update_lines()
        
        return self.horizontal_line, self.vertical_line

    def show(self):
        # 动态更新十字交叉线的位置
        ani = FuncAnimation(self.fig, self.update_data, frames=100, interval=1000, blit=True)
        plt.show()

# 创建并显示陀螺仪模拟器
gyroscope = GyroscopeSimulator()
gyroscope.show()
