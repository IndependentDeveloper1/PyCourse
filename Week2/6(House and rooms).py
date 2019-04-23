a = int(input())
b = int(input())
if a == 1:
    print("YES")
elif a == b:
    print("YES")
elif (a - 1) > (b - a):
    print("YES")
else:
    print("NO")
