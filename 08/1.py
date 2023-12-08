import re
ptn = re.compile(r"\((\w+), (\w+)\)")

m = {}
path = ""
with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    path=lines[0].strip()

    for line in lines[2:]:
        n = line[:3]
        p = ptn.findall(line)[0]
        m[n] = {"L": p[0], "R": p[1]}

i = 0
curr = "AAA"
cnt = 0
while curr != "ZZZ":
    cnt += 1
    c = path[i]
    i = (i + 1) % len(path)
    curr = m[curr][c]
print(cnt)
