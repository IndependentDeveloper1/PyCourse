x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 > 0 and y1 > 0:
    if x2 > 0 and y2 > 0:
        print("YES")
    else:
        print("NO")
elif x1 > 0 and y1 < 0:
    if x2 > 0 and y2 < 0:
        print("YES")
    else:
        print("NO")
elif x1 < 0 and y1 > 0:
    if x2 < 0 and y2 > 0:
        print("YES")
    else:
        print("NO")
else:
    if x2 < 0 and y2 < 0:
        print("YES")
    else:
        print("NO")
