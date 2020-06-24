# -*- coding: UTF-8 -*-
from appium import webdriver
import time

print("配置基础信息")

cap = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "2911a8d0",
    "udid": "2911a8d0",
    "appPackage": "com.jm.video",
    "appActivity": "com.jm.video.ui.main.SplashActivity",
    "noReset": True
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", cap)


def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)


l = get_size()
x1 = int(l[0] * 0.5)
y1 = int(l[1] * 0.75)
y2 = int(l[1] * 0.25)
num = 0
while True:
    try:
        driver.swipe(x1, y1, x1, y2)
        num += 1
        time.sleep(12)
        print("小视频跑了%d次" % num)
    except:
        pass