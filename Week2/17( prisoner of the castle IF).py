a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
if d > e:
    (d, e) = (e, d)
if a > b:
    if a > c:
        if b < c:
            (b, c) = (c, b)
        (a, c) = (c, a)
    else:
        if b < c:
            (a, b) = (b, a)
elif b > c:
    if a < c:
        (b, c) = (c, b)
    else:
        (a, c) = (c, a)
        (b, c) = (c, b)
if (a <= d and b <= e) or (a <= e and b <= d):
    print("YES")
else:
    print("NO")
