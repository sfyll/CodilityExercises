def solution(A):
    lenA = len(A)
    answerArray = [0] * (1000001)
    sumvals = 0
    for idx in range(lenA):
        if(A[idx] >= 0 and answerArray[A[idx]] == 0):
            answerArray[A[idx]] = A[idx]
            sumvals+= A[idx]
        else:
            pass
    if(lenA == 1 and (0 <= A[0] <=1 )):
        return A[-1] + 1
    if(lenA == 1 and A[0] > 1):
        return 1
    if(sumvals == 0):
        return 1
    if(lenA == 2 and A[0]+1 < A[1]):
        return answerArray[0]+1
    answerArray.pop(0)
    for idx in range(len(answerArray)):
        if answerArray[idx] == 0:
            return answerArray[idx-1]+1
    return answerArray[-1]+1