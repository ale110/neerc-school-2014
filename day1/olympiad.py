#!/usr/bin/python
# encoding: utf-8
 
def intersect(i, js, tasks):
    ti = tasks[i]
    i10n = []
    for j in js:
        tj = tasks[j]
        if tj['start'] < ti['end'] < tj['end'] \
          or tj['start'] < ti['start'] < tj['end'] \
          or ti['start'] < tj['end'] < ti['end'] \
          or ti['start'] < tj['start'] < ti['end']:
            i10n.append(j)
            continue
     
    return i10n
 
 
infile = open("olympiad.in")
outfile = open("olympiad.out", 'w')
 
infile.readline() # Skip `n`
 
tasks = []
 
for line in infile.readlines():
    start, time, reward = map(int, line.strip().split())
    tasks.append({
        'start': start,
        'time': time,
        'end': start + time,
        'reward': reward
    })
 
to_solve = []
 
for i in range(len(tasks)):
    i10n = intersect(i, to_solve, tasks)
    i_reward = sum(map(lambda x: tasks[x]['reward'], i10n))
    if  i_reward < tasks[i]['reward']:
        for j in i10n:
            to_solve.remove(j)
        to_solve.append(i)
 
outfile.write(str(sum(map(lambda x: tasks[x]['reward'], to_solve))) + "\n")
outfile.write(str(len(to_solve)) + "\n")
outfile.write(" ".join(map(lambda i: str(i+1), to_solve)))
outfile.close()