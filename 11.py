# parse the input
with open("11-input.txt") as f:
    energy = [[int(c) for c in l.strip()] for l in f.readlines()]

width = len(energy[0])
height = len(energy)


def neighbouring(j, i):
    # j, i neighbour list including diagonals
    c = set([(i - 1, j - 1) for i in range(3) for j in range(3)])
    c.remove((0, 0))
    if i == 0:
        c -= set([(n, -1) for n in (-1, 0, 1)])
    elif i == width - 1:
        c -= set([(n, 1) for n in (-1, 0, 1)])
    if j == 0:
        c -= set([(-1, n) for n in (-1, 0, 1)])
    elif j == height - 1:
        c -= set([(1, n) for n in (-1, 0, 1)])
    return set([(j + y, i + x) for (y, x) in c])


def flash_maybe(j, i) -> int:
    count = 0
    energy[j][i] += 1
    if energy[j][i] >= 10:
        count += 1
        energy[j][i] = -1000
        for (y, x) in neighbouring(j, i):
            count += flash_maybe(y, x)
    return count


flashes = 0
firstsync = 0
for step in range(1000):
    for j in range(height):
        for i in range(width):
            flashes += flash_maybe(j, i)

    for j in range(height):
        for i in range(width):
            if energy[j][i] < 0:
                energy[j][i] = 0

    total = sum(energy[j][i] for j in range(height) for i in range(width))
    if firstsync == 0 and total == 0:
        firstsync = step + 1

print("Answer 1: ", flashes)
print("Answer 2: ", firstsync)
