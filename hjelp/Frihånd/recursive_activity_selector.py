

def r_a_s(s, f, i, n):
    global a
    m = i + 1
    while m <= n and s[m] < f[i]:
        m += 1
    if m <= n:
        print(a)
        return a.append(r_a_s(s, f, m, n))
    else:
        return []


def main():
    s = [12, 12, 6, 15, 20, 0, 4, 6]
    f = [14, 17, 10, 18, 24, 22, 7, 9]


    recs = 0
    ans = r_a_s(s, f, 0, len(s)-1)

if __name__ == '__main__':
    a = []
    main()
