#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2024/10/31 11:17
@Author  : admin
@File    : 02小饭桌商业融资资讯抓取jsonPath.py
@Project : test_selenum

1. 打开网页，寻找链接
2. 创建请求
3. 转成json
4. 使用jsonpath 提取关键字内容
4. 生成文件

"""
import json
import time
import random

import requests
from jsonpath import jsonpath

# #--------单独只爬一页网址-----------------------------------------------------
# url = 'https://www.xfz.cn/api/website/articles/?p=1&n=20&type='
#
# response = requests.get(url)
# result = response.json()
# result_format = json.dumps(result, indent=4, ensure_ascii=False)
# # 写文件方式一
# json.dump(result, open('result_format1.json', 'w', encoding='utf-8'), indent=4, ensure_ascii=False)
#
# # 写文件方式二
# with open('result_format2.json', 'w', encoding='utf-8') as f:
#     f.write(result_format)
#
# for item in result['data']:
#     title = jsonpath(item, '$.title')[0]
#     author = jsonpath(item, '$...name')[0]
#     author_photo = jsonpath(item, '$..photo')[0]
#     time1 = jsonpath(item, '$.time')[0]


#--------分页爬取网站-----------------------------------------------------
for i in range(1,10):
    url = 'https://www.xfz.cn/api/website/articles/?p={}&n=20&type='.format(i)
    response = requests.get(url)
    result = response.json()
    # result_format = json.dumps(result, indent=4, ensure_ascii=False)
    # # 写文件方式一
    # json.dump(result, open('result_format1.json', 'w', encoding='utf-8'), indent=4, ensure_ascii=False)
    #
    # # 写文件方式二
    # with open('result_format2.json', 'w', encoding='utf-8') as f:
    #     f.write(result_format)

    with open('result_小饭桌.txt','a',encoding='utf-8') as f:
        for item in result['data']:
            title = jsonpath(item, '$.title')[0]
            author = jsonpath(item, '$...name')[0]
            author_photo = jsonpath(item, '$..photo')[0]
            time1 = jsonpath(item, '$.time')[0]

            f.write(title + '\t' + author + '\t' + author_photo + '\t' + time1+'\n')
    f.close()

    time.sleep(random.uniform(1, 3.2))
