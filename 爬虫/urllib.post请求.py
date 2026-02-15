import urllib.request
import urllib.parse
import json

url='https://dict.youdao.com/webtranslate'
# UA绕过,请求头模拟
headers={
  # "Accept": "application/json, text/plain, */*",
  # "Accept-Encoding": "gzip, deflate, br",
  # "Accept-Language": "zh-CN,zh;q=0.9",
  # "Connection": "keep-alive",
  # "Content-Length": "139",
  # "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryTp3W65QlzFo65BZB",
  # "Cookie": "OUTFOX_SEARCH_USER_ID=221904889@240e:43d:4c0c:3151:7de0:c7b5:5125:7298; OUTFOX_SEARCH_USER_ID_NCOO=221384400.10757795; _uetsid=ad13d530d28811efb15a51105c0413f1; _uetvid=ad13dd60d28811efa461fd48ca488502; DICT_DOCTRANS_SESSION_ID=ZmExMDNiNDctZDZkZC00YmI5LWE1YWUtZDAxNjQ4ZTJlY2Uw",
  # "Host": "dict.youdao.com",
  # "Origin": "https://fanyi.youdao.com",
  # "Referer": "https://fanyi.youdao.com/",
  # "Sec-Ch-Ua": "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"",
  # "Sec-Ch-Ua-Mobile": "?0",
  # "Sec-Ch-Ua-Platform": "\"Windows\"",
  # "Sec-Fetch-Dest": "empty",
  # "Sec-Fetch-Mode": "cors",
  # "Sec-Fetch-Site": "same-site",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36 Core/1.116.457.400 QQBrowser/13.4.6233.400"
}

data={
        "i": "love",
        "from": "auto",
        "to": "",
        "useTerm": "false",
        "dictResult": "true",
        "keyid": "webfanyi",
        "sign": "8b802521f4ea3cc89cc91b38333ae0a4",
        "client": "fanyideskweb",
        "product": "webfanyi",
        "appVersion": "1.0.0",
        "vendor": "web",
        "pointParam": "client,mysticTime,product",
        "mysticTime": 1736867061186,
        "keyfrom": "fanyi.web",
        "mid": 1,
        "screen": 1,
        "model": 1,
        "network": "wifi",
        "abtest": 0,
        "yduuid": "abcdefg"
    }
# 编码转换
data=urllib.parse.urlencode(data).encode('utf-8')

# 请求对象定制
request=urllib.request.Request(url,data=data,headers=headers)
# 响应
response=urllib.request.urlopen(request)
# 读取数据
content=response.read().decode('utf-8')
print(content)

# 乱码考虑字符串转json
# obj=json.loads(content)
# print(obj)

