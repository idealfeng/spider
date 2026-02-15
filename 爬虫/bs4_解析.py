from bs4 import BeautifulSoup

soup=BeautifulSoup(open('bs4_test.html',encoding='utf-8'),'lxml')

# 找到第一个符合条件的数据
# print(soup.a)
# 返回标签的属性和属性值
# print(soup.a.attrs)

# bs4中的一些函数
# find返回第一个符合条件的数据,冲突关键词可加_如class_
# print(soup.find('a',class_="a2"))

# find_all返回所有数据，若想获取多数据，要添加列表
# print(soup.find_all('a'))
# print(soup.find_all(['a','span']))

# limit限定查找几个数据
# print(soup.find_all('li',limit=2))

# select返回一个列表有多数据
# print(soup.select('a'))

# 可以通过.代表class,称为类选择器
# print(soup.select('.a2'))

# 属性选择器，查找li标签中的id标签
# print(soup.select('li[id]'))

# 查找到li标签中id为12的标签
# print(soup.select('li[id="12"]'))

# 层级选择器
# 后代选择器
# print(soup.select('div li'))
# 子代选择器
# print(soup.select('div>ul>li'))

# 找到a标签和li标签
# print(soup.select('a,li'))

# 获取节点信息
obj=soup.select('#d1')[0]
# 如果标签中只有内容string和get_text均可使用
# 若有标签和内容只能用get_text
print(obj.string)
print(obj.get_text())

# 节点的标签与属性
obj=soup.select('#p1')[0]
# name是标签名字
# print(obj.name)
# 将属性值作为一个字典返回
print(obj.attrs)

# 获取节点的标签的属性
obj=soup.select('#p1')[0]
print(obj.attrs.get('class'))
