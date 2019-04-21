a, b, c = int(input()), int(input()), int(input())
if a == b and a == c:
    print(3)
elif b == c:
    print(2)
elif a == c:
    print(2)
elif a == b:
    print(2)
else:
    print(0)
