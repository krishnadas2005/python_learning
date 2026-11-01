#Ask the user for a whole number and convert it using int.
x = int(input("Enter the value of X: "))
n = x #Store it in number

#Create these Boolean variables
is_positive = n > 0

is_under_100 = n < 100

is_between = is_positive and is_under_100

is_zero_or_negative = not is_positive

#Print all four Boolean values with f-strings
print(f'is_positive: {is_positive}.')
print(f'is_under_100: {is_under_100}.')
print(f'is_between: {is_between}.')
print(f'is_zero_or_negative: {is_zero_or_negative}.')

#Add an if/else statement
if is_between:
    print (f"{n} is between 1 and 100.")
else:
    print(f"{n} is not between 1 and 100.")

print("end of the program.")