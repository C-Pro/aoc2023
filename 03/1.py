
with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    smm = 0
    numbers = []
    symbols = []
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
                if ch != ".":
                    symbols.append((row, col, ch))
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

    for s in symbols:
        for n in numbers:
            if abs(n["row"] - s[0]) <= 1 \
                and s[1] >= n["start_col"]-1 \
                and s[1] <= n["end_col"]+1:
                    n["is_part"] = True
    for n in numbers:
        if n["is_part"]:
            smm += int(n["num"])
print(smm)
