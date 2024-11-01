#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2024/11/1 17:51
@Author  : admin
@File    : 01selenium反爬检测案例.py
@Project : test_selenum



"""

from selenium import webdriver

from test_selenum.weixin import driver, options

url = 'https://www.aqistudy.cn/'

opt = webdriver.ChromeOptions()
# 添加检测的参数
opt.add_argument('--disable-infobars')
opt.add_experimental_option("wxcludeSwitches", ["enable-automation"])
opt.add_experimental_option('useAutomationExtension',False)
driver = webdriver.Chrome(options=opt)
with open('')

