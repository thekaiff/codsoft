def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


num1 = float(input("\nEnter first  number : "))
num2 = float(input("Enter second number : "))


print("\nSelect operation to perform :\n")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation_choice = int(input("\nEnter your choice (1/2/3/4): "))

if operation_choice == 1:
    print(f"\nThe result is: {add(num1, num2)}")
elif operation_choice == 2:
    print(f"\nThe result is: {subtract(num1, num2)}")
elif operation_choice == 3:
    print(f"\nThe result is: {multiply(num1, num2)}")
elif operation_choice == 4:
    print(f"\nThe result is: {divide(num1, num2)}")
else:
    print("\nInvalid input")
