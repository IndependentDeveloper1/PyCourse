n = int(input())
div = 2
while div <= n:
    if n % div == 0:
        print(div)
        break
    else:
        div += 1
