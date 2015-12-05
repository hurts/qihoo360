#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date   : 
# @Author : 
# @Usage  : 

import sys
reload(sys)
sys.setdefaultencoding('utf8')

if __name__ == '__main__':
	file_d = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/download_pre', 'r')
	file_b = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/browse_pre', 'r')
	file_out = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/log_merge', 'w')
	sign_d = 0
	sign_b = 0
	while 1:
		if sign_d == 0:
			line_d = file_d.readline()
			segs_d = line_d.strip().split('\t')
		if sign_b == 0:
			line_b = file_b.readline()
			segs_b = line_b.strip().split('\t')
		if not line_d:
			while 1:
				file_out.write(('%s') % (line_b))
				line_b = file_b.readline()
				if not line_b:
					break
			break
		if not line_b:
			while 1:
				file_out.write(('%s') % (line_d))
				line_d = file_d.readline()
				if not line_d:
					break
			break
		if segs_d[0] == segs_b[0]:
			if int(segs_d[2]) < int(segs_b[2]):
				file_out.write(('%s') % (line_d))
				sign_d = 0
				sign_b = 1
			else:
				file_out.write(('%s') % (line_b))
				sign_d = 1
				sign_b = 0
		else:
			if sign_d == 0:
				file_out.write(('%s') % (line_b))
				sign_d = 1
				sign_b = 0
			else:
				file_out.write(('%s') % (line_d))
				sign_d = 0
				sign_b = 1
	file_out.close()
	file_d.close()
	file_b.close()