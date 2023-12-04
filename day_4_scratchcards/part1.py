document = open("input1.txt")
result = 0
for line in document.readlines():
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
    left = left
    right = right
    n = 0
    for token in left:
        if token in right:
            n += 1

    if n > 0:
        result += 2 ** (n - 1)

print(result)