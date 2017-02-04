n = int(input())
numberOfPointsInEachLine = []

for i in range(1,n+1):
    numberOfPointsInEachLine.append(2*i-1)

print(*numberOfPointsInEachLine)

diffInNumberOfPoints = []

for i in range (0,n):
   diff = numberOfPointsInEachLine[i] - n;
   diffInNumberOfPoints.append(diff)

print(diffInNumberOfPoints)

sum = 0
for i in range (0,n):
    temp = diffInNumberOfPoints[i]
    if(temp > 0):
        sum =+ temp
    else:
        continue

print(sum)
