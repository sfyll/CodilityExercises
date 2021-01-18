# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    pass
def solution(S):
    lenS = len(S)
    if(lenS == 0):
        return 1
    stack = list()
    for i in range(lenS):
        if len(stack) == 0:
            stack.append(S[i])
        else:
            if(match(S[i]) == stack[-1]):
                stack.pop()
            else:
                stack.append(S[i])
    if len(stack) > 0:
        return 0
    else:
        return 1

def match(element):
    if element == "]":
        return "["
    elif element ==  "}":
        return "{"
    elif element == ")":
        return "("