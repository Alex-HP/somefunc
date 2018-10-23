#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
	base64 字符转图片
"""
import os,base64

target = "ccc.txt"

imgdata = None
with open(target,'rb') as src:
	imgdata = base64.b64decode(src.read())
with open(target.split('.')[0]+".jpg",'wb') as fl:
	fl.write(imgdata)
