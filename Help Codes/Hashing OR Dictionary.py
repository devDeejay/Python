D = {}

D['a'] = 1
D['b'] = 2
D['c'] = 3

print(D)

# D[key] = value

for k in D.keys():
    print(k) #prints keys
    print(D[k]) #prints values


for k,v in D.items():
    print(str(k)+":"+str(v))

#Zipping values from two arrays into One
a = [1,2,3,4,5]
b = ['a','b','c','d','e']

hash = {k:v for k,v in zip(a,b)}
print(hash)

hash = {k:v for k,v in zip(b,a)}
print(hash)
