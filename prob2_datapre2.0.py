# -*- coding:utf-8 –*
"""
此代码主要用来将训练数据进行预处理,使其符合CRF++的模式
这里使用的是4Tag模型,再加上对应的字在训练集中出现的次数
的特征,训练集中某个字出现的次数,可以通过加载train_woards.npy
来得到
"""

import numpy as np
import json


def file_writer(outputfile, data):
    for i in np.arange(0, len(data), 3):
        outputfile.write(data[i].encode('utf-8')+'\t')
        outputfile.write(data[i+1].encode('utf-8'))
        outputfile.write('\t')
        outputfile.write(data[i+2].encode('utf-8')+'\n')
    outputfile.write('\n')


def tag4(line_split, words_dic):
    result = []
    for p in line_split:
        if len(p) == 1:
            result.append(p)
            result.append(str(words_dic.get(p, 0)))
            result.append(u'S')
        elif len(p) == 2:
            result = result + [p[0], str(words_dic.get(p[0], 0)), u'B', p[1],
                               str(words_dic.get(p[1], 0)), u'E']
        elif len(p) > 2:
            result = result + [p[0], str(words_dic.get(p[0], 0)), u'B']
            for temp in p[1:-1]:
                result.append(temp)
                result.append(str(words_dic.get(temp, 0)))
                result.append(u'M')
            result.append(p[-1])
            result.append(str(words_dic.get(p[-1], 0)))
            result.append(u'E')
    return result


def main():
    datafile = open(r'./icwb2-data/training/pku_training.utf8', 'r')
    outputfile = open(r'./crf++/train_file_fre4.utf8', 'w')
    line = datafile.readline()
    with open('train_words.json', 'r') as words_file:
        words_dic = json.load(words_file)
    while line:
        line = line.strip()
        line = line.strip('\n')
        line = line.decode('utf-8', "ignore")
        line_split = line.split('  ')
        result = tag4(line_split, words_dic)
        file_writer(outputfile, result)
        line = datafile.readline()

    datafile.close()
    outputfile.close()

if __name__ == '__main__':
    main()
