#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date   : 
# @Author : 
# @Usage  : 

import sys
reload(sys)
sys.setdefaultencoding('utf8')

def get_m2():
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/m2', 'r')
	m2 = []
	while 1:
		line = file.readline()
		if not line:
			break
		else:
			m2.append(line.strip())
	file.close()
	return m2

def get_download():
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/download', 'r')
	count = {}
	while 1:
		line = file.readline()
		if not line:
			break
		else:
			segs = line.strip().split('\t')
			if len(segs[1]) == 19:
				segs = segs[1].split(' ')
				year, month, day = segs[0].split('-')
				hour, minute, second = segs[1].split(':')
				try:
					count[int(month)] += 1
				except:
					count[int(month)] = 0
	file.close()
	print count

def get_browse():
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/browse', 'r')
	lines = file.readlines(100)
	file.close()
	for line in lines:
		segs = line.strip().split('\t')
		for i in range(len(segs)):
			print i, segs[i]

if __name__ == '__main__':
	#m2
	m2 = get_m2()
	print len(m2)
	#browse
	#get_browse()
	#download
	get_download()
	