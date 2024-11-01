#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2024/11/1 13:50
@Author  : admin
@File    : 04selenium等待的三种方式.py
@Project : test_selenum

# 1.强制等待，无论网页有没有加载完成，都会进行等待
time.sleep(10)

# 2.隐式等待，表示我们定位某个元素的时候，最长的等待时间是10秒，如果超过设定的等待时间，如果是找不到，会抛出异常
driver.implicitly_wait(10)

# 3.显式等待，可以设置等待条件，等待到元素可见、元素可点击；某些情况找不到，就要用显示等待
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 显式等待的代码演示
url = "https://mail.qq.com/"
driver = webdriver.Chrome()

# 1. 强制时间等待
time.sleep(2)

driver.get(url)

# 2. 隐式等待
#driver.implicitly_wait(5)

# 3.显式等待

# 1) 创建一个等待对象   最大时间10秒，每隔0.2秒找一次
wait = WebDriverWait(driver, 10, 0.2).until(
    # 等待元素可见 入参是元祖
    EC.visibility_of_element_located((By.XPATH, '//*[@id="switcher_plogin"]'))

    # 等待元素可点击 入参是元祖
    # EC.element_to_be_clickable((By.XPATH, '//*[@id="switcher_plogin"]'))
)

time.sleep(2)
driver.quit()