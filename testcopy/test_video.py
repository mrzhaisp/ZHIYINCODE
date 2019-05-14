#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time
from  selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class biliVideo():
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.bilibili.com/video/av16041375/")
    def playPause(self):
        video=WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@id='bilibiliPlayer']/div[1]/div[2]/div[7]/video")))  # 找到视频
        url=self.driver.execute_script("return arguments[0].currentSrc;",video)  # 打印视频地址
        print(url)
        print("start")
        self.driver.execute_script("return arguments[0].play()",video)  # 开始播放
        time.sleep(15)
        print("stop")
        self.driver.execute_script("return arguments[0].pause()",video) # 暂停
if __name__ == '__main__':
    po = biliVideo()
    po.playPause()