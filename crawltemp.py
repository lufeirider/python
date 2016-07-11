import re
from BeautifulSoup import BeautifulSoup
import socket
import urllib2
import re
import sys
import urlparse
import Queue
import threading

domain = "wybjpkc.henu.edu.cn"

SIMILAR_SET = set()

#获取url地址的特征
def format(url):
    if re.search("(?<=\?).+(?=htm)",url):
	r = re.search('(?<=\?).+html|(?<=\?).+htm',url)
	if r:    
	    url = re.sub('\?.+html|\?.+htm','', url)	    
    
    if urlparse.urlparse(url)[2] == '':
	url = url + '/'
    url_structure = urlparse.urlparse(url)
    netloc = url_structure[1]
    path = url_structure[2]
    query = url_structure[4]
    
    if ".html" in url:
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
    return temp

#URL相似度的判断
def url_similar_control(url):
    t = format(url)
    if t not in SIMILAR_SET:
	SIMILAR_SET.add(t)
	return True
    return False

#获取源码中得超链接
def getHyperLinks(url):
    links=[]
    urls=[]
    
    data=getPageSource(url)
    if data[0]=="200":
	urls = []
	#获取script里面的location的地址
	script = re.findall("(?<=window.location=')(.*?)(?=')",data[1])
	urls = urls + script
	
	#把类似<!-xxx-!>的语句删除 不然beautifusoup会删除下面的内容
	data[1] = re.sub('<!-.*?-!>', '', data[1])
	soup=BeautifulSoup(data[1])
	a=soup.findAll("a",{"href":re.compile(".*")})
	post=soup.findAll("form",{"action":re.compile(".*")})

	for i in a:
	    urls.append(i.get('href'))
	    
	for i in urls:
	    _url=i
	    try:
		if re.match("(javascript|:;|#)",str(_url),re.I) or str(_url) is None or re.search("(\.jpg|\.gif|\.png|\.bmp|\.mp3|\.wma|\.wmv|\.gz|\.zip|\.rar|\.iso|\.pdf|\.txt|\.db|\.doc|\.ppt|mailto:|ftp|tel)",str(_url),re.I):
		    continue
	    except TypeError:
		print "[*] Type is Error! :" + str(_url)
		continue
	    
	    #然后判断它是不是http|https开头,对于这些开头的都要判断是否是本站点， 不做超出站点的爬虫
	    if re.match('^(http|https)',_url):
		if not re.search(domain,_url):
		    continue
		else:
		    if url_similar_control(_url):
			links.append(_url)  
	    else:
		if _url[0] in '/':
		    if url_similar_control("http://" + domain + _url):
			links.append("http://" + domain + _url)
			
		elif _url[0:2] in './':
		    if url_similar_control("http://" + domain + _url[1:]):
			links.append("http://" + domain + _url[1:])
			
		elif _url[0:3] in "../":
		    isNull = re.sub('\.\./', '', _url)
		    if not isNull:
			continue
		    
		    #获取网页的url然后加上/ 不然后面的正则会多删除
		    if '.' not in _url.split('/')[-1]:
			if _url[-1] not in '/':
			    _url = _url + '/'			
		    
		    if '.' not in url.split('/')[-1] and not url.split('/')[-1].isdigit() and "/" not in url[-1]:
			url = url + "/"
				
		    #把../ 换成 url地址
		    reg=re.compile("\.\./")
		    length=len(reg.findall(_url))
		    r = re.search('.*?(?=\/\.\.)',_url[::-1] )

		    _url = '/'.join(url.split('/')[0:-length-1])+"/"+r.group()[::-1]
	    
		    
		    if url_similar_control(_url):
			links.append(_url)			
					    
		else:
		    if url_similar_control("/".join(url.split('/')[:-1])+"/" + _url):
			if "index.php/" in url:
			    urlSub = re.sub('index.php/.+', '', url)
			    links.append(urlSub + _url)
			else:
			    links.append("/".join(url.split('/')[:-1])+"/" + _url)
	print links
	return links

def getPageSource(url,timeout=100,coding=None):
    try:
        socket.setdefaulttimeout(timeout)
        req = urllib2.Request(url)
        req.add_header('User-agent', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')
        response = urllib2.urlopen(req)
        if coding is None:
            coding= response.headers.getparam("charset")
        if coding is None:
            page=response.read()
        else:
            page=response.read()
            page=page.decode(coding).encode('utf-8')
        return ["200",page]
    except Exception,e:
        print str(e)
        return [str(e),None]
    

    
    
#data=getPageSource("http://wybjpkc.henu.edu.cn/reg.php")

#print data[1]

getHyperLinks("http://yixue.henu.edu.cn/yzp/jingpinkecheng/mianyixue/newkj/jingpkc/ywkj/9chapter4IgStructureandFactions.mht")


