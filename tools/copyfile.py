# coding=utf8
# -*- coding: UTF-8 -*-
import re
import shutil
f = open("dll.txt", "r")  
while True:  
    line = f.readline()  
    if line:  
        pass    # do something here 
        line=line.strip()
        shutil.copyfile("vcode1.png", "dll/"+line)  
        print line
    else:  
        break
f.close()
