document = open("input1.txt")
lines = document.readlines()
document.close()

directions = lines[0].strip()

desert_map = dict()
i = 2
while i < len(lines):
    line = lines[i].strip()
    line = line.split()
    # ["JKT", "=", "(KFV,", "CFQ)"]
    start = line[0]
    left = line[2][1:4]
    right = line[3][0:3]
    desert_map[start] = (left, right,)
    i += 1

steps = 0

current = "AAA"
i = 0
while current != "ZZZ":
    if directions[i] == "L":
        current = desert_map[current][0]
    else:
        current = desert_map[current][1]

    i = (i + 1) % len(directions)
    steps += 1

print(steps)