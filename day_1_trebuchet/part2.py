def reverse(string):
    return string[::-1]


forward = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
]

wordToNumAsString = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "0": "0",
}


def findFirstNum(line):
    first = -1
    word = "0"
    for target in forward:
        i = line.find(target)
        if i != -1 and (i < first or first == -1):
            first = i
            word = target

    return wordToNumAsString[word]


backward = [reverse(string) for string in forward]


def findLastNum(line):
    # reverse line
    lineReverse = reverse(line)
    last = -1
    word = "0"
    for target in backward:
        i = lineReverse.find(target)
        if i != -1 and (i < last or last == -1):
            last = i
            word = target

    return wordToNumAsString[reverse(word)]


result = 0

with open("input1.txt", "r") as input1:
    lines = input1.readlines()

    for line in lines:
        left = findFirstNum(line)
        right = findLastNum(line)

        result += int(left + right)

print(result)
