# 请用 python+selenium  爬取 XXX 网站上的所有a链接的 href属性并访问，输出访问地址和状态码
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

driver = webdriver.Chrome()
# 这里以百度为例
driver.get("https://www.dushu.com/")

wait = WebDriverWait(driver, 10)
links = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a")))

# 遍历所有的链接元素，并输出href属性值
for link in links:
    href = link.get_attribute("href")
    if href.startswith("http"):
        response = requests.get(href)
        print(href, response.status_code)
    else:
        link.click()
        print(driver.current_url, driver.execute_script('return document.readyState'),
              requests.get(driver.current_url).status_code)

# 关闭浏览器
driver.quit()