#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2024/11/1 16:39
@Author  : admin
@File    : 08selenium模拟鼠标操作.py
@Project : test_selenum



"""
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(10)

# 进入子界面 iframe
driver.switch_to.frame('iframeResult')

# 创建一个鼠标对象
ac = ActionChains(driver)
# 找到要点击的对象
ac.move_to_element(driver.find_element(By.XPATH,'//*[@id="draggable"]'))
# 按下鼠标
ac.click_and_hold()
# 找到目的位置或者对象
ac.move_to_element(driver.find_element(By.XPATH,'//*[@id="droppable"]'))
# 释放鼠标
ac.release()
# 执行操作
ac.perform()

time.sleep(5)
driver.quit()