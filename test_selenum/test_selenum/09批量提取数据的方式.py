#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2024/10/26 14:08
@Author  : admin
@File    : 09批量提取数据的方式.py
@Project : test_selenum


1. 导入lxml
2. 将获取到的网页内容转换为xml
3. 通过xpath去定位和解析页面中的内容

xpath 数据提取的技巧
    1. 定位到包含所有数据的元素 //ol
    2. 再从中找到包含单条数据所有内容的元素 //ol/li
    3. 对定位到包含所有元素的列表进行遍历，得到包含单条数据的元素
    4. 再提取单条数据中的详细内容

"""
'  '
import sys
import os

from lxml import etree

# 读取html页面内容（请求得到的response.content.decode()）
page = open('douban.html', 'r', encoding='utf-8').read()

# 将html页面的内容转换为xml文件对象
html = etree.HTML(page)

# 再从中找到包含单条数据所有内容的元素 //ol/li
data_list = html.xpath('//ol/li')
[print(data_list)]

# 对定位到包含所有元素的列表进行遍历，得到包含单条数据的元素
for li in data_list:
    #提取单条数据中的详细内容
    title = li.xpath(".//span[@class='title'][1]/text()")
    score = li.xpath(".//span[@class='rating_num'][1]/text()")
    print('电影名称：', title[0], ' 评分：', score[0])
    # xpath 的入参前面，一定要加一个.