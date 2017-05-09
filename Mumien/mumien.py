from sys import stdin, stderr

Inf = float('Inf')


class Node:

    def __init__(self):
        self.prob = 0
        self.neighbours = []


def best_path(nm, prob):
    graph = make_graph(nm, prob)
    q = [node for node in graph]
    s = []
    while len(q) != 0:
        u = extract_max(graph, q)
        s.append(u)
        for v in u.neighbours:
            relax(u, v, graph)
    return s


def extract_max(graph, q):
    m = 0
    to_pop = None
    for node in q:
        if node.prob > m:
            print("Endring")
            m = node.prob
            to_pop = node
    q.remove(to_pop)
    return to_pop


def relax(u, v, graph):
    print(type(u))
    print(type(v))
    v = graph[v]

    if v.prob > u.prob * v.prob:  ######
        v.prob = u.prob * v.prob
        if u not in v.neighbours:
            v.neighbours.append(u)


def make_graph(nm, prob):
    nodes = len(nm)
    graph = [Node() for x in range(nodes)]
    c = 0
    for i in range(nodes):
        graph[i].prob = prob[i]
        j = i + 1
        while j <= nodes - 1:
            if nm[i][j] == 1:
                graph[i].neighbours.append(j)
                graph[j].neighbours.append(i)
            j += 1
    return graph


n = int(stdin.readline())
probabilities = [float(x) for x in stdin.readline().split()]
neighbour_matrix = []
for line in stdin:
    neighbour_row = [0] * n
    neighbours = [int(neighbour) for neighbour in line.split()]
    for neighbour in neighbours:
        neighbour_row[neighbour] = 1
    neighbour_matrix.append(neighbour_row)
print(best_path(neighbour_matrix, probabilities))