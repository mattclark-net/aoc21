# parse the input
with open("5-input.txt") as f:
    data = f.readlines()
    endpoints = []
    for l in data:
        s = l.split()
        start, end = (
            [int(v) for v in s[0].split(",")],
            [int(v) for v in s[2].split(",")],
        )
        endpoints.append([start, end])
        width = max([max(line[0][0], line[1][0]) for line in endpoints]) + 1
        height = max([max(line[0][1], line[1][1]) for line in endpoints]) + 1


def horizontal_or_vertical(coords):
    return coords[0][0] == coords[1][0] or coords[0][1] == coords[1][1]


def drawnfield(field, line):
    newfield = field.copy()
    sx, sy, ex, ey = [v for coord in line for v in coord]
    if horizontal_or_vertical(line):
        for x in range(min(sx, ex), max(sx, ex) + 1):
            for y in range(min(sy, ey), max(sy, ey) + 1):
                newfield[y][x] = newfield[y][x] + 1
    else:
        # 45 degree line, per requirements for puzzle 2
        if sx > ex:
            # swap the coords so the leftmost is first
            sx, sy, ex, ey = ex, ey, sx, sy 
        up_or_down = 1 if ey > sy else -1
        y = sy
        for x in range(sx, ex + 1):
            newfield[y][x] = newfield[y][x] + 1
            y += up_or_down
    return newfield

def overlaps(field, minimum):
    o = 0
    for row in field:
        for point in row:
            if point >= minimum:
                o += 1
    return o


# Puzzle 1

# This special syntax is required to avoid the same list object being used for each row
field = [[0 for i in range(width)] for j in range(height)]
for line in endpoints:
    if horizontal_or_vertical(line):
        field = drawnfield(field, line)
print(overlaps(field, 2))

# Puzzle 2
field = [[0 for i in range(width)] for j in range(height)]
for line in endpoints:
   field = drawnfield(field, line)
print(overlaps(field, 2))

