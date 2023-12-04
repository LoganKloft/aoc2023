document = open("input1.txt")
lines = document.readlines()
line_count = len(lines)
card_count = [1] * line_count

# populate the score of each card
for i in range(line_count):
    line = lines[i]
    line = line.strip()
    tokens = line.split(" ")
    left = []
    right = []
    tokens = tokens[2:]

    seenPipe = False
    for token in tokens:
        if token == "": continue
        if token == "|":
            seenPipe = True
            continue
        
        if seenPipe:
            right.append(token)
        else:
            left.append(token)
    
    n = 0
    for token in left:
        if token in right:
            n += 1
    
    for j in range(i + 1, i + n + 1):
        card_count[j] += card_count[i]

print(sum(card_count))