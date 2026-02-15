import scrapy


class CarSpider(scrapy.Spider):

    name = "car"

    allowed_domains = ["car.autohome.com.cn"]

    start_urls = ["https://www.autohome.com.cn/price/ev"]

    def parse(self, response):
        print("-------------------")
        span=response.xpath('//a[@href="/price/ev"]/h2')[0]
        print(span)
