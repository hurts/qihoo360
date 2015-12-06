#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date   : 
# @Author : 
# @Usage  : 

import datetime
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

def get_browse():
	min_now = 86400 * 365
	max_now = 0
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/browse', 'r')
	while 1:
		line = file.readline()
		if not line:
			break
		else:
			segs = line.strip().split('\t')
			if len(segs[1]) == 19:
				seconds = time_to_seconds(segs[1])
			else:
				continue
			if seconds < min_now:
				min_now = seconds
				min_sign = segs[1]
			if seconds > max_now:
				max_now = seconds
				max_sign = segs[1]
	file.close()
	print min_sign, max_sign

def get_download():
	min_now = 86400 * 365
	max_now = 0
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/download', 'r')
	while 1:
		line = file.readline()
		if not line:
			break
		else:
			segs = line.strip().split('\t')
			if len(segs[1]) == 19:
				seconds = time_to_seconds(segs[1])
			else:
				continue
			if seconds < min_now:
				min_now = seconds
				min_sign = segs[1]
			if seconds > max_now:
				max_now = seconds
				max_sign = segs[1]
	file.close()
	print min_sign, max_sign

begin = datetime.datetime(2014, 1, 1, 0, 0, 0)
def time_to_seconds(logtime):
	segs = logtime.split(' ')
	try:
		year, month, day = segs[0].split('-')
	except:
		print segs[0]
	hour, minute, second = segs[1].split(':')
	now = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))
	return int((now-begin).total_seconds())

if __name__ == '__main__':
	#m2
	m2 = get_m2()
	print len(m2)
	#browse
	get_browse()
	#download
	get_download()
	