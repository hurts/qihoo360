#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date   : 
# @Author : 
# @Usage  : 

import matplotlib as mpl
import matplotlib.pyplot as plt
import sys
reload(sys)
sys.setdefaultencoding('utf8')
mpl.rcParams["font.family"] = "Times New Roman"

def get_m2():
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/m2_sample', 'r')
	m2 = []
	while 1:
		line = file.readline()
		if not line:
			break
		else:
			m2.append(line.strip())
	file.close()
	return m2

def get_browse():
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/browse_sample', 'r')
	browse = {}
	while 1:
		line = file.readline()
		if not line:
			break
		else:
			segs = line.strip().split('\t')
			if browse.has_key(segs[0]):
				browse[segs[0]].append(segs)
			else:
				browse[segs[0]] = []
				browse[segs[0]].append(segs)
	return browse
	file.close()

def get_download():
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/download_sample', 'r')
	download = {}
	while 1:
		line = file.readline()
		if not line:
			break
		else:
			segs = line.strip().split('\t')
			if download.has_key(segs[0]):
				download[segs[0]].append(segs)
			else:
				download[segs[0]] = []
				download[segs[0]].append(segs)
	return download
	file.close()

def plot_m2(m2, browse_m2, download_m2):
	index = range(250)
	browse_count = [0] * 250
	download_count = [0] * 250
	for bi in browse_m2:
		browse_count[int(bi[2])/86400] += 1
	for di in download_m2:
		download_count[int(di[2])/86400] += 1
	fig, ax = plt.subplots()
	plt.plot(index, browse_count, color = 'r', label = 'Browsing Behaviors')
	plt.plot(index, download_count, color = 'b', label = 'Downloading Behaviors')
	plt.legend(loc = 'best')
	plt.savefig('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/case_study/' + m2 + '.png')
	
if __name__ == '__main__':
	m2 = get_m2()
	browse = get_browse()
	download = get_download()
	for mi in m2:
		if browse.has_key(mi):
			if download.has_key(mi):
				plot_m2(mi, browse[mi], download[mi])
			else:
				plot_m2(mi, browse[mi], [])
		else:
			plot_m2(mi, [], download[mi])

	

	