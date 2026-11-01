#Ask for x, y, and operation
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
operation = input("Enter the operation: ")
operation = operation.strip().lower()
def calculate(x, y, operation):
    if operation == "add":
        return x + y
    elif operation == "subtract":
        return x - y
    elif operation == "multiply":
        return x * y
    elif operation == "divide":
        if y == 0:
            return "Invalid operation"
        return x / y
    else:
        return "Invalid operation"

result = calculate(x, y, operation)

if isinstance(result, (int, float)):
    print(f'Result: {result:.2f}')
else:
    print(f'Result: {result}')