# -*- coding:utf-8 –*

"""
在使用CRF训练的时候,需要用到不同的特征,这里提供一个字典
帮助得到CRF中需要使用的字的频数特征
"""
import json

datafile = open(r'./icwb2-data/training/pku_training.utf8', 'r')
words_dic = {}
line = datafile.readline()
while line:
    line = line.strip()
    line = line.strip('\n')
    line = line.decode('utf-8')
    for p in line:
        if p == ' ':
            continue
        if words_dic.get(p, -1) == -1:
            words_dic[p] = 1
        else:
            words_dic[p] += 1
    line = datafile.readline()
with open('train_words.json', 'w') as outfile:
    json.dump(words_dic, outfile)
    outfile.write('\n')
datafile.close()