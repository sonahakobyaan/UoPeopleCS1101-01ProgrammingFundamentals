# import math

# Part 1: Circumference Calculation

def print_circum(radius):
    """
    Calculates and prints the circumference of a circle.
    Formula: 2 * pi * r
    """
    pi = 3.14159  # Value specified in the assignment
    # or pi = math.pi
    circumference = 2 * pi * radius
    print(f"Radius: {radius} -> Circumference: {circumference}")

# Calling the function three times with different values
print_circum(5)
print_circum(10.5)
print_circum(21)