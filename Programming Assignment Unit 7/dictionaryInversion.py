
# Dictionary Inversion

def invert_dictionary(original_dict):
    """
    Inverts a dictionary where values are lists. 
    The list items become keys, and the original keys become values.
    """
    invertedDict = dict()
    
    # Iterate through the original dictionary using items()
    for student, courses in original_dict.items():
        # Iterate through each course in the student's list
        for course in courses:
            # If the course is not yet a key, create a new list with the student
            if course not in invertedDict:
                invertedDict[course] = [student]
            # If the course already exists, append the student to the list
            else:
                invertedDict[course].append(student)
                
    return invertedDict

# 1. Construct the original dictionary
studentsCourses = {
    'Stud1': ['CS1101', 'CS2402', 'CS2001'],
    'Stud2': ['CS2402', 'CS2001', 'CS1102']
}

# 2. Print the original dictionary
print("Original Dictionary:")
print(studentsCourses)
print("\n") # Adding a blank line for readability

# 3. Invert the dictionary and print the result
invertedResult = invert_dictionary(studentsCourses)
print("Inverted Output:")
print(invertedResult)