smm=0
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
        if len(matches) > 0:
            smm += 2**(len(matches)-1)

print(smm)
