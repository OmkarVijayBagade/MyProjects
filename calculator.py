#calculator 
# 3 * 3 = 9

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# operator = input("Enter operator (+, -, *, /): ")
# result = 0
# if operator == "+":
#     result = num1 + num2
# elif operator == "-":
#     result = num1 - num2
# elif operator == "*":
#     result = num1 * num2 
# elif operator == "/":
#     result = num1 / num2 
# else:
#     print("Invalid operator")

# print(f"{num1} {operator} {num2} = {result}" )

while True:
    # input for the first number
    user_input = input("Enter first number (or type 'Q' to quit): ")
    if user_input.lower() == 'q':
        print("Exiting the program. Goodbye!")
        break

    try:
        num1 = float(user_input)  # Allow for floating-point numbers
    except ValueError:
        print("Invalid input. Please enter a number or 'Q' to quit.")
        continue

    # input for the second number
    num2 = float(input("Enter second number: "))

    #  input for the operator
    operator = input("Enter operator (+, -, *, /): ")

    #  calculation
    result = None
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            continue
    else:
        print("Invalid operator")
        continue

    # Display the result
    print(f"{num1} {operator} {num2} = {result}")

    # question to the user to continue or not 
    choice = input("Do you want to perform another calculation? (yes/no): ").lower()
    if choice not in ('yes', 'y'):
        print("Exiting the program. Goodbye!")
        break