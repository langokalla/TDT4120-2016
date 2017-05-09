from random import randint

A = [5, 1, 6, 8, 3, 2, 7, 3]


def qsort(A, a, b):
    while a < b:
        p = partition(A, a, b)
        if p - a < b - p:
            qsort(A, a, p-1)
            a = p + 1
        else:
            qsort(A, p+1, b)
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


def main():
    A = [12, 90, 5, 18, 140, 130, 143, 70]
    print(A)
    qsort(A, 0, len(A) - 1)
    print(A)


if __name__ == "__main__":
    main()
