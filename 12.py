# parse the input
with open("12-input.txt") as f:
    raw_edges = [l.strip() for l in f.readlines()]

# make a full bidirectional list of nodes - this will have some things in it we need to remove
nodes = dict()
for e in raw_edges:
    (n1, n2) = e.split("-")
    try:
        nodes[n1].append(n2)
    except KeyError:
        nodes[n1] = [n2]
    try:
        nodes[n2].append(n1)
    except KeyError:
        nodes[n2] = [n1]

# remove edges pointing back to start, and remove end as a start node for any edges
nodes.pop("end")
for n1, n2list in nodes.items():
    try:
        n2list.remove("start")
        nodes[n1] = n2list
    except ValueError:
        pass

smallnodes = [k for k in nodes.keys() if k.islower() and k != "start"]


def explore(pathlist, q=1):
    # if all paths lead to 'end' we are done, just return the list
    endings = [n[-1] for n in pathlist]
    if endings.count("end") == len(pathlist):
        return pathlist

    nextpaths = []
    for path in pathlist:
        if path[-1] == "end":
            # keep all the current solutions
            nextpaths.append(path)
        else:
            # explore each possible next node
            for nextnode in nodes[path[-1]]:
                if nextnode == "end":
                    # easy, we have a complete path, just add it to the list
                    nextpaths.append(path + ["end"])
                else:
                    if nextnode not in smallnodes:
                        # it's a big node, so can be added without any checks
                        nextpaths.append(path + [nextnode])
                    else:
                        # It's a small node, so check it's not already in the path
                        if q == 1:
                            if nextnode not in path:
                                nextpaths.append(path + [nextnode])
                        elif q == 2:
                            if nextnode not in path:
                                nextpaths.append(path + [nextnode])
                            # or that we don't already have a small node twice, if the question is q2
                            elif max([path.count(n) for n in smallnodes]) < 2:
                                nextpaths.append(path + [nextnode])
    return explore(nextpaths, q)


paths = [["start"]]
paths = explore(paths, q=1)
print("\nQ1 found", len(paths), "paths")

paths = [["start"]]
paths = explore(paths, q=2)
print("Q2 Found", len(paths), "paths")
