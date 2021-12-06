# parse the input
with open("6-input.txt") as f:
    fish = [int(n) for n in f.readline().split(",")]

startcounts = dict(zip(range(0, 9), [0 for x in range(9)]))
for f in fish:
    startcounts[f] += 1


def updatedcounts(counts):
    newcounts = {}
    newcounts[8] = counts[0]
    newcounts[7] = counts[8]
    newcounts[6] = counts[7] + counts[0]
    newcounts[5] = counts[6]
    newcounts[4] = counts[5]
    newcounts[3] = counts[4]
    newcounts[2] = counts[3]
    newcounts[1] = counts[2]
    newcounts[0] = counts[1]
    return newcounts


counts = startcounts
for day in range(80):
    print(day, [counts[v] for v in range(9)])
    counts = updatedcounts(counts)
print("\n\n", sum(counts.values()), "\n\n")

counts = startcounts
for day in range(256):
    print(day, [counts[v] for v in range(9)])
    counts = updatedcounts(counts)
print("\n\n", sum(counts.values()), "\n\n")
