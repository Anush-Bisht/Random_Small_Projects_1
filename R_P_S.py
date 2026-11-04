import random
import time

choices = ["r", "p", "s"]
emoji_choice = {"r" : "🪨" ,
            "p" : "📃",
            "s" : "✂️"}

computer_choice = random.choice(choices)

while True:
    userinput = input("Do you want to play (y/n): \n")

    if(userinput == 'y'):
        user_choice = input("\nChoose Rock, Paper and Scissor (r,p,s): \n").lower()
        
        time.sleep(1.70)
        if user_choice not in choices:
            print("Invaild\n")
            

        print(f"\nYou Choose {emoji_choice[user_choice]}")
        print(f"Computer Choose {emoji_choice[computer_choice]}\n")

        time.sleep(1.70)

        if user_choice == computer_choice:
            print("Tie!\n")

        if ((user_choice == "r" and computer_choice == "s"),
            (user_choice == "p" and computer_choice == "r"), 
            (user_choice == "s" and computer_choice == "p")):
            print("You Win!\n")

        elif ((computer_choice == "r" and user_choice == "s"),
            (computer_choice == "p" and user_choice == "r"), 
            (computer_choice == "s" and user_choice == "p")):
            print("You Lose!\n")

    
    elif (userinput == 'n'):
        print("\nThanks for Playing!")
        break
