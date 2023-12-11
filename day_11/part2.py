document = open("input1.txt")
lines = document.readlines()
document.close()

empty_rows = []
empty_cols = []

for i in range(len(lines)):
    lines[i] = lines[i].strip()
    flag = 1000000
    for j in range(len(lines[i])):
        if lines[i][j] == "#":
            flag = 0
            break
    empty_rows.append(flag)

for i in range(len(lines[0])):
    flag = 1000000
    for j in range(len(lines)):
        if lines[j][i] == "#":
            flag = 0
            break
    empty_cols.append(flag)

space = []
for i in range(len(lines)):
    space.append([])
    for j in range(len(lines[i])):
        space[i].append(lines[i][j])

        if empty_cols[j] == 1000000 or empty_rows[i] == 1000000:
            space[i][j] = 1000000


galaxies = []
for i in range(len(space)):
    for j in range(len(space[i])):
        if space[i][j] == "#":
            galaxies.append((i, j,))

result = 0
for i in range(len(galaxies) - 1):
    galaxy1 = galaxies[i]
    for j in range(i + 1, len(galaxies)):
        galaxy2 = galaxies[j]

        s = 0
        low = min(galaxy1[0], galaxy2[0])
        high = max(galaxy1[0], galaxy2[0])
        while low != high:
            if space[low][galaxy1[1]] == 1000000:
                s += 1000000
            else:
                s += 1
            low += 1
        
        low = min(galaxy1[1], galaxy2[1])
        high = max(galaxy1[1], galaxy2[1])
        while low != high:
            if space[galaxy1[0]][low] == 1000000:
                s += 1000000
            else:
                s += 1
            low += 1
        
        result += s

print(result)