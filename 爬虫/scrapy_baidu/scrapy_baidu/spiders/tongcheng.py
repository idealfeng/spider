# 该案例被重定向了
# 1. HTTP 302 重定向：
# 爬虫在尝试访问页面 （） 时遇到重定向响应 （HTTP 302）。https://hf.58.com/songcany/?PGTID=0d100000-0034-59ba-bb17-35e9d75d31ab&ClickID=5
# 它被重定向到验证页面：，该页面需要验证（可能是 CAPTCHA 或某些机器人检测机制）。https://callback.58.com/antibot/verifylogin
import scrapy

class TongchengSpider(scrapy.Spider):
    name = "tongcheng"

    allowed_domains = ["hf.58.com"]
    start_urls = ["https://hf.58.com/songcany/?PGTID=0d100000-0034-59ba-bb17-35e9d75d31ab&ClickID=5"]

    # 执行start_urls之后执行的方法，response是返回的对象
    # 相当于response=urllib.request.urlopen()
    #           response=requests.get()
    def parse(self, response):
        # 字符串
        content=response.text
        # 返回二进制
        # content=response.body
        print('--------------------------')
        # 直接使用xpath解析
        # span=response.xpath('//a[@target="_blank"]/span[@class="name"]')[0]
        # print(span)