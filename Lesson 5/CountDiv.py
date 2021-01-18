def solution(A, B, K):
    return numberofmultiples(B,K) - numberofmultiples(A-1,K)
def numberofmultiples(x,y):
    return x//y