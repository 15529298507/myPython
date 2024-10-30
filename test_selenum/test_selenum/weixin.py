#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2024/10/23 23:45
@Author  : admin
@File    : weixin.py
@Project : test_selenum
"""
'  '
import sys
import os

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置浏览器
options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# 目标网址
url = 'https://weixin.sogou.com/'

# 打开网址
driver.get(url)

# 输入关键字并搜索
search_box = driver.find_element(By.NAME, 'query')
search_box.send_keys('AI')

# 点击搜索按钮
search_button = driver.find_element(By.XPATH, '//input[@type="submit" and @value="搜文章"]')
search_button.click()

# 等待页面加载
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "news-box")]')))

# 存储结果
results = []

# 爬取前5页
for page in range(1, 6):
    print(f"正在爬取第 {page} 页...")

    # 获取文章列表
    articles = driver.find_elements(By.XPATH, '//div[contains(@class, "news-box")]//h3/a')

    for article in articles:
        try:
            title = article.text
            link = article.get_attribute('href')
            # 摘要和来源可以尝试其他选择器获取
            summary = article.find_element(By.XPATH, '..//following-sibling::p').text
            source = article.find_element(By.XPATH, '..//following-sibling::div[contains(@class, "sour")]').text

            results.append({
                '标题': title,
                '摘要': summary,
                '链接': link,
                '来源': source
            })
        except Exception as e:
            print(f"提取失败: {e}")

    # 下一页
    try:
        next_button = driver.find_element(By.LINK_TEXT, '下一页')
        next_button.click()
        time.sleep(5)  # 等待页面加载
    except:
        print("没有更多页面可爬取。")
        break

# 保存到Excel文件
df = pd.DataFrame(results)
filename = f"AI_微信_{time.strftime('%Y%m%d_%H%M%S')}.xlsx"
df.to_excel(filename, index=False)

print(f"爬取完成，结果已保存为 {filename}.")

# 关闭浏览器
driver.quit()
