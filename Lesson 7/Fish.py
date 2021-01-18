# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import deque 

def solution(A, B):
    downstreamStack = deque()
    upstreamFishes = 0
    for idx, values in enumerate(B):
        #no fish going downstream and current fish going upstream
        if(stackEmpty(downstreamStack) and values == 0):
            upstreamFishes +=1
        #no fish going downstream (no need of specification for this use case) and current fish going downstream
        elif(values == 1):
            downstreamStack.append(A[idx])
        #we have fishes crossing pathes
        elif(stackEmpty(downstreamStack) == False and values == 0):
            #fights until fish going upstream eats all the fishes going downstream or he dies
            while(downstreamStack[-1] < A[idx]):
                downstreamStack.pop()
                #all downstream fishes were eaten
                if(stackEmpty(downstreamStack)):
                    upstreamFishes +=1
                    break
            #upstream fish was eaten    
            else:
                continue
    return (len(downstreamStack) + upstreamFishes)
        
def stackEmpty(S):
    if len(S) == 0:
        return True
    else:
        return False