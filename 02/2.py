import re

re = re.compile(r"(\d+)\s+(\w+)")


def parse(l):
    game = []
    i = l.find(":")
    if i == -1:
        return None
    l = l[i+1:]
    sets = l.split(";")
    for s in sets:
        theset = {"red":0, "blue":0, "green":0}
        cubes = s.split(",")
        for c in cubes:
            m = re.match(c.strip())
            if m is None:
                raise ValueError(f"Invalid cube: '{c}'")
            theset[m.group(2)] = int(m.group(1))
        game.append(theset)
    return game


with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    smm = 0
    for n, l in enumerate(lines):
        g = parse(l)
        print(l)
        #print(g)
        m = {"red":0, "blue":0, "green":0}
        for s in g:
            for k, v in s.items():
                if m[k] < v:
                    m[k] = v
        print(m["red"] * m["blue"] * m["green"])
        smm += m["red"] * m["blue"] * m["green"]
    print(smm)
