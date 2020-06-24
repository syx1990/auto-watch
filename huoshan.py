from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time

# Appium 基本参数
platformName = 'Android'
platformVersion = '6'
deviceName = 'emulator-5554'
drvierserver = 'http://localhost:4725/wd/hub'
noReset = 'True'
timeout = 600

class Automation():
    def __init__(self,appPackage,appActivity):
        self.desired_caps = {
            'platformName':platformName,
            'platformVersion':platformVersion,
            'deviceName':deviceName,
            'appPackage':appPackage,
            'appActivity':appActivity,
            'noReset':noReset,
            'newCommandTimeout':timeout
        }
        print('打开 appium 服务器...')
        print('配置 appium ...')
        self.driver = webdriver.Remote(drvierserver,self.desired_caps)
        self.wait = WebDriverWait(self.driver, 15)
        self.size = self.driver.get_window_size()

class Huoshan(Automation):
    def __init__(self,APP_PACKAGE,APP_ACTIVITY):
        super().__init__(APP_PACKAGE,APP_ACTIVITY)

    def dailyClick(self):
        # 点击红包
        self.driver.find_element_by_id('com.ss.android.ugc.livelite:id/wl').click()
        print('红包')

    # 具体方法
    def main(self):
        # 每天签到
        self.dailyClick()

eastnews_appPackage = 'com.ss.android.ugc.livelite'
eastnews_appActivity = 'com.ss.android.ugc.live.main.MainActivity'

if __name__ == '__main__':
    eastnews = Huoshan(eastnews_appPackage,eastnews_appActivity)
    eastnews.main()


