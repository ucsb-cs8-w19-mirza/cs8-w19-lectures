import turtle
import random

def drawVV(t, n):
    if n == 0: # Base case
        return
    # Recursive case
    t.left(30)
    t.forward(50)
    drawVV(t, n-1)
    
    
def drawStamp(t, color):
    t.color(color, color)
    t.stamp()
    t.color("red")

    
# setup the turtle
t = turtle.Turtle()
t.shape("turtle")
t.width(5)
t.color("red", "red")
t.shapesize(1)
t.speed(0)
t.left(90)
t.penup()
t.goto(0,-100)
t.pendown()
drawVV(t, 10)


