

def solution(N, P, Q):
    answer = list()
    if N == 1:
        for idx in range(len(P)):
            answer.append(0)
        return answer
    primes = sieves(N)
    semiPrimesList = semiPrimes(primes, N)
    prefSumArr = prefixSum(semiPrimesList)
    for idx, values in enumerate(P):
        answer.append(prefSumArr[Q[idx]] - prefSumArr[values-1])
    return answer

#construct array of primes up to N/2
def sieves(N):
    sieve = [True] * ((N+2)//2)
    sieve[0] = sieve[1] = False
    i = 2
    while (i * i <= ((N+1)//2)):
        if(sieve[i]):
            k = i*i
            while(k<=((N+1)//2)):
                sieve[k] = False
                k += i
        i +=1
    return sieve

#construct array of semiprimes up to N
def semiPrimes(sieve, N):
    semiPrimes = [0] * (N+1)
    i = 2
    while(i*i <= N):
        if(sieve[i]):
            secondMultiplicator = i
            while(secondMultiplicator <= N//2 and i * secondMultiplicator <= N):
                if(sieve[secondMultiplicator]):
                    semiPrimes[secondMultiplicator * i] = True
                    secondMultiplicator += 1
                else:
                    secondMultiplicator +=1
        i += 1
    return semiPrimes

#create a prefixsum array of semiprimes up to N
def prefixSum(semiPrimesList):
    lenSemis = (len(semiPrimesList))
    prefixSumArray = [0] * lenSemis
    for i in range(lenSemis):
        if(semiPrimesList[i]):
            prefixSumArray[i] = prefixSumArray[i-1] + 1
        else:
            prefixSumArray[i] = prefixSumArray[i-1]
    return prefixSumArray