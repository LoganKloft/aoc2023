document = open("input1.txt")
lines = document.readlines()
document.close()
races = []

i = 1
times = lines[0].split()
distances = lines[1].split()
while i < len(times):
    races.append((int(times[i]), int(distances[i])))
    i += 1

result = 1
for time, distance in races:
    c = 0
    for i in range(time):
        d = i * (time - i)
        if d > distance:
            c += 1
    result *= c

print(result)