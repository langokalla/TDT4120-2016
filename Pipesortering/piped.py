from sys import stdin
from random import randint


def qsort(A, a, b):
    while a < b:
        p = partition(A, a, b)
        if p - a < b - p:
            qsort(A, a, p - 1)
            a = p + 1
        else:
            qsort(A, p + 1, b)
            b = p - 1
    return A


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


def find(A, nedre, ovre):
    indeks_nedre = binsok(A, nedre)
    indeks_ovre = binsok(A, ovre)
    if A[indeks_nedre] > nedre and indeks_nedre != 0:
        indeks_nedre -= 1
    if A[indeks_ovre] < ovre and indeks_ovre != len(A) - 1:
        indeks_ovre += 1
    return [A[indeks_nedre], A[indeks_ovre]]


def binsok(A, verdi):
    l = 0
    r = len(A) - 1
    while l <= r:
        m = (l + r) // 2
        if verdi == A[m]:
            break
        elif verdi < A[m]:
            r = m - 1
        else:
            l = m + 1
    return m

def main():
    input_list = []
    for x in stdin.readline().split():
        input_list.append(int(x))

    sorted_list = qsort(input_list, 0, len(input_list)-1)

    for line in stdin:
        word = line.split()
        minimum = int(word[0])
        maximum = int(word[1])
        result = find(sorted_list, minimum, maximum)
        print(str(result[0]) + " " + str(result[1]))


if __name__ == "__main__":
    main()

