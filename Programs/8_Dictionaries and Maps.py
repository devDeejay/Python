key = []
value = []
dictionary = {}
inputNames = []
n  = int(input())

#storing the keys and values in array first
for i in range (0,n):
    keys,values = input().split(" ")
    key.append(keys)
    value.append(values)

#iterating over the array and appending the details into the dictionary
for i in range (0,n):
    dictionary[key[i]] = {value[i]}

#storing the names in the array to be searched
for i in range(0,n):
    name = input()
    inputNames.append(name)


for i in range(0,n):
    for names in dictionary:
        flag = False
        if inputNames[i] == names:
            print(names + "=" + str(*dictionary[names]))
            flag = True
            break
    if flag == False:
        print("Not found")


'''
n = int(input())
name_numbers = [input().split() for _ in range(n)]
phone_book = {k: v for k,v in name_numbers}
while True:
    try:
        name = input()
        if name in phone_book:
            print('%s=%s' % (name, phone_book[name]))
        else:
            print('Not found')
    except:
        break
'''
