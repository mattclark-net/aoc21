# parse the input
with open("10-input.txt") as f:
    lines = [l.strip() for l in f.readlines()]

brackets = ("{}", "()", "<>", "[]")
opening = list(b[0] for b in brackets)
closing = dict((b[0], b[1]) for b in brackets)
points1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
points2 = {")": 1, "]": 2, "}": 3, ">": 4}

total1 = 0
completions = []
for l in lines:
    stack = []
    corrupted = False
    for i, c in enumerate(l):
        if c in opening:
            stack.extend(c)
        elif c == closing[stack[-1]]:
            stack.pop()
        else:
            total1 += points1[c]
            corrupted = True
            break
    if not corrupted:
        completions.append(stack)

print("Answer 1: {}".format(total1))

subtotals = []
for l in completions:
    subtotal = 0
    for c in reversed(l):
        subtotal = subtotal * 5 + points2[closing[c]]
    subtotals.append(subtotal)

print("Answer 2: {}".format(sorted(subtotals)[(len(subtotals) // 2)]))
