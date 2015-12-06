#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date   : 
# @Author : 
# @Usage  : 

import sys
reload(sys)
sys.setdefaultencoding('utf8')

def merge(m2, data_x, data_y):
	data = {}
	data_x_n = len(data_x)
	data_y_n = len(data_y)
	for i in range(data_x_n + data_y_n):
		if i < data_x_n:
			data[i] = int(data_x[i][1])
		else:
			data[i] = int(data_y[i-data_x_n][1])
	data_sorted = sorted(data.iteritems(), key = lambda x:x[1], reverse = False)
	file_out = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/log_merge', 'a')
	for di in data_sorted:
		if di[0] < data_x_n:
			file_out.write(('%s\t%s\n') % (m2, '\t'.join(data_x[di[0]])))
		else:
			file_out.write(('%s\t%s\n') % (m2, '\t'.join(data_y[di[0]-data_x_n])))
	file_out.close()

if __name__ == '__main__':
	file_out = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/log_merge', 'w')
	file_out.close()
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/download_pre', 'r')
	download = {}
	count = 0
	while 1:
		line = file.readline()
		count += 1
		if not line:
			break
		else:
			segs = line.strip().split('\t')
			try:
				download[segs[0]].append(segs[1:])
			except:
				download[segs[0]] = []
				download[segs[0]].append(segs[1:])
		if count%10000 == 0:
			print count
	file.close()
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/browse_pre', 'r')
	line = file.readline()
	pre = line.strip().split('\t')
	browse = []
	browse.append(pre[1:])
	while 1:
		line = file.readline()
		if not line:
			if download.has_key(pre[0]):
				merge(pre[0], browse, download[pre[0]])
			else:
				merge(pre[0], browse, [])
			break
		else:
			cur = line.strip().split('\t')
			if pre[0] == cur[0]:
				browse.append(cur[1:])
				pre = cur
			else:
				if download.has_key(pre[0]):
					merge(pre[0], browse, download[pre[0]])
					del download[pre[0]]
					browse = []
				else:
					merge(pre[0], browse, [])
					browse = []
				pre = cur
				browse.append(pre[1:])
	for di in download.keys():
		merge(di, [], download[di])
	file.close()


