# -*- coding:utf-8 –*
""" 此代码主要用来将test数据集做预处理,使其能够被crf++使用 """


def main():
    testfile = open(r'./icwb2-data/testing/pku_test.utf8', 'r')
    crftestfile = open(r'./crf++/testdata.utf8', 'w')

    line = testfile.readline()
    while line:
        line = line.strip()
        line = line.strip('\n')
        line = line.decode('utf-8')
        for p in line:
            crftestfile.write(p.encode('utf-8'))
            crftestfile.write('\n')
        crftestfile.write('\n')
        line = testfile.readline()

    testfile.close()
    crftestfile.close()

if __name__ == '__main__':
    main()
