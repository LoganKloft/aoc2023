# changes to algorithm 1:
# parse seeds into tuples which are ranges
# translation will split seeds into smaller ranges
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
temp_seeds = []
seeds = []
for i in range(0, len(line) - 1, 2):
    seeds.append((int(line[i]), int(line[i]) + int(line[i + 1]) - 1))

# create ranges
src_rngs = [[] for _ in range(7)]
dst_rngs = [[] for _ in range(7)]

i = 0
src_rng = src_rngs[i]
dst_rng = dst_rngs[i]
j = 3
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
        src_rng.append((src, src + rng - 1, j))
        dst_rng.append((dst, dst + rng - 1, j))
    
    j += 1

# sort ranges
for rng in src_rngs:
    rng.sort()

new_dst_rngs = []
for i in range(len(src_rngs)):
    new_dst_rng = []
    for src_rng in src_rngs[i]:
        src_rng_id = src_rng[-1]
        for dst_rng in dst_rngs[i]:
            if dst_rng[-1] == src_rng_id:
                new_dst_rng.append(dst_rng)
    new_dst_rngs.append(new_dst_rng)
dst_rngs = new_dst_rngs

# create function that translates from source to destination
def translate(seed, src_rng, dst_rng):
    low = seed[0]
    high = seed[1]
    new_rngs = []
    for j in range(len(src_rng)):
        if low == -1 and high == -1:
            break

        start = src_rng[j][0]
        end = src_rng[j][1]

        # low is after this src range
        if low > end:
            continue
        
        # low is before this src range
        if low < start:
            if high < start:
                new_rngs.append((low, high, -1))
                low, high = -1, -1
                break

            if high >= start and high <= end:
                new_rngs.append((low, start - 1, -1))
                new_rngs.append((start, high, j))
                low, high = -1, -1
                break

            if high > end:
                new_rngs.append((low, start - 1, -1))
                new_rngs.append((start, end, j))
                low = end + 1
                continue

        # low is inside this src range
        if low >= start:
            if high <= end:
                new_rngs.append((low, high, j))
                low, high = -1, -1
                continue
            if high > end:
                new_rngs.append((low, end, j))
                low = end + 1
    
    if low != -1 and high != -1:
        new_rngs.append((low, high, -1))

    result = []
    for low, high, category in new_rngs:
        if category == -1:
            result.append((low, high))
        else:
            offset_0 = low - src_rng[category][0]
            offset_1 = high - src_rng[category][0]
            result.append((dst_rng[category][0] + offset_0, dst_rng[category][0] + offset_1))

    return result

for i in range(7):
    temp_seeds = []
    for j in range(len(seeds)):
        new_rngs = translate(seeds[j], src_rngs[i], dst_rngs[i])
        
        for new_rng in new_rngs:
            temp_seeds.append(new_rng)
    
    seeds = temp_seeds

min_seed = seeds[0][0]
for seed in seeds:
    if seed[0] < min_seed:
        min_seed = seed[0]

print(min_seed)