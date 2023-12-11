g = []
void_r = []
void_c = []
with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    row=0
    for line in lines:
        col=0
        for c in line:
            if c == "#":
                g.append((row, col))
            col+=1
        row+=1

void_r = set(range(0, row)).difference(set([x[0] for x in g]))
void_c = set(range(0, col)).difference(set([x[1] for x in g]))


smm = 0
for i, g_from in enumerate(g):
    for g_to in g[i+1:]:
        if g_from == g_to:
            continue
        dist_raw = abs(g_from[0] - g_to[0]) + abs(g_from[1] - g_to[1])
        voids_r = [x for x in void_r if x > min(g_from[0], g_to[0]) and x < max(g_from[0], g_to[0])]
        voids_c = [x for x in void_c if x > min(g_from[1], g_to[1]) and x < max(g_from[1], g_to[1])]
        dist_expanded = dist_raw + len(voids_r) + len(voids_c)
        smm += dist_expanded
print(smm)
