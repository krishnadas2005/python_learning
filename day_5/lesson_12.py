#Defines a function named add_numbers
def add_numbers(x, y):
    return x + y #Returns their sum using return.

x = int(input("Enter the value of X: "))#Gives it two parameters: x and y.
y = int(input("Enter the value of y: "))

result = add_numbers(x, y)
print(f'sum: {result}.')

