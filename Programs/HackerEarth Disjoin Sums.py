n = int(input())
mainSet = input().strip().split()

a = []
b = []

mainSet.sort()

for i in range(0,len(mainSet)):
    nums = int(mainSet[i])
    if i%2 == 0:
        if nums in a:
         a.append(nums)

    elif i%2 != 0:
        b.append(nums)

aSum = 0
bSum = 0

for num in a:
    aSum += num

for num in b:
    bSum += num

Q = abs (1.0 - bSum / aSum)
print("{0:.6f}".format(round(Q,6)))
