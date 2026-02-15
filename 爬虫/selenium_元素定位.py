# id,xpath,link text,teg name,class name,css selector
from selenium import webdriver

driver=webdriver.Edge()
url='https://www.baidu.com'
driver.get(url)

# 找到id中为su的标签
# button=driver.find_element(by='id',value='su')
# print(button)
# button = driver.find_element('name','wd')
# print(button)

# 根据路径获取对象
# button = driver.find_element(by='xpath',value='//input[@id="su"]')
# print(button)

# 根据标签名获取对象
# button=driver.find_element('tag name','input')
# print(button)

# bs4选择器获取对象
# button=driver.find_element('css selector','#su')
# print(button)

# 获取链接名
button=driver.find_element('link text','新闻')
print(button)
