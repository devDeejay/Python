def cube(n):
    return n**3

def generatorFunction(n):
    currentN = 1
    while currentN <= n :
        print(cube(currentN))
        currentN += 1

generatorFunction(10000)
