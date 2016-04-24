#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date   :
# @Author :
# @Usage  :

import random
import sys
reload(sys)
sys.setdefaultencoding('utf8')

m2_sample_dict = {}
def sample_m2():
	'''
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/m2_all.txt', 'r')
	m2 = []
	while 1:
		line = file.readline()
		if not line:
			break
		else:
			m2.append(line.strip())
	file.close()
	random.seed(628)
	sample_n = 10000
	m2_sample = random.sample(m2, sample_n)
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/m2_sample.txt', 'w')
	for i in range(sample_n):
		file.write(('%s\n') % (m2_sample[i]))
		m2_sample_dict[m2_sample[i]] = 1
	file.close()
	'''
	m2_all = {}
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/log_merge.txt', 'r')
	while 1:
		line = file.readline()
		if not line:
			break
		else:
			segs = line.strip().split('\t')
			if m2_all.has_key(segs[0]):
				m2_all[segs[0]] += 1
			else:
				m2_all[segs[0]] = 1
	file.close()
	m2_all_sorted = sorted(m2_all.items(), key=lambda d:d[1], reverse = True)
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/m2_sample.txt', 'w')
	sample_n = 1000
	for i in range(sample_n):
		file.write(('%s\n') % (m2_all_sorted[i][0]))
		m2_sample_dict[m2_all_sorted[i][0]] = 1
	file.close()


def sample_browse():
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/browse_pre.txt', 'r')
	file_out = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/browse_sample.txt', 'w')
	while 1:
		line = file.readline()
		if not line:
			break
		else:
			segs = line.strip().split('\t')
			if m2_sample_dict.has_key(segs[0]):
				file_out.write(('%s') % (line))
	file_out.close()
	file.close()

def sample_download():
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/download_pre.txt', 'r')
	file_out = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/download_sample.txt', 'w')
	while 1:
		line = file.readline()
		if not line:
			break
		else:
			segs = line.strip().split('\t')
			if m2_sample_dict.has_key(segs[0]):
				file_out.write(('%s') % (line))
	file_out.close()
	file.close()

def sample_merge():
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/log_merge.txt', 'r')
	file_out = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/log_merge_sample.txt', 'w')
	while 1:
		line = file.readline()
		if not line:
			break
		else:
			segs = line.strip().split('\t')
			if m2_sample_dict.has_key(segs[0]):
				file_out.write(('%s') % (line))
	file_out.close()
	file.close()

def sample_session():
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/session.txt')
	file_out = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/session_sample.txt', 'w')
	while 1:
		line = file.readline()
		if not line:
			break
		else:
			segs = line.strip().split('\t')
			if m2_sample_dict.has_key(segs[0]):
				file_out.write(('%s') % (line))
	file_out.close()
	file.close()

if __name__ == '__main__':
	sample_m2()
	sample_browse()
	sample_download()
	sample_merge()
	sample_session()
