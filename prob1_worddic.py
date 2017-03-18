#-*- coding:utf-8 –*
""" 此代码用来得到training里面的字典,然后存入train_word_dic.npy文件之中 """

import re
import sys
import numpy as np


train_file = open(r"/Users/xurui/THU/wu48/NLP&TM/HW1code/icwb2-data/training/pku_training.utf8", 'r')
word_dic = [set([]) for i in range(10)]

line = train_file.readline()
line_counter = 0

while line:
    line = line.strip()
    line = line.strip('\n')
    line = line.decode('utf-8', "ignore")
    line_split = line.split('  ')
    for p in line_split:
        if p:
            if len(p) > 9:
                word_dic[-1].add(p)
                continue
            else:
                word_dic[len(p)-1].add(p)
    line_counter += 1
    if line_counter % 100 == 0:
        print '%d lines have been read' % line_counter
    line = train_file.readline()

np.save('train_word_dic.npy', word_dic)
train_file.close()
