#!/usr/bin/python
# encoding: utf-8

# O(N^2) !!!
# ~~ Not more than N == ~3000 ~~
# LOLWAT?

# revisions:
# 0. INITIAL COMMIT
# 1. performance: now we assume that at least one box fits
# 2. do not divide :3
#    1. remove perf checker

from math import floor
#import time

def find(max_size, box_width, box_height, box_depth):
  maximal = (0, 0, 0)
  # volume, width, height
  
  for i in range(box_width, max_size - box_height - box_depth, box_width):
    for j in range(box_height, max_size - i + 1, box_height):
      volume = i * j * (max_size - i - j)
      # We don't need to floor() everything because
      # i % a == j % b == k % c == 0
      if maximal[0] < volume:
        maximal = (volume, i, j)

  return maximal

if __name__ == "__main__":
  infile = open("sweets.in")
  outfile = open("sweets.out", 'w')

  n, a, b, c = map(int, infile.readline().strip().split())
  
  #time.perf_counter()
  volume, width, height = find(n, a, b, c)
  depth = n - width - height
  #print((width, height, depth), volume, time.perf_counter())
  
  outfile.write("%i %i %i" % (width, height, depth))
  outfile.close()
