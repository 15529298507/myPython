#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2024/11/1 10:31
@Author  : admin
@File    : 03selenium数据抓取案例1.py
@Project : test_selenum

抓取领导留言板

"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 目标浏览器
url = 'https://liuyan.people.com.cn/threads/list?fid=5052&formName=%E5%9B%BD%E5%AE%B6%E5%8F%91%E5%B1%95%E5%92%8C%E6%94%B9%E9%9D%A9%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%9A%E7%BB%84%E4%B9%A6%E8%AE%B0%E3%80%81%E4%B8%BB%E4%BB%BB%E9%83%91%E6%A0%85%E6%B4%81&position=1'

# 创建浏览器驱动
driver = webdriver.Chrome()
driver.get(url)

# 等待网页加载完成
time.sleep(3)

# 获取并打印元素
# 1.获取列表
result_list = driver.find_elements(By.XPATH, '//ul[@class="replyList"]/li')
# 2. 遍历获取留言标题，留言时间，留言内容
for item in result_list:
    title = item.find_element(By.XPATH, './/h1').text
    t = item.find_element(By.XPATH, './/div[@class="headMainS fl"]//p').text
    content = item.find_element(By.XPATH, './/*[@class="replyContent"]//*[@style="color: rgb(0, 0, 0);"]').text

    print('留言标题： ' + title)
    print("留言时间： " + t)
    print("留言内容： " + content)

time.sleep(1)

# 退出浏览器驱动
driver.quit()