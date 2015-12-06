#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date   : 
# @Author : 
# @Usage  : 

from __future__ import division
import matplotlib.pyplot as plt
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def session(data, session_last, session_n):
	print session_n, data[0][0], data[0][1], data[len(data)-1][1], len(data)

if __name__ == '__main__':
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
		if session_n == 10000:
			break
	file.close()
