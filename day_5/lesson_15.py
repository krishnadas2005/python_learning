#Write a function called power that Takes two parameters: base and exponent
def power(base, exponent=2): #Gives exponent a default value of 2
    return base ** exponent

result_1 = power(5)
result_2 = power(2, 3)   

print(f'result_1: {result_1}.')
print(f'result_2: {result_2}.')
