#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date   : 
# @Author : 
# @Usage  : 

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys
reload(sys)
sys.setdefaultencoding('utf8')
mpl.rcParams["font.family"] = "Times New Roman"

session = []
def get_session():
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/session')
	lines = file.readlines()
	for line in lines:
		session.append(line.strip().split('\t'))
	file.close()
	
duration = []
last_session_begin = []
last_session_end = []

def get_seconds():
	for si in session:
		duration.append(int(si[6]))
		if si[7] != '0':
			last_session_begin.append(int(si[7]))
			last_session_end.append(int(si[8]))
	print len(duration), len(last_session_begin), len(last_session_end)

def plot_distribution():
	fig, ax = plt.subplots()
	ax.set_xscale('log')
	ax.set_yscale('log')
	n_bins = 10000
	plt.hist(duration, n_bins, histtype = 'step', label = 'duration')
	#plt.hist(last_session_begin, n_bins, histtype = 'step', label = 'last_session_begin')
	#plt.hist(last_session_end, n_bins, histtype = 'step', label = 'last_session_end')
	plt.legend(loc = 'best')
	plt.savefig('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/distribution.png')

if __name__ == '__main__':
	get_session()
	get_seconds()
	plot_distribution()
	