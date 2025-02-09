# Lists in Python - Two Ways to Create Them
# 1. Using square brackets []
# 2. Using the list() function

# Example of list creation
list1 = [3, 5, 6, 7, 5, 3]

# Append method - Adds an element at the end of the list
list1.append(555)

# Remove method - Removes the first occurrence of an element
list1.remove(6)

print("Updated List:", list1)

# Sort method - Sorts the list in ascending order
# Note: Sorting does not work with mixed data types like [34, 3, "orange"]
list1.sort()
print("Sorted List:", list1)

# Converting a string into a list
father_name = "yalemgeta demoz"
print("List from string:", list(father_name))  # Does not change the original string
print("Original string:", father_name)

# If you want to permanently change it into a list:
father_name_list = list(father_name)
print("Permanently converted list:", father_name_list)

# ---------------- Practical Example ----------------

# Create a list of ages using input and determine how many people are minors (<18) and how many are adults (>=18)
ages = []
num_seniors = 0
num_minors = 0

your_age = int(input("Enter an age (Enter 0 to stop): "))

while your_age != 0:
    if your_age < 18:
        num_minors += 1
    else:
        num_seniors += 1
    ages.append(your_age)
    
    your_age = int(input("Enter another age (Enter 0 to stop): "))

print(f"All ages entered: {ages}")
print(f"Number of minors: {num_minors}, Number of adults: {num_seniors}")

# ---------------- List from a String Using split() ----------------
# The split() function splits a string based on a separator and converts it into a list.

name = "donald"
print("Splitting with default (space):", name.split())  # Default splits by spaces

print("Splitting with '-':", name.split("-"))  
# Since there is no "-" in the string, it returns the entire string as a single list element.

# Note: The separator used in split() is not included in the final list.
