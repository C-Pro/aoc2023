
def apply(x, translation):
    destination, source, amount = translation
    if x < source or x >= source + amount:
        return x
    return destination + (x - source)

assert apply(97, [50,98,2]) == 97
assert apply(98, [50,98,2]) == 50
assert apply(99, [50,98,2]) == 51
assert apply(100, [50,98,2]) == 100


with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    seeds = [int(x) for x in lines[0].split(":")[1].strip().split(" ")]

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



    values = set(seeds)
    #print(values)
    for m in maps:
        new_values = set()
        for val in values:
            added = False
            for translation in m:
                n = apply(val, translation)
                if n != val:
                    new_values.add(n)
                    added = True
                    break
            if not added:
                new_values.add(val)
        #print(new_values)
        values = new_values

    print(min(values))
