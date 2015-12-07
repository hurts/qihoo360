#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date   : 
# @Author : 
# @Usage  : 

import random
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def sample_m2():
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/m2_all', 'r')
	m2 = []
	while 1:
		line = file.readline()
		if not line:
			break
		else:
			m2.append(line.strip())
	file.close()
	random.seed(628)
	m2_sample = random.sample(m2, 100)
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/m2_sample', 'w')
	for i in range(100):
		file.write(('%s\n') % (m2_sample[i]))
	file.close()
	return m2_sample

def sample_browse(m2):
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/browse_pre', 'r')
	file_out = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/browse_sample', 'w')
	while 1:
		line = file.readline()
		if not line:
			break
		else:
			segs = line.strip().split('\t')
			if segs[0] in m2:
				file_out.write(('%s') % (line))
	file_out.close()
	file.close()

def sample_download(m2):
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/download_pre', 'r')
	file_out = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/download_sample', 'w')
	while 1:
		line = file.readline()
		if not line:
			break
		else:
			segs = line.strip().split('\t')
			if segs[0] in m2:
				file_out.write(('%s') % (line))
	file_out.close()
	file.close()

def sample_merge(m2):
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/log_merge', 'r')
	file_out = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/log_merge_sample', 'w')
	while 1:
		line = file.readline()
		if not line:
			break
		else:
			segs = line.strip().split('\t')
			if segs[0] in m2:
				file_out.write(('%s') % (line))
	file_out.close()
	file.close()

if __name__ == '__main__':
	m2 = sample_m2()
	sample_browse(m2)
	sample_download(m2)
	sample_merge(m2)
