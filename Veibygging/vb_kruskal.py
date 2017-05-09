from sys import stdin


def mst(n, edges):
    mintree = kruskal(n, edges)
    return max([w for (w, f, t) in mintree])


def kruskal(n, edges):
    edges.sort()
    T = [x for x in range(n)]
    C = [[i] for i in range(n)]
    spanning_tree = []
    trees = n
    for (weight, u, v) in edges:
        Tu = T[u]
        Tv = T[v]
        if Tu != Tv:
            if len(C[Tu]) > len(C[Tv]):
                u, v = v, u
                Tu, Tv = Tv, Tu
            C[Tv] += C[Tu]
            for w in C[Tu]:
                T[w] = Tv
            C[Tu] = []
            spanning_tree.append((weight, u, v))
            trees -= 1
            if trees == 1:
                break
    return spanning_tree


edges = []
f = 0
for line in stdin:
    for k in line.split():
        data = k.split(':')
        t = int(data[0])
        weight = int(data[1])
        edges.append((weight, f, t))
    f += 1
print(mst(f, edges))
