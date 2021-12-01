with open("1-input.txt") as f:
    input = [int(l) for l in f.readlines()]
print(input)

# puzzle 1
m = 0
for (a, b) in zip(input, input[1:]):
    if b > a:
        m += 1
print(m)

# puzzle 2
m = 0
windows = [a * b * c for a, b, c in zip(input, input[1:], input[2:])]
for (a, b) in zip(windows, windows[1:]):
    if b > a:
        m += 1
print(m)
