# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from BeautifulSoup import BeautifulSoup
import socket
import urllib2
import re
import sys
import urlparse
import Queue
import threading


def format(url):
    
    if urlparse.urlparse(url)[2] == '':
	url = url + '/'
    url_structure = urlparse.urlparse(url)
    netloc = url_structure[1]
    path = url_structure[2]
    query = url_structure[4]
    

    if path.split('/')[-1].isdigit():
	path = "/".join(path.split('/')[:-1])
    
    if ".html" in url or ".htm" in url:
	pathList = path.split('/')
	temp = pathList[:]
	
	#for i in temp:
	    #subHtml = re.sub('\.html|\.htm', '', i)
	    #if subHtml.isdigit():
		#pathList.remove(i)
		    
	flag = 0
	for i in temp:
	    if ".html" in i or ".htm" in i:
		subHtml = re.sub('\.html|\.htm', '', i)
		pathList.remove(i)
		if not subHtml.isdigit():
		    r = re.search('[a-z]+',i)
		    query = r.group()
		    flag = 1
		
	    if i.isdigit():
		pathList.remove(i)
		
	if not flag:
	    query = "number=1"
	
	
	path = '/'.join(pathList)
    
    temp = (netloc,tuple([i for i in path.split('/')]),tuple(sorted([i.split('=')[0] for i in query.split('&')])))
    print temp

    
    

#http://bio.henu.edu.cn/a/xueyuangaikuang/shiziduiwu/yuanshi/2012/0918/30.html
#/test/list_8_2.html


format("http://zbb.henu.edu.cn/Article/HTML/235.htm")

format("http://zbb.henu.edu.cn/Article/HTML/235.htm")

#format("http://127.0.0.1/index.php?id=1")

#format("http://127.0.0.1/index.php?id=2")

#format("http://127.0.0.1/index.php?id=3")
