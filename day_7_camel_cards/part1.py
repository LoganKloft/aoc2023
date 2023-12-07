value = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}

def isFiveOfKind(cards):
    seen = dict()
    for card in cards:
        if card not in seen:
            seen[card] = 0
        seen[card] += 1
    
    if len(seen) == 1: return 1
    return 0

def isFourOfKind(cards):
    seen = dict()
    for card in cards:
        if card not in seen:
            seen[card] = 0
        seen[card] += 1
    
    for key, val in seen.items():
        if val == 4: return 1
    return 0

def isFullHouse(cards):
    seen = dict()
    for card in cards:
        if card not in seen:
            seen[card] = 0
        seen[card] += 1
    
    if len(seen) != 2: return 0

    for key, val in seen.items():
        if val == 3: return 1
    return 0

def isThreeOfKind(cards):
    seen = dict()
    for card in cards:
        if card not in seen:
            seen[card] = 0
        seen[card] += 1
    
    if len(seen) != 3: return 0

    for key, val in seen.items():
        if val == 3: return 1
    return 0

def isTwoPair(cards):
    seen = dict()
    for card in cards:
        if card not in seen:
            seen[card] = 0
        seen[card] += 1
    
    if len(seen) != 3: return 0

    for key, val in seen.items():
        if val == 2: return 1
    return 0

def isOnePair(cards):
    seen = dict()
    for card in cards:
        if card not in seen:
            seen[card] = 0
        seen[card] += 1
    
    if len(seen) == 4: return 1
    return 0

def getType(cards):
    if isFiveOfKind(cards): return 7
    if isFourOfKind(cards): return 6
    if isFullHouse(cards): return 5
    if isThreeOfKind(cards): return 4
    if isTwoPair(cards): return 3
    if isOnePair(cards): return 2
    return 1

def breakTie(cards1, cards2):
    for i in range(len(cards1)):
        if value[cards1[i]] > value[cards2[i]]:
            return 1
        elif value[cards1[i]] < value[cards2[i]]:
            return -1
    
    return 0

# will never be a tie
def compareHands(hand1, hand2):
    cards1 = hand1[0]
    cards2 = hand2[0]

    t1 = getType(cards1)
    t2 = getType(cards2)

    if (t1 > t2): return 1 # hand1 better
    if (t2 > t1): return -1 # hand2 better
    
    return breakTie(cards1, cards2)

document = open("input1.txt")
lines = document.readlines()
document.close()

hands = []
for line in lines:
    line = line.strip()
    line = line.split()
    hands.append((line[0], int(line[1]),))

for i in range(len(hands) - 1):
    for j in range(len(hands) - 1):
        if compareHands(hands[j], hands[j + 1]) == 1:
            hands[j], hands[j + 1] = hands[j + 1], hands[j]

s = 0
for i in range(len(hands)):
    hand = hands[i]
    s += (hand[1] * (i + 1))

print(s)