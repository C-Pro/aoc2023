smm=0
games=[]
with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    for line in lines:
        idx = line.find(":")
        if idx == -1:
            raise ValueError(f"Invalid line: {line}")
        (winningS, gotS) = line[idx+1:].split("|")
        winning = [int(c) for c in winningS.strip().split(" ") if c.isnumeric()]
        got = [int(c) for c in gotS.strip().split(" ") if c.isnumeric()]
        matches = set(winning).intersection(set(got))
        games.append((1, len(matches)))

for i, g in enumerate(games):
    m = g[1]
    c = g[0]
    if m == 0:
        continue
    for j in range(min(m, len(games))):
        x = i+j+1
        games[x] = (games[x][0]+c, games[x][1])

for (i, m) in games:
    smm += i

print(smm)
