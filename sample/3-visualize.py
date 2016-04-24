#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date   : 
# @Author : 
# @Usage  : 

from __future__ import division
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding('utf8')

m2 = {}
cat = {}
app = {}
def get_data():
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/m2_sample.txt', 'r')
	lines = file.readlines()
	file.close()
	for line in lines:
		m2[line.strip()] = len(m2.keys())
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/open_category_online.txt', 'r')
	lines = file.readlines()
	file.close()
	for line in lines:
		cat_id, cat_name, cat_num = line.strip().split('\t')
		cat[cat_id] = cat_name
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/app_info.txt', 'r')
	lines = file.readlines()
	file.close()
	for line in lines:
		segs = line.strip().split('\t')
		if cat.has_key(segs[1]) and cat.has_key(segs[2]):
			app[segs[0]] = cat[segs[2]] + ':' + segs[3]


nt_type = {'0': '其它', '1': 'wifi', '2': '2G', '3': '3G', '4': '其它'}										
at_type = {'0': '其它', '1': '净下载', '2': '更新下载', '3': '省流量更新', '4': '自动更新'}
def sample_study():
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/log_merge_sample.txt', 'r')
	lines = file.readlines()
	file.close()
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/log_merge_sample_visual.txt', 'w')
	for line in lines:
		segs = line.strip().split('\t')
		if len(segs) == 7:
			if app.has_key(segs[6]):
				segs[6] = app[segs[6]]
			file.write(('%s\t用户%d\t浏览: %s\t%s\t%s\t%s\n') % (segs[1], m2[segs[0]], segs[6], segs[3], segs[4], segs[5]))
		else:
			if app.has_key(segs[8]):
				segs[8] = app[segs[8]]
			file.write(('%s\t用户%d\t%s: %s\t%s@%s\t%s\t%s\n') % (segs[1], m2[segs[0]], at_type[segs[7]], segs[8], segs[3], nt_type[segs[6]], segs[4], segs[5]))
	file.close()

if __name__ == '__main__':
	get_data()
	sample_study()
	

	

	