#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2024/10/26 21:59
@Author  : admin
@File    : 11批量提取数据的方式-类.py
@Project : test_selenum



"""
import requests
from lxml import etree

class DouBan:
    # 请求头是字典格式
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }

    base_url = 'https://movie.douban.com/top250?start={}&filter='

    def __init__(self):
        # 定义一个属性，用来保存所有url
        self.url_list = []

        # 生成url
        for i in range(10):
            url = self.base_url.format(i * 25)
            self.url_list.append(url)

    def get_page_data(self, url):
        response = requests.get(url=url, headers=self.headers)
        page = response.content.decode()

        # 将html页面的内容转换为xml文件对象
        html = etree.HTML(page)

        # 再从中找到包含单条数据所有内容的元素 //ol/li
        data_list = html.xpath('//ol/li')

        # 对定位到包含所有元素的列表进行遍历，得到包含单条数据的元素
        for li in data_list:
            # 提取单条数据中的详细内容
            title = li.xpath(".//span[@class='title'][1]/text()")
            score = li.xpath(".//span[@class='rating_num'][1]/text()")
            print('电影名称：', title[0], ' 评分：', score[0])
            # xpath 的入参前面，一定要加一个.

    def run(self):
        for url in self.url_list:
            print('***********开始抓取的url = ', url)
            self.get_page_data(url)

if __name__ == '__main__':
    db = DouBan();
    db.run()
