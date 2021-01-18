# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    n = len(A)
    lead = leader(A, n)
    if lead == -1:
        return -1
    else:
        count = 0
        for i in range(n):
            if (A[i] == lead):
                count +=1
                temp = i
        if (count > n//2):
            leadFinal = temp
            return leadFinal
        else:
            return -1
            
def leader(A, n):
    size = 0
    for i in range(n):
        if size == 0:
            size += 1
            value = A[i]
        else:
            if(value != A[i]):
                size -=1
            else:
                size +=1
    candidate = -1
    if size > 0:
        candidate = value
    return candidate