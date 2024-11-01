#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2024/10/31 17:30
@Author  : admin
@File    : 02selenium和xpath元素定位.py
@Project : test_selenum



"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://liuyan.people.com.cn/login'

driver = webdriver.Chrome()
driver.get(url)

# 定位账号输入框
driver.find_element(By.XPATH, '//*[@placeholder="登录名/手机号/邮箱"]').send_keys('1238516184')
time.sleep(2)

# 定位密码输入框
driver.find_element(By.XPATH, '//*[@placeholder="请输入密码"]').send_keys('23563135')
time.sleep(2)

# 点击登录按钮
driver.find_element(By.XPATH, '//button[@style]').click()

time.sleep(10)
driver.quit()