# -*- coding: UTF-8 -*-
from appium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait

cap = {
    "platformName": "Android",
    "platformVersion": "6.0.1",
    "deviceName": "emulator-5554",
    "udid": "emulator-5554",
    "appPackage": "com.zheyun.bumblebee",
    "appActivity": "com.zheyun.bumblebee.ui.LauncherActivity",
    "noReset": True
}

print("开启配置")
driver = webdriver.Remote("http://localhost:4727/wd/hub", cap)
print("appium服务器启动")


def get_size():
    print("获取尺寸")
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)


l = get_size()
x1 = int(l[0] * 0.5)
y1 = int(l[1] * 0.85)
y2 = int(l[1] * 0.15)

# 点击设置
if WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(
        "//android.widget.ImageView[@resource-id='com.zheyun.bumblebee:id/base_card_dialog_close']")):
    driver.find_element_by_xpath(
        "//android.widget.ImageView[@resource-id='com.zheyun.bumblebee:id/base_card_dialog_close']").click()

time.sleep(5)
num = 0
while True:
    try:
        driver.swipe(x1, y1, x1, y2)
        print("滑动")
        time.sleep(13)
        num += 1
        print("小视频跑了%d次" % num)
    except:
        pass
