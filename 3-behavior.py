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

installed = {}
def get_data():
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/installed.txt', 'r')
	while 1:
		line = file.readline()
		if not line:
			break
		else:
			segs = line.strip().split('\t')
			installed[segs[0]] = segs[1].split(',')
	file.close()

def behavior():
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/behavior.txt', 'w')
	file.close()
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/log_merge_filter.txt', 'r')
	line = file.readline()
	segs = line.strip().split('\t')
	m2_old = segs[0]
	data = [segs[1:]]
	term_old = '\t'.join(segs[3:])
	while 1:
		line = file.readline()
		if not line:
			break
		else:
			segs = line.strip().split('\t')
			if segs[0] == m2_old:
				if term_old != '\t'.join(segs[3:]):
					data.append(segs[1:])
					term_old = '\t'.join(segs[3:])
			else:
				extract(m2_old, data)
				m2_old = segs[0]
				data = [segs[1:]]
				term_old = '\t'.join(segs[3:])
	extract(m2_old, data)
	file.close()

def extract(m2, data):
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/behavior.txt', 'a')
	data_n = len(data)
	result = []
	for i in range(data_n):
		if len(data[i]) == 8:
			if data[i][6] == '1':
				result.append(data[i][1] + '-d-' + data[i][7])
			elif data[i][6] in ['2', '3', '4']:
				result.append(data[i][1] + '-u-' + data[i][7])
		elif len(data[i]) == 6:
			if data[i][3].find('getAppInfoByIds'):
				result.append(data[i][1] + '-b-' + data[i][5])
	if len(result) > 0:
		file.write(('%s\t%s\n') % (m2, ','.join(result)))
	file.close()
	'''
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/behavior.txt', 'a')
	data_n = len(data)
	for i in range(data_n):
		if len(data[i]) == 8:
			if app.has_key(data[i][7]):
				if data[i][4].find('updapp') >= 0:
					if data[i][6] == '4':
						file.write(('%s\t%s\t%s\t1\n') % (m2, data[i][0], data[i][7]))
					elif data[i][6] == '2' or '3':
						file.write(('%s\t%s\t%s\t2\n') % (m2, data[i][0], data[i][7]))
				elif data[i][6] == '1':
					if i >= 1:
						if len(data[i-1]) == 6 and data[i-1][5] == data[i][7] and data[i-1][3].find('getAppInfoByIds') >= 0 and int(data[i][1]) <= int(data[i-1][1]) + 60:
							file.write(('%s\t%s\t%s\t4\n') % (m2, data[i][0], data[i][7]))
						else:
							file.write(('%s\t%s\t%s\t3\n') % (m2, data[i][0], data[i][7]))
					else:
						file.write(('%s\t%s\t%s\t3\n') % (m2, data[i][0], data[i][7]))
		elif len(data[i]) == 6:
			if app.has_key(data[i][5]):
				if data[i][3].find('getAppInfoByIds'):
					if i < data_n - 1:
						if len(data[i+1]) == 6:
							file.write(('%s\t%s\t%s\t5\n') % (m2, data[i][0], data[i][5]))
					else:
						file.write(('%s\t%s\t%s\t5\n') % (m2, data[i][0], data[i][5]))
	file.close()
	'''

count = {}
type_dict = {'1': '自动更新', '2': '手动更新', '3': '直接下载', '4': '查看详情后下载', '5': '查看详情后未下载'}
def desc():
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/behavior.txt', 'r')
	while 1:
		line = file.readline()
		if not line:
			break
		else:
			segs = line.strip().split('\t')
			if count.has_key(segs[0]):
				count[segs[0]] += 1
			else:
				count[segs[0]] = 1
	file.close()
	data = {}
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/behavior.txt', 'r')
	while 1:
		line = file.readline()
		if not line:
			break
		else:
			segs = line.strip().split('\t')
			if count[segs[0]] >= 200:
				#if segs[3] == '5':
				#	continue
				if data.has_key(segs[0]):
					data[segs[0]].append(type_dict[segs[3]] + ':' + app[segs[2]])
				else:
					data[segs[0]] = [type_dict[segs[3]] + ':' + app[segs[2]]]
	file.close()
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/behavior_texts.txt', 'w')
	for di in data.keys():
		file.write(('%s\n') % (','.join(data[di])))
	file.close()

if __name__ == '__main__':
	#get_data()
	behavior()
	#desc()
	

	

	