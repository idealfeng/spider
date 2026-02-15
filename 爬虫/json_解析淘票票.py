import urllib.request
url='https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1737648400922_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'
headers = {
     'referer':'https://dianying.taobao.com/?spm=a1z21.3046609.city.2.32c0112aR8pMa4&city=310100',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0'
}
request=urllib.request.Request(url,headers=headers)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')

content=content.split('(')[1].split(')')[0]
print(content)
with open('city.json','w',encoding='utf-8') as f:
    f.write(content)

import json
import jsonpath

obj=json.load(open('city.json','r',encoding='utf-8'))
list=jsonpath.jsonpath(obj,'$..regionName')
print(list)