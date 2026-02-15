import urllib.request
import urllib.parse

def create_request(page):
    url=('https://movie.douban.com/j/chart/top_list?type=25&interval_id=100%3A90&action=&')

    headers={
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36 Edg/131.0.0.0'
    }

    data={
        'start':(page-1)*20,    #url数据更新
        'limit':20
    }

    data = urllib.parse.urlencode(data)
    url=url+data
    request=urllib.request.Request(url,headers=headers)

    return request
def get_content(request):
    response=urllib.request.urlopen(request)

    content=response.read().decode('utf-8')

    print(content)

if __name__=='__main__':
    start_page=int(input("请输入起始页码"))
    end_page=int(input("请输入终止页码"))

    for page in range(start_page,end_page+1):
        request=create_request(page)
        get_content(request)

