document = open("input1.txt")
lines = document.readlines()
document.close()

empty_rows = []
empty_cols = []

for i in range(len(lines)):
    lines[i] = lines[i].strip()
    flag = 1
    for j in range(len(lines[i])):
        if lines[i][j] == "#":
            flag = 0
            break
    empty_rows.append(flag)

for i in range(len(lines[0])):
    flag = 1
    for j in range(len(lines)):
        if lines[j][i] == "#":
            flag = 0
            break
    empty_cols.append(flag)

total_rows = sum(empty_rows) + len(empty_rows)
total_cols = sum(empty_cols) + len(empty_cols)

space = [['.'] * total_cols for _ in range(total_rows)]
row_offset = 0
for i in range(len(lines)):
    row_offset += empty_rows[i]
    col_offset = 0
    for j in range(len(lines[i])):
        col_offset += empty_cols[j]
        space[i + row_offset][j + col_offset] = lines[i][j]

galaxies = []
for i in range(len(space)):
    for j in range(len(space[i])):
        if space[i][j] == "#":
            galaxies.append((i, j,))

result = 0
for i in range(len(galaxies) - 1):
    for j in range(i + 1, len(galaxies)):
        result += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])

print(result)