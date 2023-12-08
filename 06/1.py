with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    times = [int(x) for x in lines[0].split(":")[1].strip().split(" ") if x.isnumeric()]
    dists = [int(x) for x in lines[1].split(":")[1].strip().split(" ") if x.isnumeric()]


ways = []
for i in range(len(times)):
    wins=0
    for j in range(times[i]):
        if (times[i]-j) * j > dists[i]:
            wins += 1
    ways.append(wins)

p = 1
for w in ways:
    p *= w
print(p)
