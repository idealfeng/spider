import urllib.request
import urllib.parse

def create_request(page):
    url='https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

    headers={
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36 Edg/131.0.0.0'
    }

    data={
        'cname': '上海',
        'pid':'',
        'pageIndex': page,      # 提交表单数据
        'pageSize': 10
    }
    data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url, data=data, headers=headers)
    return request

def create_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    print(content)

if __name__=='__main__':
    start_page=int(input('请输入起始页码'))
    end_page=int(input('请输入终止页码'))
    for page in range(start_page,end_page+1):
        request=create_request(page)
        create_content(request)