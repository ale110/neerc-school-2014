#!/usr/bin/python
# encoding: utf-8
 
from math import sqrt, floor
 
infile = open("pobeda.in")
outfile = open("pobeda.out", 'w')
 
a1, a2, b1, b2 = map(int, infile.readline().strip().split())
squares = min([a1, a2]) + min([b1, b2])
side = floor(sqrt(squares))
 
outfile.write(str(side))
 
outfile.close()
