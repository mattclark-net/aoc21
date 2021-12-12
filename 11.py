# parse the input
with open("11-input.txt") as f:
    energy = [[int(c) for c in l.strip()] for l in f.readlines()]

width = len(energy[0])
height = len(energy)


def neighbouring(j, i):
    # j, i neighbour list including diagonals
    xstart, xend, ystart, yend = (-1, 1, -1, 1)
    if i == 0:
        xstart = 0
    elif i == width - 1:
        xend = 0
    if j == 0:
        ystart = 0
    elif j == height - 1:
        yend = 0
    c = set(
        (
            (j + y, i + x)
            for x in range(xstart, xend + 1)
            for y in range(ystart, yend + 1)
        )
    )
    c.remove((j, i))  # it's a neighbour list so shouldn't include the input position
    return c


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
