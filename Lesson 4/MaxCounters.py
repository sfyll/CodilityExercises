"""Instead of updating array values each time we have an element == N+1, remember the "baseline value"
and update only at the end in one loop"""

def solution(N, A):
    array = [0] * (N)
    maximum = 0
    baseline = 0
    for elements in A:
        if (elements == N+1):
            baseline = maximum
        else:
            if(array[elements-1] < baseline):
                array[elements-1] = baseline +1
                if(array[elements-1] > maximum):
                    maximum = array[elements-1]
            else:
                array[elements-1] +=1
                if(array[elements-1] > maximum):
                    maximum = array[elements-1]
    for idx in range(N):
        if array[idx] < baseline:
            array[idx] = baseline
    return(array)