import urllib.request

url = 'http://www.baidu.com'
# response是HTTPResponse的类型
response = urllib.request.urlopen(url)
# 一行一行读
content = response.readlines()
print(content)
# 返回状态码，200则逻辑正确
print(response.getcode())
# 返回url地址
print(response.geturl())
# 返回状态信息
print(response.getheaders())
