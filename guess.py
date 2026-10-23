import random

secret_number = random.randint(1, 10)

play = input("Do you want to guess a number between 1 and 10? (yes/no): ").strip().lower()
if play == "yes":
    while True:
        print("Enter your guess:")
        try:
            guess = int(input())
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if guess < secret_number:
            print("Your guess is too low. Try again.")
        elif guess > secret_number:
            print("Your guess is too high. Try again.")
        else:
            print("Congratulations! You guessed the number.")
            break


            