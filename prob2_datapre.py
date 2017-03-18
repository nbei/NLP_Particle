# -*- coding:utf-8 –*
"""
    此代码主要用来将训练数据进行预处理,使其符合CRF++的模式,
    这里只用训练集的单词的特征,使用的是4Tag模型
"""

import numpy as np


def file_writer(outputfile, data):
    for i in np.arange(0, len(data), 2):
        outputfile.write(data[i].encode('utf-8')+'\t'+data[i+1].encode('utf-8')+'\n')
    outputfile.write('\n')


def tag4(line_split):
    result = []
    for p in line_split:
        if len(p) == 1:
            result.append(p)
            result.append(u'S')
        elif len(p) == 2:
            result = result + [p[0], u'B', p[1], u'E']
        elif len(p) > 2:
            result = result + [p[0], u'B']
            for temp in p[1:-1]:
                result.append(temp)
                result.append(u'M')
            result.append(p[-1])
            result.append(u'E')
    return result


def main():
    datafile = open(r'./icwb2-data/training/pku_training.utf8', 'r')
    outputfile = open(r'./crf++/train_file_6.utf8', 'w')
    line = datafile.readline()

    while line:
        line = line.strip()
        line = line.strip('\n')
        line = line.decode('utf-8', "ignore")
        line_split = line.split('  ')
        result = tag4(line_split)
        file_writer(outputfile, result)
        line = datafile.readline()

    datafile.close()
    outputfile.close()

if __name__ == '__main__':
    main()
