import draw
import turtle
joe = turtle.Turtle()
joe.speed(0)
joe.width(8)
joe.up() # Lift the pen up
joe.goto(0,-50) # move to a new location
joe.down() # Place the pen down

 # Function call
draw.fancyCircle(joe, 50, "black", "black")
