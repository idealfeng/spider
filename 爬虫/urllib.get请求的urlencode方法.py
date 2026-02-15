import urllib.request
import urllib.parse

# urlencode使用场景：多个参数

base_url = 'http://www.baidu.com/s?'
data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '中国台湾'
}
# 编码转换
new_data = urllib.parse.urlencode(data)
# 路径拼接
url = base_url + new_data

# UA绕过
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36 Core/1.116.457.400 QQBrowser/13.4.6233.400'
}

# 请求对象的定制
request = urllib.request.Request(base_url, headers=headers)
# 发送请求
response = urllib.request.urlopen(request)
# 读取数据
content = response.read().decode('utf-8')

# 打印
print(content)
