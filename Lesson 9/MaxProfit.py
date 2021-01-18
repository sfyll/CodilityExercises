def solution(A):
    maxEnding = maxSlice = 0
    delta = [A[i]-A[i-1] for i in range(1, len(A))]
    for a in delta:
        maxEnding = max(0, a + maxEnding)
        maxSlice = max(maxSlice, maxEnding)
    return maxSlice


"""solution below uses divide and conquer approach to maximum Sub-array problems and gets a score of
77% with 80% in correctness and 78% in Performance, but it is not the optimal way (both in terms of understanding
and easiness to code) to answer the task at hand"""

def solution(A):
    delta=list()
    for i in range(1, len(A)):
        delta.append(A[i]-A[i-1])
    low = 0
    high = len(delta)
    mid = len(delta)//2
    if high == (low+1):
        return(A[low-1])
    elif high == low:
        return 0
    else:
        leftSum = maxSubarray(delta, low, mid)
        rightSum = maxSubarray(delta, mid, high)
        crossSum = findMaxCrossingSubarray(delta, low, mid, high)
        if leftSum < 0 and rightSum < 0 and crossSum < 0:
            return 0
        if leftSum >= rightSum and leftSum >= crossSum:
            return leftSum
        elif rightSum >= leftSum and rightSum >= crossSum:
            return rightSum
        else:
            return crossSum
    
def maxSubarray(A, low, high):
    left_sum = -200001
    summ = 0
    for i in range(low, high):
        summ = summ + A[i]
        if summ > left_sum:
            left_sum = summ
    return left_sum
    
def findMaxCrossingSubarray(A, low, mid, high):
    left_sum = -200001
    summ = 0
    for i in range(mid, low, -1):
        summ = summ + A[i]
        if summ > left_sum:
            left_sum = summ
            max_left = i
    right_sum = -200001
    summ = 0
    for j in range(mid+1, high):
        summ = summ + A[j]
        if summ > right_sum:
            right_sum = summ
            max_right = j
    return(left_sum + right_sum)