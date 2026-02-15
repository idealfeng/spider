import time
from selenium import webdriver
# edge
driver = webdriver.Edge()
driver.get("http://www.jd.com")
# time.sleep(10)

content=driver.page_source
print(content)


