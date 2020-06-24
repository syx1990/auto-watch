# -*- coding: UTF-8 -*-
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time, random

# 基础参数
platformName = 'Android'
platformVersion = '5'
deviceName = 'QG6H5SNNNJPZNJNF'
drvierserver = 'http://localhost:4727/wd/hub'
timeout = 600
noReset = 'True'
FLICK_STRAT_X = 300
FLICK_START_Y = 300
FLICK_DISTANCE = 700


class Automation():
    def __init__(self, appPackage, appActivity):
        self.desired_caps = {
            'platformName': platformName,
            'platformVersion': platformVersion,
            'deviceName': deviceName,
            'udid': deviceName,
            'appPackage': appPackage,
            'appActivity': appActivity,
            'noReset': noReset,
            'newCommandTimeout': timeout
        }
        print("打开appium服务器...")
        print("配置 appium...")
        self.driver = webdriver.Remote(drvierserver, self.desired_caps)
        self.wait = WebDriverWait(self.driver, 30)
        self.size = self.driver.get_window_size()

    # 屏幕方法
    def swipeUp(self):
        # 向上滑动屏幕
        self.driver.swipe(self.size['width'] * 0.5,
                          self.size['height'] * 0.85,
                          self.size['width'] * 0.5,
                          self.size['height'] * 0.15)
        print('向上滑动屏幕')

    def swipeDown(self):
        # 向右滑动屏幕
        self.driver.swipe(self.size['width'] * random.uniform(0.55, 0.65),
                          self.size['height'] * random.uniform(0.25, 0.35),
                          self.size['width'] * random.uniform(0.55, 0.65),
                          self.size['height'] * random.uniform(0.65, 0.75), random.uniform(800, 1200))

        print('向下滑动屏幕')

    def swipeRight(self):
        # 向右滑动屏幕
        self.driver.swipe(self.size['width'] * random.uniform(0.01, 0.11),
                          self.size['height'] * random.uniform(0.75, 0.89),
                          self.size['width'] * random.uniform(0.89, 0.98),
                          self.size['height'] * random.uniform(0.75, 0.89), random.uniform(800, 1200))

        print('向右滑动屏幕')


class XiangKantoutiao(Automation):

    def __init__(self, APP_PACKAGE, APP_ACTIVITY):
        super().__init__(APP_PACKAGE, APP_ACTIVITY)

    # 阅读文章
    def read_article(self, interval):
        print('阅读文章')

    # 小视频
    def smallvideo(self, interval):
        print('小视频')
        # 首页
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='首页']").click()
        print('点击底部菜单:首页...')
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='小视频']").click()
        print('点击底部菜单:小视频...')
        self.driver.find_element_by_id("com.xiangkan.android:id/tv_mini_video_desc").click()
        print('点击底部菜单:点击小视频内容...')
        num = 0
        start = time.time()
        while True:
            try:
                time.sleep(10)
                self.swipeUp()
                num += 1
                print("小视频跑了%d次" % num)
                end = start + interval
                now = time.time()
                if now >= end:
                    print('结束小视频循环')
                    break
            except:
                pass

    # 入口函数
    def main(self):
        print('打开 {} App ...'.format('想看头条'))
        func_list = ['smallvideo']
        for i in range(1):
            exp = 'self.{}({})'.format(random.choice(func_list), random.randint(100, 500))
            eval(exp)
            print('App {} 今日任务完成！'.format('想看头条'))


eastnews_appPackage = 'com.xiangkan.android'
eastnews_appActivity = 'com.bikan.reading.activity.SplashActivity'

if __name__ == '__main__':
    eastnews = XiangKantoutiao(eastnews_appPackage, eastnews_appActivity)
    eastnews.main()
