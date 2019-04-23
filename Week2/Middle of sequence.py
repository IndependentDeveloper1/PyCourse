now = int(input())
sumSeq = 0
countNum = 0
while now != 0:
    sumSeq += now
    countNum += 1
    now = int(input())
print(sumSeq / countNum)
