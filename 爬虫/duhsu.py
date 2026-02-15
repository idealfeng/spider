from bs4 import BeautifulSoup
from lxml import etree
import requests


# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
# link = "https://www.dushu.com/lianzai/1124.html"
# r = requests.get(link, headers=headers)
# r.encoding = 'utf-8'
#
# soup = BeautifulSoup(r.text, 'lxml')
# house_list = soup.find_all('div', class_="book-info")
# html = etree.HTML(r.text)
# # name=html.xpath('//div[@class="property-content-title"]/h3/text()')
# # for house in house_list:
# #     name=soup.find('div',class_="nlist").a.strong.text()
# #
# #     print(name)
# name = html.xpath('//div[@class="book-info"]//img/@alt')
#
# # href=html.xpath('//div[@class="nlist"]/div/ul/li/a/@href')
#
# print(name)
# for i in name:
#     print(i)




# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
# link = "https://www.dushu.com/lianzai/1124.html"
# r = requests.get(link, headers=headers)
# r.encoding = 'utf-8'
#
# soup = BeautifulSoup(r.text, 'lxml')
# house_list = soup.find_all('div', class_="book-info")
# html = etree.HTML(r.text)
# # name=html.xpath('//div[@class="property-content-title"]/h3/text()')
# # for house in house_list:
# #     name=soup.find('div',class_="nlist").a.strong.text()
# #
# #     print(name)
# name = html.xpath('//div[@class="book-info"]//img/@alt')
# author = html.xpath('//div[@class="book-info"]/text()')
# # href=html.xpath('//div[@class="nlist"]/div/ul/li/a/@href')
#
# # print(type(author))
# for i, o in zip(name, author):
#     print('<<' + i + '>>', o)


# 请用 python+selenium  爬取 XXX 网站上的所有a链接的 href属性并访问，输出访问地址和状态码
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

driver = webdriver.Chrome()
# 这里以百度为例
driver.get("https://www.dushu.com/lianzai/1124.html")

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