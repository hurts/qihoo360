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
	m2_browse = {}
	min_now = 86400 * 365
	max_now = 0
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/browse_pre', 'r')
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
			m2_browse[segs[0]] = 1
			if seconds < min_now:
				min_now = seconds
				min_sign = segs[1]
			if seconds > max_now:
				max_now = seconds
				max_sign = segs[1]
	file.close()
	print min_sign, max_sign
	return m2_browse.keys()

def get_download():
	m2_download = {}
	min_now = 86400 * 365
	max_now = 0
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/download_pre', 'r')
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
			m2_download[segs[0]] = 1
			if seconds < min_now:
				min_now = seconds
				min_sign = segs[1]
			if seconds > max_now:
				max_now = seconds
				max_sign = segs[1]
	file.close()
	print min_sign, max_sign
	return m2_download.keys()

begin = datetime.datetime(2014, 10, 1, 0, 0, 0)
def time_to_seconds(logtime):
	segs = logtime.split(' ')
	year, month, day = segs[0].split('-')
	hour, minute, second = segs[1].split(':')
	now = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))
	return int((now-begin).total_seconds())

if __name__ == '__main__':
	#m2
	m2 = get_m2()
	#browse
	m2_browse = get_browse()
	#download
	m2_download = get_download()
	m2_all = list(set(m2_browse + m2_download))
	print len(m2), len(m2_browse), len(m2_download), len(m2_all)
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/m2_all', 'w')
	for mi in m2_all:
		file.write(('%s\n') % (mi))
	file.close()
	