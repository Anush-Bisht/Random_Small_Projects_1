import random

print("Welcome to Guess the number game.\n")

userinput = input("Do you want to play (y/n): ").lower()

if userinput == 'y':
    low = int(input("Enter a lower bound: "))
    high = int(input("Enter a high bound: "))

    computer_guess = random.randint(low, high)

    print("You have 5 chance to guess the number.\n")

    chances = 5
    no_of_guesses = 0

    while chances > no_of_guesses:
        no_of_guesses += 1
        
        user_guess = int(input(f"Enter the number between {low} and {high}: \n")) 

        if user_guess == computer_guess:
            print(f"Correct, You number {user_guess} is same as Computers number which is {computer_guess}")
            break

        elif no_of_guesses >= chances and user_guess != computer_guess:
            print(f"Sorry!, The number was {computer_guess}. Try again!")

# make a function for try again thing

        elif user_guess > computer_guess:
            print(f"The Guessed number {user_guess} is too high")
            
        elif user_guess < computer_guess:
            print(f"The Guessed number {user_guess} is too low")

elif userinput == 'n':
    print("Thank You.")

else:
    print("Error!")