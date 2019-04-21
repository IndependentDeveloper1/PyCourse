a = int(input())
b = int(input())
c = int(input())
cosA = (pow(a, 2) + pow(b, 2) - pow(c, 2)) / (2 * a * b)
cosB = (pow(a, 2) + pow(c, 2) - pow(b, 2)) / (2 * a * c)
cosG = (pow(b, 2) + pow(c, 2) - pow(a, 2)) / (2 * b * c)
if (a + b) > c and (b + c) > a and (a + c) > b:
    if cosA == 0 or cosB == 0 or cosG == 0:
        print("rectangular")
    elif cosA < 0 or cosB < 0 or cosG < 0:
        print("obtuse")
    else:
        print("acute")
else:
    print("impossible")
