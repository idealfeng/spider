import requests

url='https://www.baidu.com/s?'

headers={       # 请求头文件有cookie
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36 Core/1.116.457.400 QQBrowser/13.4.6233.400"
}

data = {
    "wd": "ip"
}

proxy={
    "http":"172.16.17.32:8888",
}

response = requests.post(url,headers=headers,data=data,proxies=proxy)

content=response.text
print(content)

