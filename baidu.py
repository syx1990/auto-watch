from selenium import webdriver

browser = webdriver.Chrome()
# 打开百度首页
browser.get('http://www.baidu.com')
# 在搜索输入框输入文本python
browser.find_element_by_id('kw').send_keys('python')
# 触发百度知道按钮
browser.find_element_by_id('su').click()
# 触发百度知道文字
# browser.find_element_by_link_text('知道').click()
browser.find_element_by_id('kw').clear()