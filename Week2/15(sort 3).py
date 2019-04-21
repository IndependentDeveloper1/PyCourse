a, b, c = int(input()), int(input()), int(input())
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
print(a, b, c)
