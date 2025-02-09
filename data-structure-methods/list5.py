# This function calculates the average of a list of numbers.
# It checks if the list is empty, returning None if true.
# If the list contains elements, it calculates the sum of all elements.
# Then it divides the sum by the length of the list to get the average.
# The function is called in a loop where sublists are created and averages are calculated.

def average(lists):
    if len(lists) == 0:
        return None
    return sum(lists) / len(lists)

num_lists = [1, 2, 3, 4]
for num in range(len(num_lists)):
    sublist = num_lists[:num + 1]
    aver = average(sublist)
    print(f"The average of {sublist} is {aver}")
