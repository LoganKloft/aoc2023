import math

document = open("input1.txt")
lines = document.readlines()
document.close()
races = []

i = 1
times = lines[0].split()
distances = lines[1].split()
time = ''
distance = ''
while i < len(times):
    time += times[i]
    distance += distances[i]
    i += 1

time = int(time)
distance = int(distance)

# brute force
c = 0
for i in range(time):
    if i * (time - i) > distance:
        c += 1
print(c)

print(time, distance)
# calculate quadratic formula
a = 1
b = -51699878
c = 377117112241505
x0 = math.floor((b + math.sqrt(b ** 2 - 4 * c))) / 2 # smaller value
x1 = math.ceil((b - math.sqrt(b ** 2 - 4 * c))) / 2 # larger value

print(x0, x1, x1 - x0 - 1)