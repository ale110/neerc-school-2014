#!/usr/bin/python
# encoding: utf-8
 
def parseSchool(s):
    return "".join(map(lambda x: x if x.isnumeric() else "", s))
 
infile = open("schools.in")
outfile = open("schools.out", 'w')
 
schools = {}
 
for line in infile.readlines():
    id_ = parseSchool(line.strip())
    if len(id_) == 0:
        continue
    if id_ in schools:
        schools[id_] += 1
    else:
        schools[id_] = 1
 
tiny = []
 
for i in schools:
    if schools[i] <= 5:
        tiny.append(i)
 
outfile.write(str(len(tiny)) + "\n")
outfile.write("\n".join(tiny))
 
outfile.close()