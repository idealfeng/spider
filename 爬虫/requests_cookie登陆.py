import requests
from bs4 import BeautifulSoup
import urllib.request

#两个VIEW作为隐藏域

# __VIEWSTATE: tzvbf8YKmhWE6yAmAmaG+9uoDQbhQPE5uSG7BSWHJnRt/Pt0CwF2lvru/24ItzP4wgrp0MY71Cfz8CeVPuu3BT6nklb4BlVn4T61f1pg+cgMTOkRetBCXLjb0H6IflhT8ipbyWw3iBElAgwdDPTL7DdCgec=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://www.gushiwen.cn/user/collect.aspx
# email: 1109214597@qq.com
# pwd: 45644645
# code: c2xl
# denglu: 登录

url='https://www.gushiwen.cn/user/login.aspx?from=http://www.gushiwen.cn/user/collect.aspx'

headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0',
    # 'cookie':'login=flase; Hm_lvt_9007fab6814e892d3020a64454da5a55=1737740551; HMACCOUNT=217B624ABB159FE5; ticketStr=201894243%7cgQHv8DwAAAAAAAAAAS5odHRwOi8vd2VpeGluLnFxLmNvbS9xLzAycWFYZlFlbGVkN2kxQUF1WE5EMTkAAgQk0ZNnAwQAjScA; ASP.NET_SessionId=cexjqgrybkqqarmjb4gj2pc3; codeyz=9c74dacff7e34025; Hm_lpvt_9007fab6814e892d3020a64454da5a55=1737741455',
    # 'referer':'https://www.gushiwen.cn/user/collect.aspx'
}
# 获取页面源码
response = requests.get(url=url,headers=headers)
content=response.text
# print(content)

# 解析页面源码
soup=BeautifulSoup(content,'lxml')

# 获取__VIEWSTATE
viewstate=soup.select('#__VIEWSTATE')[0].attrs.get('value')
# 获取__VIEWSTATEGENERATOR
viewstategenerate=soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')
# print(viewstate)
# print(viewstategenerate)
# LGb0c/pDICiMra6ifBIYClwkKCmEElvaselealFB2lFBY7/fG+vY8xfNzrVAtJlzcQD37udLyExkIf6tewPzd9CtJ0WWYDnoKdQmgYgdPEdszT9VisYkLmwFr4U1Q9RGvr/DmUvfP3bWAb8tPLT+fgIOnBM=
# C93BE1AE

# 获取验证码图片
code=soup.select('#imgCode')[0].attrs.get('src')
# print(code)
# 拼接code得到验证码地址
code_url='https://www.gushiwen.cn'+code
# print(code_url)

# 获取验证码图片后下载到本地，在控制台输入验证码传给code参数可登录urlretrieve不行，要用session方法
# urllib.request.urlretrieve(code_url,filename='code.png')
session=requests.session()
# 验证码的url内容
response_code=session.get(code_url,headers=headers)
# 注意此时用二进制数据，因为使用的是图片的下载,wb将二进制写入文件
content_code=response_code.content
with open('code.jpg','wb') as fp:
    fp.write(content_code)

code_name=input('请输入你的验证码')

url_post='https://www.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fwww.gushiwen.cn%2fuser%2fcollect.aspx'
data_post={
    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstategenerate,
    'from': 'http://www.gushiwen.cn/user/collect.aspx',
    'email': '595165358@qq.com',
    'pwd': 'action',
    'code': 'c2xl',
    'denglu': '登录'
}

response_post=session.post(url=url_post,headers=headers,data=data_post)
content_post=response_post.text
with open('gushiwen.html','w',encoding='utf-8') as fp:
    fp.write(content_post)


