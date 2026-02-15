import json
import jsonpath

obj=json.load(open('jsonpath_本地文件.json','r',encoding="utf-8"))
# print(obj)

# 书店所有书的作者
# author_list=jsonpath.jsonpath(obj,'$.store.books[*].author')
# print(author_list)

# 所有作者
# author_list=jsonpath.jsonpath(obj,'$..author')
# print(author_list)

# store下面所有元素
# tag_list=jsonpath.jsonpath(obj,'$.store.*')
# print(tag_list)

# store下面所有东西的price
# price_list=jsonpath.jsonpath(obj,'$.store..price')
# print(price_list)

# 第三本书
# books=jsonpath.jsonpath(obj,'$..books[2]')
# print(books)

# 最后一本书
# books=jsonpath.jsonpath(obj,'$..books[(@.length-1)]')
# print(books)

# 前两本书
# book_list=jsonpath.jsonpath(obj,'$..books[0,1]')
# book_list=jsonpath.jsonpath(obj,'$..books[:2]')
# print(book_list)

# 过滤出含有price>10的书
# book_list=jsonpath.jsonpath(obj,'$..books[?(@.price>10)]')
# print(book_list)

