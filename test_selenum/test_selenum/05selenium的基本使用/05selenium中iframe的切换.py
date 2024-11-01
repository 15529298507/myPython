#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2024/11/1 13:50
@Author  : admin
@File    : 05selenium中iframe的切换.py
@Project : test_selenum

# 方式一: 切换iframe： 通过iframe的名字（name属性）进行切换
driver.switch_to.frame("")

# 方式二： 通过element元素去进行切换
driver.switch_to.frame(driver.find_elements(By.TAG_NAME, "iframe")[0])

# 方式三： 通过索引切换
driver.switch_to.frame(1)

"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 显式等待的代码演示
url = "https://mail.qq.com/"
driver = webdriver.Chrome()
driver.get(url)

driver.switch_to.frame(driver.find_elements(By.XPATH, '//*[@id="QQMailSdkTool_login_loginBox_qq"]/iframe')[0])
driver.switch_to.frame('ptlogin_iframe')

# 点击密码登录
driver.find_element(By.XPATH,'//*[@id="switcher_plogin"]').click()

# 输入账号
driver.find_element(By.XPATH,'//*[@name="u"]').send_keys('12313134')

time.sleep(1)

# 输入密码
driver.find_element(By.XPATH,'//*[@name="p"]').send_keys('12313134')

# 点击登录按钮
# driver.find_element(By.XPATH,'//*[@id="login_button"]').click()
time.sleep(2)

# 切换回默认的HTML页面中
driver.switch_to.default_content()

# 切换回父级的iframe中
# driver.switch_to.parent_frame()

time.sleep(2)
driver.quit()