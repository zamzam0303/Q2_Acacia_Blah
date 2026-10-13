def calculate(num1, num2, choice):
    # Perform the selected operation
    if choice == 1:
        return num1 + num2
    elif choice == 2:
        return num1 - num2
    elif choice == 3:
        return num1 * num2
    elif choice == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero."
    else:
        return "Invalid choice."


# Display the menu
print("=== Modular Calculator ===")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Get user input
choice = int(input("Choose an operation (1-4): "))
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Pass arguments to the function
result = calculate(num1, num2, choice)

# Display the returned value
print("Result:", result)


# REFLECTION

# 1. What functions did you create in your calculator program?
# I created a function called calculate() that performs
# addition, subtraction, multiplication, and division.

# 2. What parameters did your functions use?
# My function used three parameters: num1, num2, and choice.

# 3. What arguments were passed when the functions were called?
# I passed num1, num2, and choice as arguments when calling
# the calculate() function.

# 4. How did your program use the returned value?
# The function returned the result of the selected operation.
# The result was stored in the variable result and displayed
# using the print() function.

# 5. Why is it better to divide the calculator program into
# functions instead of writing everything in one long block?
# Functions make the program more organized, readable, and
# easier to debug, maintain, and reuse.
