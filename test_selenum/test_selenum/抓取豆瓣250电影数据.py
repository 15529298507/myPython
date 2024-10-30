#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2024/10/26 12:37
@Author  : admin
@File    : 抓取豆瓣250电影数据.py
@Project : test_selenum
"""
'  '
import sys
import os
import requests

url = 'https://movie.douban.com/top250'

# 请求头是字典格式
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

response = requests.get(url=url, headers=headers)

with open('douban.html','w',encoding='utf-8') as f:
    f.write(response.content.decode())