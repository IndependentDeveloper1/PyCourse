n = int(input())
edt = 1
degree = 0
while edt <= n:
    if edt == n:
        print("YES")
        exit()
    else:
        edt *= 2
        degree += 1
print("NO")
