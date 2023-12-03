# look at each number and look for symbols around it: need to know of row above and below current row
# look at each symbol and look for numbers around it: could introduce double counting issue, need to know row above and below current row

# could be slower to look around each number as opposed to symbols
# logic looking around number more complex than a symbol - unless we privot 8 spots around each character in the number
translations = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def processWindow(row, window):
    res = 0
    i = 0
    foundSymbol = False
    while i < len(window[row]):
        # get the entire number and check for symbols
        if window[row][i].isnumeric():
            num = ""
            while i < len(window[row]) and window[row][i].isnumeric():
                num += window[row][i]

                # check for symbol
                for dx, dy in translations:
                    if (
                        row + dy < 3
                        and row + dy > -1
                        and i + dx < len(window[row])
                        and i + dx > -1
                        and window[row + dy][i + dx] != "."
                        and not window[row + dy][i + dx].isnumeric()
                    ):
                        foundSymbol = True

                i += 1

            if foundSymbol:
                res += int(num)
                foundSymbol = False

        i += 1

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
