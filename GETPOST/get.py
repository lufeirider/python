#!/usr/bin/env python
# -*- coding: gbk -*-
# -*- coding: utf_8 -*-
# Date: 2014/11/25
# Created by 独自等待
# 博客 http://www.waitalone.cn/
import re

try:
    import requests
except ImportError:
    raise SystemExit('\n[!] requests模块导入错误,请执行pip install requests安装!')

print '\n网络信息安全攻防学习平台脚本关第2题\n'
s = requests.Session()
url = 'http://1.hacklist.sinaapp.com/xss2_0d557e6d2a4ac08b749b61473a075be1/index.php'
r = s.get(url)
res = unicode(r.content, 'utf-8').encode('gbk')
# print res

num = re.findall(re.compile(r'<br/>\s+(.*?)='), res)[0]
print '当前获取到需要口算的表达式及计算结果为:\n\n%s=%d\n' % (num, eval(num))

r = s.post(url, data={'v': eval(num)})
print re.findall(re.compile(r'<body>(.*?)</body>'), r.content)[0]
