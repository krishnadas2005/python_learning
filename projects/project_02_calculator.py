def calculator():
    try:
        n_1 = int(input("Enter the first number: "))
        n_2 = int(input("Enter the second number: "))

    except ValueError:
        print("Enter a valid integer.")
        return
    operation = input("Enter the operator (+, -, *, /): ")

    if operation == "+":
        print(f'the sum is {n_1 + n_2}.')
    elif operation == "-":
        print(f'the difference is {n_1 - n_2}.')
    elif operation == "*":
        print(f'the product is {n_1 * n_2}.') 
    elif operation == "/":       
        if n_2 == 0:
            print("Cannot divide by zero.")
        else:
            print(f'the quotient is {n_1 / n_2}.')
    else:
        print("Invalid input.")

while True:
    calculator()
    
    again = input("do you want to run the calculator again (yes/no): ")
    
    if again == "no":
        break