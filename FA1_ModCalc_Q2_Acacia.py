print("1. Add | 2. Subtract | 3. Multiply | 4. Divide")
choice = input("Choose operation (1-4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

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
