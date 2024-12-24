def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operator = input("Enter the operation to perform: ")

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

if operator == '+':
    print(add(a, b))

elif operator == '-':
    print(subtract(a, b))

elif operator == '*':
    print(multiply(a, b))

elif operator == '/':
    if b != 0:
        print(divide(a, b))
    else:
        print("Division by zero isn't possible.")
