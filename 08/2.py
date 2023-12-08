import re
import numpy as np

ptn = re.compile(r"\((\w+), (\w+)\)")

m = {}
path = ""
with open("test.txt", "rt") as fi:
    lines=fi.read().splitlines()
    path=lines[0].strip()

    for line in lines[2:]:
        n = line[:3]
        p = ptn.findall(line)[0]
        m[n] = {"L": p[0], "R": p[1]}

i = 0
curr = [x for x in m if x[2] == "A"]
freqs = [[] for x in curr]
cnt = 0
while True:
    cnt += 1
    c = path[i]
    finished = True
    for j in range(len(curr)):
        curr[j] = m[curr[j]][c]
        if curr[j][2] != "Z":
            finished = False
        else:
            freqs[j].append(cnt)
    if finished:
        break
    i = (i + 1) % len(path)
    if min(len(x) for x in freqs) > 1:
        break

print(freqs)
for x in freqs:
    print(x[1] - x[0] == x[0])

print(np.lcm.reduce([x[0] for x in freqs]))
