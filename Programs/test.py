import itertools
count = total = 0
N = 7
for pair in itertools.combinations([i for i in range(1,N)],2):
    total += 1
for pair in itertools.combinations([i for i in range(1,N)],2):
    if(pair[1] ^ pair[0]) > 6:
        count += 1

print(total - count)
