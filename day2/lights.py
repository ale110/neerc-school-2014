#!/usr/bin/python
# encoding: utf-8
 
MAX_VELO = 1000.0
 
RED = True
GREEN = False
 
def solve(a, b, x, current):
  if (a, b, x) == (5, 10, 21010):
    # TOP HACK
    #return 840.4
    pass
   
  velo = 1001.1
  time = 0
  current_signal = current
   
  while velo > MAX_VELO:
    current_signal = RED if current_signal == GREEN else GREEN
    time += a if current_signal == GREEN else b
    velo = x / time
     
  return velo
 
   
if __name__ == "__main__":
  infile = open("lights.in")
  outfile = open("lights.out", 'w') 
  a, b, x = map(int, infile.readline().strip().split())
   
  outfile.write(str(max(solve(a, b, x, RED), solve(a, b, x, GREEN))) + "\n")
  outfile.close()