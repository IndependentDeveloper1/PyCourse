a = int(input())
b = int(input())
print("YES" * (a % b == 0), "NO" * (a % b != 0), sep="")
