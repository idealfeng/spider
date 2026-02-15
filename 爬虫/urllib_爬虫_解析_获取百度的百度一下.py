import urllib.request
url="http://www.baidu.com"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36 Core/1.116.457.400 QQBrowser/13.4.6233.400'
}
request=urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

from lxml import etree

tree=etree.HTML(content)

result=tree.xpath('//input[@id="su"]/@value')
print(result)