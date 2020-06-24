# -*- coding: UTF-8 -*-
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

cap = {
    "platformName": "Android",
    "platformVersion": "6.0.1",
    "deviceName": "emulator-5554",
    "udid": "emulator-5554",
    "appPackage": "com.jifen.dandan",
    "appActivity": "com.jifen.dandan.sub.welcome.activity.WelcomeActivity",
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

time.sleep(10)
while True:
    try:
        if WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(
                "//android.widget.ImageView[@resource-id='com.jifen.dandan:id/close_bottom_button']")):
            driver.find_element_by_xpath(
                "//android.widget.ImageView[@resource-id='com.jifen.dandan:id/close_bottom_button']").click()
            print("点击关闭广告")
        # if WebDriverWait(driver, 30).until(lambda x: x.find_element_by_xpath(
        #         "//android.widget.ImageView[@resource-id='com.jifen.dandan:id/tt_video_ad_close']")):
        #     print("结束广告")
        #     driver.find_element_by_xpath(
        #         "//android.widget.ImageView[@resource-id='com.jifen.dandan:id/tt_video_ad_close']").click()
    except:
        pass
    time.sleep(5)
    driver.swipe(x1, y1, x1, y2, 500)
    print("滑动")
    time.sleep(12)
    print("等待12秒")
