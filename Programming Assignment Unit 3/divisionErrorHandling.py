
# Part 2: Division Error Handling

# Fixed Code Snippet
def safe_division_program():
    print("--- Safe Division Calculator ---")
    try:
        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))
        
        result = num1 / num2
        print(f"The result is: {result:.2f}")
        
    except ZeroDivisionError:
        # This block runs ONLY if num2 is 0
        print("Error: Cannot divide by zero! Please enter a non-zero denominator.")
        
    except ValueError:
        # This block runs if the user enters text instead of numbers
        print("Error: Invalid input. Please enter numeric values only.")


safe_division_program()
