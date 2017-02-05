ans = []
TestCases = int(input())
count = 0
while(TestCases!=0):
    binary = []
    num = int(input())
    while(num!=0):
        q = int(num/2)
        remainder = int(num%2)
        binary.append(remainder)
        num = q

    count = 0
    for j in range(0,len(binary)):
        if binary[j] == 1:
            count += 1

    ans.append(count)


    TestCases = TestCases - 1

for i in range (0,len(ans)):
    print(ans[i])
