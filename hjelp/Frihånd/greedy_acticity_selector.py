
a = []


def g_a_s(s, f):
    n = len(s)
    A = [a[-1]]
    i = 1
    for m in range(1, n):
        if s[m-1] >= f[i-1]:
            A = A.append(a[m-1])
            i = m
    return A

