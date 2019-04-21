a = int(input())
b = int(input())
c = int(input())
if a % 2 == 0:
    if b % 2 == 0:
        if c % 2 == 0:
            print("NO")
        else:
            print("YES")
    else:
        print("YEs")
else:
    if b % 2 == 0:
        print("YES")
    else:
        if c % 2 == 0:
            print("YES")
        else:
            print("NO")
