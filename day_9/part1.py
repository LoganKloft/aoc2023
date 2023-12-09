document = open("input1.txt")
lines = document.readlines()
document.close()

result = 0
for line in lines:
    line = line.strip()
    line = line.split()

    # generate histories
    history = []
    for i in range(len(line)):
        history.append(int(line[i]))
    histories = []
    histories.append(history)
    while True:
        flag = True
        history = []
        i = len(histories) - 1
        j = 0

        while j < len(histories[i]) - 1:
            diff = histories[i][j + 1] - histories[i][j]
            history.append(diff)
            if diff != 0:
                flag = False
            j += 1
        
        histories.append(history)
        if flag:
            histories[-1].append(0)
            break
    
    # extrapolate values - part 1
    i = len(histories) - 2
    while i >= 0:
        histories[i].append(histories[i][-1] + histories[i + 1][-1]) 
        i -= 1
    result += histories[0][-1]

    # part 2
    # i = len(histories) - 2
    # new = 0
    # while i >= 0:
    #     new = histories[i][0] - new
    #     i -= 1
    # result += new



print(result)