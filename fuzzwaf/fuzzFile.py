# coding=utf8
# -*- coding: UTF-8 -*-
import re
import shutil

for i in range(0,256):
	shutil.copyfile("test.php", "php/" + str(i) + ".php")
	copyPhpFile = open("php/" + str(i) + ".php","r+b")
	copyPhpFile.seek(9)
	i = format(i, '#04x').replace("0x","")
	i = bytes.fromhex(i)
	copyPhpFile.write(i)
	copyPhpFile.close()
