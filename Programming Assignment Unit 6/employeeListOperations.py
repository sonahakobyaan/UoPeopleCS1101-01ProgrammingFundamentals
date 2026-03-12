
# Part 1: Employee and Salary List Operations

def employee_management():
    # 1. Initial list of 10 employees
    employees = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]
    print("Original List:", employees)

    # 2. Split the list into subList1 and subList2 (5 names each)
    subList1 = employees[:5]
    subList2 = employees[5:]
    print("SubList 1:", subList1)
    print("SubList 2:", subList2)

    # 3. Add "Kriti Brown" to subList2
    subList2.append("Kriti Brown")
    print("SubList 2 after addition:", subList2)

    # 4. Remove the second employee's name from subList1 (Index 1)
    del subList1[1]
    print("SubList 1 after removal:", subList1)

    # 5. Merge both lists
    mergedList = subList1 + subList2
    print("Merged List:", mergedList)

    # 6. Salary List: Give a 4% rise to every employee
    salaryList = [50000, 52000, 48000, 60000, 55000, 58000, 47000, 51000, 53000, 59000]
    # We use a list comprehension to apply the 4% raise (current * 1.04)
    salaryList = [round(salary * 1.04, 2) for salary in salaryList]
    print("Updated Salary List (4% rise):", salaryList)

    # 7. Sort the SalaryList and show top 3 salaries
    salaryList.sort(reverse=True)
    print("Top 3 Salaries:", salaryList[:3])


# Main execution
if __name__ == "__main__":
    employee_management()