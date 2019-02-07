# Find the sum of all elements in a list
# e.g. lst = [1, 5, 3]
# return 9
##
##sumL = lst[0] + lst[1] + lst[2]
##
##mysum = lst[0] + lst[1] + lst[2] + lst[3]
##
##mysum= 0
##
##mysum = mysum + lst[0]
##mysum = mysum + lst[1]
##mysum = mysum + lst[2]

def sumList(lst):
    mysum = 0
    for x in lst:
        #print(x)
        mysum = mysum + x
        #return mysum # Premature return
                     # The function will return
                     # in the first iteration of
                     # the loop
    return mysum
# word = apple                    
def numVowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for x in word:
        if x in vowels: # evaluates to True
                        # if x is a vowel
            count = count + 1

    # Outside the for loop
    return count
        
def numVowels_2(word):
    vowels = "aeiouAEIOU"
    count = 0
    for x in vowels:
        # Write some code
        count = count + word.count(x)

    # Outside the for loop
    return count

# example
# lst = [0, 1, 2]
# newlist = [ 2**0, 2**1, 2**2]
def powerOfTwo(lst):
    # Accumulate into a list
    newlist = []
    for x in lst:
        newlist.append(2**x)

    return newlist


def countOddNumbers(lst):
    count = 0
    for x in lst:
        if x % 2 == 1:
            count = count + 1
    return count

    
    
    

