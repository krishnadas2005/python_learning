import random


def play_game():
    secret_number = random.randint(0, 10)
    player_guess = int(input("Enter a number between 0 and 10: "))
    attempt = 1

    while player_guess != secret_number:
        if player_guess > secret_number:
            print("Too high! Try again!")
        else:
            print("Too low! Try again!")

        player_guess = int(input("Enter a number between 0 and 10: "))
        attempt += 1

    print(f"Congrats! You found the number in {attempt} attempts.")


play_game()