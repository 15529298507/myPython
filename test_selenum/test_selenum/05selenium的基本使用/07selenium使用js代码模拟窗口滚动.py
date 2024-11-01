#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2024/11/1 16:30
@Author  : admin
@File    : 07selenium使用js代码模拟窗口滚动.py
@Project : test_selenum



"""
import random
import time

from selenium import webdriver

url = 'https://liuyan.people.com.cn/threads/list?fid=5052&formName=%E5%9B%BD%E5%AE%B6%E5%8F%91%E5%B1%95%E5%92%8C%E6%94%B9%E9%9D%A9%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%9A%E7%BB%84%E4%B9%A6%E8%AE%B0%E3%80%81%E4%B8%BB%E4%BB%BB%E9%83%91%E6%A0%85%E6%B4%81&position=1'
driver = webdriver.Chrome()

driver.get(url)
driver.implicitly_wait(10)

for i in range(1,5):
    # 在网页的控制台界面能够编写js代码
    js = 'window.scrollBy(0,100)'
    # 启动执行js代码
    driver.execute_script(js)
    time.sleep(2)

time.sleep(2)
driver.quit()