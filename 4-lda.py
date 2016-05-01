#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date   : 
# @Author : 
# @Usage  : 

from __future__ import division
from gensim import corpora, models
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

texts = []
app = {}
def get_data():
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/app_info.txt', 'r')
	lines = file.readlines()
	file.close()
	for line in lines:
		segs = line.strip().split('\t')
		app[segs[0]] = segs[3]
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/behavior_texts.txt', 'r')
	lines = file.readlines()
	file.close()
	for line in lines:
		segs = line.strip().split('\t')
		behaviors = segs[1].replace('.', '').split(' ')
		if len(behaviors) >= 200:
			texts.append(behaviors)

def topic_model():
	topic_n = 100
	dictionary = corpora.Dictionary(texts)
	corpus = [dictionary.doc2bow(text) for text in texts]
	lda = models.LdaModel(corpus, num_topics = topic_n)
	for i in range(topic_n):
		terms = lda.get_topic_terms(i, topn = 20)
		tmp = []
		for ti in terms:
			#segs = dictionary[ti[0]].split('-')
			#tmp.append(str(ti[1]) + '*' + segs[0] + '-' + app[segs[1]])
			tmp.append(str(ti[1]) + '*' + app[dictionary[ti[0]]])
		print 'topic' + str(i) + ':', ' + '.join(tmp)

if __name__ == '__main__':
	get_data()
	topic_model()