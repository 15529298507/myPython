#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2024/10/26 21:10
@Author  : admin
@File    : 10批量提取数据的方式-分页.py
@Project : test_selenum

1. 准备好top250电影数据所有的url地址，存储在一个列表中
2. 遍历列表中的url地址，进行抓取
3. 代码优化

"""

# 1. 抓取页面

import requests
from lxml import etree

def get_data(url):
    # 请求头是字典格式
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }

    response = requests.get(url=url, headers=headers)
    page = response.content.decode()

    # 将html页面的内容转换为xml文件对象
    html = etree.HTML(page)

    # 再从中找到包含单条数据所有内容的元素 //ol/li
    data_list = html.xpath('//ol/li')
    [print(data_list)]

    # 对定位到包含所有元素的列表进行遍历，得到包含单条数据的元素
    for li in data_list:
        # 提取单条数据中的详细内容
        title = li.xpath(".//span[@class='title'][1]/text()")
        score = li.xpath(".//span[@class='rating_num'][1]/text()")
        print('电影名称：', title[0], ' 评分：', score[0])
        # xpath 的入参前面，一定要加一个.

if __name__ == '__main__':
    url = 'https://movie.douban.com/top250'
    get_data(url)