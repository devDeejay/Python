A = []
T = int(input())
for t in range (0,T):
    S = input()
    A.append(S)

for strings in A:
    E = ""
    O = ""
    for i in range(0,len(strings)):
        if(i%2 == 0):
            E+= strings[i]
        else:
            O+= strings[i]

    print(E + " " + O)
