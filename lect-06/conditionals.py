def check_integer(x):
    return type(x) == int

def check_integer(x):
    if type(x) == int:
        return True
    else:
        return False

def is_neg_integer(x):
    '''return True if x is
     a negative integer'''
    
    result  = (type(x) == int) and (x <0)  
    return result

def is_Odd(x):
    ''' return True if x is an odd integer'''
    return type(x) == int and (x%2 !=0)

    
# int is a keyword in Python
# that refers to the integer type

# str: string
# float: float
# list: lists
# tuple: tuples

