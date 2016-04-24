#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date   : 
# @Author : 
# @Usage  : 

from __future__ import division
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys
reload(sys)
sys.setdefaultencoding('utf8')
mpl.rcParams["font.family"] = "Times New Roman"

m2 = []
def get_m2():
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/m2_sample.txt', 'r')
	while 1:
		line = file.readline()
		if not line:
			break
		else:
			m2.append(line.strip())
	file.close()

browse = {}
def get_browse():
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/browse_sample.txt', 'r')
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
	file.close()

download = {}
def get_download():
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/download_sample.txt', 'r')
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
	file.close()

session = {}
def get_session():
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/session_sample.txt', 'r')
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
	count = 0
	for mi in m2:
		if len(session[mi]) >= 10:
			count += 1
	print count

def plot_behavior():
	for mi in m2:
		if browse.has_key(mi):
			if download.has_key(mi):
				plot_m2(mi, browse[mi], download[mi])
			else:
				plot_m2(mi, browse[mi], [])
		else:
			plot_m2(mi, [], download[mi])
	
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

def plot_distribution():
	count = 0
	for i in range(10):
		for j in range(10):
			mi = m2[i + j * 10]
			if len(session[mi]) >= 10:
				count+= 1
			else:
				continue
			fig = plt.subplot(6, 5, count)
			duration = []
			last_session_begin = []
			last_session_end = []
			for si in session[mi]:
				duration.append(int(si[6])/60)
				if si[7] != '0':
					last_session_begin.append(int(si[7])/86400)
					last_session_end.append(int(si[8])/86400)
			'''
			plt.xlim(xmin = 0, xmax = 60)
			plt.ylim(ymin = 0, ymax = 0.5)
			if count >= 2:
				fig.axes.get_xaxis().set_visible(False)
				fig.axes.get_yaxis().set_visible(False)
			num_bins = 60
			n, bins, patches = plt.hist(duration, num_bins, normed = 1)
			plt.xlim(xmin = 0, xmax = 60)
			plt.ylim(ymin = 0, ymax = 0.5)
			if count >= 2:
				fig.axes.get_xaxis().set_visible(False)
				fig.axes.get_yaxis().set_visible(False)
			num_bins = 30
			n, bins, patches = plt.hist(last_session_end, num_bins, normed = 1)
			'''
			plt.xlim(xmin = 0, xmax = 60)
			plt.ylim(ymin = 0, ymax = 0.5)
			if count >= 2:
				fig.axes.get_xaxis().set_visible(False)
				fig.axes.get_yaxis().set_visible(False)
			num_bins = 30
			n, bins, patches = plt.hist(last_session_begin, num_bins, normed = 1)
	plt.show()

if __name__ == '__main__':
	get_m2()
	#get_browse()
	#get_download()
	get_session()
	#plot_behavior()
	plot_distribution()
	

	

	