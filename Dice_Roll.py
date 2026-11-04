import random

def dice_roll():
    while True:
        x = input("Enter y/n: ").lower()

        if (x == 'y'):
            r1 = random.randint(1, 6)
            r2 = random.randint(1, 6)

            print(f"({r1},{r2})\n")
        elif (x == 'n'):
            print("Thanks for playing\n")
            break
        else:
            print("Invaild Input\n")


dice_roll()