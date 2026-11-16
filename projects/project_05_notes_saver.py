# Note Saver App
from datetime import datetime


print("______NOTE SAVER APP______")


def menu():
    while True:
        print("\n1. Add note")
        print("2. View all notes")
        print("3. Exit")

        try:
            choice = int(input("Choose any one option from (1/2/3): "))
        except ValueError:
            print("Enter a vsaild input from (1/2/3): ")
            continue

        if choice == 1:
            note = input("Enter your note: ")
            today = datetime.now().strftime("%d-%m-%Y %H:%M")

            with open("notes.txt", "a") as file:
                file.write(f"{today}\t{note}\n")

            print("Note added successfully in the file.")

        elif choice == 2:
            try:
                with open("notes.txt", "r") as file:
                    contents = file.read()

                if contents.strip() == "":
                    print("Your file is empty.")
                else:
                    print("\n______Your Notes______ \n")
                    print(contents)

            except FileNotFoundError:
                print("File not found! No notes have been saved yet.")

        elif choice == 3:
            print("Exiting... Thank you!")
            break

        else:
            print("Invalid input. Try again!")


menu()