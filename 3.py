# parse the input
with open("3-input.txt") as f:
    lines = [l.strip() for l in f.readlines()]
bits = len(lines[0])
half = len(lines) // 2
bitarrays = []
for l in lines:
    bitarray = [0] * (bits)
    for b in range(0, bits):
        if l[b] == "1":
            bitarray[b] = 1
    bitarrays.append(bitarray)

# puzzle 1
one_counts = [0] * bits
for b in range(0, bits):
    one_counts[b] = sum([bitarray[b] for bitarray in bitarrays])
print(one_counts)

gammabits = ["0"] * 12
epsilonbits = ["0"] * 12
for b in range(0, bits):
    if one_counts[b] > half:
        gammabits[b] = "1"
    else:
        epsilonbits[b] = "1"

gamma = int("".join(gammabits), 2)
epsilon = int("".join(epsilonbits), 2)
print(gamma, epsilon, gamma * epsilon)


# puzzle 2
def choose(candidates, selectmost):
    for b in range(0, bits):
        ones_count = sum([bitarray[b] for bitarray in candidates])
        if ones_count > len(candidates) / 2:
            select = 1 if selectmost else 0
        elif ones_count < len(candidates) / 2:
            select = 0 if selectmost else 1
        else:
            select = 1 if selectmost else 0
        candidates = [c for c in candidates if c[b] == select]
        if len(candidates) == 1:
            print("select {}: {}".format(select, candidates[0]))
            return candidates[0]


ogc = choose(bitarrays.copy(), True)
csc = choose(bitarrays.copy(), False)
ogr = int("".join([str(v) for v in ogc]), 2)
csr = int("".join([str(v) for v in csc]), 2)
print(ogc, csc, ogr, csr, ogr * csr)
