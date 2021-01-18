#first construct the divisors list of N, then loop through it to find the rectangle with the lowest perimeter

def solution(N):
    divList = divisors(N)
    lenDivList = len(divList)
    if(lenDivList == 1):
        return 2* (divList[0]*2)
    minimPerimeter = 2*(1000000001*2)
    for i in range(1,lenDivList,2):
        tempPerimeter = 2*(divList[i] + divList[i-1]) 
        if tempPerimeter < minimPerimeter:
            minimPerimeter = tempPerimeter
    return minimPerimeter
    
def divisors(N):
    i = 1
    divisorList = list()
    while(i*i <N):
        if(N%i == 0):
            divisorList.append(i)
            divisorList.append(N//i)
        i +=1
    if(i*i==N):
        #append twice
        divisorList.append(i)
        divisorList.append(i)
    return divisorList