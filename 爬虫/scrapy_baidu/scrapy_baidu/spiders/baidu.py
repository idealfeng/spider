import scrapy


class BaiduSpider(scrapy.Spider):

    name = "baidu"

    allowed_domains = ["baidu.com"]

    start_urls = ["http://www.baidu.com/"]

    def parse(self, response):


        print("********")
        page_title = response.css('title::text').get()
        self.log(f'页面标题: {page_title}')



