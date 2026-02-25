
# Part 1: Recursive Count Program


def countdown(n):
    # Recursively counts down from a positive number to 0.
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n - 1)


def countup(n):
    # Recursively counts up from a negative number to 0.
    if n >= 0:
        print("Blastoff!")
    else:
        print(n)
        countup(n + 1)

def main():
    # getting keyboard input from the user
    try:
        user_input = int(input("Enter a number: "))

        if user_input > 0:
            # Case 1: Positive number calls countdown
            countdown(user_input)
        elif user_input < 0:
            # Case 2: Negative number calls countup
            countup(user_input)
        else:
            # Case 3: Zero input logic
            # I have chosen to call countdown for zero
            countdown(user_input)

    except ValueError:
        print("Invalid input. Please enter an integer.")


main()
