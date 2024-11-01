#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2024/11/1 16:02
@Author  : admin
@File    : 06selenium中窗口的滚动.py
@Project : test_selenum



"""
import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://liuyan.people.com.cn/threads/list?fid=5052&formName=%E5%9B%BD%E5%AE%B6%E5%8F%91%E5%B1%95%E5%92%8C%E6%94%B9%E9%9D%A9%E5%A7%94%E5%91%98%E4%BC%9A%E5%85%9A%E7%BB%84%E4%B9%A6%E8%AE%B0%E3%80%81%E4%B8%BB%E4%BB%BB%E9%83%91%E6%A0%85%E6%B4%81&position=1'

driver = webdriver.Chrome()
driver.get(url)
# 隐式等待
driver.implicitly_wait(10)

while True:
    try:
        # 1. 定位元素“查看更多”
        ele = driver.find_element(By.XPATH, '//*[@class="mordList"]')
        time.sleep(2)
        # 2. 滚动页面，使得元素可见
        pos = ele.location_once_scrolled_into_view
        # 3. 点击按钮
        ele.click()
        time.sleep(random.randint(1,5))
    except:
        break

# -------------------------------- 提取数据-------------------------

# 1.获取列表
result_list = driver.find_elements(By.XPATH, '//ul[@class="replyList"]/li')
print(len(result_list))
# 2. 遍历获取留言标题，留言时间，留言内容
for item in result_list:
    title = item.find_element(By.XPATH, './/h1').text
    t = item.find_element(By.XPATH, './/div[@class="headMainS fl"]//p').text
    content = item.find_element(By.XPATH, './/*[@class="replyContent"]//*[@style="color: rgb(0, 0, 0);"]').text

    print('留言标题： ' + title)
    print("留言时间： " + t)
    print("留言内容： " + content)

driver.quit()
