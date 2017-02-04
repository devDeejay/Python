s = input().strip()
#n = int(input().strip())
#for a0 in range(n):
    #x = int(input().strip())

letters = []
index = -1
repeated = []
count = 0
i = 0
while( i < len(s)):
    if index == -1:
        index += 1
        letters.insert(index, s[i])

    elif s[i] != letters[index]:
        index += 1
        letters.insert(index,s[i])

    elif s[i] == letters[index]:
        char = s[i]
        new = s[i]
        try:
            while(s[i+1] == s[i]):
                count += 1
                i+=1

        except:
            pass

        print(count)
        for c in range(0, count-1):
            char = new + char
            letters.insert(index,char)
            index += 1

    i += 1

print(letters)
