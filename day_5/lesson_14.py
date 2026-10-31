#Asks for two whole numbers and converts them using int().
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
operation = input("Enter the operation: ")
operation = operation.strip().lower()

def calculate (x, y, operation):
    if operation == "add":
        return x + y
    elif operation == "subtract":
        return x - y
    elif operation == "multiply":
        return x * y
    elif operation == "divide":
        return x / y
    else:
        print("Invalid operation")

result = calculate (x, y, operation)
print(f'result: {result}.')