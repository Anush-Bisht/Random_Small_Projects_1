import random

print("Welcome to Word Guessing Game\n")

user_decision = input("Do you want to play the word guessing game? (y/n): \n")

name = input("Enter your name: ")
print("Good Luck! ", name)

words_list = [
    'rainbow', 'computer', 'science', 'programming',
    'python', 'mathematics', 'player', 'condition',
    'reverse', 'water', 'board', 'geeks'
]
computer_word = random.choice(words_list)

print("\nGuess a character: ")
guesses_made = ''

chances = 10

if user_decision == 'y':
    while chances > 0:
        
        failed = 0

        for char in computer_word:
            if char in guesses_made:
                print(char, end=" ")
            else:
                print("_", end=" ")
                failed -= 1

        print()

        if failed == 0:
            print("You Win")
            print("The word is: ",computer_word)
            break
            
        guess = input("\nGuess a character: ").lower()

        if len(guess) != 1:
            print("Enter a single character!")
        
        if guess in guesses_made:
            print("\nYou already guessed this character.")
            continue

        guesses_made += guess
        
        if guess not in computer_word:
            chances -= 1
            print("Wrong!")
            print(f"\nYou have {chances} guesses remaining")

            if chances == 0:
                print("You Lose!")
                print(f"The word was: {computer_word}")

elif user_decision == 'n':
    print("Thank you")

else:
    print("Invaild Input!")