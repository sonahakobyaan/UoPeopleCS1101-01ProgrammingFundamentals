import math

# Part 1: Hypotenuse Calculator

def hypotenuse(a, b):
    aSquared = a ** 2
    bSquared = b ** 2
    hSquared = aSquared + bSquared
    result = math.sqrt(hSquared)
    return result

# Final test calls
print("Call 1:", hypotenuse(3, 4))
print("Call 2:", hypotenuse(5, 12))
print("Call 3:", hypotenuse(8, 15))