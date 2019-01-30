#draw.py

import turtle
## Function definition
def fancyCircle(t, radius, penColor, fillColor):
    '''t: turtle object
       radius: integer
       Draws a circle with a given
       radius, pen color, fill color
       '''
    t.color(penColor, fillColor)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    
    return

print(__name__)
if __name__ =="__main__":
    jane = turtle.Turtle() # Jane is a turtle object
    jane.speed(0)
    fancyCircle(jane, 100, "red", "red") 




