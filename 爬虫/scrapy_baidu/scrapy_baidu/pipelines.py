# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyBaiduPipeline:
    def open_spider(self,spider):       #在爬虫文件开始前执行
        self.fp=open('books.json','w',encoding='utf-8')


    def process_item(self, item, spider):
        # with open('books.json', 'a', encoding='utf-8') as fp:        # 注意写入模式a
        #     fp.write(str(item))                                                     # 注意对象转字符串

        self.fp.write(str(item))

        return item

    def close_spider(self,spider):      # 在爬虫文件执行后执行
        self.fp.close()

import urllib.request
# 多管道，1.定义管道类   2.settings开启管道
class DangDangDownloadPipeline:
        def process_item(self,item, spider):
            url='http:'+item.get('src',[])[0]
            filename='./books/'+item.get('name',[])[0]+'.jpg'
            urllib.request.urlretrieve(url,filename)

            return item


