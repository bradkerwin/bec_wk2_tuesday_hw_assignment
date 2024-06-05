# Task 1: Create functions for each arithmetic operation, with parameters for two numbers to be used in the operation.
def addition(num1, num2):
    return (num1 + num2)
addition_total = addition(3, 3) # Calculates (3 + 3)
print(addition_total) # Prints 6.
def subtraction(num1, num2):
    return (num1 - num2)
subtraction_total = subtraction(10, 5) # Calculates (10 - 5)
print(subtraction_total) # Prints 5
def multiplication(num1, num2):
    return (num1 * num2)
multiplication_total = multiplication(6, 4) # Calculates (6 * 4)
print(multiplication_total) # Prints 24
def division(num1, num2):
    return (num1 / num2)
division_total = division(20, 5) # Calculates (20 / 5)
print(division_total) # Prints 4.0 

# Task 2: Implement user input to receive numbers and an operation choice, their response for operation should call the associated function

operation_input = input("Please choose an operation. ")
num1_input = int(input("Now please enter your first number. "))
num2_input = int(input("Now please enter your second number. "))
if operation_input == "addition":
    print(addition(num1_input, num2_input))
if operation_input == "subtraction":
    print(subtraction(num1_input, num2_input))
if operation_input == "multiplication":
    print(multiplication(num1_input, num2_input))
if operation_input == "division":
    print(division(num1_input, num2_input))