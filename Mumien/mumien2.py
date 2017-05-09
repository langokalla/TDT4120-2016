from sys import stdin, stderr


def best_path(nm, prob):
    n = len(prob)
    visited = [False]*n
    cumulative_prob = [0.0]*n
    cumulative_prob[0] = prob[0]
    prev = [x for x in range(n)]
    best_node = 0
    for i in range(n):
        node = best_node
        visited[node] = True
        highest_c_prob = -1.0
        for neigh in range(n):
            if not visited[neigh]:
                if nm[node][neigh]:
                    offer = cumulative_prob[node] * prob[neigh]
                    if offer > cumulative_prob[neigh]:
                        prev[neigh] = node
                        cumulative_prob[neigh] = offer
                    if cumulative_prob[neigh] > highest_c_prob:
                        best_node = neigh
                        highest_c_prob = cumulative_prob[neigh]
    if cumulative_prob[-1] == 0.0:
        return '0'
    index = n - 1
    path = []
    while index != 0:
        path.append(index)
        index = prev[index]
    path.append(0)
    return '-'.join(map(str, reversed(path)))


def main():
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


if __name__ == '__main__':
    main()