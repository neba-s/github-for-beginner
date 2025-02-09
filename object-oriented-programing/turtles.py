"""
This program creates three turtle objects, each with a different color but the same width.  
It then draws three triangles in a vertical column at different positions.  
Each triangle is filled with its respective solid color after being drawn.  
The drawing remains on the screen after completion.  
The Turtle module is used to create and display the shapes.  
"""

# Import the turtle module
from turtle import *

# Create three turtle objects with different colors but the same width
t1 = Turtle()
t1.color("blue")
t1.width(3)

t2 = Turtle()
t2.color("red")
t2.width(3)

t3 = Turtle()
t3.color("magenta")
t3.width(3)

# Lift the pen to move turtles without drawing
t1.penup()
t2.penup()
t3.penup()

# Position the turtles in a vertical column
t1.goto(-100, 100)   # First triangle at the top
t2.goto(-100, 0)     # Second triangle in the middle
t3.goto(-100, -100)  # Third triangle at the bottom

# Put the pen down to start drawing
t1.pendown()
t2.pendown()
t3.pendown()

# Begin filling the triangles with solid color
t1.begin_fill()
t2.begin_fill()
t3.begin_fill()

# Draw three triangles using a loop
for _ in range(3):
    t1.forward(100)
    t1.right(120)

    t2.forward(100)
    t2.right(120)

    t3.forward(100)
    t3.right(120)

# End the fill to complete the solid color effect
t1.end_fill()
t2.end_fill()
t3.end_fill()

# Keep the window open after drawing
done()
