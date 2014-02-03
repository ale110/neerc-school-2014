#!/usr/bin/python
# encoding: utf-8

def updateWith(d1, d2, k, v):
  if not k in d1:
    d1[k] = set()
  
  if not v in d2:
    d2[v] = set()
  
  d1[k].add(v)
  d2[v].add(k)
  return d1, d2

def indirectRel(d, k):
  owned = d[k]
  checked = []
  while not set(checked) == set(owned):
    for employee in owned:
      if not employee in checked:
        if employee in d:
          owned.update(d[employee])
        checked.append(employee)
        break
  
  return owned

if __name__ == "__main__":
  infile = open("volunteers.in")
  outfile = open("volunteers.out", 'w')

  n, scientists_count, _2 = map(int, infile.readline().strip().split())
  
  owned = {}
  owners = {}
  
  i = 1
  for _ in range(n):
    sci, tch = map(int, infile.readline().strip().split())
    owned, owners = updateWith(owned, owners, 'sci_%i' % sci, 'vol_%i' % i)
    owned, owners = updateWith(owned, owners, 'tch_%i' % tch, 'vol_%i' % i)
    i += 1
    
  i = 1
  for onna in map(int, infile.readline().strip().split()):
    owned, owners = updateWith(owned, owners, 'sci_%i' % onna, 'sci_%i' % i)
    i += 1
  
  i = 1
  for onna in map(int, infile.readline().strip().split()):
    owned, owners = updateWith(owned, owners, 'tch_%i' % onna, 'tch_%i' % i)
    i += 1
  
  total_conflicts = 0
  for i in range(1, scientists_count+1):
    scientist = 'sci_%i' % i
    techies = []
    for o in indirectRel(owned, scientist):
      for buddy in indirectRel(owners, o):
        if 'tch_' in buddy and buddy not in techies:
          techies.append(buddy)
          total_conflicts += 1
  
  outfile.write(str(total_conflicts))
  
  outfile.close()
