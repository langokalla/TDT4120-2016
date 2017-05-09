from sys import stdin, stderr

from sys import stdin


def main():
    lines = stdin.readlines()
    n = int(lines[0])
    P = [float(x) for x in lines[1].split()]
    if n == 1:
        return '0'
    heap = [(P[0], 0, 0)]
    S = [False] * n
    previous = [x for x in range(n)]
    while heap:
        p, u, prev = heappop(heap)
        if S[u]:
            continue
        previous[u] = prev
        S[u] = True
        for v in reversed([int(x) for x in lines[2 + u].split()]):
            if v == n - 1:
                previous[v] = u
                if p * P[v] != 0.0:
                    return trace_path(previous)
                else:
                    return '0'
            heappush(heap,(p * P[v], v, u))
    return '0'


def trace_path(predecessors):
    index = len(predecessors) - 1
    path = []
    while index != 0:
        path.append(index)
        index = predecessors[index]
    path.append(0)
    return '-'.join(map(str, reversed(path)))


def heappop(heap):
    heap[0], heap[-1] = heap[-1], heap[0]
    x = heap.pop()
    n = len(heap)
    i = 0
    while True:
        l = 2 * i + 1
        r = l + 1
        if l < n:
            b = l
            if r < n and heap[r] > heap[l]:
                b = r
            if heap[b] > heap[i]:
                heap[b], heap[i] = heap[i], heap[b]
                i = b
            else:
                break
        else:
            break
    return x


def heappush(H, x):
    H.append(x)
    i = len(H) - 1
    while i > 0:
        p = (i-1) // 2
        if H[p] < H[i]:
            H[p], H[i] = H[i], H[p]
            i = p
        else:
            break


if __name__ == '__main__':
    m = main()
    print(m)
