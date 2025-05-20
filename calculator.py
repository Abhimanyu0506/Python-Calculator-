print("Welcome to the Python Calculator!")
print("Type 'exit' at any time to quit.\n")

while True:
    # Get first number
    num1_input = input("Enter first number: ")
    if num1_input.lower() == 'exit':
        break
    num1 = float(num1_input)

    # Get operator
    operator = input("Enter operator (+, -, *, /, %): ")
    if operator.lower() == 'exit':
        break

    # Get second number
    num2_input = input("Enter second number: ")
    if num2_input.lower() == 'exit':
        break
    num2 = float(num2_input)

    # Perform calculation
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            continue
    elif operator == '%':
        # Calculate percentage: "num1 percent of num2"
        result = (num1 / 100) * num2
    else:
        print("Invalid operator.")
        continue

    print("Result:", result)
    print("-" * 30)