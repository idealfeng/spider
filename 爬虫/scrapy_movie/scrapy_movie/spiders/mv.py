# 爬取电影名及！电影名点开链接后的图片
import scrapy
from scrapy_movie.items import ScrapyMovieItem

class MvSpider(scrapy.Spider):
    name = "mv"
    allowed_domains = ["dydytt.net"]
    start_urls = ["https://dydytt.net/html/gndy/rihan/index.html"]

    def parse(self, response):
        a_list=response.xpath('//ul//b/a')
        for a in a_list:
            name=a.xpath('./text()').extract_first()
            href=a.xpath('./@href').extract_first()
            # print(name,href)

            url='https://dydytt.net'+href

            # 对第二页的链接发起访问
            yield scrapy.Request(url,callback=self.parse_second,meta={'name':name})

    def parse_second(self,response):
        print('----------------------------------')
        # xpath失败none多试，尽量精简
        src=response.xpath('//ul//img/@src').extract_first()
        # 接受到请求的meta参数的值
        name=response.meta['name']
        movie=ScrapyMovieItem(src=src,name=name)

        yield movie
