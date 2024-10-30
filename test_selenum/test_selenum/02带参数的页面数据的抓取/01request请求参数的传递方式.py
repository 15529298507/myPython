#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2024/10/30 13:27
@Author  : admin
@File    : 01request请求参数的传递方式.py
@Project : test_selenum


方式一：
    直接拼接到url后面
        https://movie.douban.com/top250?start={}&filter=
        https://www.baidu.com/s?wd=%E6%95%B0%E5%AD%A6   数学


方式二：
    通过params参数传递

"""

import requests

# 请求头是字典格式
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}


# requests请求方式一
url = 'https://www.baidu.com/s?wd=%E6%95%B0%E5%AD%A6'

response = requests.get(url=url,headers=headers)
# print(response.content.decode())


# requests请求方式二
url2 = 'https://www.baidu.com/s'

# 请求参数（查询参数）
params ={
    'ie':'utf-8',
    'wd':'数学'
}

# 发送请求时，传递参数，使用params进行

response2 = requests.get(url=url2,headers=headers,params=params)
print(response2.content.decode())