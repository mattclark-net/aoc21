# parse the input
with open("7-input.txt") as f:
    positions = [int(n) for n in f.readline().split(",")]

distances = [0] * (max(positions) + 1)
for p in range(max(positions) + 1):
    for c in positions:
        distances[p] += abs(c - p)

print(min(distances))

distances = [0] * (max(positions) + 1)
for p in range(max(positions) + 1):
    for c in positions:
        steps = abs(c - p)
        distances[p] += steps * (steps + 1) / 2

print(min(distances))
