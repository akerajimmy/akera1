# Simple Calculator Program

# Ask for the first number
num1 = float(input("Enter the first number: "))

# Ask for the second number
num2 = float(input("Enter the second number: "))

# Ask for the operation
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation
if operation == '+':
    result = num1 + num2
    print("Result:", result)
elif operation == '-':
    result = num1 - num2
    print("Result:", result)
elif operation == '*':
    result = num1 * num2
    print("Result:", result)
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operation.")
