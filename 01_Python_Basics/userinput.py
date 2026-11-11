"""
Program: User Input Calculator
Purpose: Accept two numbers from the user and perform arithmetic operations.
Language: Python
"""

# Accept input from the user
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Perform arithmetic operations
addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number

# Display the results
print("--- Calculation Results ---")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)

# Check before division
if second_number != 0:
    division = first_number / second_number
    print("Division:", division)
else:
    print("Division: Cannot divide by zero.")
