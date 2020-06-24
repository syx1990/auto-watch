# coding=utf-8
'''
Created on 2017/12/24 0024
@author:Changge
'''

from appium import webdriver
import time
import threading

desired_caps = {
    'platformName': 'Android',
    'deviceName': '2911a8d0',
    'udid': '2911a8d0',
    'platformVersion': '9',
    "appPackage": "com.kuaishou.nebula",
    "appActivity": "com.yxcorp.gifshow.HomeActivity",
    "noReset": True
}

desired_caps2 = {
    'platformName': 'Android',
    'deviceName': 'QG6H5SNNNJPZNJNF',
    'udid': 'QG6H5SNNNJPZNJNF',
    'platformVersion': '5',
    "appPackage": "com.kuaishou.nebula",
    "appActivity": "com.yxcorp.gifshow.HomeActivity",
    "noReset": True
}


def get_size(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)


def task1():
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    ##休眠20s等待页面加载完成
    time.sleep(20)

    l = get_size(driver)
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.85)
    y2 = int(l[1] * 0.15)
    num = 0
    while True:
        driver.swipe(x1, y1, x1, y2)
        num += 1
        time.sleep(13)
        print("task1小视频跑了%d次" % num)
    # driver.quit()


def task2():
    driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub', desired_caps2)
    ##休眠20s等待页面加载完成
    time.sleep(20)

    l = get_size(driver)
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.85)
    y2 = int(l[1] * 0.15)
    num = 0
    while True:
        driver.swipe(x1, y1, x1, y2)
        num += 1
        time.sleep(13)
        print("task2小视频跑了%d次" % num)
    # driver.quit()


threads = []
t1 = threading.Thread(target=task1)
threads.append(t1)

t2 = threading.Thread(target=task2)
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.start()
