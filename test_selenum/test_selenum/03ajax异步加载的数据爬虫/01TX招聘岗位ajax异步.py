#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2024/10/30 17:22
@Author  : admin
@File    : 01TX招聘岗位ajax异步.py
@Project : test_selenum

有些页面的请求，页面找不到对应的数据，页面返回的是js代码，js异步请求后，获取新的数据

直接最上面的请求结果，搜索页面中对应的数据，复制请求的url，新的页面直接请求，能够获取到对应的信息

"""

import time
import requests

f = open('TX岗位列表.txt','a+',encoding='utf-8')

url = 'https://careers.tencent.com/tencentcareer/api/post/Query'
for i in range(1,11):
    params = {
        'timestamp': int(time.time() * 1000),
        'countryId': '',
        'cityId': '',
        'bgIds': '',
        'productId': '',
        'categoryId': '',
        'parentCategoryId': '',
        'attrId': '',
        'keyword': '',
        'pageIndex': i,
        'pageSize': 10,
        'language': 'zh-cn',
        'area': 'cn'
    }

    response = requests.get(url, params=params)

    # 获取返回的json数据，会自动转换成字典格式
    result = response.json()

    lists = result['Data']['Posts']

    for pos in lists:
        print(pos)
        f.write(str(pos) + '\n')

f.close()
