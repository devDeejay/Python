def calculate(x):
    n = x
    count = 0
    for A in range(1,n):
        if((A ^ n) == (A + n)):
            count += 1
    print(count)

testCases = int(input())
for i in range(0,testCases):
    X = int(input())
    calculate(X)
