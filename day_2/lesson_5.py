#Asks for the user’s full name.
name = input("Enter your  name: ")

#remove the spaces of name and make it to title case
name = name.strip().title()

#Asks what the user wants to learn.
study = input("what you want to learn: ")

#makes the input remove the space and make it lower case
study = study.strip().lower()

#displays the answer with f-string
print(f'your name is {name}. you want to learn {study}.')