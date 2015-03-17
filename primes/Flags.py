# https://codility.com/demo/results/demoZEXVMU-YYH/

def solution(A):
    
    peaks = [i for i in range(1, len(A)-1) if A[i-1] < A[i] and A[i] > A[i+1]]
    if not peaks:
        return 0
    elif len(A) <= 3:
        return 1

    n = len(A)
    to = max([i for i in range(1, n) if i*(i-1) < n-1])
    for k in range(to, 0, -1):
        current = 1
        currentVal = peaks[0]
        count = 1
        while(current < len(peaks)):
            if peaks[current] >= currentVal + k:
                currentVal = peaks[current]
                count +=1
            current += 1 
            if count == k:
                return k;
    return 0

def test(expected, A):
    result = solution(A)
    if expected == result:
        print("Ok")
    else:
        print("Error: " + str(result))

test(3, [1, 6, 3, 6, 5, 6, 5, 6, 3, 2, 6, 1])
test(3, [1,5,3,4,3,4,1,2,3,4,6,2])
test(4, [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0])
test(5, [0, 0,0,0,0,0,1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0])