# you can use print for debugging purposes, e.g.
# print "this is a debug message"
import math
# https://codility.com/demo/results/demoYN29JM-43V/
def solution(N, P, Q):
    
    sieve = [0 for i in range(N + 1)]
    
    for i in [i for i in range(2, len(sieve)) if i * i < len(sieve)]:
        k = i * i
        while(k < len(sieve)):
            if not sieve[k]:
                sieve[k] = i
            k += i
            
    prefixFactorial = []
    count = 0
    for i in range(0, len(sieve)):
        stepsUntilPrime = 0
        j = i
        while(sieve[j]):
            j /= sieve[j]
            stepsUntilPrime += 1
        if stepsUntilPrime == 1:
            count += 1
        prefixFactorial.append(count)
            
    result = []
    for p, q in zip(P, Q):
        result.append(prefixFactorial[q] - prefixFactorial[p-1])
    
    return result


def test(expected, N, P, Q):
    result = solution(N, P, Q)
    if expected == result:
        print("Ok")
    else:
        print("Error: " + str(result))

test([10, 4, 0], 26, [1, 4, 16], [26, 10, 20])
test([10], 26, [1], [26])
