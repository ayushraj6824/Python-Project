# Dice Rolling Game
import random
while True:
    choice = input("Do you want to roll the dice? (yes/no): ").strip().lower()
    if choice == 'yes':
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        print(f"You rolled a {roll1} and a {roll2}.")
    elif choice == 'no':
        print("Thanks for playing!")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

        


        