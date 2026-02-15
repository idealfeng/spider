import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_dushu.items import ScrapyDushuItem

# 命令行多进入了一层文件导致scrapy crawl错误

class ReadSpider(CrawlSpider):
    name = "read"
    allowed_domains = ["www.dushu.com"]
    start_urls = ["https://www.dushu.com/lianzai/1124.html"]

    rules = (Rule(LinkExtractor(allow=r'/lianzai/1124_\d+\.html'), callback="parse_item", follow=False),)

    def parse_item(self, response):
        img_list=response.xpath('//div[@class="book-info"]//img')
        for img in img_list:
            name=img.xpath('./@alt').extract_first()
            src=img.xpath('./@data-original').extract_first()
            print(name,src)
            # print(img.extract_first())
            book=ScrapyDushuItem(name=name,src=src)
            yield book


