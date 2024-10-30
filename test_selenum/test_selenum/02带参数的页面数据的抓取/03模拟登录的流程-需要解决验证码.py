#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2024/10/30 14:53
@Author  : admin
@File    : 03模拟登录的流程-需要解决验证码.py
@Project : test_selenum

1. 通过控制台抓包
    登录的url地址；
    登录时传递的参数；
    请求方法；

2. 网站用户鉴权的方式
    网站的后台服务校验用户是否登录的方法：
    1） cookie + session 去实现
    2） 通过token鉴权（一般常见于前后端分离的项目）

    如何判断网站使用的是哪种方式的鉴权
    方法1：登录时传递的参数是 表单 格式的（Form Data），百分之九十以上使用的是 cookie + session 鉴权
    方法2：登录时传递的参数是 json 格式的（Request Payload），前后端分析，百分之九十以上使用的是 token 鉴权
    方法3：登录的请求地址和网页的地址不一致（前面的域名），百分之九十使用的 token 鉴权

3. 实现步骤
    1） 先请求登录接口，传递正确的账号密码
    2） 保存登录成功之后的cookie信息
    3） 请求其他页面时，带上登录之后的token即可

4. 使用 cookie + session 鉴权的方式登录流程
    1） 传递账号密码，进行登录
    2） 登录之后保存 cookie （返回时在响应头的set-cookie 字段中）
    3） 请求其他页面时，携带 cookie

5. 使用 token 鉴权的方式登录流程
    1） 传递账号密码，进行登录
    2） 登录之后保存 token （返回时在响应体中）
    3） 请求其他页面时，携带 cookie

"""

import requests

# *****************************************************************************************
# 中华网的模拟登录 cookie + session

# 请求的地址
login_url = 'https://accounts.douban.com/j/mobile/login/basic'

# 请求头是字典格式
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony',
    'Cookie':'douban-fav-remind=1; viewed="1822808_5354316"; bid=deVByfAQcRw; ll="118375"; _pk_id.100001.8cb4=bcd48c287d994ba9.1729917409.; __utmc=30149280; ap_v=0,6.0; push_noty_num=0; push_doumail_num=0; __utmv=30149280.28370; __yadk_uid=WfY61LGVPZMMa8H4FCIeovyyLN9Ic8IJ; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1730276022%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; _pk_ses.100001.8cb4=1; __utma=30149280.57021194.1647942129.1730273421.1730276023.7; __utmz=30149280.1730276023.7.3.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmb=30149280.3.10.1730276023; dbcl2="283708116:PjMot7M+MF4"'
}

# 请求参数
params = {
    'remember': 'true',
    'name': '15529298507',
    'password': '123456jwj'
}

# cookie 参数的传递方式一
"""
request.get(cookies = response.cookies)
"""
# cookie 参数的传递方式二
"""
headers = {
        'Cookie': '字符串格式cookie值'
    }
    
    requests.get()
"""
# cookie 参数的传递方式三
"""
使用request请求中的session自动处理cookie
1. 使用requests.session的方法创建一个对象
http = requests.session()
http.post()

2. 后续的步骤都用创建的http session类进行操作
"""


response = requests.post(url=login_url,headers=headers,data=params)
print(response.content.decode())