import scrapy
import json
# post请求小节,post 请求没有参数将无任何意义
# 所以start_url 没用，parse也没用

# 修改了接口错误的问题

class Baidu_fanyiSpider(scrapy.Spider):

    name = "baidu_fanyi"

    allowed_domains = ["fanyi.baidu.com"]

    # start_urls = ["https://fanyi.baidu.com/sug"]
    #
    # def parse(self, response):

    def start_requests(self):
        url='https://fanyi.baidu.com/sug'
        data={
            'kw':'final'
        }
        # get请求用request，post请求用formrequest
        yield scrapy.FormRequest(url=url,formdata=data,callback=self.parse_second)

    def parse_second(self,response):
        content=response.text
        # print(content)
        obj=json.loads(content)
        print(obj)

