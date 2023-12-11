FROM_LEFT = 1
FROM_RIGHT = 2
FROM_BELOW = 3
FROM_ABOVE = 4 

document = open("input1.txt")
lines = document.readlines()
document.close()

visited = []
pipes = []

for line in lines:
    line = line.strip()
    pipes.append(line)
    visited.append([0] * len(line))

# find s
start = None
for i in range(len(pipes)):
    found = False
    for j in range(len(pipes[i])):
        if pipes[i][j] == "S":
            start = (i, j,)
            found = True
            break
    
    if found: break

# dfs from s marking visited areas
result = 0
i = start[0]
j = start[1]
frontier = []
frontier.append((FROM_ABOVE, i + 1, j, 1))
frontier.append((FROM_BELOW, i - 1, j, 1))
frontier.append((FROM_LEFT, i, j + 1, 1))
frontier.append((FROM_RIGHT, i, j - 1, 1))

while result == 0:
    previous, row, col, steps = frontier.pop()

    if row < 0 or row >= len(pipes): continue
    if col < 0 or col >= len(pipes[0]): continue
    if pipes[row][col] == "S": continue

    # reached search criteria
    if visited[row][col] > 0 and visited[row][col] == steps:
        result = steps
        break

    if previous == FROM_ABOVE:
        if pipes[row][col] == "|":
            visited[row][col] = steps
            frontier.append((FROM_ABOVE, row + 1, col, steps + 1))
        elif pipes[row][col] == "L":
            visited[row][col] = steps
            frontier.append((FROM_LEFT, row, col + 1, steps + 1))
        elif pipes[row][col] == "J":
            visited[row][col] = steps
            frontier.append((FROM_RIGHT, row, col - 1, steps + 1))
    elif previous == FROM_BELOW:
        if pipes[row][col] == "|":
            visited[row][col] = steps
            frontier.append((FROM_BELOW, row - 1, col, steps + 1))
        elif pipes[row][col] == "F":
            visited[row][col] = steps
            frontier.append((FROM_LEFT, row, col + 1, steps + 1))
        elif pipes[row][col] == "7":
            visited[row][col] = steps
            frontier.append((FROM_RIGHT, row, col - 1, steps + 1))
    elif previous == FROM_LEFT:
        if pipes[row][col] == "-":
            visited[row][col] = steps
            frontier.append((FROM_LEFT, row, col + 1, steps + 1))
        elif pipes[row][col] == "J":
            visited[row][col] = steps
            frontier.append((FROM_BELOW, row - 1, col, steps + 1))
        elif pipes[row][col] == "7":
            visited[row][col] = steps
            frontier.append((FROM_ABOVE, row + 1, col, steps + 1))
    elif previous == FROM_RIGHT:
        if pipes[row][col] == "-":
            visited[row][col] = steps
            frontier.append((FROM_RIGHT, row, col - 1, steps + 1))
        elif pipes[row][col] == "L":
            visited[row][col] = steps
            frontier.append((FROM_BELOW, row - 1, col, steps + 1))
        elif pipes[row][col] == "F":
            visited[row][col] = steps
            frontier.append((FROM_ABOVE, row + 1, col, steps + 1))

print(result)