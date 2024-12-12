import folium
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QVBoxLayout, QWidget
import get_px4_information
import io

class MapViewer(QWidget):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        super().__init__(parent)
        # 設置QWebEngineView並將其添加到布局
        self.map_view = QWebEngineView(self)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.map_view)

        # 初始化地圖位置和標記
        lon, lat = 120.6622577, 24.13261135  #get_px4_information.get_gps_position()
        self.latitude, self.longitude = lat, lon  # 初始位置
        self.initialize_map()

    def initialize_map(self):
        # 創建地圖對象
        self.map = folium.Map(location=[self.latitude, self.longitude], zoom_start=14)

        # 初始標記
        self.marker = folium.Marker(
            [self.latitude, self.longitude],
            tooltip="Drone Position"
        )
        self.marker.add_to(self.map)

        # 將地圖保存到 HTML 中
        self.map_data = io.BytesIO()
        self.map.save(self.map_data, close_file=False)
        self.map_view.setHtml(self.map_data.getvalue().decode())

    def update_map(self, latitude, longitude):
        # 更新地圖的標記位置
        self.latitude, self.longitude = latitude, longitude
        self.marker.location = [self.latitude, self.longitude]

        # 重新保存並顯示更新後的地圖
        self.map_data.seek(0)
        self.map.save(self.map_data, close_file=False)
        self.map_view.setHtml(self.map_data.getvalue().decode())

