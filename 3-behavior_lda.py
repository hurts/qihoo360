#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date   : 
# @Author : 
# @Usage  : 

from __future__ import division
from gensim import corpora, models
import sys
reload(sys)
sys.setdefaultencoding('utf8')

texts = []
def get_data():
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/behavior_texts.txt', 'r')
	lines = file.readlines()
	file.close()
	for line in lines:
		segs = line.strip().split(',')
		texts.append(segs)

def topic_model():
	topic_n = 200
	dictionary = corpora.Dictionary(texts)
	corpus = [dictionary.doc2bow(text) for text in texts]
	lda = models.LdaModel(corpus, num_topics = topic_n)
	for i in range(topic_n):
		terms = lda.get_topic_terms(i, topn = 20)
		terms = [str(ti[1]) + '*' + dictionary[ti[0]] for ti in terms]
		print 'topic' + str(i) + ':', ' + '.join(terms)

if __name__ == '__main__':
	get_data()
	topic_model()