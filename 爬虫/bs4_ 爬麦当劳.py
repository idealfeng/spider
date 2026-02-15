import urllib.request

url='https://www.mcdonalds.com.cn/index/Food/menu/Dessert-11'

response=urllib.request.urlopen(url)

content=response.read().decode('utf-8')

# print(content)

from bs4 import BeautifulSoup

soup=BeautifulSoup(content,'lxml')
# //div[@class="row"]//a//span
name_list=soup.select('div[class="row"] a span')

for name in name_list:
    print(name.text)