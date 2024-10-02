#!/usr/bin/env python3
import rosbag
import cv2
import numpy as np
from cv_bridge import CvBridge
import os

# rosbag 파일 경로
bag_file = 'data235.bag'

# 저장할 이미지 경로
output_folder_lane = f"{bag_file.split('.')[0]}"+"_lane_images"
output_folder_traffic = f"{bag_file.split('.')[0]}"+"_traffic_images"

os.makedirs(output_folder_lane, exist_ok=True)
os.makedirs(output_folder_traffic, exist_ok=True)

# CvBridge 객체 생성
bridge = CvBridge()

# rosbag 열기
with rosbag.Bag(bag_file, 'r') as bag:
    for i, (topic, msg, t) in enumerate(bag.read_messages(topics=['/image_jpeg_lane/compressed'])):
        
        # fps = 30, ignoring under 3 is 10frames_per_sec
        ignore_num = 2
        if i % ignore_num != 0:
            continue

        # 이미지 메시지를 OpenCV 이미지로 변환
        np_arr = np.frombuffer(msg.data, np.uint8)
        cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        name = topic.split('/')[1].split('_')[-1]

        # 파일 이름 생성 (timestamp 또는 카운터 사용 가능)
        filename = f"{output_folder_lane}"+"/"+f"{name}{i:08d}.jpg"
        
        # 이미지 저장
        cv2.imwrite(filename, cv_image)
        print(f"Saved: {filename}")

    for i, (topic, msg, t) in enumerate(bag.read_messages(topics=['/image_jpeg_traffic/compressed'])):
                
        # fps = 30, ignoring under 3 is 10frames_per_sec
        ignore_num = 3
        if i % ignore_num != 0:
            continue

        # 이미지 메시지를 OpenCV 이미지로 변환
        np_arr = np.frombuffer(msg.data, np.uint8)
        cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        name = topic.split('/')[1].split('_')[-1]

        # 파일 이름 생성 (timestamp 또는 카운터 사용 가능)
        filename = f"{output_folder_traffic}"+"/"+f"{name}{i:08d}.jpg"
        
        # 이미지 저장
        cv2.imwrite(filename, cv_image)
        print(f"Saved: {filename}")