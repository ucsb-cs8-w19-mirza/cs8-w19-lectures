def dbl(x):
    '''returns the double of x'''
    #print("Hey I am in a function")
    print(2*x)


def printName():
    print("My name is turtle")
    # Function that does not have
    # an explicit return value
    # returns None by default


#y = dbl(3) # This is a function call
       # To call a function:
       # use its name and pass in
       # a value (parameter), e.g. 3
#print(y)

def halve(x):# x = 42
    print("Inside halve x = ", x)
    print("Calling div")
    z = div(x,2)# div(42,2)
    print("Return the result from div")
    return z

def div(y, x):# y = 42, x = 2
    print("Inside div y = ",y, "x= ", x)
    return y/x # 42/2






