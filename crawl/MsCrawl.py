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

#初始化curl设置
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

#获取网页数据
def GetData(curl, url):
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

#保存文件
def wx(filename,context):
    f= file(filename,"a+")
    f.write(context)
    f.close()


#通过BeautifulSoup筛选数据
def FilterData(url):
	c = initCurl()
	html = GetData(c, url)
	html = unicode(html, 'utf-8','ignore')
	soup = BeautifulSoup(html,"html.parser")
	msTitle = soup.findAll("h1",{"class":re.compile("title")})
	kbTitle = soup.findAll("h2",{"class":re.compile("subheading")})
	cveTitles = soup.findAll("span",{"class":re.compile("LW_CollapsibleArea_Title")})

	msTitleString = msTitle[0].string.replace("\n", "").strip()
	if re.findall("MS(.*?)(?= )", msTitleString):
		writeData = "MS"+re.findall("MS(.*?)(?= )", msTitleString)[0]

	
	if re.findall("\d\d\d\d\d+", kbTitle[0].string):
		writeData = writeData + " KB" + re.findall("\d\d\d\d\d+", kbTitle[0].string)[0]

	for cveTitle in cveTitles:
		if re.findall('CVE', unicode(cveTitle.string)):
			if re.findall("CVE(.*)", cveTitle.string):
				cveTitleString = re.findall("CVE(.*)", cveTitle.string)[0]
				writeData = writeData + " CVE" + cveTitleString
	print writeData
	wx("ms-2014.txt", writeData+"\n")


#获取links
def FilterLink(url):
	c = initCurl()
	html = GetData(c, url)
	html = unicode(html, 'utf-8','ignore')
	soup = BeautifulSoup(html,"html.parser")
	linkList = soup.find_all('div', {"class": re.compile("id")}) 

	return linkList[0].find_all('a')


links = FilterLink("https://technet.microsoft.com/zh-cn/library/security/dn632720.aspx")
for link in links:
	curLink = link.get('href')
	FilterData(curLink)


