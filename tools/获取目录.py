# coding=utf8
# -*- coding: UTF-8 -*-
import os

dirPath = "c:\\windows\\system32"
files = os.listdir(dirPath)

f = file("AllDll.txt","a+")
for name in files:
	if ".dll" in name[-4:].lower():
		print name.lower()
		f.write(name.lower() + "\n")
f.close()
