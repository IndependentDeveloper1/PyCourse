x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == 0 or abs(x1 - x2) == 1:
    if abs(y1 - y2) == 0 or abs(y1 - y2) == 1:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
