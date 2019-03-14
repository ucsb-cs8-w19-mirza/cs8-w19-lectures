import turtle
import random

def drawVV(t, n):
    if n == 0:
        return
    t.left(30)
    t.forward(50)
    drawVV(t, n-1)
    
    
def drawStamp(t, color):
    t.color(color, color)
    t.stamp()
    t.color("red")
    
def drawV(t):
    coin = random.randrange(0, 3)
    
    t.left(30)
    t.forward(50)
    if coin <2:
        drawStamp(t, "red")
    else:
        drawV(t)
    t.backward(50)
    t.right(60)
    t.forward(50)
    coin = random.randrange(0, 3)
    if coin <2:
        drawStamp(t, "red")
    else:
        drawV(t)

    t.backward(50)
    t.left(30)
    
# setup the turtle
t = turtle.Turtle()
t.shape("turtle")
t.width(5)
t.color("red", "red")
t.shapesize(1)
t.speed(0)
t.left(90)
t.penup()
t.goto(0,-200)
t.pendown()

while(1):
    t.clear()
    t.forward(100) 
    drawVV(t, 3)
    t.backward(100)
    x = input('Do you want to continue(y)? ')
    if(x!='y'):
        break

