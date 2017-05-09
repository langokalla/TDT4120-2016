
def counting_sort(array):
    counted = count(array)
    modify(counted)
    places = ['']*(len(array))

    for n in array:
        i = counted[n]-1
        places[i] = n
        counted[n] -= 1

    return places


def modify(c):
    for i in range(1, len(c)):
        c[i] += c[i-1]


def count(array):
    m = max(array)
    c = [0]*(m+1)
    for x in array:
        c[x] += 1
    return c
