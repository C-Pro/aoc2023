
with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    smm = 0
    numbers = []
    gears = []
    for row, l in enumerate(lines):
        in_number = False
        num = {
            "row": row,
            "start_col": 0,
            "end_col": 0,
            "num": "",
            "is_part": False,
        }
        for col, ch in enumerate(list(l)):
            if ch.isdigit():
                if in_number==False:
                    num["start_col"] = col
                    in_number = True
                num["end_col"] = col
                num["num"] += ch
            else:
                if in_number:
                    in_number = False
                    numbers.append(num)
                    num = {
                        "row": row,
                        "start_col": 0,
                        "end_col": 0,
                        "num": "",
                        "is_part": False,
                    }
                if ch == "*":
                    gears.append((row, col))
            if col == len(l)-1 and in_number:
                num["end_col"] = col
                in_number = False
                numbers.append(num)
                num = {
                    "row": row,
                    "start_col": 0,
                    "end_col": 0,
                    "num": "",
                    "is_part": False,
                }
    for s in gears:
        adj = []
        for n in numbers:
            if abs(n["row"] - s[0]) <= 1 \
                and s[1] >= n["start_col"]-1 \
                and s[1] <= n["end_col"]+1:
                    adj.append(n)
        if len(adj) == 2:
            smm += int(adj[0]["num"]) * int(adj[1]["num"])

print(smm)
