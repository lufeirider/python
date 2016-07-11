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

q=Queue.Queue()

SIMILAR_SET = set()

class MyCrawler:
    def __init__(self,seeds):
        #使用种子初始化url队列
	if "http" in seeds:
	    pattern = re.compile(r'(?<=//).+(?<!/)')
	    match = pattern.search(seeds)
	    self.domain=match.group()
	else:
	    self.domain = seeds
	    seeds = "http://" + seeds + "/"

	self.url_similar_control(seeds)
	self.url_similar_control(self.domain)
	
        self.linkQuence=linkQuence()
        if isinstance(seeds,str):
            self.linkQuence.addUnvisitedUrl(seeds)
        if isinstance(seeds,list):
            for i in seeds:
                self.linkQuence.addUnvisitedUrl(i)
        print "Add the seeds url \"%s\" to the unvisited url list"%str(self.linkQuence.unVisited)
    #抓取过程主函数
    def crawling(self,seeds,crawl_count):
        #循环条件：待抓取的链接不空且专区的网页不多于crawl_count
        while self.linkQuence.unVisitedUrlsEnmpy() is False and self.linkQuence.getVisitedUrlCount()<=crawl_count:
            #队头url出队列
            visitUrl=self.linkQuence.unVisitedUrlDeQuence()
            print "Pop out one url \"%s\" from unvisited url list"%visitUrl
            if visitUrl is None or visitUrl=="":
                continue
            #获取超链接
            links=self.getHyperLinks(visitUrl)
	    
	    if "notlink" not in links:
		if re.search("\?|.html|.shtml|.htm|/\d",visitUrl):
		    writeFile(self.domain + ".txt", visitUrl + "\n")
		    writeFile("urls.txt", visitUrl + "\n")
		    
		print "Get %d new links"%len(links)
		#将url放入已访问的url中
		#self.linkQuence.addVisitedUrl(visitUrl)
		print "Visited url count: "+str(self.linkQuence.getVisitedUrlCount())
		#未访问的url入列
		for link in links:
		    self.linkQuence.addUnvisitedUrl(link)
		print "%d unvisited links:"%len(self.linkQuence.getUnvisitedUrl())
            
    #获取源码中得超链接
    def getHyperLinks(self,url):
	links=[]
	urls=[]
	
	data=self.getPageSource(url)
	
	if data[0]!= "200":
	    return "notlink"
	
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
	    
	    if post:
		for i in post:
		    if self.url_similar_control(i.get('action')):
			writeFile("posts.txt", url + "\n")
			urls.append(i.get('action'))
			writeFile("posts.txt", i.get('action') + "\n")

	    for i in a:
		urls.append(i.get('href'))
		
	    for i in urls:
		_url=i
		try:
		    if re.match("(javascript|:;|#)",str(_url),re.I) or str(_url) is None or re.search("(\.jpg|\.gif|\.png|\.bmp|\.mp3|\.wma|\.wmv|\.gz|\.zip|\.rar|\.iso|\.pdf|\.txt|\.db|\.doc|\.xls|\.swf|mailto:|ftp|tel)",str(_url),re.I):
			continue
		except TypeError:
		    print "[*] Type is Error! :" + str(_url)
		    continue
		
		#然后判断它是不是http|https开头,对于这些开头的都要判断是否是本站点， 不做超出站点的爬虫
		if re.match('^(http|https)',_url):
		    if not re.search(self.domain,_url):
			continue
		    else:
			#print "################################"
			#print _url
			#print "################################"			
			if self.url_similar_control(_url):
			    links.append(_url)  
		else:
		    #try:
			#print _url
		    #except:
			#print _url.encode("utf-8")
			
		    if _url[0] in '/':
			
			if self.url_similar_control("http://" + self.domain + _url):
			    links.append("http://" + self.domain + _url)
			    
		    elif _url[0:2] in './':
			if self.url_similar_control("http://" + self.domain + _url[1:]):
			    links.append("http://" + self.domain + _url[1:])
			    
		    elif _url[0:3] in "../":
			isNull = re.sub('\.\./', '', _url)
			if not isNull:
			    continue
			
			#获取网页的url然后加上/ 不然后面的正则会多删除
			if '.' not in _url.split('/')[-1]:
			    if _url[-1] not in '/':
				_url = _url + '/'
				
			#解决 site.com/test 这样的后面没反斜杠的目录
			if '.' not in url.split('/')[-1] and not url.split('/')[-1].isdigit() and "/" not in url[-1]:
			    url = url + "/"			
			
			#把../ 换成 url地址
			reg=re.compile("\.\./")
			length=len(reg.findall(_url))
			r = re.search('.*?(?=\/\.\.)',_url[::-1] )

			_url = '/'.join(url.split('/')[0:-length-1])+"/"+r.group()[::-1]
			
			if self.url_similar_control(_url):
			    links.append(_url)			
					    
		    else:
			if self.url_similar_control("/".join(url.split('/')[:-1])+"/" + _url):
			    if "index.php/" in url:
				urlSub = re.sub('index.php/.+', '', url)
				links.append(urlSub + _url)
			    else:
				links.append("/".join(url.split('/')[:-1])+"/" + _url)
				
			    #links.append("/".join(url.split('/')[:-1])+"/" + _url)			    
	print links 
	return links
    
    #获取网页源码
    def getPageSource(self,url,timeout=100,coding=None):
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
    
    #获取url地址的特征
    def format(self,url):	    
	if urlparse.urlparse(url)[2] == '':
	    url = url + '/'
	url_structure = urlparse.urlparse(url)
	netloc = url_structure[1]
	path = url_structure[2]
	query = url_structure[4]
	
	
	#解决http://xb.henu.edu.cn/index.php/former/one_article/6 这样伪静态
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
		    #解决 html之类结尾的伪静态特征
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
    def url_similar_control(slef,url):
	t = slef.format(url)
	if t not in SIMILAR_SET:
	    SIMILAR_SET.add(t)
	    return True
	return False
    
    #测试链接是否能访问
    def testUrl(self,url):
	statusCode = urllib2.urlopen(url).getcode()
	if (statusCode == 200):
	    return True
	else:
	    return False    
    
