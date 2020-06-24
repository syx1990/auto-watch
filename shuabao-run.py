# -*- coding: UTF-8 -*-
from appium import webdriver
import time
import multiprocessing


def handle_appium(device, platformVersion,port):
    print("配置基础信息")
    cap = {
        'platformName': 'Android',
        'platformVersion': platformVersion,
        'deviceName': device,
        'udid': device,
        'appPackage': 'com.jm.video',
        'appActivity': 'com.jm.video.ui.main.SplashActivity',
        'noReset': True,
        "unicodekeyboard": True,
        "resetkeyboard": True
    }

    print(cap)


    print("启动appium服务器")
    driver = webdriver.Remote('http://localhost:'+str(port)+'/wd/hub', cap)

    print(str(port))

    handle_shuabao(driver)


def get_size(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)


def handle_shuabao(driver):
    l = get_size(driver)
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


if __name__ == '__main__':
    m_list = []
    # 定义两台虚拟设备
    devices_list = [['2911a8d0', '9'], ['QG6H5SNNNJPZNJNF', '5']]
    for device in range(len(devices_list)):
        port = 4723 + 2 * device

        m_list.append(multiprocessing.Process(target=handle_appium,args=(devices_list[device][0], devices_list[device][1], port,)))

        for m1 in m_list:
            m1.start()

        for m2 in m_list:
            m2.join()
