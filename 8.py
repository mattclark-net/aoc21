# parse the input
with open("8-input.txt") as f:
    data = [[part.split() for part in l.split("|")] for l in f.readlines()]


# part 1
counts = dict(zip(range(8), [0] * 8))
for line in data:
    for output in line[1]:
        if len(output == 5):
            counts[len(output)] += 1

print(sum([counts[x] for x in (2, 3, 4, 7)]))

# part 2
counts = dict(zip(range(8), [0] * 8))
for line in data:
    mapping = dict(zip("abcdefg"), [None] * 7)
    observations = line[0]
    for ones_signal in [o for o in observations if len(o) == 2].pop():
        mapping["c"] = ones_signal
        mapping["f"] = ones_signal
    for seven_signal in [o for o in observations if len(o) == 3].pop():
        mapping["c"] = ones_signal
        mapping["f"] = ones_signal

        if len(output == 5):
            counts[len(output)] += 1
