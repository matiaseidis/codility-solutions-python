from sets import Set
# https://codility.com/demo/results/demoWMGSTH-TAK/
def solution(A):

    result = 0
    
    if len(A) < 3:
        return result
    
    # peak_counts = list(cumsum([False] * 2 + [c > p and c > n for c, p, n in zip(A[1:-1], A[:-1], A[2:])] + [False]))
    peaks = [i for i in range(1, len(A)-1) if A[i-1] < A[i] and A[i] > A[i+1]]
    
    if not peaks:
        return result
    
    peaksPrefixSum = [0]
    current = 0
    
    for i in range(1, len(A)-1):
        if A[i-1] < A[i] and A[i] > A[i+1]:
            current += 1
        peaksPrefixSum.append(current)
    peaksPrefixSum.append(current)
    
    divisors = Set([1, len(A)])
    last = 2
    while(last <= len(A)):
        if len(A) % last == 0:
            divisors.add(last)
            divisors.add(len(A) / last)
        last += 1
    
    for i, v in enumerate(divisors):
        step = len(A) / v
        ini = 0
        end = step
        count = 0
        allChunksWithPeak = True
        while(end <= len(A) and allChunksWithPeak):
            allChunksWithPeak = count < peaksPrefixSum[end-1]
            count = peaksPrefixSum[end-1]
            end += step
            ini += step
        
        if allChunksWithPeak and v > result:
            result = v        
            
    return result


#solution([0, 1000000000])
print("result: " + str(1 == solution([1, 2, 3, 4, 6, 5])))
print("result: " + str(3 == solution([1,2,3,4,3,4,1,2,3,4,6,2])))  
print("result: " + str(7 == solution([0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0])))
print("result: " + str(4 == solution([5, 6, 5, 6, 1, 1, 1, 1, 6, 5, 6, 5])))
print("result: " + str(4 == solution([1, 6, 1, 1, 1, 1, 1, 6, 1, 1, 1, 1, 1, 1, 1, 1, 6, 1, 1, 1, 1, 1, 6, 1])))
