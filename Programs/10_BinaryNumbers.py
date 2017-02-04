binary = []
counts = []

num = int(input())
while(num!=0):
    q = int(num/2)
    remainder = int(num%2)
    binary.append(remainder)
    num = q

binary.reverse()
length = len(binary)

for i in range (0,length-1):
    if binary[i] == 1:
        count = 1
        counts.append(count)
        try:
            while(binary[i+1] == 1):
                count += 1
                counts.append(count)
                i+=1
        except:
            continue

print(max(counts))
