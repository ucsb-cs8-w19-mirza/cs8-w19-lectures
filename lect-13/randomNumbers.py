from random import *

def rollDie():
    '''return the value of rolling a single die'''
    return randrange(1, 13)


def rollDistribution(n):
    '''n : number of times to repeat the experiment of
       rolling a die, returns a list of counts'''
    #### For lab06
    # how would you store the information about the
    # count of each outcome {2-12}
    # [ 4, 17, 25 39, 28, 10]
    # Assume that the index of each element in the list
    # corresponds to one of the possible outcomes 2 -12
    # index 0 -> 2
    # index 1 -> 3
    ############
    # index 0 -> 1
    count = [0]*12
    for i in range(n):
        value = rollDie() # roll the die once and record the outcome
        count[value-1] = count[value-1] +1
        
    return count

def printDistribution(lst):
    ''' display the historgram
        of the counts'''
    for i in range(12):
        print(i+1, lst[i])
    
