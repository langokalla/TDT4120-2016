# Top-down
def top_down_fib(n):
    mem = {0: 1, 1: 1}
    if n in mem.keys():
        return mem[n]
    f = top_down_fib(n-1) + top_down_fib(n-2)
    mem[n] = f
    print(mem)
    return f


# Bottom-up
def bottom_up_fib(n):
    fibs = []
    for i in range(n+1):
        if i <= 1:
            fibs.append(1)
        else:
            fibs.append(fibs[i-1] + fibs[i-2])
        print(fibs)
    return fibs[-1]


def main():
    mem = {0: 1, 1: 1}
    top_down_fib(5)
    print('\n')
    bottom_up_fib(5)


if __name__ == '__main__':
    main()
