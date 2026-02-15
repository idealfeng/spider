from lxml import etree

# xpath解析
# 本地文件
# 服务器响应数据

tree=etree.parse('urllib_解析_path.html')
# print('urllib_解析_path.html')

# tree.xpath('xpath路径')
# 查找子节点,//查找所有子孙节点/查找子节点
# li_list=tree.xpath('//body/ul/li')
# print(li_list)



# 谓词查询
# 查找所有有"id"的属性的li标签
# text()获取标签中的内容
# li_list=tree.xpath('//ul/li[@id]/text()')
# print(li_list)

# 找到id为11的li标签
# li_list=tree.xpath('//ul/li[@id="11"]/text()')
# print(li_list)



# 属性查询
# 查找到id为11的li标签的class的属性值
# li=tree.xpath('//ul/li[@id="11"]/@class')
# print(li)



# 模糊查询
# 查询id包含1的li标签
# li_list=tree.xpath('//ul/li[contains(@id,"1")]/text()')
# print(li_list)

# 查询id以1开头的li标签
# li_list=tree.xpath('//ul/li[starts-with(@id,"1")]/text()')
# print(li_list)



# 逻辑运算
# 查询id为11并且class为c1的
# li_list=tree.xpath('//ul/li[@id="11" and @class="c1"]/text()')
# print(li_list)
# 查询id为11或id为12的标签
li_list=tree.xpath('//ul/li[@id="11"]/text() | //ul/li[@id="12"]/text()')
print(li_list)

