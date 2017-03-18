# -*- coding:utf-8 –*


import numpy as np

test_file = open(r'./icwb2-data/testing/pku_test.utf8', 'r')
word_dict = np.load('train_word_dic.npy')
fout_forward = open('prob1_test_forward.txt', 'w')
fout_backward = open('prob1_test_backward.txt', 'w')
fout_bidirection = open('prob1_test_bidirection.txt', 'w')


def is_punc(input):
    punc_list = u'，；、：“”‘’《》（）。？！……'
    if input in punc_list:
        return True
    else:
        return False


def forward_match(origin, fout):
    strlen = len(origin)
    str_start = 0
    write_cache = []
    while str_start < strlen:
        if is_punc(origin[str_start]):
            fout.write(origin[str_start].encode('utf-8'))
            fout.write('  ')
            write_cache.append(origin[str_start].encode('utf-8'))
            str_start += 1
            continue
        str_end = strlen
        while str_end > str_start:
            if is_punc(origin[str_end-1]):
                str_end -= 1
            if str_end-str_start > 9:
                if origin[str_start:str_end] in word_dict[-1]:
                    fout.write(origin[str_start:str_end].encode('utf-8'))
                    fout.write('  ')
                    write_cache.append(origin[str_start:str_end].encode('utf-8'))
                    str_start = str_end
                    continue
                else:
                    str_end -= 1
                    continue
            if str_end-str_start <= 9:
                if origin[str_start:str_end] in word_dict[str_end-str_start-1]:
                    fout.write(origin[str_start:str_end].encode('utf-8'))
                    fout.write('  ')
                    write_cache.append(origin[str_start:str_end].encode('utf-8'))
                    str_start = str_end
                    break
                else:
                    if str_end-str_start == 1:
                        fout.write(origin[str_start:str_end].encode('utf-8'))
                        fout.write('  ')
                        write_cache.append(origin[str_start:str_end].encode('utf-8'))
                        str_start = str_end
                        break
                    else:
                        str_end -= 1
    fout.write('\n')
    return write_cache


def backward_match(origin):
    strlen = len(origin)
    str_end = strlen
    write_cache = []
    while str_end > 0:
        if is_punc(origin[str_end-1]):
            write_cache.append(origin[str_end-1].encode('utf-8'))
            str_end -= 1
            continue
        str_start = 0
        while str_start < str_end:
            if is_punc(origin[str_start]):
                str_start += 1
            if str_end - str_start > 9:
                if origin[str_start:str_end] in word_dict[-1]:
                    write_cache.append(origin[str_start:str_end].encode('utf-8'))
                    str_end = str_start
                    break
                else:
                    str_start += 1
                    continue
            if str_end - str_start <= 9:
                if origin[str_start:str_end] in word_dict[str_end - str_start - 1]:
                    write_cache.append(origin[str_start:str_end].encode('utf-8'))
                    str_end = str_start
                    break
                else:
                    if str_end - str_start == 1:
                        write_cache.append(origin[str_start:str_end].encode('utf-8'))
                        str_end = str_start
                        break
                    else:
                        str_start += 1
    return write_cache


def file_write(fout, cache):
    for i in cache:
        fout.write(i)
        fout.write('  ')
    fout.write('\n')


def main():
    line = test_file.readline()
    line_counter = 0
    while line:
        line = line.strip()
        line = line.strip('\n')
        line = line.decode('utf-8', "ignore")
        forward_res = forward_match(line, fout_forward)
        backward_res = backward_match(line)
        backward_res.reverse()

        write_bidirec = forward_res if len(forward_res) < len(backward_res) else backward_res

        file_write(fout_backward, backward_res)
        file_write(fout_bidirection, write_bidirec)

        line_counter += 1
        if line_counter == 94:
            pass
        print line_counter
        line = test_file.readline()

    fout_backward.close()
    fout_bidirection.close()
    fout_forward.close()
    test_file.close()


if __name__ == '__main__':
    main()

