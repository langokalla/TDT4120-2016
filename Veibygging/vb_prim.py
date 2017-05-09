from sys import stdin

Inf = float(1e3000)


def mst(nm):
    min_tree = prim(nm)
    most_expensive = 0
    for (f, t) in min_tree:
        most_expensive = max(most_expensive, nm[f][t])
    return most_expensive


def prim(nm):
    nodes = len(nm)
    tree = []
    best_neigh = [None]*nodes
    best_price = [Inf]*nodes
    not_visited = [x for x in range(1, nodes)]
    prev = 0
    next_to = None
    while len(not_visited) > 0:
        for i in not_visited:
            if nm[i][prev] < best_price[i]:
                best_neigh[i] = prev
                best_price[i] = nm[i][prev]
        min_price = Inf
        for i in not_visited:
            if best_price[i] < min_price:
                min_price = best_price[i]
                next_from = i
                next_to = best_neigh[i]
        tree.append((next_from, next_to))
        not_visited.remove(next_from)
        prev = next_from
    return tree


lines = []
for s in stdin:
    lines.append(s)
n = len(lines)
neighbour_matrix = [None] * n
node = 0
for line in lines:
    neighbour_matrix[node] = [Inf] * n
    for k in line.split():
        data = k.split(':')
        neighbour = int(data[0])
        weight = int(data[1])
        neighbour_matrix[node][neighbour] = weight
    node += 1
print(mst(neighbour_matrix))