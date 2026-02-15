# 出验证码加cookie
from selenium import webdriver

driver=webdriver.Edge()

url='https://www.baidu.com'
driver.get(url)

import time
time.sleep(2)

# 获取文本框的对象
input=driver.find_element('id','kw')
# 在文本框输入对象
input.send_keys('星穹铁道')
time.sleep(2)
# 获取百度一下的按钮
button=driver.find_element('id','su')
# 点击按钮
button.click()
time.sleep(3)
# 滑到底部，第一行模拟js代码滚动，第二行执行js代码
js_bottom='document.documentElement.scrollTop=100000'
driver.execute_script(js_bottom)
time.sleep(3)
# 获取下一页的按钮
next_=driver.find_element('xpath','//a[@class="n"]')
# 点击下一页
next_.click()
time.sleep(3)
# 回到上一页
driver.back()
time.sleep(3)
# 回去
driver.forward()
time.sleep(3)
# 关闭浏览器
driver.quit()
