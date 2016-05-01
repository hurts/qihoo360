#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date   : 
# @Author : 
# @Usage  : 

from __future__ import division
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def documents():
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/behavior_texts.txt', 'w')
	file.close()
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/behavior.txt', 'r')
	while 1:
		line = file.readline()
		if not line:
			break
		else:
			segs = line.strip().split('\t')
			extract(segs[0], segs[1].split(','))
	file.close()

def extract(m2, data):
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/behavior_texts.txt', 'a')
	data_n = len(data)
	doc = []
	for i in range(data_n):
		segs = data[i].split('-', 1)
		segs[1] = segs[1][2:]
		if i == 0:
			sec_old = int(segs[0])
			sen = [segs[1]]
		else:
			sec_new = int(segs[0])
			if sec_new - sec_old >= 86400:
				doc.append(' '.join(sen))
				sen = [segs[1]]
			else:
				sen.append(segs[1])
			sec_old = sec_new
	doc.append(' '.join(sen))
	file.write(('%s\t%s\n') % (m2, '. '.join(doc)))
	file.close()

if __name__ == '__main__':
	documents()
	

	

	