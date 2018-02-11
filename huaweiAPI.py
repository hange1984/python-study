# -*- coding:utf-8 -*-
import json

import requests


# Disable warning
requests.packages.urllib3.disable_warnings()
# 建立session
session = requests.Session()
# 用户接入地址，可从此地址得到TOKEN，查看手册得到。
session_url = 'https://10.128.112.55:8088/deviceManager/rest/xxxxx/sessions'
# 查看用户地址，
query_user_url = 'https://10.128.112.55:8088/deviceManager/rest/210235876310EB000001/user/admin'
# 用户名密码。
pass_wd = {'username': 'admin', 'password': 'stg@W)P!Q%T', 'scope': '0'}
# 链接用户接入地址，从返回消息中，查到token。
r = session.post(session_url, json=pass_wd, verify=False)
token= r.json()['data']['iBaseToken']

# 根据手册，除了接入认证，其他所有查询都要带上消息头，消息头中要有直接接入时的token。
headers1 = {
    'Accept': 'text/plain, text/html',
    'Accept-Encoding': 'gzip,default',
    'Accept-Language': 'zh-CN,zh;en-US,en;',
    # "Cache-Control": "no-store",
    "Connection": "keep-alive",
    "Host": "10.128.112.55:8088",
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36',
    "Date": "",
    "Content-Type": "application/json;charset=utf-8",
    # "Content-Length": "348",
    'X-Requested-With': 'XMLHttpRequest',
    'iBaseToken': token
}

# 获取用户信息
u = session.get(query_user_url, headers=headers1,verify=False)
print(u.text)








