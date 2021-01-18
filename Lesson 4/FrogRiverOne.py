def solution(X, A):
    partial_sum = 0
    countingArray = [0] * (X+1)
    for idx in range(len(A)):
        if(countingArray[A[idx]] == 0):
            countingArray[A[idx]] +=1
            partial_sum+=1
            if (partial_sum == X):
                return idx
    return -1
        