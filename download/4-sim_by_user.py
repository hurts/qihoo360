#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date   :
# @Author :
# @Usage  :

from __future__ import division
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys
reload(sys)
sys.setdefaultencoding('utf8')

cat_name = {}
cat_num = {}
app_info = {}

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

user = {}
def desc_by_user():
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/download_list/by_session_cat2.txt', 'r')
	lines = file.readlines()
	file.close()
	for line in lines:
		segs = line.strip().split(',')
		m2 = segs[1]
		if not user.has_key(m2):
			user[m2] = [0, 0]
		downloads = segs[4].split('\t')
		sign = 0
		for ci in cat_num.keys():
			downloads_ci = downloads.count(ci)
			if downloads_ci > 1:
				sign = 1
				break
		if sign == 0:
			user[m2][1] += 1
		else:
			user[m2][0] += 1
	proportion = []
	for ui in user.keys():
		proportion.append(user[ui][0]/sum(user[ui]))
	plt.hist(proportion, 20)
	plt.show()

if __name__ == '__main__':
	get_data()
	desc_by_user()
