# aMAP_stride_championship
## 2024-10-05 

# Rosbag으로 이미지 토픽 Record하기
---
### 데모(연습)
홈(~) 경로에서 현재 레포지토리를 깃 클론합니다.
```bash
$ git clone https://github.com/Sejong-AIV/rosbag2capturedImage
```
rosbags폴더의 하위 파일(rosbag2image.py, test.bag)들을 이용해서 연습해봅시다.\
먼저 rosbag play를 통해서 test.bag에 어떤 토픽이 record 되었는지 봅시다.
```bash
$ # ~/rosbags 폴더로 이동.
$ cd rosbags

# rosbag play하기
# 양식:rosbag play /path/to/your/file.bag
$ rosbag play ./test.bag
```
다른 터미널에서 rostopic list를 사용하면,/image_jpeg_lane/compressed /image_jpeg_traffic/compressed로 모두 CompressedImage 타입의 이미지토픽이 녹화된 것을 확인 할 수 있습니다.(rostopic info로 타입 조회 가능)

첨부한 rosbag2image.py 파일을 통해서 실행하여, 특정 FPS로 CompressedImage타입의 토픽을 캡쳐해서 .jpg로 만들 수 있습니다.
```bash
# ~ /rosbag 폴더에서
$ python rosbag2image.py
# or python3 rosbag2image.py 
```

ls명령어를 통해, 캡쳐된 이미지를 조회할 수 있습니다. \
(추가적으로, test.bag를 시각화하려면, rviz로 토픽을 구독해서 확인 할 수 있습니다.)

---
### rosbag으로 record하기(추가)
```bash
# ~ 경로에 rosbag저장 폴더 만들기
$ mkdir rosbags

# ~/rosbags 폴더에 rosbag record하기
# 양식:rosbag record -O </path/to/directory/name.bag> <topic1> <topic2> 
$ rosbag record -O ~/rosbags/test.bag /image_jpeg_lane/compressed /image_jpeg_traffic/compressed
```