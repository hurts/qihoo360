#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date   : 
# @Author : 
# @Usage  : 

from __future__ import division
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

data = {}
voca = {}
def tojson():
	data['docs'] = []
	data['vocabulary'] = []
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/behavior_texts.txt', 'r')
	lines = file.readlines()
	file.close()
	count = 1
	for line in lines:
		if count > 10000:
			break
		count += 1
		m2, doc = line.strip().split('\t')
		behaviors = doc.replace('.', '').split(' ')
		if len(behaviors) >= 100:
			data['docs'].append(generate_doc(doc))
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/behavior_texts.json', 'w')
	file.write(('%s\n') % (json.dumps(data, indent = 4)))
	file.close()
	print len(data['docs'])

def generate_doc(doc):
	sens = doc.split('. ')
	doc = {}
	doc['sentences'] = []
	for i in range(len(sens)):
		doc['sentences'].append({})
		doc['sentences'][i]["words"] = []
		words = sens[i].split(' ')
		for word in words:
			if voca.has_key(word):
				doc['sentences'][i]["words"].append(voca[word])
			else:
				voca[word] = len(voca.keys())
				data['vocabulary'].append(word)
				doc['sentences'][i]["words"].append(voca[word])
	return doc

if __name__ == '__main__':
	tojson()