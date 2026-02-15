import urllib.request

proxies_pool=[
    {'http':'172.16.17.32:8080'},
    {'http':'172.16.17.32:8081'},
]

import random

proxies=random.choice(proxies_pool)

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36 Core/1.116.457.400 QQBrowser/13.4.6233.400'
}

request = urllib.request.Request(url, headers=headers)

handler=urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)

content = response.read().decode('utf-8')

print(content)