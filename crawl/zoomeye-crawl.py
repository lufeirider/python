# coding=utf8
# -*- coding: UTF-8 -*-
import re
from bs4 import BeautifulSoup
import sys
import pycurl
import StringIO
import urllib
import certifi
reload(sys)
sys.setdefaultencoding('utf8')

def initCurl():
    c = pycurl.Curl()
    #c.setopt(pycurl.COOKIEFILE, "cookie_file_name")#把cookie保存在该文件中
    c.setopt(pycurl.COOKIEJAR, "cookie_file_name")
    c.setopt(pycurl.FOLLOWLOCATION, 1) #允许跟踪来源
    c.setopt(pycurl.MAXREDIRS, 5)
    #设置代理 如果有需要请去掉注释，并设置合适的参数
    #c.setopt(pycurl.PROXY, ‘http://11.11.11.11:8080′)
    #c.setopt(pycurl.PROXYUSERPWD, ‘aaa:aaa’)
    return c

def GetDate(curl, url):
    head = ["User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36",
            "Cookie: __jsluid=f608f2b6ab98ed247f42c68a9e05ebf1; __jsl_clearance=1468249118.269|0|KcPxOxfchLmUYR%2BKiF6GtghUbug%3D;"]
    buf = StringIO.StringIO()
    curl.setopt(pycurl.WRITEFUNCTION, buf.write)
    curl.setopt(pycurl.CAINFO, certifi.where())
    curl.setopt(pycurl.URL, url)
    curl.setopt(pycurl.HTTPHEADER,  head)
    curl.perform()
    the_page =buf.getvalue()
    buf.close()
    return the_page

pn = 1
flag = 1
c = initCurl()

while(flag):
    
    html = GetDate(c, ("https://www.zoomeye.org/search?q=APMServ%20.5.2.6%20port%3A9000&p={0}&t=host").format(pn))
    pn = pn + 1
    
    html = unicode(html, 'utf-8','ignore')
    
    soup = BeautifulSoup(html,"html.parser",from_encoding="utf-8")
    
    
    page = soup.findAll("ul",{"class":re.compile("pagination")})
    
    
    if not re.findall('active(.*)li', unicode(page)):
        flag = 0
    
    As = soup.findAll("a",{"class":re.compile("ip")})
    
    for a in As:
        print a.string
