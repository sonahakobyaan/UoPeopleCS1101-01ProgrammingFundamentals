
# Part 2: Custom Function Portfolio

def calculate_bmi(weight, height):
    heightSquared = height ** 2
    bmiResult = weight / heightSquared
    return bmiResult

# Three calls with different arguments
print("BMI Test 1 (Normal):", calculate_bmi(70, 1.75))
print("BMI Test 2 (Underweight):", calculate_bmi(50, 1.80))
print("BMI Test 3 (Overweight):", calculate_bmi(100, 1.70))

calculate_bmi(70, 1.75)