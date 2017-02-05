'''
Gudi, a fun loving girl from the city of Dun, travels to Azkahar - a strange land beyond the mountains. She arrives at the gates of Castle Grey, owned by Puchi,the lord of Azkahar to claim the treasure that it guards. However, destiny has other plans for her as she has to move through floors, crossing obstacles on her way to reach the treasure.
The gates of the castle are closed. An integer N is engraved on the gates. A writing on the wall says

Tap the gates as many times as there are unordered pairs of distinct integers from 1 to  N
N whose bit-wise XOR does not exceed  N
'''
import itertools

def Calculate(num):
    count = 0
    total = 0
    N = num

    for pair in itertools.combinations([i for i in range(1,N+1)],2):
        if(pair[1] ^ pair[0]) <= N:
            count += 1

    return count

TestCase = int(input())
while(TestCase != 0):
    temp = int(input())
    print(Calculate(temp))
    TestCase -= 1
