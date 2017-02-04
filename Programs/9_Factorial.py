def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

inputNumber = int(input())
f = factorial(inputNumber)
print(str(f))
