"""
This program allows the user to draw shapes using the Turtle module.  
It provides two functions: one for drawing a square and another for drawing a triangle.  
The user can choose which shape to draw, specify its size, and repeat the process in a loop.  
The loop continues until the user types "stop" to exit.  
Shapes are drawn in separate locations to avoid overlapping.  
"""

# Import the turtle module for drawing shapes
from turtle import *

# Function to draw a square
def draw_square(t, size):
    """Draws a square using the given turtle object and size."""
    
    # Move the turtle to a starting position (avoiding overlap with other shapes)
    t.penup()
    t.goto(-size, -100)  
    t.pendown()
    
    # Draw the square (4 sides, 90-degree turns)
    for _ in range(4):
        t.forward(size)
        t.left(90)

# Function to draw a triangle
def draw_triangle(t, size):
    """Draws a triangle using the given turtle object and size."""
    
    # Move the turtle to a different position to avoid overlapping with the square
    t.penup()
    t.goto(size, -100)  
    t.pendown()
    
    # Draw the triangle (3 sides, 120-degree turns)
    for _ in range(3):
        t.forward(size)
        t.left(120)

# Main loop to repeatedly ask the user which shape to draw
while True:
    # Asking the user which shape they want to draw
    shape = input("What shape do you want to draw? ('square', 'triangle', 'both', 'stop' to quit): ").lower()

    if shape == "stop":
        break  # Exit the loop

    # Get the size of the shape from the user
    size = int(input("Enter the size of the shape: "))
    
    # Create a new turtle object for drawing
    t = Turtle()

    # Call the correct function based on the user's choice
    if shape == "square":
        draw_square(t, size)
    elif shape == "triangle":
        draw_triangle(t, size)
    elif shape == "both":
        draw_square(t, size)
        draw_triangle(t, size)
    else:
        print("Invalid shape choice. Please enter 'square', 'triangle', 'both', or 'stop'.")

# Finish the turtle drawing
done()
