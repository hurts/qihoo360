#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date   :
# @Author :
# @Usage  :

import sys
reload(sys)
sys.setdefaultencoding('utf8')

def session_list():
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/session_list.txt', 'w')
	file.close()
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/log_merge.txt', 'r')
	line = file.readline()
	pre = line.strip().split('\t')
	session_n = 0
	last_session_begin = 0
	last_session_end = 0
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
					if last_session_end == 0:
						session_n += 1
						last_session_begin, last_session_end = session(data, last_session_begin, last_session_end, session_n)
						data = []
						pre = cur
						data.append(pre)
					else:
						session_n += 1
						last_session_begin, last_session_end = session(data, int(data[0][2])-last_session_begin, int(data[0][2])-last_session_end, session_n)
						data = []
						pre = cur
						data.append(pre)
			else:
				if last_session_end == 0:
					session_n += 1
					session(data, last_session_begin, last_session_end, session_n)
				else:
					session_n += 1
					session(data, int(data[0][2])-last_session_begin, int(data[0][2])-last_session_end, session_n)
				data = []
				last_session_begin = 0
				last_session_end = 0
				pre = cur
				data.append(pre)
	file.close()

def session(data, last_session_begin, last_session_end, session_n):
	m2 = data[0][0]
	start_time = data[0][1]
	end_time = data[len(data)-1][1]
	behavior_list = behavior(data)
	if len(behavior_list) > 1:
		file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/session_list.txt', 'a')
		file.write(('%d\t%s\t%s\t%s\t%s\n') % (session_n, m2, start_time, end_time, ','.join(behavior_list)))
		file.close()
	start_seconds = int(data[0][2])
	end_seconds = int(data[len(data)-1][2])
	return start_seconds, end_seconds

def behavior(data):
	behavior_list = []
	start_seconds = int(data[0][2])
	for di in data:
		if len(di) == 9:
			at = int(di[7])
			if at == 1:
				cur_seconds = int(di[2])
				if di[8] != 'N/A':
					si = di[8]
					behavior_list.append(str(cur_seconds-start_seconds) + ':d:' + si)
		else:
			cur_seconds = int(di[2])
			if di[6] != 'N/A':
				si = di[6]
				behavior_list.append(str(cur_seconds-start_seconds) + ':b:' + si)
	return behavior_list

if __name__ == '__main__':
	session_list()
