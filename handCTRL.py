"""
_*_ coding utf-8 _*_
 @Author: 水煮蛋
 @Email: 3220064177@qq.com
 @FileName: handCTRL.py
 @DateTime: 2024-1-8 上午 10:33
 @SoftWare: PyCharm
"""
import cv2
import pynput
from handsDetect import HandDetector


class HandCTRL():
    def __init__(self):
        self.ctr = pynput.mouse.Controller()
        self.hand_detector = HandDetector()
        self.flag = 1  # 初始化flag变量

    def ctrl(self,img):

        hand_L = 'Left'
        tips = [4, 8, 12, 16, 20]
        tip_data = {4: 0, 8: 0, 12: 0, 16: 0, 20: 0}

        self.hand_detector.process(img)
        position = self.hand_detector.find_position(img)
        for tip in tips:
            ltp1 = position[hand_L].get(tip, None)  # 左手显示关节坐标
            ltp2 = position[hand_L].get(tip - 2, None)
            ltp_8 = position[hand_L].get(8, None)
            ltp_4 = position[hand_L].get(4, None)
            ltp_0 = position[hand_L].get(0, None)

            if ltp1 and ltp2:

                cv2.circle(img, (ltp_8[0], ltp_8[1]), 7, (0, 255, 255), cv2.FILLED)  # 食指
                # cv2.circle(img, (ltp_12[0], ltp_12[1]), 7, (0, 255, 255), cv2.FILLED)  # 中指
                cv2.line(img, (ltp_8[0], ltp_8[1]), (ltp_4[0], ltp_4[1]), (255, 255, 255), 3)  # 食指中指之间的线

                t_1 = int((ltp_4[0] + ltp_8[0]) / 2)
                t_2 = int((ltp_4[1] + ltp_8[1]) / 2)
                cv2.circle(img, (t_1, t_2), 7, (255, 0, 255), cv2.FILLED)  # 食指和中指中间的点

                print(ltp_4[1] - ltp_8[1])
                if (self.flag == 1) and (ltp_4[1] - ltp_8[1]) <= 20:
                    self.ctr.click(pynput.mouse.Button.left, 2) #鼠标左键双击
                    self.flag = 0
                if (self.flag == 1) and (ltp_4[1] - ltp_8[1]) <= 50 and (ltp_4[1] - ltp_8[1]) >= 30:
                    # pyautogui.click()
                    self.ctr.press(pynput.mouse.Button.left) #按下鼠标左键
                    self.flag = 0

                if (self.flag == 0) and (ltp_4[1] - ltp_8[1]) > 50:
                    self.ctr.release(pynput.mouse.Button.left) #释放鼠标左键
                    self.flag = 1
                cv2.circle(img, (ltp1[0], ltp1[1]), 7, (255, 255, 0), cv2.FILLED)  # end,可以去掉
                cv2.circle(img, (ltp2[0], ltp2[1]), 5, (255, 0, 0), cv2.FILLED)  # end,可以去掉
                if tip == 4:
                    if ltp1[0] > ltp2[0]:  # ltp[i]，i=1的时候，是y坐标，i=0的时候，是x坐标
                        tip_data[tip] = 1
                    else:
                        tip_data[tip] = 0
                else:
                    if ltp1[1] > ltp2[1]:
                        tip_data[tip] = 0
                    else:
                        tip_data[tip] = 1
                if int(list(tip_data.values()).count(1)) > 2:
                    self.ctr.position = ((ltp_0[0] - 100) * 3, (ltp_0[1] - 150) * 3)

        hand_R = 'Right'
        tips = [4, 8, 12, 16, 20]
        tip_data = {4: 0, 8: 0, 12: 0, 16: 0, 20: 0}

        # self.hand_detector.process(img)
        position = self.hand_detector.find_position(img)
        for tip in tips:
            rtp1 = position[hand_R].get(tip, None)  # 左手显示关节坐标
            rtp2 = position[hand_R].get(tip - 2, None)
            rtp_8 = position[hand_R].get(8, None)
            rtp_4 = position[hand_R].get(4, None)
            rtp_0 = position[hand_R].get(0, None)

            if rtp1 and rtp2:

                cv2.circle(img, (rtp_8[0], rtp_8[1]), 7, (0, 255, 255), cv2.FILLED)  # 食指
                # cv2.circle(img, (ltp_12[0], ltp_12[1]), 7, (0, 255, 255), cv2.FILLED)  # 中指
                cv2.line(img, (rtp_8[0], rtp_8[1]), (rtp_4[0], rtp_4[1]), (255, 255, 255), 3)  # 食指中指之间的线

                tt_1 = int((rtp_4[0] + rtp_8[0]) / 2)
                tt_2 = int((rtp_4[1] + rtp_8[1]) / 2)
                cv2.circle(img, (tt_1, tt_2), 7, (255, 0, 255), cv2.FILLED)  # 食指和中指中间的点

                print(rtp_4[1] - rtp_8[1])
                if (self.flag == 1) and (rtp_4[1] - rtp_8[1]) <= 20:
                    self.ctr.click(pynput.mouse.Button.left, 2)  # 鼠标左键双击
                    self.flag = 0
                if (self.flag == 1) and (rtp_4[1] - rtp_8[1]) <= 50 and (rtp_4[1] - rtp_8[1]) >= 30:
                    # pyautogui.click()
                    self.ctr.press(pynput.mouse.Button.left)  # 按下鼠标左键
                    self.flag = 0

                if (self.flag == 0) and (rtp_4[1] - rtp_8[1]) > 50:
                    self.ctr.release(pynput.mouse.Button.left)  # 释放鼠标左键
                    self.flag = 1
                cv2.circle(img, (rtp1[0], rtp1[1]), 7, (255, 255, 0), cv2.FILLED)  # end,可以去掉
                cv2.circle(img, (rtp2[0], rtp2[1]), 5, (255, 0, 0), cv2.FILLED)  # end,可以去掉
                if tip == 4:
                    if rtp1[0] > rtp2[0]:  # ltp[i]，i=1的时候，是y坐标，i=0的时候，是x坐标
                        tip_data[tip] = 1
                    else:
                        tip_data[tip] = 0
                else:
                    if rtp1[1] > rtp2[1]:
                        tip_data[tip] = 0
                    else:
                        tip_data[tip] = 1
                if int(list(tip_data.values()).count(1)) > 2:
                    self.ctr.position = ((rtp_0[0] - 100) * 3, (rtp_0[1] - 150) * 3)

        # 在ctrl方法中的手势检测循环中
        # 根据手部上下移动模拟滚轮滚动
        vertical_movement_threshold = 30  # 用于判断手部上下移动的阈值
        # 检测手部上下移动，模拟滚轮滚动
        position = self.hand_detector.find_position(img)

        # 确保左手关键点存在
        if 'Left' in position:
            ltp1 = position['Left'].get(4, None)  # 左手大拇指指尖
            ltp2 = position['Left'].get(8, None)  # 左手食指指尖

            # 继续后续的逻辑
            if ltp1 and ltp2:
                # 进行手部上下移动的逻辑判断
                if abs(ltp1[1] - ltp2[1]) > vertical_movement_threshold:
                    # 手部上移
                    if ltp1[1] < ltp2[1]:
                        self.ctr.scroll(0, 1)  # 向上滚动
                    # 手部下移
                    else:
                        self.ctr.scroll(0, -1)  # 向下滚动
