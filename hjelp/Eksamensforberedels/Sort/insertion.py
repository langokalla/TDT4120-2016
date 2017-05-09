from random import randint
from time import sleep


def insertion_sort(A, p=False):
    if p is True:
        print(A)
        for j in range(1, len(A)):
            key = A[j]
            print('Key:', key)
            print()
            i = j - 1
            print(A)
            while i >= 0 and A[i] > key:
                print('ith = ', A[i])
                print()
                print('Move forward', A[i])
                A[i+1] = A[i]
                i -= 1
                print(A)
            print()
            print('Move key to', i+1)
            A[i+1] = key
            print(A)
    else:
        for j in range(1, len(A)):
            key = A[j]
            i = j - 1
            while i >= 0 and A[i] > key:
                A[i + 1] = A[i]
                i -= 1
            A[i + 1] = key
    return A


def make_list():
    l = []
    for x in range(10):
        n = randint(0, 100)
        while n in l:
            n = randint(0, 100)
        l.append(n)
    return l


A = make_list()
p = input('Run with print? y/n:')
print()
if p == 'y':
    print(insertion_sort(A, True))
else:
    print(insertion_sort(A))
