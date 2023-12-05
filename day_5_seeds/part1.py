document = open("input1.txt")
lines = document.readlines()
document.close()

# preprocess all lines - remove '\n'
for i in range(len(lines)):
    lines[i] = lines[i].strip()

# parse seeds
line = lines[0]
line = line.split(" ")
line = line[1:]
seeds = []
for seed in line:
    seeds.append(int(seed))

# create ranges
src_rngs = [[] for _ in range(7)]
dst_rngs = [[] for _ in range(7)]

i = 0
src_rng = src_rngs[i]
dst_rng = dst_rngs[i]
j = 4
line = lines[j]
while j < len(lines):
    line = lines[j]
    if line == "":
        j += 1
        i += 1
        src_rng = src_rngs[i]
        dst_rng = dst_rngs[i]
    
    else:
        dst, src, rng = line.split(" ")
        dst = int(dst)
        src = int(src)
        rng = int(rng)
        src_rng.append((src, src + rng - 1))
        dst_rng.append((dst, dst + rng - 1))
    
    j += 1

# create function that translates from source to destination
def translate(seed, src_rng, dst_rng):
    i = -1
    offset = 0
    for j in range(len(src_rng)):
        start = src_rng[j][0]
        end = src_rng[j][1]
        if seed >= start and seed <= end:
            i = j
            offset = seed - start
            break
    
    if i == -1:
        return seed

    start = dst_rng[i][0]
    return start + offset

for i in range(7):
    for j in range(len(seeds)):
        seeds[j] = translate(seeds[j], src_rngs[i], dst_rngs[i])

print(min(seeds))