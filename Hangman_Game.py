import random
from collections import Counter


words = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

words = words.split(' ')

stages = [
'''
  -----
  |   |
      |
      |
      |
      |
---------
''',
'''
  -----
  |   |
  O   |
      |
      |
      |
---------
''',
'''
  -----
  |   |
  O   |
  |   |
      |
      |
---------
''',
'''
  -----
  |   |
  O   |
 /|   |
      |
      |
---------
''',
'''
  -----
  |   |
  O   |
 /|\\  |
      |
      |
---------
''',
'''
  -----
  |   |
  O   |
 /|\\  |
 /    |
      |
---------
''',
'''
  -----
  |   |
  O   |
 /|\\  |
 / \\  |
      |
---------
'''
]

computer_words = random.choice(words)

if __name__ == '__main__':
    print("Guess the word! HINT: word is a fruit")

    for _ in computer_words:
        print("_", end=' ')
    print()

    letter_Guessed = ''
    wrong_Guesses = 0
    max_chances = len(stages) - 1
    flag = 0

    try:
        while wrong_Guesses < max_chances and flag == 0:
            print()
            user_guess = input("Enter a letter to guess: ").lower()

            if not user_guess.isalpha():
                print('Enter only a letter!')
                continue
            
            elif len(user_guess) > 1:
                print("Enter only a single character!")
                continue

            elif user_guess in letter_Guessed:
                print("You already guessed that letter!")
                continue
                
            if user_guess in computer_words:
                letter_Guessed += user_guess * computer_words.count(user_guess)
            else:
                wrong_Guesses += 1
                print(stages[wrong_Guesses])
            
            for char in computer_words:
                if char in letter_Guessed:
                    print(char, end=' ')
                else:
                    print('_', end=' ')
                
            if Counter(letter_Guessed) == Counter(computer_words):
                print("\nCongratulations! You guessed the word: ", computer_words)

                flag = 1
                break

            if wrong_Guesses == max_chances:
                print("\nYou Lost! The word was: ", computer_words)

    except KeyboardInterrupt:
        print("\nGame interrupted. Bye!")                