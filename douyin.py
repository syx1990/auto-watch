from appium import webdriver
import time

cap = {
    "platformName": "Android",
    "platformVersion": "6.0.1",
    "deviceName": "emulator-5554",
    "appPackage": "com.ss.android.ugc.aweme.lite",
    "appActivity": "com.ss.android.ugc.aweme.main.MainActivity",
    "noReset": True
}

driver = webdriver.Remote("http://localhost:4727/wd/hub", cap)


def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)


l = get_size()
x1 = int(l[0] * 0.5)
y1 = int(l[1] * 0.85)
y2 = int(l[1] * 0.15)
while True:
    driver.swipe(x1, y1, x1, y2)
    time.sleep(13)
