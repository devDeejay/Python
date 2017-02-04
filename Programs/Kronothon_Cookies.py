n = int(input())
numberOfPointsInEachLine = []
diffInNumberOfPoints = []
for i in range(1, n+1):
    numberOfPointsInEachLine.append(2*i-1)

print(numberOfPointsInEachLine)
for i in range(0, n):
    diff = numberOfPointsInEachLine[i] - n
    diffInNumberOfPoints.append(diff)
answer = 0
for values in diffInNumberOfPoints:
    if values > 0:
        answer = answer + values
print("output "+ str(answer))
