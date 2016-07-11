# -*- coding:utf-8 -*-
import os,sys
import urllib2
import threading
import Queue
q=Queue.Queue()

baidu_spider="Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"

lines=open("dir.txt",'r')
for line in lines:
    line=line.rstrip()
    q.put(line)



def scaner():
    while not q.empty():
        domain=q.get()
        url="%s%s" % (domain,dirs)
        print "url   "+url
        headers={}
        headers['User-Agent']=baidu_spider
        requset=urllib2.Request(url,headers=headers)
        try:
            response = urllib2.urlopen(requset)
            content=response.read()
            if len(content):
                print "Status [%s] - path: %s" % (response.code,url)
                wx('sb.txt',url+'\n')
            response.close()
        except Exception:
            pass   


def wx(filename,context):
    f= file(filename,"a+")
    f.write(context)
    f.close()


if __name__ == '__main__':
    thread_num=1
    dirs="/phpmyadmin/"
    for i in range(1): 
        t = threading.Thread(target=scaner)
        t.start()
