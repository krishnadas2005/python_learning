#Asks for a first number that may include decimals
x = float(input("Enter the number: "))

y = float(input("Enter the number: "))

#Calculates their sum, difference, product, and quotient
a = x + y
b = x - y
c = x * y
d = x / y

#Displays each result on its own line using an f-string
print(f'sum: {a}.')
print(f'difference: {b}.')
print(f'product: {c}.')
print(f'quotient: {d}.')