s = input()
a = []
b = []
temp = []

for i in range(0,10):
    a.append(i)
    b.append(0)

hash = {k:v for k,v in zip(a,b)}

for i in s:
    temp.append(i)

for num in temp:
    hash[int(num)] += 1

for k,v in hash.items():
    print(str(k)+" "+str(v))
