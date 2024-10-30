#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2024/10/26 09:03
@Author  : admin
@File    : 字符串转换.py
@Project : test_selenum
"""
'  '
import sys
import os

s = 'hello python'

# 将字符串转换为bytes类型,通常成为二进制字符串
res = s.encode()
print(res)

# 将bytes类型转换成字符串
res2 = res.decode()