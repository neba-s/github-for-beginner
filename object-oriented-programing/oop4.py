"""
This program defines a superclass `Vehicle` and a subclass `Style`.  
- The `Vehicle` class holds general car attributes and methods to check make, model, year, and budget.  
- The `Style` class inherits from `Vehicle` and adds a feature to determine if a car is a family or sports car.  
- Objects of both classes are created, and their methods are tested.  
"""

# Superclass: Vehicle
class Vehicle:
    """A class representing a general vehicle."""

    def __init__(self, make, model, year, price):
        self.make = make  # Car brand (e.g., Ford, Toyota)
        self.model = model  # Car model (e.g., Mustang, Camry)
        self.year = year  # Year of manufacture
        self.price = price  # Price of the vehicle

    def make_check(self):
        """Checks if the car is American-made or imported."""
        if self.make.lower() in ["ford", "chevy", "tesla"]:
            return "American made"
        else:
            return "Imported"

    def vehicle_model(self):
        """Returns the model of the vehicle."""
        return self.model

    def year_check(self):
        """Checks if the car is from the 21st century or old."""
        return "The car is from the 21st century" if self.year > 2000 else "This car is old"

    def max_price(self):
        """Checks if the vehicle's price is within the user's budget."""
        while True:
            try:
                price = int(input("Enter the maximum price you are willing to pay: "))
                break  # Exit loop if input is valid
            except ValueError:
                print("Invalid input! Please enter a numeric value.")

        return "Within your budget" if price >= self.price else "Over budget"

# Subclass: Style (inherits from Vehicle)
class Style(Vehicle):
    """A subclass of Vehicle that includes car style attributes."""

    def __init__(self, make, model, year, price, num_of_doors):
        super().__init__(make, model, year, price)
        self.num_of_doors = num_of_doors  # Number of doors

    def type_of_car(self):
        """Determines if the car is a family car or a sports car."""
        return "Family car" if self.num_of_doors == 4 else "Sports car"

# Main program execution
if __name__ == "__main__":
    # Creating a Vehicle object
    vehicle1 = Vehicle("Ford", "Mustang", 2022, 500)  # Changed "Mercedes" to "Mustang"
    print(vehicle1.make_check())  
    print(vehicle1.year_check())  

    # Creating Style objects (subclass objects)
    vehicle2 = Style("Chevy", "Jaguar", 2023, 1000, 5)  # Fixed year value for realism
    vehicle3 = Style("Tesla", "Lamborghini", 2023, 1000, 4)  # Fixed spelling (lambergini -> Lamborghini)

    print(vehicle2.max_price())  
    print(vehicle2.type_of_car())  

    print(vehicle3.max_price())  
    print(vehicle3.type_of_car())  
