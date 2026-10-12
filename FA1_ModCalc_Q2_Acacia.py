print("1. Add | 2. Subtract | 3. Multiply | 4. Divide")

# Adding \n at the end moves the user's typing down to the next line
choice = input("Choose operation (1-4):\n")
num1 = float(input("Enter first number:\n"))
num2 = float(input("Enter second number:\n"))

if choice == "1":
  print("Result:", num1 + num2)
elif choice == "2":
  print("Result:", num1 - num2)
elif choice == "3":
  print("Result:", num1 * num2)
elif choice == "4":
  print("Result:", num1 / num2)
else:
  print("Invalid choice!")


