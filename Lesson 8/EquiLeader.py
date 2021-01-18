def solution(A):
    n = len(A)
    lead, count = leader(A,n)
    if lead == "NoDominator":
        return 0
    equileader = 0
    temp_count = 0
    for idx in range(n):
        if A[idx] == lead:
            temp_count +=1
        if (temp_count > (idx+1)//2) and (count-temp_count > ((n-idx-1)//2)):
            equileader +=1
    return equileader
    

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
    count = 0
    for k in range(n):
        if(A[k] == candidate):
            count +=1
        if(count>n // 2):
            leader = candidate
    if count<n // 2:
        return "NoDominator", count
    return leader, count