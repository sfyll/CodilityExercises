"""Non optimal (in terms of performance). working 100% sol ==> unnest the loop, but the idea remains the same
i.e. compute the frequency of occurence of each element, then their divisors and just substract your
answer the the length of the array"""

def solution(A):
    divisorDic = dict()
    lenA = len(A)
    if lenA < 2:
        return [0]
    #construct a list of every integer present in A
    intList = integerList(A)
    counter = 0
    answer = list()
    #loop through the list
    for i in range(lenA):
        #if we already check for this int divisor
        if A[i] in divisorDic:
            answer.append(divisorDic[A[i]])
        else:
            #else count divisors
            for y in range(A[i] // 2 +1 ):
                if intList[y] == 0:
                    continue
                if A[i] % y == 0:
                    counter += intList[y]
            #special case where the divisor is excluded by the loop
            if (intList[A[i]] != 0):
                counter += intList[A[i]]
            divisorDic[A[i]] =  lenA - counter
            answer.append(lenA - counter)
            counter = 0
    return answer

def integerList(A):
    lenMax = 2*len(A)
    intList = [0] * (lenMax+1)
    for i in range(len(A)):
        intList[A[i]] +=1
    return intList