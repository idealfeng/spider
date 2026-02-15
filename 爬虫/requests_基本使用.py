import requests

url='http://www.baidu.com'

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36 Core/1.116.475.400 QQBrowser/13.5.6267.400'
}

response=requests.get(url=url)
# 设置编码响应格式
response.encoding='utf-8'

# 以字符串形式返回网页源码
# print(response.text)

# 返回url地址
# print(response.url)

# 返回二进制数据
# print(response.content)

# 返回响应的状态码
print(response.status_code)

# 返回响应头
print(response.headers)