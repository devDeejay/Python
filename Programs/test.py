s = input()
a = []
b = []
temp = []

for i in range(0,10):
    a.append(i)
    b.append(0)

print(a)
print(b)

hash = {k:v for k,v in zip(a,b)}

for i in s:
    temp.append(i)

print(temp)
