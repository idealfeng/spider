import urllib.request
import urllib.parse
import json

url='https://fanyi.baidu.com/sug'
# UA绕过,请求头模拟
headers={       # 请求头文件有cookie
  # "Accept": "*/*",
  # "Accept-Encoding": "gzip, deflate, br",
  # "Accept-Language": "zh-CN,zh;q=0.9",
  # "Connection": "keep-alive",
  # "Content-Length": "7",
  # "Content-Type": "application/x-www-form-urlencoded",
  # "Cookie": "BIDUPSID=575A7F72602D039FB6D541C736054325; PSTM=1735911445; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BAIDUID=50A67EC02619ECDEB7A13F8D4A3D8513:FG=1; BA_HECTOR=24840h2ha5852k2g258k81858c65i81joctic1v; BAIDUID_BFESS=50A67EC02619ECDEB7A13F8D4A3D8513:FG=1; ZFY=dqi:BDSU9I2Xcr49izXNnpLLa70K:B4wqsKLKYYGfLTCY:C; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1736866950; BDRCVFR[S_ukKV6dOkf]=mk3SLVN4HKm; PSINO=1; delPer=0; H_PS_PSSID=61027_60853_61685_61731_61746_61744_61743_61782_61844_61804_61868; ab_sr=1.0.1_MzA1NWRhNWE1MTQ4ODNmMmIwN2NlM2U0ZTg3MDhlOTMwYjczZTJmMjIwN2JlNjFlNzg2YTI3M2ZlYzJlYTM5NGE4NzQ0MGFiNzk3MDA1OTYzNGUzM2JkN2RiZGY4MTJhZGZmMGQ2ODUyODYwMDZlYmNjMTY1YWYwMzRhMmFkMDM4NmRjYWQzMjUyOGViOGI1Mjc4MTQ2ZTMxYWI0YzFlOGVjMzM1ZmNlYTMzOThhYWFhMjY2ZDE1YWQ2NmM3ZjMwMTI2ZjFkM2UzM2EwZWI2YjUyMjVkNTcyMTY5OTAxMjE=; RT=\"z=1&dm=baidu.com&si=0d6c700d-d57c-48f8-b961-266869d6fcd8&ss=m5wn27s2&sl=1&tt=15u&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=29x\"",
  # "Host": "fanyi.baidu.com",
  # "Origin": "https://fanyi.baidu.com",
  # "Referer": "https://fanyi.baidu.com/mtpe-individual/multimodal?aldtype=16047&ext_channel=Aldtype",
  # "Sec-Ch-Ua": "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"",
  # "Sec-Ch-Ua-Mobile": "?0",
  # "Sec-Ch-Ua-Platform": "\"Windows\"",
  # "Sec-Fetch-Dest": "empty",
  # "Sec-Fetch-Mode": "cors",
  # "Sec-Fetch-Site": "same-origin",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36 Core/1.116.457.400 QQBrowser/13.4.6233.400"
}

data={
    'kw': 'love'
}
# post请求必须编码转换
data=urllib.parse.urlencode(data).encode('utf-8')

# 请求对象定制
request=urllib.request.Request(url,data=data,headers=headers)
# 响应
response=urllib.request.urlopen(request)
# 读取数据
content=response.read().decode('utf-8')
# print(content)

# 乱码考虑字符串转json
obj=json.loads(content)
print(obj)

