import random

secret_num = random.randrange(1000, 10000)

attempts = 0

print("Welcome to Mastermind!")
print("Try to guess the 4-digit  number.\n")

while True:
    try:
        guess = int(input("Guess the 4-digit number: "))
        if guess < 1000 or guess > 10000:
            print("Please enter a vaild 4-digit number.\n")
            continue

    except ValueError:
        print("Please enter numeric digits only.\n")
        continue

    attempts += 1

    if guess == secret_num:
        print("\nYou have become the Mastermind!")
        print(f"It only took you {attempts} tries.")
        break

    guess_str = str(guess)
    secret_str = str(secret_num)

    count = 0
    correct = ['X'] * 4

    for i in range(4):
        if guess_str[i] == secret_str[i]:
            count += 1
            correct[i] = guess_str[i]

    print(f"\nNot quite the number. You did get {count} digits correct.")

    if count > 0:
        print("Correctly placed digits:")
        print(" ".join(correct))
        
    print()