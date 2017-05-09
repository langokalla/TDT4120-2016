from sys import stdin
""""
from random import randint


def sort_list(A):
    S = A.copy()
    qsort(S, 0, len(S)-1)
    return S

def qsort(A, a, b):
    while a < b:
        p = partition(A, a, b)
        if p - a < b - p:
            qsort(A, a, p - 1)
            a = p + 1
        else:
            qsort(A, p + 1, b)
            b = p - 1

def partition(A, a, b):
    piv_index = randint(a, b)
    piv = A[piv_index]
    A[piv_index], A[b] = A[b], piv
    i = a
    j = b - 1
    while i <= j:
        while A[i] <= piv and i <= j:
            i += 1
        while A[j] >= piv and j >= i:
            j -= 1
        if i < j:
            A[j], A[i] = A[i], A[j]
    A[b], A[i] = A[i], piv
    return i
"""
def sort_list(liste):
    n = len(liste)
    if len(liste) is 1:
        return liste

    l1 = liste[:int(n/2)]
    l2 = liste[int(n/2):]

    l1 = sort_list(l1)
    l2 = sort_list(l2)

    return merge(l1, l2)


def merge(l1, l2):
    l3 = []

    while (len(l1) != 0) and (len(l2) != 0):
        if l1[0] > l2[0]:
            l3.append(l2[0])
            del l2[0]
        else:
            l3.append(l1[0])
            del l1[0]

    while len(l1) != 0:
        l3.append(l1[0])
        del l1[0]

    while len(l2) != 0:
        l3.append(l2[0])
        del l2[0]

    return l3

def find(A, min, max):
    # Binary Search
    lower = binarySearch(A, min)
    upper = binarySearch(A, max)
    if A[lower] > min and lower != 0:
        lower -= 1
    if A[upper] < upper and upper != len(A) - 1:
        upper += 1
    return [A[lower], A[upper]]


def binarySearch(A, val):
    start = 0
    end = len(A) - 1
    m = 0
    while start <= end:
        m = (start + end) // 2
        if val == A[m]:
            break
        elif val < A[m]:
            end = m - 1
        else:
            start = m + 1
    return m


def main():
    input_list = []
    for x in stdin.readline().split():
        input_list.append(int(x))

    sorted_list = sort_list(input_list)

    for line in stdin:
        word = line.split()
        minimum = int(word[0])
        maximum = int(word[1])
        result = find(sorted_list, minimum, maximum)
        print(str(result[0]) + " " + str(result[1]))


if __name__ == "__main__":
    main()
