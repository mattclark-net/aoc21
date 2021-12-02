# parse the input
with open("2-input.txt") as f:
    lines = [(a[0], int(b)) for a, b in [l.split(" ") for l in f.readlines()]]

# puzzle 1
h, d = 0, 0
for v, m in lines:
    if v == "f":
        h = h + m
    elif v == "u":
        d = d - m
    elif v == "d":
        d = d + m
print(h, d, h * d)

# puzzle 2
h, d, a = 0, 0, 0
for v, m in lines:
    if v == "f":
        h = h + m
        d = d + a * m
    elif v == "u":
        a = a - m
    elif v == "d":
        a = a + m
print(h, d, h * d)
