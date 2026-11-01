#Asks the user for two whole numbers and converts them with int()
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

is_equal = a == b

is_not_equal = a != b

is_greater = a > b

is_less = a < b

is_greater_or_equal = a >= b

is_less_or_equal = a <= b

print(f'is_equal: {is_equal}.')         
print(f'is_not_equal: {is_not_equal}.')
print(f'is_greater: {is_greater}.') 
print(f'is_less: {is_less}.')
print(f'is_greater_or_equal: {is_greater_or_equal}.')  
print(f'is_less_or_equal: {is_less_or_equal}.')       