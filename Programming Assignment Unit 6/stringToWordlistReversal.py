
# Part 2: String to Wordlist Conversion and Reversal

def string_operations():
    sentence = "Learning Python is fun and productive"
    
    # Convert sentence into wordlist
    wordlist = sentence.split()
    print("\nWord List:", wordlist)
    
    # Reverse the wordlist
    wordlist.reverse()
    print("Reversed Word List:", wordlist)

# Main execution
if __name__ == "__main__":
    string_operations()