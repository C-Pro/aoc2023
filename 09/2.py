v = []
with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    for line in lines:
        v.append([int(x) for x in line.split()])

def get_next(s):
    t = [s]
    while True:
        s = t[-1]
        n = []

        zeros = True
        for a, b in [(s[i], s[i+1]) for i in range(len(s)-1)]:
            diff = b - a
            n.append(diff)
            if diff != 0:
                zeros = False
        t.append(n)
        if zeros:
            break
    diff = 0
    for i in range(len(t)-2, -1, -1):
        diff = t[i][0] - diff
    return(diff)

smm = 0
for s in v:
    smm+=get_next(s)
print(smm)
