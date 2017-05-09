def merge_sort(liste):
    n = len(liste)
    if len(liste) is 1:
        return liste

    l1 = liste[:int(n/2)]
    l2 = liste[int(n/2):]

    l1 = merge_sort(l1)
    l2 = merge_sort(l2)

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


print(merge_sort([5,3,2,4,6,8,9,1,7]))