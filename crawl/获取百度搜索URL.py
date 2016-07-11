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
    c.setopt(pycurl.COOKIEFILE, "cookie_file_name")#把cookie保存在该文件中
    c.setopt(pycurl.COOKIEJAR, "cookie_file_name")
    c.setopt(pycurl.FOLLOWLOCATION, 1) #允许跟踪来源
    c.setopt(pycurl.MAXREDIRS, 5)
    #设置代理 如果有需要请去掉注释，并设置合适的参数
    #c.setopt(pycurl.PROXY, ‘http://11.11.11.11:8080′)
    #c.setopt(pycurl.PROXYUSERPWD, ‘aaa:aaa’)
    return c

def GetDate(curl, url):
    head = ['Accept:*/*',
            'User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11']
    buf = StringIO.StringIO()
    curl.setopt(pycurl.WRITEFUNCTION, buf.write)
    curl.setopt(pycurl.CAINFO, certifi.where())
    curl.setopt(pycurl.URL, url)
    curl.setopt(pycurl.HTTPHEADER,  head)
    curl.perform()
    the_page =buf.getvalue()
    buf.close()
    return the_page

pn = 0
flag = 1
c = initCurl()

while(flag):
    try:
        p = urllib.quote("我")
        print p
        html = GetDate(c, ("https://www.baidu.com/s?wd="+ p +"&pn={0}").format(pn))
        
        pn = pn + 10
        
        html = unicode(html, 'utf-8','ignore')
        
        soup = BeautifulSoup(html,"html.parser",from_encoding="utf-8")
        
        divs = soup.findAll("div",{"class":re.compile("c-container")})
        
        page = soup.findAll("div", attrs = {'id': 'page'})
        
        if not re.findall('fk fk_cur(.*)fk fkd', unicode(page)):
            flag = 0
        
        
        for divstr in divs:
            if divstr.find("a", style=re.compile("text-decoration:none")):
                text = divstr.find("a", style=re.compile("text-decoration:none")).get_text()
                text = text.encode('utf8')
                script = re.findall("(.*?)/",text)
                print script[0]
    except:
        pass
