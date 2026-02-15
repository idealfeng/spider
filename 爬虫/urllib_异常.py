import urllib.request

url='https://blog.csdn.net/qq_37945670/article/details/145117870'

headers={
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36 Edg/131.0.0.0'
    }

try:
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    print(content)

# http错误如/后缀
except urllib.error.HTTPError:
    print("系统正在升级")
# url错误
except urllib.error.URLError:
    print("我都说了系统在升级")
