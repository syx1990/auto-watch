# -*- coding: UTF-8 -*-
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

cap = {
    "platformName": "Android",
    "platformVersion": "5.0",
    "deviceName": "QG6H5SNNNJPZNJNF",
    "udid": "QG6H5SNNNJPZNJNF",
    "appPackage": "com.lechuan.mdwz",
    "appActivity": "com.lechuan.mdwz.ui.activity.WelcomeActivity",
    "noReset": True,
    "automationName":"uiautomator2"
}

print("开启配置")
driver = webdriver.Remote("http://localhost:4723/wd/hub", cap)
print("appium服务器启动")

def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)


try:
    if WebDriverWait(driver,15).until(lambda x:x.find_element_by_xpath("//android.widget.RadioGroup[@resource-id='com.lechuan.mdwz:id/ls']/android.widget.RadioButton[3]")):
        print("点击书架....")
        driver.find_element_by_xpath("//android.widget.RadioGroup[@resource-id='com.lechuan.mdwz:id/ls']/android.widget.RadioButton[3]").click()
except:
    pass

try:
    if WebDriverWait(driver, 15).until(lambda x: x.find_element_by_xpath("//android.widget.TextView[@resource-id='com.lechuan.mdwz:id/a84']")):
        print("具体小说题目....")
        driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.lechuan.mdwz:id/a84']").click()
except:
    pass

l = get_size()
x1 = int(l[0] * 0.75)
y1 = int(l[1] * 0.85)
x2 = int(l[1] * 0.25)
num = 0
time.sleep(5)
while True:
    driver.swipe(x1, y1, x2, y1)
    num += 1
    time.sleep(20)
    print("小说跑了%d遍" % num)

