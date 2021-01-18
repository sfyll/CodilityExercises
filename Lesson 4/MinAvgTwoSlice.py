"""The Lowest avg in any slices k always lies within a subset of length 2 or 3"""
"""Score 90%, could be done in an easier fashion (as ex: https://codesays.com/2014/solution-to-min-avg-two-slice-by-codility/)
but here we explicitly use PrefixSums (even though one could argue that the link above use them indirectly)


def solution(A):
    lenA = len(A)
    minAvg=0
    index = 0
    prefArray = prefixsum(lenA, A)
    for idx in range(0, lenA-1):
        z = idx + 1
        if(z == lenA-1):
            for y in range(z, idx + 2):
                if idx == 0:
                    minAvg = prefArray[y] / (y - idx +  1)
                    index = idx
                    y += 1
                else:
                    tempMinAvg = (prefArray[y]-prefArray[idx-1]) / (y - idx + 1)
                    if(tempMinAvg < minAvg):
                        index = idx
                        minAvg = tempMinAvg
        else:
            for y in range(z, idx + 3):
                if idx == 0:
                    minAvg = prefArray[y] / (y - idx +  1)
                    index = idx
                    y += 1
                else:
                    tempMinAvg = (prefArray[y]-prefArray[idx-1]) / (y - idx + 1)
                    if(tempMinAvg < minAvg):
                        index = idx
                        minAvg = tempMinAvg
    return index
        
            
    
def prefixsum(lenA, A):
    prefixarray = [0] * lenA
    for idx in range(lenA):
        if idx == 0:
            prefixarray[idx] = A[idx]
        else:
            prefixarray[idx] = A[idx] + prefixarray[idx-1]
    return prefixarray