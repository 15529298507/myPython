#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2024/10/31 17:19
@Author  : admin
@File    : 01selenium的基本使用.py
@Project : test_selenum



"""
import time

from selenium import webdriver

# 创建一个driver对象（启动浏览器）
driver = webdriver.Chrome()

# 打开一个网页
driver.get("https://www.baidu.com")
time.sleep(2)

# 窗口最大化
driver.maximize_window()
time.sleep(3)

# 刷新页面
driver.refresh()
time.sleep(2)

# 获取页面的源码, 页面渲染之后的源码，数据内容比requests请求的内容全
source = driver.page_source

# 截取当前的页面
driver.save_screenshot('baidu.jpg')

# 关闭浏览器
driver.quit()

"""
通常通过selenium，关闭的时候没有使用driver.quite退出，会导致系统中启动多个chromedriver的进程，可以在命令
行执行下面的命令，批量删除chromedirver的进程
"""

