#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date   : 
# @Author : 
# @Usage  : 

from __future__ import division
import numpy as np
import math
import sys
reload(sys)
sys.setdefaultencoding('utf8')

m2 = []
def get_m2():
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/m2_sample', 'r')
	while 1:
		line = file.readline()
		if not line:
			break
		else:
			m2.append(line.strip())
	file.close()

session = {}
def get_session():
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/session_sample', 'r')
	while 1:
		line = file.readline()
		if not line:
			break
		else:
			segs = line.strip().split('\t')
			if session.has_key(segs[0]):
				session[segs[0]].append(segs)
			else:
				session[segs[0]] = []
				session[segs[0]].append(segs)
	file.close()

def cal_clump():
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/session_sample_clump', 'w')
	for mi in m2:
		x = []
		for ri in session[mi]:
			x.append(int(ri[3]))
			file.write(('%s\t%f\t%f\t%f\t%f\n') % ('\t'.join(ri), second_moment(x), entropy(x), log_utility(x), largest_components(x)))
	file.close()

def second_moment(x):
	n = len(x) + 1
	if n == 2:
		return 1
	else:
		min_value = n * ((max(x)/n) ** 2)
		max_value = max(x) ** 2
		cur_value = 0
		x = [0] + x 
		for i in range(len(x)-1):
			cur_value += (x[i+1] - x[i]) ** 2
		return (cur_value - min_value)/(max_value - min_value)

def entropy(x):
	n = len(x) + 1
	if n == 2:
		return 1
	else:
		min_value = n * max(x)/n * math.log(max(x)/n)
		max_value = max(x) * math.log(max(x))
		cur_value = 0
		x = [0] + x
		for i in range(len(x)-1):
			cur_value += (x[i+1] - x[i]) * math.log(x[i+1] - x[i])
		return (cur_value - min_value)/(max_value - min_value)

def log_utility(x):
	n = len(x) + 1
	if n == 2:
		return 1
	else:
		min_value = - n * math.log(max(x)/n)
		max_value = - math.log(max(x))
		cur_value = 0
		x = [0] + x
		for i in range(len(x)-1):
			cur_value += - math.log(x[i+1] - x[i])
		return (cur_value - min_value)/(max_value - min_value)

def largest_components(x):
	n = len(x) + 1
	if n <= 3:
		return 1
	else:
		min_value = max(x) / n * 3
		max_value = max(x)
		cur_value = 0
		x = [0] + x
		y = []
		for i in range(len(x)-1):
			y.append(x[i+1] - x[i])
		z = sorted(y, reverse = True)
		cur_value = sum(z[:3])
		return (cur_value - min_value)/(max_value - min_value)

if __name__ == '__main__':
	get_m2()
	get_session()
	cal_clump()
	