import random


def easy_level():
    count = 10
    comp_number = random.randint(1, 100)
    print(f"You have {count} attempts remaining to guess the number.")
    while count > 0:
        user_guess = int(input("Make a guess:"))
        if user_guess > comp_number:
            print("Too high")
            print("Guess again")
        elif user_guess < comp_number:
            print("Too low")
            print("Guess again")
        elif user_guess == comp_number:
            print(f"You got it!. The answer was {comp_number}")
            break
        count -= 1
        print(f"You have {count} attempts remaining to guess the number")


def hard_level():
    count = 5
    comp_number = random.randint(1, 100)
    print(f"You have {count} attempts remaining to guess the number.")
    while count > 0:
        user_guess = int(input("Make a guess:"))
        if user_guess > comp_number:
            print("Too high")
            print("Guess again")
        elif user_guess < comp_number:
            print("Too low")
            print("Guess again")
        elif user_guess == comp_number:
            print(f"You got it!. The answer was {comp_number}")
            break
        count -= 1
        print(f"You have {count} attempts remaining to guess the number")


print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")
user_choice = input("Choose a difficulty. Type 'easy' or 'hard':")
user_choice.lower()
if user_choice == 'easy':
    easy_level()
elif user_choice == 'hard':
    hard_level()
else:
    print("Incorrect")
