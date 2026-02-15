import urllib.request
from lxml import etree

def create_request(page):
    if(page==1):
        #url='https://sc.chinaz.com/tupian/meinvtupian.html'
        url='https://sc.chinaz.com/ppt/pptbeijing.html'
    else:
       # url='https://sc.chinaz.com/tupian/meinvtupian_'+str(page)+'.html'
        url='https://sc.chinaz.com/ppt/pptbeijing_'+str(page)+'.html'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36 Core/1.116.457.400 QQBrowser/13.4.6233.400'
    }

    request=urllib.request.Request(url=url,headers=headers)
    return request

def get_content(request):
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    return content
# 下载每一页的图片
def download(content):
    tree=etree.HTML(content)
    # 现在必须用最大的class标签比如class=container 诸如class=ppt-list masonry的无效，img后跟@data-original
    # 诸如 @src无效,xpath-tool最多观察到img后的结果，加入@标签后无结果
    src_list=tree.xpath('//div[@class="container clearfix"]//img/@data-original')
    name_list=tree.xpath('//div[@class="container clearfix"]//img/@alt')
    for i in range(len(src_list)):
        name=name_list[i]
        src=src_list[i]
    # print(name,src)
    #获取到的路径不完整
        url='https:'+src
        urllib.request.urlretrieve(url=url,filename=name+'.jpg')

if __name__=='__main__':
    start_page=int(input('请输入起始页码'))
    end_page=int (input('请输入结束页码'))

    for page in range(start_page,end_page+1):
        request=create_request(page)
        content=get_content(request)
        download(content)