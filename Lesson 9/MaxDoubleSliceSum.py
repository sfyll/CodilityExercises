# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

'''Create two subarrays, one containing max sum of a subarray starting at this position, and one containing max of a subarray ending here, then simply sum the two by omitting one elements of the max beginning array'''

def solution(A):
    lenA = len(A)
    maxEnding = 0
    maxEndingList = [0] * lenA
    for idx in range(1, lenA-2):
        maxEnding = max(0, A[idx] + maxEnding)
        maxEndingList[idx] = maxEnding
    maxBeginning  = 0
    maxBeginningList = [0] * lenA
    for idx in range(lenA-2, 1, -1):
        maxBeginning = max(0, A[idx] + maxBeginning)
        maxBeginningList[idx] = maxBeginning
    maxDoubleSlice = 0
    for idx in range(0, lenA-2):
        maxDoubleSlice = max(maxDoubleSlice, maxEndingList[idx]+maxBeginningList[idx+2])
    return maxDoubleSlice