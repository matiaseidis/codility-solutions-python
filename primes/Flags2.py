import math

# https://codility.com/demo/results/demoCKYU9W-33T/
# this version is really O(N)

def binarySearch(peaks, current, k):
    left = current
    right = len(peaks)
    mid = 0
    next_valid = 0
    while(left <= right and left < len(peaks)):
        mid = (left + right) / 2
        next_valid = peaks[current] + k
        if peaks[mid] > next_valid:
            right = mid - 1
        elif peaks[mid] < next_valid:
            left = mid + 1
        else: 
            return mid
    
    return left


def solution(A):
    peaks = [i for i in range(1, len(A) - 1) if A[i - 1] < A[i] and A[i] > A[i + 1]]
    if not peaks:
        return 0
    elif len(A) <= 3:
        return 1
    
    return fromPeaks(peaks, len(A))
    
def fromPeaks(peaks,  n):
    to = max([i for i in range(1, n) if i * (i - 1) < n - 1])
    for k in range(to, 0, -1):
        current = 0
        flags = 1
        for i in range(k): 
            current = binarySearch(peaks, current, k)
            if current < len(peaks): 
                flags += 1
                if flags == k:
                    return k
            else: 
                break
    
    return 0     

peakss = [12, 17, 24, 41, 48, 75, 93, 99, 109, 131, 133, 143, 160, 166, 169, 176, 194, 201, 203, 205, 209, 216, 228, 232, 238, 242, 268, 280, 291, 294, 314, 319, 324, 329, 331, 340, 343, 347, 353, 364, 370, 396, 406, 415, 438, 458, 461, 467, 478, 485, 488, 503, 530, 534, 548, 561, 590, 611, 619, 632, 651, 658, 665, 669, 698, 713, 717, 726, 754, 764, 771, 773, 776, 779, 783, 792, 810, 832, 836, 853, 859, 866, 868, 870, 879, 881, 887, 891, 894, 910, 917, 923, 931, 938, 944, 948, 973, 977, 982, 984]

print(str(fromPeaks(peakss, 1000)))
