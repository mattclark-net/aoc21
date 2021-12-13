# parse the input
with open("13-input.txt") as f:
    lines = [l.strip() for l in f.readlines()]

dots = []
folds = []
for l in lines:
    if "," in l:
        dots.append([int(c) for c in l.split(",")])
    elif "=" in l:
        a, n = l.split(" ")[2].split("=")
        folds.append((a, int(n)))
print(dots)
print(folds)


def folded(dotlist, axis, line):
    folded_list = []
    for d in dotlist:
        newdot = d
        if axis == "x" and newdot[0] > line:
            newdot[0] = line - (newdot[0] - line)
        elif axis == "y" and newdot[1] > line:
            newdot[1] = line - (newdot[1] - line)
        folded_list.append(newdot)
    return folded_list


for f in [folds[0]]:
    folded_dots = folded(dots, f[0], f[1])
unique = set([tuple(d) for d in folded_dots])
print("Answer 1:", len(unique))

for f in folds:
    folded_dots = folded(dots, f[0], f[1])
unique = set([tuple(d) for d in folded_dots])

w = max([u[0] for u in unique]) + 1
h = max([u[1] for u in unique]) + 1
grid = [[" " for x in range(w)] for y in range(h)]
for u in unique:
    grid[u[1]][u[0]] = "#"

print("Answer 2:")
for r in grid:
    print("".join(r))
