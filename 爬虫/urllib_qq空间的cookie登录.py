import urllib.request
import urllib.parse

url = 'https://user.qzone.qq.com/1109214597/infocenter'

headers={
'Cookie':'_qimei_uuid42=19103152402100bd49f93674498629276cfc7eaa1c; _qimei_q32=8784a86d9c0e3fb974d35d3ef957fea3; _qimei_q36=35c6a340ecd6779d87ebc52b300012718b11; _qimei_fingerprint=a448349c708856f24f9a741eebe3846a; _qimei_h38=19c5ffa649f936744986292702000001619103; RK=J3FIj6uOWg; ptcz=2c3618c84a184d09484d881a1dbdb6d535ba7e5ccc3855831e22790fefa84b3f; uin=o1109214597; skey=@MJFkBbQDl; p_uin=o1109214597; pt4_token=XGFI82L2RgvV-He*k2UUP3Jz*TOSaj6kniMWJjhgYmA_; p_skey=s6BOz6lIiB0RIDmS6JZYxAlaia3jRq6QXUDyP0WBXKw_; Loading=Yes; pgv_pvid=2738387840; pgv_info=ssid=s9122695641',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36 Core/1.116.457.400 QQBrowser/13.4.6233.400'
}

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)
with open('qq空间.html','w',encoding='utf-8') as fp:
    fp.write(content)

