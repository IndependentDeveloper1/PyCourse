k, m, n = int(input()), int(input()), int(input())
time = 0
if k >= n:
    time = 2 * m * n
    print(time)
else:
    while k <= n:
        time += (m * 2)
        n -= k

    print(time)
