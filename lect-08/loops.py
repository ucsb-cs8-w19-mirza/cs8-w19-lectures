
def drawL(tur, width, height):
    tur.stamp()
    tur.backward(width)
    tur.left(90)
    tur.forward(height)
    tur.backward(height)
    tur.right(90)
    tur.forward(width)
    
draw_turtle = 0
if 
import turtle
fred= turtle.Turtle()
fred.shape("turtle")
fred.width(4)
drawL(fred, 50, 100)

def quadratic(a, b, c, x):
    '''return ax^2+bx+c
    If any of a, b, c, x is not
    an integer return 0'''
    
    if (type(a)!=int) or (type(b)!=int) or type(c)!=int or type(x) !=int:
        return 0 # inside the if block

    result =  a*x**2+b*x+c
    return result

def quadratic(a, b, c, x):
    # This is also correct
    if type(a) == int and type(b)==int and type(c)==int:
        return a*x**2+b*x+c
    else:
        return 0

##def test_case1():
##    assert quadratic(1, 1, 1, 1)==pytest.approx(3)
##
##def test_case2():
##    assert quadratic("UCSB", 3, 4, 1)== 0

def print_dbl(x):
    print(2*x)
y = print_dbl(2)
print(y)


