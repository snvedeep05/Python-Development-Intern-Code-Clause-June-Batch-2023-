def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Calculator Program")
print("Operations:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("0. Exit")

while True:
    choice = input("Enter your choice (0-4): ")

    if choice == '0':
        print("Exiting the calculator program.")
        break

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            result = add(num1, num2)
            print("Result:", result)
        elif choice == '2':
            result = subtract(num1, num2)
            print("Result:", result)
        elif choice == '3':
            result = multiply(num1, num2)
            print("Result:", result)
        elif choice == '4':
            if num2 != 0:
                result = divide(num1, num2)
                print("Result:", result)
            else:
                print("Error: Cannot divide by zero!")
    else:
        print("Invalid input. Please try again.")
