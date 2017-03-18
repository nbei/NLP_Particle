# -*- coding:utf-8 –*

import numpy as np

back_res = open(r'./res_score/score_backward.txt', 'r')
forward_res = open(r'./res_score/score_forward.txt', 'r')
crf_res = open(r'./crf++/score_crf.txt', 'r')
crf_4fre_res = open(r'./crf++/4tag_new.score_crf.txt', 'r')

back_recall = []
back_precise = []
back_length = []

forward_recall = []
forward_precise = []
forward_length = []

crf_recall = []
crf_precise = []
crf_length = []

crf_4fre_recall = []
crf_4fre_precise = []
crf_4fre_length = []

line = back_res.readline()
while line:
    line = line.strip('\n')
    if line[:6] == 'NTRUTH':
        line_split = line.split('\t')
        back_length.append(int(line_split[-1]))
        line = back_res.readline()
        line = back_res.readline()
        line_split = line.split('\t')
        back_recall.append(float(line_split[-1]))
        line = back_res.readline()
        line_split = line.split('\t')
        back_precise.append(float(line_split[-1]))
        line = back_res.readline()
    line = back_res.readline()

line = forward_res.readline()
while line:
    line = line.strip('\n')
    if line[:6] == 'NTRUTH':
        line_split = line.split('\t')
        forward_length.append(int(line_split[-1]))
        line = forward_res.readline()
        line = forward_res.readline()
        line_split = line.split('\t')
        forward_recall.append(float(line_split[-1]))
        line = forward_res.readline()
        line_split = line.split('\t')
        forward_precise.append(float(line_split[-1]))
        line = forward_res.readline()
    line = forward_res.readline()

line = crf_res.readline()
while line:
    line = line.strip('\n')
    if line[:6] == 'NTRUTH':
        line_split = line.split('\t')
        crf_length.append(int(line_split[-1]))
        line = crf_res.readline()
        line = crf_res.readline()
        line_split = line.split('\t')
        crf_recall.append(float(line_split[-1]))
        line = crf_res.readline()
        line_split = line.split('\t')
        crf_precise.append(float(line_split[-1]))
        line = crf_res.readline()
    line = crf_res.readline()

line = crf_4fre_res.readline()
while line:
    line = line.strip('\n')
    if line[:6] == 'NTRUTH':
        line_split = line.split('\t')
        crf_4fre_length.append(int(line_split[-1]))
        line = crf_4fre_res.readline()
        line = crf_4fre_res.readline()
        line_split = line.split('\t')
        crf_4fre_recall.append(float(line_split[-1]))
        line = crf_4fre_res.readline()
        line_split = line.split('\t')
        crf_precise.append(float(line_split[-1]))
        line = crf_4fre_res.readline()
    line = crf_4fre_res.readline()

back_recall = np.array(back_recall)
back_precise = np.array(back_precise)
back_length = np.array(back_length)

back_recall_mean = np.mean(back_recall)
back_precise_mean = np.mean(back_precise)

forward_recall = np.array(forward_recall)
forward_precise = np.array(forward_precise)
forward_length = np.array(forward_length)

forward_recall_mean = np.mean(forward_recall)
forward_precise_mean = np.mean(forward_precise)

bf_precise = back_precise >= forward_precise
bf_length = back_length < forward_length
bf_recall = back_recall >= forward_recall

bf_length = bf_length.astype(int)
bf_recall = bf_recall.astype(int)
bf_precise = bf_precise.astype(int)

bf_length_final = np.sum(bf_length)

crf_recall_mean = np.mean(np.array(crf_recall))
crf_precise_mean = np.mean(np.array(crf_precise))
cb_length = crf_length < back_length
cb_length_final = np.sum(cb_length.astype(int))

crf_4fre_recall_mean = np.mean(np.array(crf_recall))
crf_4fre_precise_mean = np.mean(np.array(crf_precise))
c4freb_length = crf_4fre_length < back_length
c4freb_length_final = np.sum(c4freb_length.astype(int))
crf_4_fre_length = crf_length > crf_4fre_length
crf_4_fre_length_final = np.sum(np.array(crf_4_fre_length).astype(int))

print '------------------------FINAL REPORT : ------------------------'
print 'backward_recall_mean : %f    forward_recall_mean : %f ' % (back_recall_mean, forward_recall_mean)
print 'backward_precise_mean : %f   forward_precise_mean : %f ' % (back_precise_mean, forward_precise_mean)
print 'backward_res_length < forward_res_length : %d' % (bf_length_final)
print 'crf_recall_mean : %f         crf_precise_mean : %f' % (crf_recall_mean, crf_precise_mean)
print 'crf_res_length < backward_res_length : %d' % (cb_length_final)
print 'crf_4fre_recall_mean : %f         crf_4fre_precise_mean : %f' % (crf_4fre_recall_mean, crf_4fre_precise_mean)
print 'crf_4fre_res_length < crf_res_length : %d' % (crf_4_fre_length_final)

back_res.close()
forward_res.close()
crf_4fre_res.close()
crf_res.close()
