x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
a = (abs(x1 - y1) % 2 == 0)
b = (abs(x2 - y2) % 2 == 0)
if (a == b):
    print("YES")
else:
    print("NO")
