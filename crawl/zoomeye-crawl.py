# coding=utf8
# -*- coding: UTF-8 -*-
import re
from bs4 import BeautifulSoup
import sys
import pycurl
import StringIO
import urllib
import certifi
import time
import random
import time

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
    r=random.randint(0,11)
    
    head = ["User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36",
            "Cookie: __jsluid=f608f2b6ab98ed247f42c68a9e05ebf1; csrftoken=bFL4Gzx7m2SZE3OzCo83gPELcHJQyZYU; sessionid=i0x8r978nw1l1s8k8m68d19urdr8thb0; __jsl_clearance=1468316989.499|0|aqESBkoy0wKVep%2BzmdSWKYZJQk8%3D; Hm_lvt_e58da53564b1ec3fb2539178e6db042e=1467966546,1468215754,1468248863,1468304365; Hm_lpvt_e58da53564b1ec3fb2539178e6db042e=1468317014"]
    buf = StringIO.StringIO()
    curl.setopt(pycurl.WRITEFUNCTION, buf.write)
    curl.setopt(pycurl.CAINFO, certifi.where())
    curl.setopt(pycurl.URL, url)
    curl.setopt(pycurl.HTTPHEADER,  head)
    curl.perform()
    the_page =buf.getvalue()
    buf.close()
    curl.close()
    return the_page

def wx(filename,context):
    f= file(filename,"a+")
    f.write(context)
    f.close()


pn = 1
flag = 1


while(flag):
    print "pn              {0}".format(pn)
    c = initCurl()
    html = GetDate(c, ("https://www.zoomeye.org/search?q=APMServ%205.2.6%20country%3AChina%20port:80&p={0}&t=host").format(pn))
    pn = pn + 1
    
    html = unicode(html, 'utf-8','ignore')
    #print html
    soup = BeautifulSoup(html,"html.parser",from_encoding="utf-8")
    
    
    page = soup.findAll("ul",{"class":re.compile("pagination")})
    
    
    if not re.findall('active(.*)li', unicode(page)):
        flag = 0
    
    As = soup.findAll("a",{"class":re.compile("ip")})
    
    for a in As:
        wx("zoomeye.txt", a.string+"\n")
        print a.string
    time.sleep(random.uniform(2,5))
