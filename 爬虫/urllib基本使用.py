# 使用urllib获取网页源码
import urllib.request

url = "http://www.baidu.com"
# 模拟浏览器向服务器发送请求,ctrl+左键查看函数
response = urllib.request.urlopen(url)
# read返回二进制数据,二进制转为字符串,一个字节一个字节读，read(字节数)
content = response.read().decode('utf-8')

print(content)
