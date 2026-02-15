import urllib.request
import urllib.parse  # 把url中的中文变为unicode编码

url = "https://www.baidu.com/s?wd="

# url组成     https://www.baidu.com/s?wd=firefly
# http协议    www.baidu.com主机    80/443端口号     s路径      wd参数      锚点
# http   80
# https  443
# mysql  3306
# oracle 1521
# redis  6379
# mongodb    27017

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36 Core/1.116.457.400 QQBrowser/13.4.6233.400'
}
# 转换为unicode
name = urllib.parse.quote('周杰伦')
url = url + name
print(url)

# urlopen中不存储字典,输出请求
request = urllib.request.Request(url, headers=headers)  # headers为缺省参数
# 响应
response = urllib.request.urlopen(request)
# 读取
content = response.read().decode('utf-8')

print(content)
