import sys
import cmath

def addC(l,r,c):
    for i in range(l,r+1):
        box[i] += c

def replace(l,r,d):
    for i in range(l,r+1):
        box[i] = box[i]//d

def minNumber(l,r):
    min = box[l]
    for i in range(l,r+1):
        if box[i] < min:
            min = box[i]
    print(min)

def sumOfAll(l,r):
    sum = 0
    for i in range(l,r+1):
        sum += box[i]
    print(sum)


n,q = input().strip().split(' ')
n,q = [int(n),int(q)]
box = list(map(int, input().strip().split(' ')))
query = []
for k in range(0,q):
    query.append(input())

def call():
    if code[0] == '1':
        case = int(code[0])
        l = int(code[1])
        r = int(code[2])
        c = int(code[3])
        addC(l, r, c)

    elif code[0] == '2':
        case = int(code[0])
        l = int(code[1])
        r = int(code[2])
        d = int(code[3])
        replace(l, r, d)

    elif code[0] == '3':
        case = int(code[0])
        l = int(code[1])
        r = int(code[2])
        minNumber(l, r)

    elif code[0] == '4':
        case = int(code[0])
        l = int(code[1])
        r = int(code[2])
        sumOfAll(l,r)

for k in  range(0,q):
    code = query[k].strip().split(' ')
    call()
