def factorialLoops(n):
    result = 1
    for i in range(1, n+1):
        result = result *i
    return result

def fact(n):
    if n==1: #Base case 
        return 1
    else:
        return n*fact(n-1)
    
        
    
def recursiveSum(lst):
    #Base case
    if lst == []:
        return 0
    if len(lst) ==1:
        return lst[0]
    return lst[0]+recursiveSum(lst[1:])






