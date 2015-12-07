#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date   : 
# @Author : 
# @Usage  : 

import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def pre_download():
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/download', 'r')
	file_out = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/download_pre', 'w')
	line = file.readline()
	segs = line.strip().split('\t')
	pre = [segs[0], time_to_seconds(segs[1])]
	data = {}
	data[line.strip()] = pre[1]
	while 1:
		line = file.readline()
		if not line:
			break
		else:
			segs = line.strip().split('\t')
			if len(segs[1]) == 19:
				cur = [segs[0], time_to_seconds(segs[1])]
				if pre[0] == cur[0]:
					data[line.strip()] = cur[1]
					pre = cur
				else:
					data_sorted = sorted(data.iteritems(), key = lambda x:x[1], reverse = False)
					for di in data_sorted:
						file_out.write(('%s\n') % ('\t'.join(process(di))))
					pre = cur
					data = {}
			else:
				continue
	file_out.close()
	file.close()

def process(di):
	segs = di[0].split('\t')
	m2 = segs[0]
	logtime = segs[1]
	logseconds = di[1]
	ip = segs[2]
	path = segs[3]
	nt = network_type(segs[6])
	fm = segs[9]
	at = download_type(segs[11])
	si = segs[15]
	data = [m2, logtime, str(logseconds), ip, path, fm, nt, at, si]
	return data

begin = datetime.datetime(2014, 10, 1, 0, 0, 0)

def time_to_seconds(logtime):
	segs = logtime.split(' ')
	year, month, day = segs[0].split('-')
	hour, minute, second = segs[1].split(':')
	now = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))
	return int((now-begin).total_seconds())

def network_type(nt):
	if nt == '1':
		return '1'
	elif nt == '2' or nt == '3':
		return '3'
	elif nt == '4' or nt == '5':
		return '2'
	elif nt == '6':
		return '4'
	else:
		return '0'

def download_type(at):
	if at == '6':
		return '4'
	elif at == '1' or at == '2' or at == '3':
		return at
	else:
		return '0'

if __name__ == '__main__':
	pre_download()
	