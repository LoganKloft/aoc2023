# look at each number and look for symbols around it: need to know of row above and below current row
# look at each symbol and look for numbers around it: could introduce double counting issue, need to know row above and below current row

# could be slower to look around each number as opposed to symbols
# logic looking around number more complex than a symbol - unless we privot 8 spots around each character in the number
translations = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def getNumber(col, line):
    i = col
    # rewind i to the left
    while i > -1 and line[i].isnumeric():
        i -= 1
    i += 1  # i stops when out of bounds or not on a number, go forward 1 to start at the first digit

    num = ""
    while i < len(line) and line[i].isnumeric():
        num += line[i]
        i += 1

    return int(num)


def processWindow(row, window):
    res = 0

    for i in range(len(window[row])):
        # check for numbers around '*'
        if window[row][i] == "*":
            # keep track of indices of numbers
            number_hits = []

            # check row above
            if row - 1 > -1:
                if window[row - 1][i].isnumeric():
                    number_hits.append(
                        (
                            row - 1,
                            i,
                        )
                    )
                else:
                    if i - 1 > -1 and window[row - 1][i - 1].isnumeric():
                        number_hits.append(
                            (
                                row - 1,
                                i - 1,
                            )
                        )
                    if (
                        i + 1 < len(window[row - 1])
                        and window[row - 1][i + 1].isnumeric()
                    ):
                        number_hits.append(
                            (
                                row - 1,
                                i + 1,
                            )
                        )

            # check current row
            if i - 1 > -1 and window[row][i - 1].isnumeric():
                number_hits.append(
                    (
                        row,
                        i - 1,
                    )
                )
            if i + 1 < len(window[row]) and window[row][i + 1].isnumeric():
                number_hits.append(
                    (
                        row,
                        i + 1,
                    )
                )

            # check row below
            if row + 1 < len(window):
                # check row above
                if window[row + 1][i].isnumeric():
                    number_hits.append(
                        (
                            row + 1,
                            i,
                        )
                    )
                else:
                    if i - 1 > -1 and window[row + 1][i - 1].isnumeric():
                        number_hits.append(
                            (
                                row + 1,
                                i - 1,
                            )
                        )
                    if (
                        i + 1 < len(window[row + 1])
                        and window[row + 1][i + 1].isnumeric()
                    ):
                        number_hits.append(
                            (
                                row + 1,
                                i + 1,
                            )
                        )

            if len(number_hits) == 2:
                num1 = getNumber(number_hits[0][1], window[number_hits[0][0]])
                num2 = getNumber(number_hits[1][1], window[number_hits[1][0]])
                res += num1 * num2

    return res


result = 0
with open("input1.txt", "r") as input1:
    lines = input1.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].strip()

    # process top line
    window = [lines[0], lines[1], lines[2]]
    result += processWindow(0, window)

    for i in range(1, len(lines) - 1):
        window = [lines[i - 1], lines[i], lines[i + 1]]
        result += processWindow(1, window)

    # process last line
    window = [lines[-3], lines[-2], lines[-1]]
    result += processWindow(2, window)

print(result)
