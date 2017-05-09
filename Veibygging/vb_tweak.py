from sys import stdin
from heapq import heappush, heappop
Inf = float(1e3000)


def mst(n, mat):
    unseen = [1]*n
    count = 1
    heaviest = 0
    heap_path = []
    min_path = [Inf]*n
    for i in mat[0]:
        heappush(heap_path, (mat[0][i], i))
        min_path[i] = mat[0][i]
    unseen[0] = 0
    while count < n:
        m, ind = heappop(heap_path)
        while not unseen[ind]:
            m, ind = heappop(heap_path)
        unseen[ind] = 0
        min_path[ind] = Inf
        heaviest = max(heaviest, m)
        for i in mat[ind]:
            if unseen[i]:
                if mat[ind][i]<min_path[i]:
                    min_path[i] = mat[ind][i]
                    heappush(heap_path, (mat[ind][i],i))
        count += 1
    return heaviest


def main():
    lines = stdin.readlines()
    n = len(lines)
    neighbour_matrix = [0] * n
    for i in range(n):
        neighbour_matrix[i]={}
    node = 0
    for line in lines:
        s = line.split()
        s.reverse()
        for k in s:
            neighbour, edge = k.split(':')
            neighbour = int(neighbour)
            if neighbour <= node:
                break
            edge = int(edge)
            neighbour_matrix[node][neighbour] = edge
            neighbour_matrix[neighbour][node] = edge
        node += 1
    print(mst(n, neighbour_matrix))

if __name__ == '__main__':
    main()