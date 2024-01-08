"""
_*_ coding utf-8 _*_
 @Author: 水煮蛋
 @Email: 3220064177@qq.com
 @FileName: handCTRL.py
 @DateTime: 2024-1-8 上午 10:33
 @SoftWare: PyCharm
"""
import cv2
from handsDetect import HandDetector
from handCTRL import HandCTRL

camera = cv2.VideoCapture(0)
hand_detector = HandDetector()
hand_ctrl = HandCTRL()

while True:
    success, img = camera.read()  # read()函数会返回两个值，一个是是否成功，一个是获取的图像
    img = cv2.flip(img, 1)  # 屏幕反转
    if success:
        # hand_detector.process(img)
        hand_ctrl.ctrl(img) #模拟鼠标控制
        cv2.imshow("camera", img)
    k = cv2.waitKey(1)  # 1ms
    if k == ord('q'):
        break

camera.release()  # 释放摄像头
cv2.destroyWindow("camera")  # 关闭窗口