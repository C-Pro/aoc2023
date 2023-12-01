repl = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def conv(l):
    s = ""
    for i in range(len(l)):
        if l[i].isdigit():
            s += l[i]
        else:
            for k, v in repl.items():
                if l[i:].startswith(k):
                    s += v
                    break
    return s

with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    s = 0
    for l in lines:
        lb = l
        l = conv(l)
        print(l)
        print(lb)
        if len(l) == 0:
            raise Exception("Empty line")
            continue
        d = [c for c in list(l) if c.isdigit()]
        if len(d) == 0:
            raise Exception("No digits")
            continue
        #print(d)
        print("".join([d[0],d[len(d)-1]]))

        s += int("".join([d[0],d[len(d)-1]]))

print(s)
