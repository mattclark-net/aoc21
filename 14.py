class intdict(dict):
    # to avoid importing defaultdict
    def __missing__(self, k):
        self[k] = 0
        return 0


# parse the input
with open("14-input.txt") as f:
    lines = [l.strip() for l in f.readlines()]

template = [l for l in lines[0]]
template = (
    ["_"] + template + ["_"]
)  # create a "virtual pair" at each end - seems neater than adding one back on to the counts later
rules = dict(((l[0], l[1]), l[-1]) for l in lines[2:])

pair_counts = intdict()
for i in range(len(template) - 1):
    pair_counts[(template[i], template[i + 1])] += 1

print(template)
print(pair_counts)


def new_counts(current_counts):
    new_pair_counts = intdict()
    for pair, count in current_counts.items():
        if pair in rules.keys():
            new_char = rules[pair]
            left = (pair[0], new_char)
            right = (new_char, pair[1])
            new_pair_counts[left] += count
            new_pair_counts[right] += count
        else:
            new_pair_counts[pair] = count
    return new_pair_counts


def runfor(iterations):
    counts = pair_counts.copy()
    for i in range(iterations):
        counts = new_counts(counts)
    char_counts = intdict()
    for k, v in counts.items():
        char_counts[k[0]] += v
        char_counts[k[1]] += v
    char_counts.pop("_")
    print(char_counts)

    print(
        "Answer",
        iterations,
        ":",
        max(char_counts.values()) // 2 - min(char_counts.values()) // 2,
    )


runfor(10)
runfor(40)
