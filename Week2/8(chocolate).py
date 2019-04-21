m = int(input())
n = int(input())
k = int(input())
if (m * n) % k == 0:
    print("YES")
elif (m * k) % ((m * n) % k) == 0:
    print("YES")
elif (k % n == 0) or (k % m == 0):
    print("YES")
else:
    print("NO")
