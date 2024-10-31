#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2024/10/31 17:30
@Author  : admin
@File    : 02selenium和xpath元素定位.py
@Project : test_selenum



"""

from selenium import webdriver

url = 'https://wwww.baidu.com'

driver = webdriver.Chrome()
driver.get(url)