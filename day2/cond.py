#!/usr/bin/python
# encoding: utf-8

def minForClass(class_, conds):
  return min(list(filter(lambda x: x[0] >= class_, conds)), key=lambda x: x[1])


if __name__ == "__main__":
  """
  Тут точно какой-то подвох, но ладно. :[
  """
  infile = open("cond.in")
  outfile = open("cond.out", 'w')

  infile.readline()
  
  classes = list(map(int, infile.readline().strip().split()))
  classes.sort()
  
  infile.readline()
  
  conds = []
  for line in infile.readlines():
    conds.append(tuple(map(int, line.strip().split())))
  
  costs = 0
  
  for class_ in classes:
    cond = minForClass(class_, conds)
    #conds.remove(cond)
    costs += cond[1]
  
  outfile.write(str(costs))
  
  outfile.close()
