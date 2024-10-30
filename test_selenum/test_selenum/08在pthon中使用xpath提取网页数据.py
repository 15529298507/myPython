#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2024/10/26 13:51
@Author  : admin
@File    : 08在pthon中使用xpath提取网页数据.py
@Project : test_selenum

1. 导入lxml
2. 将获取到的网页内容转换为xml
3. 通过xpath去定位和解析页面中的内容

"""

'  '
import sys
import os

from lxml import etree

# 读取html页面内容（请求得到的response.content.decode()）
page = open('douban.html', 'r', encoding='utf-8').read()

# 将html页面的内容转换为xml文件对象
html = etree.HTML(page)

# 使用xpath语法提取页面数据
titles = html.xpath("//*[@class='title'][1]/text()")
score = html.xpath("//*[@class='rating_num'][1]/text()")
print(titles)
print(score)
