result = 0

with open("input1.txt", "r") as input1:
    lines = input1.readlines()

    for line in lines:
        # go from left to right until find first integer
        left = 0
        for i in range(len(line)):
            if line[i].isnumeric():
                left = i
                break

        # go from right to left until find first integer
        right = len(line) - 1
        for i in range(len(line) - 1, -1, -1):
            if line[i].isnumeric():
                right = i
                break

        result += int(line[left] + line[right])

print(result)
