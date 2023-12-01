with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    s = 0
    for l in lines:
        print(l)
        if len(l) == 0:
            continue
        d = [c for c in list(l) if c.isdigit()]
        if len(d) == 0:
            continue
        print(d)
        print("".join([d[0],d[len(d)-1]]))

        s += int("".join([d[0],d[len(d)-1]]))

print(s)
