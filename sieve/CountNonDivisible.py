# you can use print for debugging purposes, e.g.
# print "this is a debug message"
import math
# https://codility.com/demo/results/demoR5PGME-DST/
def solution(A):
    
    result = {i:len(A) for i in A}
    count = {i:0 for i in A}
    for i in A: count[i] += 1
   
    maxVal = max(A)
    for i in set(sorted(A)):
        j = i
        while(j <= maxVal):
            if j in result:
                result[j] = result[j] - count[i]
            j += i
    
    return [result[i] for i in A]
   
    


def test(expected, A):
    print("in: " + str(A))
    result = solution(A)
    if expected == result:
        print("Ok")
    else:
        print("Error: " + str(result) + " expected: " + str(expected))

test([2, 4, 3, 2, 0], [3, 1, 2, 3, 6])
