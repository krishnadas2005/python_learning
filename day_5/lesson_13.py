#Defines a function named calculate.
def calculate(x, y, operation):
    if operation == "add":
        return x + y
    elif operation == "subtract":
        return x - y
    elif operation == "multiply":
        return x * y
    else:
        return "Invalid operation"
x = int(input("Enter the value of X: "))
y = int(input("Enter the value of y: "))
operation = input("Enter the operation: ")

result = calculate(x, y, operation)
print(f'result: {result}.')