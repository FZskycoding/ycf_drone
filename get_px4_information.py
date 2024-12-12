from pymavlink import mavutil
import math
# 連接到 Pixhawk
def connect_to_px4(com,baud):
    connection = mavutil.mavlink_connection(com, baud)
    # 等待心跳信號以確認連接成功
    connection.wait_heartbeat()

    # 請求更高頻率的 IMU 資料
    connection.mav.request_data_stream_send(
        connection.target_system,
        connection.target_component,
        mavutil.mavlink.MAV_DATA_STREAM_RAW_SENSORS,  # 請求 IMU 資料
        10,  # 訊息頻率（例如 10 Hz）
        1  # 開始傳送
    )

    connection.mav.request_data_stream_send(
        connection.target_system,
        connection.target_component,
        mavutil.mavlink.MAV_DATA_STREAM_EXTRA1,  # 姿態資料
        10,  # 訊息頻率（例如 10 Hz）
        1  # 開始傳送
    )

    connection.mav.request_data_stream_send(
        connection.target_system,
        connection.target_component,
        mavutil.mavlink.MAV_DATA_STREAM_POSITION,  # 位置資料
        5,  # 訊息頻率（例如 5 Hz）
        1  # 開始傳送
    )
    return connection


def get_angular_velocity(connection):
    while connection:
        msg = connection.recv_match(blocking=True)
        if not msg:
            continue

        # 顯示訊息類型以確認接收的訊息
        msg_type = msg.get_type()
        #print(f"接收到的訊息類型: {msg_type}")
        # 顯示陀螺儀數據 (單位：mrad/s)
        if msg_type == 'RAW_IMU':
            #print(f"陀螺儀 - x: {msg.xgyro}, y: {msg.ygyro}, z: {msg.zgyro}")
            return msg.xgyro,msg.ygyro,msg.zgyro
        

def get_attitude(connection):
    while connection:
        msg = connection.recv_match(blocking=True)
        if not msg:
            continue
        msg_type = msg.get_type()
        # 取得俯仰角、橫滾角、航向角 (弧度轉度數)
        if msg_type == "ATTITUDE":
            roll = math.degrees(msg.roll)   # 橫滾角
            pitch = math.degrees(msg.pitch) # 俯仰角
            yaw = math.degrees(msg.yaw)     # 航向角
            return roll, pitch, yaw
        #return roll,pitch,yaw

def get_gps_position(connection):
    while connection:
        msg = connection.recv_match(blocking=True)
        if not msg:
            continue
        msg_type = msg.get_type()
        if msg_type == "GLOBAL_POSITION_INT":
            lon = msg.lon / 1e7 
            lat = msg.lat / 1e7 
            return lon, lat
        #return roll,pitch,yaw

def get_satellites(connection):
    while connection:
        msg = connection.recv_match(blocking=True)
        if not msg:
            continue
        msg_type = msg.get_type()
        if msg_type == "GPS_RAW_INT":
            satellites_visible = msg.satellites_visible
            # print(satellites_visible)
            return satellites_visible

def get_compass(connection):
    while connection:
        msg = connection.recv_match(blocking=True)
        if not msg:
            continue
        msg_type = msg.get_type()
        # 取得俯仰角、橫滾角、航向角 (弧度轉度數)
        if msg_type == "ATTITUDE":
            yaw = msg.yaw    # 航向角
            yaw = (yaw + math.pi / 2) % (2 * math.pi)  # 使 yaw 在 [0, 2π] 範圍內
            return yaw
        

# connection = connect_to_px4('COM4',115200)
# print(get_satellites(connection))
# print(get_gps_position(connection))
