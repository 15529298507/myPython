#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2024/10/30 13:38
@Author  : admin
@File    : 02post请求和模拟登录.py
@Project : test_selenum

使用场景：
    登录注册
    参数需要传输大文本内容的时候

发送post请求的方法：
    requests.post()

参数传递：
    1. 表单参数：from-data
        requests.post(url=ulr,data=字典参数)
    2. json参数
        requests.post(url=ulr,json=字典参数)
"""
import requests

# 请求头是字典格式
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}


# 方式1：表单参数请求
url = 'https://fanyi.baidu.com/sug'

params = {
    'kw':'学习'
}

response = requests.post(url=url, headers=headers, data=params)
# print(response.content.decode())


# 方式二：json参数请求

url = 'https://fanyi.baidu.com/ait/text/translate'

jsons = {
    "query":"学习",
    "from":"zh",
    "to":"en",
    "reference":"",
    "corpusIds":[],
    "needPhonetic":'false',
    "domain":"common",
    "milliTimestamp":1730267083137}

response2 = requests.post(url=url, headers=headers,json= jsons)
print(response2.content.decode())