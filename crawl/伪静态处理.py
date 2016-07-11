import re;
#url = "http://www.site.com/index.php/index/id/14"
#url = "http://www.site.com/index.php/newsContent/id/341.html"
#url = "http://www.site.com/show/?29-575.html"
#url = "http://www.site.com/guest/?page=2"
#url = "http://www.site.com/show/hash-da39ab.html"

if re.search('html|htm|sthml',url) or url.find("?") == -1:
    flag = 0
    suffix = ""
    if re.search('html|htm|sthml',url):
        suffix = "." + re.search('html|htm|sthml',url).group()
    urlList = url.split("/")
    
    returnList = []
    
    for i in urlList:
        i = re.sub('\.shtml|\.html|\.htm','', i)
        if i.isdigit():
            returnList.append(i + "*")
            flag = 1
        else:
            returnList.append(i)
    url = '/'.join(returnList) + suffix
    
    returnList = []
    if flag == 0:
        for i in urlList:
            if re.search('html|htm|sthml',i):
                digitList = re.findall('\d+\w+',i)
                for digit in digitList:
                    i = i.replace(digit, digit + "*")
                returnList.append(i)
            else:
                returnList.append(i)
        url = '/'.join(returnList)    
    print url
