# 总结，参数使用params传递
# 参数要urlencode编码
# 无需请求对象定制
# 请求资源路径中的?可加可不加

# urllib
# get请求 #
# post请求 #
# ajax的get请求
# ajax的post请求
# cookie登陆 #
# 代理 #

import requests
url='http://www.baidu.com/s?'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36 Core/1.116.475.400 QQBrowser/13.5.6267.400'
}

data={
    'wd':'北京'
}

response=requests.get(url,data,headers=headers)

content=response.text
print(content)

