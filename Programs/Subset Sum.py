from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

nums = input("Enter the Elements").strip().split()
inputSum = int(input("Enter the Sum You want"))

for i, combo in enumerate(powerset(nums), 1):
    sum = 0
    for num in combo:
        sum += int(num)
    if sum == inputSum:
        print(combo)
