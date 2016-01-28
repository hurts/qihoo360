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


if __name__ == '__main__':
	delta = []
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/log_merge.txt', 'r')
	line = file.readline()
	pre = line.strip().split('\t')
	while 1:
		line = file.readline()
		if not line:
			break
		else:
			cur = line.strip().split('\t')
			if pre[0] == cur[0] and pre[3] != cur[3]:
				delta_minute = (int(cur[2])-int(pre[2]))/60
				if delta_minute >= 10 and delta_minute <= 90:
					delta.append(delta_minute)
			pre = cur
	file.close()
	fig, ax = plt.subplots()
	plt.hist(delta, bins = 80)
	plt.show()