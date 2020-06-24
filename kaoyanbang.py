import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

cap = {
    "platformName": "Android",
    "platformVersion": "6.0.1",
    "deviceName": "emulator-5554",
    "appPackage": "com.tal.kaoyan",
    "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
    "noReset": True
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", cap)


def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)


try:
    if WebDriverWait(driver, 3).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tip_commit']")):
        driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tip_commit']").click()
except:
    pass

try:
    if WebDriverWait(driver, 3).until(
            lambda x: x.find_element_by_id("com.android.packageinstaller:id/permission_deny_button")):
        driver.find_element_by_id("com.android.packageinstaller:id/permission_deny_button").click()
except:
    pass

try:
    if WebDriverWait(driver, 3).until(
            lambda x: x.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tv_skip']")):
        driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tv_skip']").click()
except:
    pass

try:
    if WebDriverWait(driver, 3).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[@resource-id='com.tal.kaoyan:id/login_code_touname']")):
        driver.find_element_by_xpath(
            "//android.widget.TextView[@resource-id='com.tal.kaoyan:id/login_code_touname']").click()
except:
    pass

try:
    if WebDriverWait(driver, 3).until(lambda x: x.find_element_by_xpath(
            "//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_email_edittext']")):
        driver.find_element_by_xpath(
            "//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_email_edittext']").send_keys("18538187569")
        driver.find_element_by_xpath(
            "//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_password_edittext']").send_keys(
            "syxsy20151008")
        driver.find_element_by_xpath(
            "//android.widget.TextView[@resource-id='com.tal.kaoyan:id/login_login_btn']").click()
except:
    pass

try:
    if WebDriverWait(driver, 8).until(lambda x: x.find_element_by_id("com.tal.kaoyan:id/kaoyan_home_schtip_close")):
        driver.find_element_by_id("com.tal.kaoyan:id/kaoyan_home_schtip_close").click()
except:
    pass

try:
    if WebDriverWait(driver, 4).until(lambda x: x.find_element_by_xpath("//android.widget.TextView[@text='研讯']")):
        driver.find_element_by_xpath("//android.widget.TextView[@text='研讯']").click()

        l = get_size()

        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.75)
        y2 = int(l[1] * 0.25)

        while True:
            driver.swipe(x1, y1, x1, y2)
            time.sleep(0.5)
except:
    pass
