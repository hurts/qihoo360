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

cat = {}
app = {}
def get_data():
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
			app[segs[0]] = segs[3]

def log_filter():
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/log_merge.txt', 'r')
	file_out = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/log_merge_filter.txt', 'w')
	while 1:
		line = file.readline()
		if not line:
			break
		else:
			segs = line.strip().split('\t')
			if app.has_key(segs[len(segs)-1]):
				file_out.write(('%s') % (line))
	file_out.close()
	file.close()


if __name__ == '__main__':
	get_data()
	log_filter()
