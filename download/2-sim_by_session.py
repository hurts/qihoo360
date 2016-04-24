#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date   :
# @Author :
# @Usage  :

from __future__ import division
import gensim
import sys
reload(sys)
sys.setdefaultencoding('utf8')

sentences = []
cat_name = []
def get_data():
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/download_list/cat2_word2vec.txt', 'r')
	lines = file.readlines()
	file.close()
	for line in lines:
		cat_list = line.strip().split('\t')
		sentences.append(cat_list)
		for ci in cat_list:
			if ci not in cat_name:
				cat_name.append(ci)

def word_vec():
	model = gensim.models.Word2Vec(sentences, window = 1, min_count = 1)
	file = open('/Users/CJW/Desktop/thu/科研/项目/360/UCD/data/download_list/cat2_sim.txt', 'w')
	for ci in cat_name:
		result = []
		sim = model.most_similar(positive=[ci])
		for si in sim[:3]:
			result.append(si[0] + ':' + str(round(si[1], 2)))
		file.write(('%s\t%s\n') % (ci, ','.join(result)))
	file.close()
	
if __name__ == '__main__':
	get_data()
	word_vec()
