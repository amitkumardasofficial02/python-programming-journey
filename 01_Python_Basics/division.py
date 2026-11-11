"""
Program: Division of Two Numbers
Purpose: Divide one number by another safely.
Language: Python
"""

# Define input values
first_number = 50
second_number = 10

# Check for division by zero
if second_number != 0:
    result = first_number / second_number
    print("Division Result:", result)
else:
    print("Error: Division by zero is not allowed.")
