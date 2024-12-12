from geopy.geocoders import Nominatim

def get_location_name(latitude, longitude):
    geolocator = Nominatim(user_agent="MyAppName_1.0")
    location = geolocator.reverse((latitude, longitude), language='zh-TW')  # 使用中文
    if location:
        return location.address  # 返回地區名稱

    else:
        return "無法查詢位置"
