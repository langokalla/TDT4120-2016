from sys import stdin
from math import log

Inf = float('Inf')


def mst(struct):
    min_tree = prim_heap(struct)
    most_expensive = 0
    for (f, t, price) in min_tree:
        most_expensive = max(most_expensive, price)
    return most_expensive


def prim_heap(nl, start = 0):
    n = len(nl)
    tree = []
    heap = [None]*n
    for i in range(n):
        heap[i] = [Inf, i, None]  # [pris, node, nabo]
    heap[start][0] = 0
    pos = [x for x in range(n)]
    heapify(heap, pos)
    for i in range(n):
        (price, node, parent) = heappop(heap, pos)
        tree.append((parent, node, price))
        for (child, price) in nl[node]:
            pc = pos[child]
            if pc is not None and price < heap[pc][0]:
                heap[pc][0] = price
                heap[pc][1] = node
                heaphoist(heap, pos, pc)
    tree.pop(0)
    return tree


def heapify(heap, pos):
    for i in range(len(heap) // 2 - 1, -1, -1):
        heapfall(heap, pos, i)


def heappop(heap, pos):
    heap[0], heap[-1] = heap[-1], heap[0]
    pos[heap[0][1]] = 0
    pos[heap[-1][1]] = None
    ret = heap.pop()
    if len(heap) > 1:
        heapfall(heap, pos, 0)
    return ret


def heapfall(heap, pos, i):
    minv = heap[i]
    mini = i
    il = i * 2 + 1
    ir = il + 1
    if il < len(heap) and heap[il] < minv:
        minv = heap[il]
        mini = il
    if ir < len(heap) and heap[ir] < minv:
        minv = heap[ir]
        mini = ir
    if mini != i:
        heap[i], heap[mini] = heap[mini], heap[i]
        pos[heap[i][1]], pos[heap[mini][1]] = pos[heap[mini][1]], pos[heap[i][1]]
        heapfall(heap, pos, mini)


def heaphoist(heap, pos, i):
    if i == 0:
        return
    p = (i - 1) / 2
    if heap[i] < heap[p]:
        pos[heap[i][1]] = p
        pos[heap[p][1]] = i
        heap[i], heap[p] = heap[p], heap[i]
        heaphoist(heap, pos, p)


def main():
    linjer = []
    for linje in stdin:
        linjer.append(linje)

    naboliste = []
    for linje in linjer:
        kanter = linje.split()
        naboer = []
        for k in kanter:
            data = k.split(':')
            nabo = int(data[0])
            vekt = int(data[1])
            naboer.append( (nabo, vekt) )
        naboliste.append(naboer)
    pris = mst(naboliste)
    print(pris)

if __name__ == '__main__':
    main()
