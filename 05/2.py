def apply(x, translation):
    destination, source, amount = translation
    if x < source or x >= source + amount:
        return x, False
    return destination + (x - source), True


def get_ranges(range, translation):
    ranges = set()
    destination, source, amount = translation
    if amount == 0:
        return ranges, False
    matched = False

    ss, se = source, source + amount - 1
    start, end = range

    if start >= ss:
        if start <= se:
            s, m = apply(start, translation)
            if m:
                matched = True
            e, m = apply(min(end, se), translation)
            if m:
                matched = True
            ranges.add((s, e))
    else:
        ranges.add((start, min(end, ss - 1)))
    if end >= ss and se >= start:
        if end <= se:
            s, m = apply(max(start, ss), translation)
            if m:
                matched = True
            e, m = apply(end, translation)
            if m:
                matched = True
            ranges.add((s, e))
        else:
            s, m = apply(max(start, ss), translation)
            if m:
                matched = True
            e, m = apply(se, translation)
            if m:
                matched = True
            ranges.add((s, e))

            s, m = apply(se, translation)
            if m:
                matched = True
            e, m = apply(end, translation)
            if m:
                matched = True
            ranges.add((s, e))


    for r in ranges:
        assert r[0] <= r[1]

    return ranges, matched


#print(get_ranges((0, 10), (0, 0, 0)))
assert get_ranges((0, 10), (0, 0, 0)) == (set([]), False)
assert get_ranges((0, 10), (1, 0, 1)) == ({(1,1),(1,10)}, True)
#print(get_ranges((3, 4), (10, 0, 10))) sSEe
assert get_ranges((3, 4), (10, 0, 10)) == ({(13, 14)}, True)
#print(get_ranges((3, 5), (5, 4, 10))) SsEe
assert get_ranges((3, 5), (5, 4, 10)) == ({(3, 3), (5, 6)}, True)
#print(get_ranges((3, 10), (5, 4, 2))) sSeE
assert get_ranges((3, 10), (5, 4, 2)) == ({(3, 3), (5, 6), (6, 10)}, True)
#print(get_ranges((3, 10), (10, 0, 4))) sSeE
assert get_ranges((3, 10), (10, 0, 4)) == ({(13, 13),(4,10)}, True)
#print(get_ranges((3, 10), (10, 0, 5))) sSeE
assert get_ranges((3, 10), (10, 0, 5)) == ({(13, 14),(5,10)}, True)
#print(get_ranges((3, 10), (15, 5, 2))) # SseE
assert get_ranges((3, 10), (15, 5, 2)) == ({(3, 4), (15, 16), (7, 10)}, True)

with open("test.txt", "rt") as fi:
    lines = fi.read().splitlines()

    nums = [int(x) for x in lines[0].split(":")[1].strip().split(" ") if x.isnumeric()]
    ranges = []
    for i in range(len(nums) // 2):
        ranges.append((nums[2 * i], nums[2 * i] + nums[2 * i + 1]))

    maps = []
    translations = []
    for line in lines[1:]:
        if line.find("map:") != -1:
            if len(translations) > 0:
                maps.append(translations)
            translations = []
            continue
        numbers = [int(x) for x in line.split(" ") if x.isnumeric()]
        if len(numbers) == 3:
            translations.append(numbers)
    maps.append(translations)

    ranges = set(ranges)
    for m in maps:
        new_ranges = set()
        for rg in ranges:
            matched = False
            for translation in m:
                n, a = get_ranges(rg, translation)
                if a:
                    matched = True
                    new_ranges.update(n)
                    break
            if not matched:
                new_ranges.add(rg)
        print(new_ranges)

        ranges = new_ranges

    print(min([x[0] for x in ranges]))
