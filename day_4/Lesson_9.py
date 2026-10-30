#Asks for a first number that may include decimals
x = float(input("Enter the number: "))

y = float(input("Enter the number: "))

#Calculates their sum, difference, product, and quotient
a = x + y
b = x - y
c = x * y
d = x / y

#Displays each result on its own line using an f-string
print(f'sum: {a:.2f} .')
print(f'difference: {b:.2f}.')
print(f'product: {c:.2f}.')
print(f'quotient: {d:.2f}.')