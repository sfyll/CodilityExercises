def solution(N):
    i = 1
    result = 0
    while(i*i<N):
        if(N%i == 0):
            result +=2
        i +=1
    if(i*i == N):
        result +=1
    return result