class linkQuence:
    def __init__(self):
        #已访问的url集合
        self.visted=[]
        #待访问的url集合
        self.unVisited=[]
    #获取访问过的url队列
    def getVisitedUrl(self):
        return self.visted
    #获取未访问的url队列
    def getUnvisitedUrl(self):
        return self.unVisited
    #添加到访问过得url队列中
    def addVisitedUrl(self,url):
        self.visted.append(url)
    #移除访问过得url
    def removeVisitedUrl(self,url):
        self.visted.remove(url)
    #未访问过得url出队列
    def unVisitedUrlDeQuence(self):
        try:
            return self.unVisited.pop()
        except:
            return None
    #保证每个url只被访问一次
    def addUnvisitedUrl(self,url):
        if url!="" and url not in self.visted and url not in self.unVisited:
            self.unVisited.insert(0,url)
    #获得已访问的url数目
    def getVisitedUrlCount(self):
        return len(self.visted)
    #获得未访问的url数目
    def getUnvistedUrlCount(self):
        return len(self.unVisited)
    #判断未访问的url队列是否为空
    def unVisitedUrlsEnmpy(self):
        return len(self.unVisited)==0
    
def main(seeds,crawl_count):
    craw=MyCrawler(seeds)
    craw.crawling(seeds,crawl_count)


def scaner():
    while not q.empty():
        url = q.get()
        t = main(url,100)
	
#保存记录
def writeFile(filename,context):
    f= file(filename,"a+")
    f.write(context)
    f.close()

if __name__=="__main__":
    #读取网址
    lines = open("domains.txt","r")
    for line in lines:
        line=line.rstrip()
        q.put(line)
    
    
    #开启线程
    for i in range(3): 
        t = threading.Thread(target=scaner)
        t.start()
