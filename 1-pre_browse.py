#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date   : 
# @Author : 
# @Usage  : 

import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def pre_browse():
	m2_model = {}
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/browse', 'r')
	file_out = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/browse_pre', 'w')
	file_out_m = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/m2_model', 'w')
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
			m2 = segs[0]
			if not m2_model.has_key(m2):
				m2_model[m2] = [segs[5], segs[19]]
				file_out_m.write(('%s\t%s\t%s\n') % (m2, segs[5], segs[19]))
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
	file_out_m.close()
	file.close()

def process(di):
	segs = di[0].split('\t')
	m2 = segs[0]
	logtime = segs[1]
	logseconds = di[1]
	ip = segs[2]
	path = segs[3]
	fm = segs[12]
	data = [m2, logtime, str(logseconds), ip, path, fm]
	return data

begin = datetime.datetime(2014, 10, 1, 0, 0, 0)

def time_to_seconds(logtime):
	segs = logtime.split(' ')
	year, month, day = segs[0].split('-')
	hour, minute, second = segs[1].split(':')
	now = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))
	return int((now-begin).total_seconds())

if __name__ == '__main__':
	pre_browse()
	