#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2024/10/26 09:15
@Author  : admin
@File    : 响应数据的获取.py
@Project : test_selenum
"""
'  '
import sys
import os
import requests

url = 'https://www.baidu.com/'

# 请求头是字典格式
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

response = requests.get(url = url, headers=headers)

print(response.content.decode() + '\n')

# 获取请求头
"""
{
'User-Agent': 'python-requests/2.32.3', 
'Accept-Encoding': 'gzip, deflate', 
'Accept': '*/*', 
'Connection': 'keep-alive'
}

"""
headers = response.request.headers
print(headers)
