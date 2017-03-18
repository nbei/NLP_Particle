#-*- coding:utf-8 –*
""" 好像他的score文件的用法需要一个training的words的字典 """

import numpy as np

word_dict = np.load('train_word_dic.npy')
outfile = open('./trainwords.utf-8', 'w')

for p in word_dict:
    for t in p:
        outfile.write(t.encode('utf-8'))
        outfile.write('\n')

outfile.close()
