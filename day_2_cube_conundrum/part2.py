result = 0


def getGameId(line):
    # gameid starts at index 5 and continues until we see ":"
    i = 5
    game_id = ""
    while line[i] != ":":
        game_id += line[i]
        i += 1
    return int(game_id)


def getGameSets(line):
    # sets start at index 8
    game_set = ""
    game_sets = []

    start_index = 0
    while line[start_index] != ":":
        start_index += 1
    start_index += 2

    for i in range(start_index, len(line)):
        if line[i] == ",":
            continue

        if line[i] == ";":
            game_sets.append(game_set.strip())
            game_set = ""
            i += 1
            continue

        game_set += line[i]

    game_sets.append(game_set.strip())
    return game_sets


def getCubesInSet(game_set):
    game_set_components = game_set.split(" ")
    cubes_in_set = []
    for i in range(0, len(game_set_components), 2):
        cubes_in_set.append(
            (
                int(game_set_components[i]),
                game_set_components[i + 1],
            )
        )

    return cubes_in_set


with open("input1.txt", "r") as input1:
    lines = input1.readlines()

    for line in lines:
        game_id = getGameId(line)  # return number
        game_sets = getGameSets(line)  # ["3 blue 4 red", "1 red 2 green 6 blue", ...]
        min_red = 0
        min_blue = 0
        min_green = 0
        for game_set in game_sets:
            cubes_in_set = getCubesInSet(game_set)  # [(3, "blue"), (4, "red")]
            for num, color in cubes_in_set:
                if color == "green":
                    min_green = max(min_green, num)
                elif color == "blue":
                    min_blue = max(min_blue, num)
                elif color == "red":
                    min_red = max(min_red, num)

        result += min_red * min_blue * min_green

print(result)
