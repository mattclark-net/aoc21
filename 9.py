# parse the input
with open("9-input.txt") as f:
    data = [[int(c) for c in l.strip()] for l in f.readlines()]

width = len(data[0])
height = len(data)


def neighbouring(j, i):
    # j, i neighhbour list
    candidates = set(((-1, 0), (1, 0), (0, -1), (0, 1)))
    if i == 0:
        candidates.remove((0, -1))
    if i == width - 1:
        candidates.remove((0, 1))
    if j == 0:
        candidates.remove((-1, 0))
    if j == height - 1:
        candidates.remove((1, 0))
    return set([(j + n[0], i + n[1]) for n in candidates])


def neighbour_vals(data, j, i):
    # j, i neighbour list
    return [data[n[0]][n[1]] for n in neighbouring(j, i)]


def grow_basin(basin: set, j, i) -> set:
    basin.add((j, i))
    nl = neighbouring(j, i).difference(basin)
    for n in nl:
        if data[n[0]][n[1]] != 9:
            grow_basin(basin, n[0], n[1])
    return


risk = 0
for j in range(height):
    for i in range(width):
        v = data[j][i]
        if v < min(neighbour_vals(data, j, i)):
            risk += v + 1
print("Risk: {}".format(risk))

basins = []
for j in range(height):
    for i in range(width):
        v = data[j][i]
        if v < min(neighbour_vals(data, j, i)):
            # low point of a basin
            basin = set()
            grow_basin(basin, j, i)
            basins.append(basin)

basins.sort(key=len)
sizes = [len(b) for b in basins[-3:]]
print(
    "Answer: {} * {} * {} = {}".format(
        sizes[0], sizes[1], sizes[2], sizes[0] * sizes[1] * sizes[2]
    )
)
