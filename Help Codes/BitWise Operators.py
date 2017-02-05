from operator import xor
a = 12
b = 11
print(xor(bool(a),bool(b)))

xor = bool(a) + bool(b) == 1
print(xor)


a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
c = 0

c = a & b;        # AND 12 = 0000 1100
print("Line 1 - Value of c is ", c)

c = a | b;        # OR 61 = 0011 1101
print ("Line 2 - Value of c is ", c)

c = a ^ b;        # XOR 49 = 0011 0001
print ("Line 3 - Value of c is ", c)

c = ~a;           # NEGATION -61 = 1100 0011
print ("Line 4 - Value of c is ", c)

c = a << 2;       # LEFTSHIFT 240 = 1111 0000
print ("Line 5 - Value of c is ", c)

c = a >> 2;       # RIGHT SHIFT 15 = 0000 1111
print ("Line 6 - Value of c is ", c)
