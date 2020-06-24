# coding=utf-8
import sys
from appium import webdriver
import time

# 获取尺寸
def get_size(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)


# 通过参数，来判断调用那个端口
def handle_run(scence):
    if scence == 1:
        cap = {
            'platformName': 'Android',
            'platformVersion': '5',
            'deviceName': 'QG6H5SNNNJPZNJNF',
            'udid': 'QG6H5SNNNJPZNJNF',
            "appPackage": "com.kuaishou.nebula",
            "appActivity": "com.yxcorp.gifshow.HomeActivity",
            "noReset": True
        }
        cap_driver = webdriver.Remote("http://localhost:4723/wd/hub", cap)
        handle_swipe(cap_driver)
    else:
        cap1 = {
            'platformName': 'Android',
            'platformVersion': '9',
            'deviceName': '2911a8d0',
            'udid': '2911a8d0',
            "appPackage": "com.kuaishou.nebula",
            "appActivity": "com.yxcorp.gifshow.HomeActivity",
            "noReset": True
        }
        cap1_driver = webdriver.Remote("http://localhost:4725/wd/hub", cap1)
        handle_swipe(cap1_driver)


# 具体的操作
def handle_swipe(driver):
    l = get_size(driver)
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.85)
    y2 = int(l[1] * 0.15)
    num = 0
    while True:
        try:
            driver.swipe(x1, y1, x1, y2)
            num += 1
            time.sleep(13)
            print("快手小视频跑了%d次" % num)
        except:    
            pass


if __name__ == '__main__':
    scence = eval(sys.argv[1])  # 获取参数，通过参数判断，是那个端口使用的
    handle_run(scence)
