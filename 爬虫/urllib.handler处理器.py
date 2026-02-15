import urllib.request
url="http://www.baidu.com"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36 Core/1.116.457.400 QQBrowser/13.4.6233.400'
}
request = urllib.request.Request(url, headers=headers)

# 获取handler对象
handler=urllib.request.HTTPHandler()

# 获取opener对象
opener=urllib.request.build_opener(handler)

# 调用open方法
response = opener.open(request)

content = response.read().decode('utf-8')
print(content)