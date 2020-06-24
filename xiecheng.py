# selenium服务
from selenium import webdriver
# 拉动区块
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
# 打开携程
driver.get('https://passport.ctrip.com/user/reg/home')
# 点击携程同意
driver.find_element_by_class_name('reg_agree').click()
time.sleep(3)
# 获取滑块区域元素
sour = driver.find_element_by_class_name('cpt-drop-btn')
print(sour.size['width'])
print(sour.size['height'])
# 获取滑动区块元素
ele = driver.find_element_by_class_name('cpt-bg-bar')
print(ele.size['width'])
print(ele.size['height'])
# 拖动区块
ActionChains(driver).drag_and_drop_by_offset(sour, ele.size['width'], -sour.size['height']).perform()
