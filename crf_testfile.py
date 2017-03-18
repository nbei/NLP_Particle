# -*- coding:utf-8 –*
"""
如果使用两个特征的话, CRF++需要特殊形式的test文件,
所以这个代码就是用来生成对应形式的testfile的
"""

import json

datafile = open(r'./crf++/testdata.utf8', 'r')
outputfile = open(r'./crf++/testdata_fetrue.utf8', 'w')
with open(r'./train_words.json', 'r') as jsonfile:
    worddic = json.load(jsonfile)

line = datafile.readline()
while line:
    line = line.decode('utf-8')
    if len(line) == 1:
        outputfile.write('\n')
        line = datafile.readline()
        continue
    outputfile.write(line[0].encode('utf-8')+'\t'+str(worddic.get(line[0], 0))+'\n')
    line = datafile.readline()

datafile.close()
outputfile.close()
