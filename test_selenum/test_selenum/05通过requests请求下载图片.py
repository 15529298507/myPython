#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2024/10/26 09:37
@Author  : admin
@File    : 05通过requests请求下载图片.py
@Project : test_selenum
"""
from requests请求 import response

'  '
import sys
import os
import requests

url = 'https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'

# 请求头是字典格式
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

response = requests.get(url=url, headers=headers)

with open('baidu.jpg', 'wb') as f:
    f.write(response.content)
