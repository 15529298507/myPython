#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2024/10/26 08:57
@Author  : admin
@File    : requests请求.py
@Project : test_selenum
"""
'  '
import sys
import os
import requests

url = 'https://www.baidu.com/'
response = requests.get(url)

# 方式一
# 获取到的是原始的二进制数据（bytes）
# 将二进制的数据转换成字符串
print(response.content.decode())

# 方式二 获取字符床
print(response.text)

# 获取http状态码
status = response.status_code

# 获取响应头
headers = response.headers

# 获取cookie 信息
cookes = response.cookies