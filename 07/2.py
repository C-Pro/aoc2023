mapping = {
    #A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
    "J": "a", # Weakest now
    "2": "b",
    "3": "c",
    "4": "d",
    "5": "e",
    "6": "f",
    "7": "g",
    "8": "h",
    "9": "j",
    "T": "k",
    "Q": "m",
    "K": "n",
    "A": "o",
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

def brute_joker(hand):
    if "J" not in hand:
        return hand_value(hand)
    max_value = 0

    for c in "AKQJT98765432":
        max_value = max(max_value, hand_value(hand.replace("J", c)))

    jokers = [i for i, c in enumerate(hand) if c == "J"]
    if len(jokers) == 2:
        for c1 in "AKQJT98765432":
            for c2 in "AKQJT98765432":
                if c1 != c2:
                    max_value = max(max_value, hand_value(hand.replace("J", c1, 1).replace("J", c2, 1)))
    return max_value


hands=[]
with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    for line in lines:
        parts = line.split()
        hand = {
            "hand": parts[0].strip(),
            "bid": int(parts[1].strip()),
            "sort": to_sort(parts[0].strip()),
            "value": brute_joker(parts[0].strip()),
        }
        hands.append(hand)

sorted_hands = sorted(hands, key=lambda x: (x["value"], x["sort"]), reverse=True)
win = 0
rank = len(sorted_hands)
for hand in sorted_hands:
    print(hand["hand"], hand["bid"], hand["value"], hand["sort"], rank)
    win += hand["bid"] * rank
    rank -= 1
print(win)
