with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    time = int(lines[0].split(":")[1].strip().replace(" ", ""))
    dist = int(lines[1].split(":")[1].strip().replace(" ", ""))

wins=0
for j in range(time):
    if (time-j) * j > dist:
        wins += 1

print(wins)
