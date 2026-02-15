from selenium import webdriver

driver=webdriver.Edge()
url='http://www.baidu.com'
driver.get(url)

input=driver.find_element('id','su')

# 获取标签属性
print(input.get_attribute('class'))

# 获取标签名字
print(input.tag_name)

# 获取元素文本
a=driver.find_element('link text','新闻')
print(a.text)