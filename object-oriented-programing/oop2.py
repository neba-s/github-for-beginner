# This program calculates the area and perimeter of a rectangle after entering its length and width.
# Then, it reduces the length of the rectangle and recalculates the perimeter of the updated rectangle.

class Rectangle:  # Fixed class name typo (rectange -> Rectangle)
    def __init__(self, length, width):
        self.length = length  # Assign length
        self.width = width  # Assign width

    def info(self):
        """Displays the dimensions of the rectangle."""
        print(f"Width of the rectangle: {self.width}")
        print(f"Length of the rectangle: {self.length}")

    def area_of_rectangle(self):
        """Calculates and returns the area of the rectangle."""
        return self.length * self.width  

    def perimeter_of_rectangle(self):
        """Calculates and returns the perimeter of the rectangle."""
        return 2 * (self.length + self.width)  

# Taking user input for the length and width of the rectangle
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

# Creating an object of the Rectangle class
rectangle1 = Rectangle(length, width)

# Display initial rectangle details
rectangle1.info()

# Display the calculated area and perimeter
print(f"The area of the rectangle is: {rectangle1.area_of_rectangle()}")
print(f"The perimeter of the rectangle is: {rectangle1.perimeter_of_rectangle()}")

# Asking user how much they want to reduce the length
reduce = int(input("By how much do you want to reduce the length of the rectangle? "))

# Updating the length and creating a new object
updated_length = length - reduce
rectangle1 = Rectangle(updated_length, width)

# Display the updated perimeter
print(f"The perimeter of the updated rectangle is: {rectangle1.perimeter_of_rectangle()}")
