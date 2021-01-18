"""create list with each value representing when will be the next pick, then use the latter
to test several combinations of flags until you find the one where you can take the max! (note
that in the problem statement they only ask the max # of flags and don't care if this was achieve
using x or x+1 tops or whatever"""


def solution(A):
    n = len(A)
    nextPicLoc = (nextPick(getPicks(A)))
    i = 1
    flags = 0
    while(i-1) * i <= n:
        position = 0
        number = 0
        while position < n and number < i:
            position = nextPicLoc[position]
            if position == -1:
                break
            number += 1
            position += i
        flags = max(flags, number)
        i+=1
    return flags
    
    
def getPicks(A):
    pickLocations = [False] * len(A)
    for idx in range(1, len(A)-1):
        if A[idx-1] < A[idx] and A[idx] > A[idx+1]:
            pickLocations[idx] = True
    return pickLocations

def nextPick(pickLocations):
    n = len(pickLocations)
    nextPickLocations = [0] * n
    nextPickLocations[n-1] = -1
    for idx in range(n-2, -1, -1):
        if pickLocations[idx]:
            nextPickLocations[idx] = idx
        else:
            nextPickLocations[idx] = nextPickLocations[idx+1]
    return nextPickLocations