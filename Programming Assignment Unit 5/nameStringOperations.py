
# String Manipulation and Iteration

def main():
    # 1. Display name and take input for 'n' characters
    myName = "Sona Hakobyan"
    print(f"Original Name: {myName}")
    
    try:
        n = int(input("Enter the number of characters to display from the left: "))
        # Slicing from index 0 to n
        leftChars = myName[:n]
        print(f"The first {n} characters are: '{leftChars}'")
    except ValueError:
        print("Invalid input. Please enter an integer.")

    # 2. Count the number of vowels using iteration
    vowels = "aeiouAEIOU"
    vowelCount = 0
    for char in myName:
        if char in vowels:
            vowelCount += 1
    print(f"Number of vowels in the name: {vowelCount}")

    # 3. Reverse the name using string slicing
    reversedName = myName[::-1]
    print(f"Name in reverse: {reversedName}")

# This correctly calls the function without causing an infinite loop
if __name__ == "__main__":
    main()