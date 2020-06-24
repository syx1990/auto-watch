# -*- coding: UTF-8 -*-
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time,random,re
from selenium.common.exceptions import NoSuchElementException

# Appium 基本参数
platformName = 'Android'
platformVersion='6.0.1'
deviceName = 'QG6H5SNNNJPZNJNF'
drvierserver = 'http://localhost:4725/wd/hub'
timeout = 600
noReset = 'True'
FLICK_STRAT_X = 300
FLICK_START_Y = 300
FLICK_DISTANCE = 700


class Automation():
    # 初始化 Appium 基本参数
    def __init__(self,appPackage,appActivity):
    	self.desired_caps = {
    	'platformName':platformName,
    	'platformVersion':platformVersion,
    	'deviceName':deviceName,
    	'udid':deviceName,
    	'appPackage':appPackage,
    	'appActivity':appActivity,
    	'noReset':noReset,
    	'newCommandTimeout':timeout
    	}
    	print('打开 appium 服务器...')
    	print('配置 appium ...')
    	self.driver = webdriver.Remote(drvierserver,self.desired_caps)
    	self.wait = WebDriverWait(self.driver,30)
    	self.size = self.driver.get_window_size()    

    # 屏幕方法
    def swipeUp(self):
        # 向上滑动屏幕
        self.driver.swipe(self.size['width'] * 0.5,
                          self.size['height'] * 0.85,
                          self.size['width'] * 0.5,
                          self.size['height'] *0.25)      

        print('向上滑动屏幕')

    def swipeDown(self):
        # 向下滑动屏幕
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


class Qutoutiao(Automation):
    def __init__(self, APP_PACKAGE, APP_ACTIVITY):
        super().__init__(APP_PACKAGE, APP_ACTIVITY)


    # 领金币
    def get_coins(self):
    	self.driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.jifen.qukan:id/lx']/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]").click()
    	self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.jifen.qukan:id/brn']").click()
    	try:
    		if self.wait.until(lambda x:x.find_element_by_xpath("//android.widget.TextView[@resource-id='com.jifen.qukan:id/a7u']")):
    			self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.jifen.qukan:id/a7u']").click()        
    	except:
    		pass         
     # 阅读新闻
    def read_article(self, interval):
    	self.driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.jifen.qukan:id/lx']/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
    	print('点击底部菜单：头条')

    	self.driver.find_element_by_xpath("//android.widget.HorizontalScrollView[@resource-id='com.jifen.qukan:id/aal']/android.widget.LinearLayout[1]/android.widget.TextView[2]").click()       
    	print("点击底部菜单：推荐")

    	start = time.time()
    	while True:
    		articles = self.driver.find_elements_by_id("com.jifen.qukan:id/aj6")
    		print("新闻数量",len(articles))
    		for article in articles:
    			article.click()
    			print("进入新闻")
    			try:
    				if self.wait.until(lambda x:x.find_element_by_xpath("//android.view.View[@resource-id='com.jifen.qukan:id/avi']")):
    					self.driver.find_element_by_xpath("//android.view.View[@resource-id='com.jifen.qukan:id/avi']").click()
    					self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.jifen.qukan:id/uy']").click()
    			except:
    				pass
    				
    			return_btn = self.driver.find_elements_by_id("com.jifen.qukan:id/hx")
    			try:
    				try:
    					for i in range(random.randint(2,6)):
    						time.sleep(random.randint(6,10))
    						self.swipeUp()

    					for i in range(random.randint(2,6)):
    						time.sleep(random.randint(6,10))
    						self.swipeDown()
    				except:
    					return_btn = self.driver.find_elements_by_id("com.jifen.qukan:id/pr")
    					print('视频关闭按钮 <')
    					time.sleep(random.randint(60,120))
    			except:
    				return_btn = self.driver.find_element_by_xpath("//android.widget.FrameLayout[@resource-id='com.jifen.qukan:id/jw']/android.widget.ImageView[1]")
    				print('图片新闻关闭按钮 X')

    			return_btn.click()
    			print('退出新闻进入菜单')
    			for i in range(random.randint(2,4)):
    				time.sleep(random.randint(1,3))
    				self.swipeUp()

    			end = start + interval
    			now = time.time()
    			if now >= end:
    				print('结束')
    				break
    			else:
    				print('时间未到')

    # 视频
    def video(self,interval):
    	self.driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.jifen.qukan:id/lx']/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]").click()
    	print('点击底部菜单:视频...')
    	t = 1
    	start = time.time()
    	while True:

    		content = self.driver.find_elements_by_id("com.jifen.qukan:id/alv")
    		time_text = self.driver.find_elements_by_id("com.jifen.qukan:id/anw")
    		print('视频数量',len(content))
    		n = 0
    		try:
    			for i in content:
    				print('第{}次进入循环... 点击第{}/{}个视频'.format(t,n+1,len(content)))
    				time_span = time_text[n].get_attribute('text').split(':')
    				time_cost = int(time_span[0]) * 60 + int(time_span[1])
    				i.click()
    				try:
    					if self.wait.until(lambda x:x.find_element_by_xpath("//android.view.View[@resource-id='com.jifen.qukan:id/avi']")):
    						self.driver.find_element_by_xpath("//android.view.View[@resource-id='com.jifen.qukan:id/avi']").click()
    						self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.jifen.qukan:id/uy']").click()

    				except:
    					pass

    				print('点击视频，时长:{}s'.format(time_cost))
    				time.sleep(time_cost) 
    				n += 1          
    				time.sleep(13)

    		except IndexError:
    			print('视频展示不完整')  

    		except NoSuchElementException:
    			print('此为广告')               

    		except:
    			pass                 

    		t += 1
    		self.swipeUp()  
    		time.sleep(random.randint(5, 10))
    		end = start + interval
    		now = time.time()   
    		if now >= end:
    			print('结束视频循环') 
    			break
    # 小视频
    def smallvideo(self,interval):      
    	self.driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.jifen.qukan:id/lx']/android.widget.FrameLayout[3]/android.widget.LinearLayout[1]/android.widget.TextView[1]").click()
    	print("点击底部菜单:小视频...")   
    	start = time.time()
    	while True:
    		try:
    			if self.wait.until(lambda x:x.find_element_by_xpath("//android.view.View[@resource-id='com.jifen.qukan:id/avi']")):
    				self.driver.find_element_by_xpath("//android.view.View[@resource-id='com.jifen.qukan:id/avi']").click()
    				self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.jifen.qukan:id/uy']").click()
    		except:             
    			pass
    		time.sleep(random.randint(5, 10))            
    		self.swipeUp()                 
    		end = start + interval     
    		now = time.time()
    		if now >= end:                                          
    			print('结束小视频循环')
    			break



    # 入口函数
    def main(self):
    	print('打开 {} App ...'.format('趣头条'))
    	#self.get_coins()      
    	func_list = ['read_article']  # 新闻阅读，小视频，视频三个方法随机. read_article video  smallvideo
    	for i in range(1):                                   
    		exp = 'self.{}({})'.format(random.choice(func_list), random.randint(100, 500))  
    		eval(exp)   
    		print('App {} 今日任务完成！'.format('趣头条'))       
   

eastnews_appPackage = 'com.jifen.qukan'
eastnews_appActivity = 'com.jifen.qkbase.main.MainActivity'

if __name__ == '__main__':
	eastnews = Qutoutiao(eastnews_appPackage,eastnews_appActivity)
	eastnews.main()                  