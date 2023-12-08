mapping = {
    #A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
    "2": "a",
    "3": "b",
    "4": "c",
    "5": "d",
    "6": "e",
    "7": "f",
    "8": "g",
    "9": "h",
    "T": "j",
    "J": "k",
    "Q": "l",
    "K": "m",
    "A": "n",
}

def to_sort(hand):
    return "".join([mapping[c] for c in hand])

def counts(hand):
    cnt = {}
    for c in hand:
        if c not in cnt:
            cnt[c] = 0
        cnt[c] += 1
    return sorted(cnt.values(), reverse=True)

def hand_value(hand):
    # Five of a kind
    if len(set(hand)) == 1:
        return 7
    # Four of a kind
    if counts(hand)[0] == 4:
        return 6
    # Full house
    if counts(hand) == [3, 2]:
        return 5
    # Three of a kind
    if counts(hand)[0] == 3:
        return 4
    # Two pair
    if counts(hand) == [2, 2, 1]:
        return 3
    # One pair
    if counts(hand) == [2, 1, 1, 1]:
        return 2
    # High card
    if counts(hand) == [1, 1, 1, 1, 1]:
        return 1
    return 0


hands=[]
with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    for line in lines:
        parts = line.split()
        hand = {
            "hand": parts[0].strip(),
            "bid": int(parts[1].strip()),
            "sort": to_sort(parts[0].strip()),
            "value": hand_value(parts[0].strip()),
        }
        hands.append(hand)

sorted_hands = sorted(hands, key=lambda x: (x["value"], x["sort"]), reverse=True)
win = 0
rank = len(sorted_hands)
for hand in sorted_hands:
    print(hand["hand"], hand["bid"], rank)
    win += hand["bid"] * rank
    rank -= 1
print(win)
