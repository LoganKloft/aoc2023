# calculate length of path for each start to nearest end
# find LCM of all calculations
# that is the number of steps
import math

document = open("input1.txt")
lines = document.readlines()
document.close()

directions = lines[0].strip()

desert_map = dict()
current = []
i = 2
while i < len(lines):
    line = lines[i].strip()
    line = line.split()
    # ["JKT", "=", "(KFV,", "CFQ)"]
    start = line[0]
    left = line[2][1:4]
    right = line[3][0:3]
    desert_map[start] = (left, right,)

    # handle A condition
    if start[-1] == "A":
        current.append(start)
    i += 1

steps = []

for start in current:
    c = start
    step = 0
    i = 0
    while True:
        if directions[i] == "L":
            c = desert_map[c][0]
        else:
            c = desert_map[c][1]

        step += 1
        i = (i + 1) % len(directions)

        if c[-1] == "Z": break
    
    steps.append(step)



print(math.lcm(*steps))