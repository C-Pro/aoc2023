v = []
with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    for line in lines:
        v.append([int(x) for x in line.split()])
# import numpy as np
# from sklearn.linear_model import LinearRegression

# ssm = 0
# for s in v:
#     X = np.array(s[:-1]).reshape(-1, 1)
#     Y = np.array(s[1:]).reshape(-1, 1)
#     reg = LinearRegression().fit(X, Y)
#     print(reg.score(X, Y))
#     ssm += round(reg.predict(np.array(s[-1]).reshape(-1, 1))[0,0])
# print(ssm)

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
    for i in range(len(t)-1, -1, -1):
        diff = t[i][-1]
        if i >= 1:
            t[i-1].append(t[i-1][-1]+diff)
    return(t[0][-1])

smm = 0
for s in v:
    smm+=get_next(s)
print(smm)
