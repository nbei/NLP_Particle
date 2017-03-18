# -*- coding:utf-8 –*


resfile = open(r'./crf++/4tag_new.rst', 'r')
outfile = open(r'./crf++/4tag_new.test.score.utf8', 'w')

line = resfile.readline()
while line:
    line = line.decode('utf-8')
    if len(line) == 1:
        outfile.write('\n')
        line = resfile.readline()
        continue
    line = line.strip('\n')
    if line[-1] == u'S':
        outfile.write(line[0].encode('utf-8')+'  ')
        line = resfile.readline()
        continue
    if line[-1] == u'B':
        outres = [line[0]]
        line = resfile.readline()
        line = line.decode('utf-8')
        line = line.strip('\n')
        while line[-1] == u'M':
            outres.append(line[0])
            line = resfile.readline()
            line = line.decode('utf-8')
            line = line.strip('\n')
        outres.append(line[0])
        for p in outres:
            outfile.write(p.encode('utf-8'))
        outfile.write('  ')
    line = resfile.readline()

outfile.close()
resfile.close()

