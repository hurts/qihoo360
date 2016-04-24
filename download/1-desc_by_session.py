#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date   :
# @Author :
# @Usage  :

from __future__ import division
import sys
reload(sys)
sys.setdefaultencoding('utf8')

cat_name = {}
cat_num = {}
app_info = {}
list_type = ['cat1', 'cat2', 'name']

def get_data():
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/open_category_online.txt', 'r')
	lines = file.readlines()
	file.close()
	for line in lines:
		segs = line.strip().split('\t')
		cat_name[segs[0]] = segs[1]
		cat_num[segs[1]] = int(segs[2])
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/app_info.txt', 'r')
	lines = file.readlines()
	file.close()
	for line in lines:
		segs = line.strip().split('\t')
		if len(segs) == 5:
			if cat_name.has_key(segs[1]) and cat_name.has_key(segs[2]):
				app_info[segs[0]] = segs[1:]

def download_by_session():
	for i in range(3):
		file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/download_list/by_session_' + list_type[i] + '.txt', 'w')
		file.close()
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/session_list.txt', 'r')
	while 1:
		line = file.readline()
		if not line:
			break
		else:
			segs = line.strip().split('\t')
			behaviors = segs[4].split(',')
			downloads = [[], [], []]
			for bi in behaviors:
				bi_segs = bi.split(':')
				if bi_segs[1] == 'd':
					if app_info.has_key(bi_segs[2]) and app_info[bi_segs[2]][2] not in downloads[2]:
						for i in range(2):
							downloads[i].append(cat_name[app_info[bi_segs[2]][i]])
						downloads[2].append(app_info[bi_segs[2]][2])
			if len(downloads[0]) > 0:
				for i in range(3):
					file_out = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/download_list/by_session_' + list_type[i] + '.txt', 'a')
					file_out.write(('%s,%s\n') % (','.join(segs[:4]), '\t'.join(downloads[i])))
					file_out.close()
	file.close()

def desc_by_session():
	num = {}
	for ci in cat_num.keys():
		num[ci] = [0, 0]
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/download_list/by_session_cat2.txt', 'r')
	lines = file.readlines()
	file.close()
	for line in lines:
		segs = line.strip().split(',')
		downloads = segs[4].split('\t')
		for ci in cat_num.keys():
			downloads_ci = downloads.count(ci)
			if downloads_ci == 1:
				num[ci][0] += 1
			elif downloads_ci > 1:
				num[ci][1] += 1
	for ni in num.keys():
		if num[ni][0] > 0:
			print ni, num[ni][0], num[ni][1], round(num[ni][1]/(num[ni][0] ** 2)*10000, 4)

if __name__ == '__main__':
	get_data()
	#download_by_session()
	desc_by_session()
