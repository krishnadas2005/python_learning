#ask user of Asks for a two-word name
name = input("Enter your name: ")

#Removes whitespace from the beginning and end and title case in name
name = name.strip().title()

#Splits the name into two parts and stores them in separate variables.
first, last = name.split()

#Displays the first name and second name separately
print( first, last)

#the user using only the first part.
print(f'first name:  {first}.')

#the user using only the second part.
print(f'last name name:  {last}.')

#Uses f-strings for the displayed results
print(f'welcome {first} {last}.')