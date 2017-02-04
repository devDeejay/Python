def cube(n):
    return n**3

def generatorFunction(n):
    currentN = 1
    while currentN <= n :
        yield cube(currentN)
        currentN += 1

generatedValues = generatorFunction(10)
print([i for i in generatedValues])
