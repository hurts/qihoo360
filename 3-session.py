#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date   : 
# @Author : 
# @Usage  : 

from __future__ import division
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def session(data, session_last, session_n):
	m2 = data[0][0]
	download_n = [0] * 5
	browse_n = 0
	network = []
	for di in data:
		if len(di) == 9:
			download_n[int(di[7])] += 1
			network.append(di[6])
		elif len(di) == 6:
			browse_n += 1
	start_time = data[0][1]
	end_time = data[len(data)-1][1]
	duration = int(data[len(data)-1][2]) - int(data[0][2])
	if len(network) == 0:
		network = '0'
	elif len(network) == 1:
		network = network[0]
	else:
		if '0' in network:
			network = [i for i in network if i != '0']
		network = ','.join(list(set(network)))
	file_out = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/session', 'a')
	file_out.write(('%s\t%d\t%s\t%s\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%s\n') % (m2, session_n, start_time, end_time, duration, session_last, download_n[1], download_n[2], download_n[3], download_n[4], sum(download_n), browse_n, network))
	file_out.close()


if __name__ == '__main__':
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/session', 'w')
	file.close()
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/log_merge', 'r')
	line = file.readline()
	pre = line.strip().split('\t')
	session_n = 0
	session_last = 0
	data = []
	data.append(pre)
	while 1:
		line = file.readline()
		if not line:
			break
		else:
			cur = line.strip().split('\t')
			if pre[0] == cur[0]:
				if (int(cur[2]) - int(pre[2])) <= 1800:
					data.append(cur)
					pre = cur
				else:
					if session_last == 0:
						session_n += 1
						session(data, session_last, session_n)
						data = []
						session_last = int(pre[2])
						pre = cur
						data.append(pre)
					else:
						session_n += 1
						session(data, int(data[0][2])-session_last, session_n)
						data = []
						session_last = int(pre[2])
						pre = cur
						data.append(pre)
			else:
				if session_last == 0:
					session_n += 1
					session(data, session_last, session_n)
				else:
					session_n += 1
					session(data, int(data[0][2])-session_last, session_n)
				data = []
				session_last = 0
				pre = cur
				data.append(pre)
	file.close()
	print session_n
