import scrapy
from scrapy_baidu.items import ScrapyDangdangItem

class DangdangSpider(scrapy.Spider):

    name = "dangdang"

    allowed_domains = ["category.dangdang.com"]

    start_urls = ["https://category.dangdang.com/cp01.01.01.00.00.00.html"]

    # 多页url
    base_url='https://category.dangdang.com/pg'
    page=1
    def parse(self, response):
        li_list=response.xpath('//ul[@id="component_59"]/li')
        for li in li_list:
            # extract提取标签属性值,text是查到标签中的内容

            # 修改了    /img变为  //img
            src=li.xpath('.//img/@data-original').extract()
            name=li.xpath('./a/@title').extract()
            # 加入了text()
            price=li.xpath('./p[@class="price"]/span[@class="search_now_price"]/text()').extract_first()
            print(src,name,price)

            book=ScrapyDangdangItem(src=src,name=name,price=price)
            # 获取一个book将其交给管道
            yield book

            if self.page<5:
                self.page=self.page+1
                url=self.base_url+str(self.page)+'-cp01.01.01.00.00.00.html'

                # scrapy.request类似get请求，callback为你要执行的函数
                yield scrapy.Request(url=url,callback=self.parse)

