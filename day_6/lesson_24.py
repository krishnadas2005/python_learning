x = int(input("Enter the value of x: "))

if x < 0:
    print(f"{x} is negative.")
elif x == 0:
    print(f"{x} is zero.")
elif x > 0 and x < 100:
    print(f"{x} is a small positive number.")
else:
    print(f"{x} is a large positive number.")

print("end of the program.")